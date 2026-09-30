# 19 · 推理与服务

> 目标：能解释 LLM 服务的显存与延迟，设计公平的负载测试，并为吞吐、交互体验和成本作出有证据的取舍。先修：Transformer attention、[硬件基础](16-hardware-systems.md)与基本 HTTP 服务；理解 [GPU 算子](17-gpu-kernels-compilers.md)有帮助。主动学习约 35–55 小时。无 GPU 可完成缓存估算和调度模拟；真实服务测试需符合引擎要求的计算设备。

本章以自回归语言模型为主。图像分类、扩散模型、语音流和 embedding 服务也需要 batching、监控与版本管理，但其计算阶段和指标不同，不能直接套用所有 LLM 结论。

## 学习顺序

1. **请求生命周期，5–8 小时**：分词、排队、prefill、decode、流式返回；把客户端和服务端时间线分开。
2. **容量账本，6–9 小时**：权重、KV cache、临时张量；手算最大并发的约束。
3. **调度与内存，8–12 小时**：动态/连续 batching、分页、前缀复用、chunked prefill。
4. **优化取舍，8–12 小时**：量化、推测解码、并行、prefill/decode 分离。
5. **工作负载实验，8–14 小时**：固定输入输出分布，对比延迟、吞吐与正确性。

## 从一个请求到共享引擎

**Prefill 和 decode 的工作不同。** Prefill 处理输入序列，能在多个位置上并行做矩阵计算；decode 每轮生成下一个 token，需要访问已有上下文的 K/V。长输入、大 batch、不同模型架构会改变二者瓶颈，因此“prefill 总是计算受限、decode 总是带宽受限”只能作为待验证假设。客户端的首 token 时间还包含排队、网络和分词，不能直接当成一个 kernel 的耗时。

**KV cache 用空间换重复计算。** 以各层具有固定 KV 头数的普通 attention 模型为例，忽略 padding、分页浪费和临时张量：

$$
M_{KV}=2\times L\times B\times T\times H_{KV}\times d_h\times s
$$

L 为层数，B 为同时驻留的序列数，T 为每序列缓存长度，H_KV 为 KV 头数，d_h 为头维度，s 为每元素字节数，前面的 2 对应 K 和 V。32 层、8 个 KV 头、头维 128、长度 2048、FP16、单请求，需要约 256 MiB。并发 8 条约 2 GiB；若 KV 头数增为 32，则再乘 4。GQA/MQA 影响的是 KV 头数，不能把查询头数直接代入；MLA、滑动窗口等架构需要另建账本。

**连续 batching 在迭代边界重新安排活跃请求。** 静态 batch 中短请求完成后，长请求可能仍占着批次；连续 batching 可以让完成的请求退出、新请求进入，提高设备利用。代价是调度、队列和公平性更复杂。PagedAttention 则把 KV 分为逻辑块与物理块，降低必须连续预留空间带来的碎片，并支持特定场景下的共享。这不是消除 KV 本身占用，而是改善分配方式。[PagedAttention 原论文](https://arxiv.org/abs/2309.06180)解释了问题与设计。

**优化要与代价一起看。** 量化将数值映射到较低位宽，例如 x≈scale×(q−zero_point)。7B 参数采用理想 4-bit 权重存储约 3.5 GB，但量化元数据、未量化层、KV 与工作区另外计算。体积缩小也不保证更快，执行后端需要有高效的低精度 kernel，还应在真实任务上验证质量。[ONNX Runtime 量化指南](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html)给出了动态/静态量化和校准区别。

推测解码让便宜的 draft 模型或机制先提出多个 token，再由目标模型批量验证。原算法通过接受与修正采样保持目标分布；不能简单地“目标模型看起来同意就全收”。收益取决于接受率、draft 成本和批处理条件。[原始论文](https://arxiv.org/abs/2211.17192)适合先学算法，再看引擎实现。

Prefill/decode 分离把两个阶段放到不同实例，便于分别满足首 token 和 token 间延迟目标，却需要传输 KV、路由请求和分配资源。它不是单机一键加速开关；[vLLM 的对应文档](https://docs.vllm.ai/en/stable/features/disagg_prefill/)仍将该功能标为实验性，强调尾延迟控制的动机。

## 核心知识与指标

| 概念/指标 | 应当如何理解 | 测量时必须固定或记录 |
| --- | --- | --- |
| TTFT | 客户端发出请求至收到首 token | 队列、网络、输入长度、缓存状态 |
| ITL / TPOT | 相邻 token 间隔 / 每请求平均后续 token 时间 | 流式实现、输出长度；二者不是同一分布 |
| 吞吐 | 单位时间完成的请求数或 token 数 | 输入/输出 token 是否混算、统计窗口 |
| goodput | 满足预定延迟等 SLO 的有效完成量 | 事先写明阈值和判定口径 |
| continuous batching | 在生成迭代间调整活跃请求 | 并发、到达率、队列上限与公平性 |
| KV 分页/前缀缓存 | 分配块与复用已计算前缀 | 命中率、前缀相似度、共享隔离 |
| chunked prefill | 长 prefill 拆块与 decode 交错 | 首 token 与尾 ITL 的取舍 |
| 量化/推测解码 | 以存储或额外计算换执行收益 | 质量、接受率、硬件和后端 |

有 N>1 个输出 token 时，常见的每请求 TPOT 口径为 `(完成时间−首 token 时间)/(N−1)`。不同工具定义可能有细节差异，必须记录；平均各请求的 TPOT 和汇总全部 token 间隔，也不是同一个统计量。[vLLM Benchmark CLI](https://docs.vllm.ai/en/stable/benchmarking/cli/)明确区分了相关指标。

## 精选资源

核验日期：2026-09-30；资源免费，真实部署的算力与网络成本另计。

| 资源 | 语言 / 级别 / 条件 | 建议范围与理由 |
| --- | --- | --- |
| [vLLM Quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart/) | 英文 / 进阶 / 可选GPU | Offline Batched Inference 与 Online Serving；先建立最小可用服务，具体 CPU/GPU 支持以安装文档为准。 |
| [PagedAttention 论文](https://arxiv.org/abs/2309.06180) | 英文 / 研究 / 无 | 问题定义、块管理与共享；理解设计，不将论文硬件上的加速数值推广到其他环境。 |
| [Speculative Decoding 论文](https://arxiv.org/abs/2211.17192) | 英文 / 研究 / 无 | draft、目标验证、接受/修正采样；掌握保持目标分布的条件。 |
| [vLLM Disaggregated Prefilling](https://docs.vllm.ai/en/stable/features/disagg_prefill/) | 英文 / 进阶 / GPU | 动机、connector 与实验性限制；知道分离为什么会增加系统复杂度。 |
| [vLLM Benchmark CLI](https://docs.vllm.ai/en/stable/benchmarking/cli/) | 英文 / 进阶 / 可选GPU | 在线基准、请求分布、TTFT/ITL/TPOT；直接指导实验记录。 |
| [ONNX Runtime 量化](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) | 英文 / 进阶 / CPU | 静态与动态量化、校准和误差排查；先理解方法，不把某格式当作万能加速方案。 |
| [DistServe 论文](https://arxiv.org/abs/2401.09670) | 英文 / 研究 / 无 | SLO、goodput 与 PD 分离；将系统目标从最高 token/s 转向符合交互要求的服务量。 |

## 实践：提交一份可复查的服务基准

1. 选择已经获得使用许可且能装入现有设备的小模型，记录模型版本、tokenizer、引擎版本、dtype 与并行配置。先根据权重与 KV 估算能否运行。
2. 准备两组负载：短输入/短输出与长输入/固定输出。固定生成参数与请求数，记录实际输出 token，避免只比较最大输出限制。
3. 从并发 1 开始，逐步增加至设备能承受的范围；每组分别记录预热、测量窗口、p50/p95 TTFT、ITL、完成率、输出 token/s 与峰值内存。
4. 仅修改一项，例如前缀缓存、量化或 batch 调度参数。保留相同质量评测集，报告收益以及退化。
5. 写出一个事先定义的 SLO，例如“本实验短请求 p95 TTFT 小于 1 秒”；说明这是实验目标，不是所有产品的标准。

**验收**：有原始请求记录与配置；至少三个并发点；延迟随负载的变化能解释；不能满足 SLO 的结果也保留。无 GPU 路径：用离散时间模拟短、长请求的静态与连续 batching，报告完成时间与等待时间，明确标注为调度模型而非引擎实测。

## 常见误区与下一步

- 只展示最高吞吐：同时展示尾延迟和失败率，否则可能只是把请求堆进队列。
- 将权重量化后的文件大小当成运行内存：KV 和临时工作区可能成为主导。
- 不固定前缀命中率：缓存可令相同“并发”测试变成不同工作负载。
- 只测 `localhost` 就宣布生产延迟：网络、认证、限流与队列都要进入最终评测。

进入 [MLOps](20-mlops.md)管理发布、监控和成本；需要离线或个人设备部署时学习 [端侧 AI](21-edge-ai.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
