# 19 · 推理与服务

> 目标：能解释 LLM 服务的显存与延迟，设计公平的负载测试，并为吞吐、交互体验和成本作出有证据的取舍。先修：Transformer attention、[硬件基础](16-hardware-systems.md)与基本 HTTP 服务；理解 [GPU 算子](17-gpu-kernels-compilers.md)有帮助。学习规划预算约 100–200 小时。无 GPU 可完成缓存估算和调度模拟；真实服务测试需符合引擎要求的计算设备。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

## 资源列表

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

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | 英文 · 进阶 | 免费 · 无 | 先 Roofline，再训练并行与推理部分；用题目练内存、通信和延迟估算，注意 TPU 与 GPU 差异。 |
| [MIT 6.5940 · TinyML and Efficient Deep Learning Computing (2024)](https://hanlab.mit.edu/courses/2024-fall-65940) | 英文 · 进阶 | 免费 · 可选GPU | 固定 2024 课程入口；选剪枝、量化与部署主题的讲义和作业，做精度、延迟和模型大小对照。 |
| [LLMs from Scratch · KV Cache 实现](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache) | 英文 · 进阶 | 免费 · CPU | 先看目录说明和基础缓存实现，再对照无缓存版本；比较生成一致性与解码耗时。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

先跑 vLLM 服务和基准，再学习解释瓶颈所需的论文。没有兼容硬件时先做 KV cache 与预算实验。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 服务基线 | [vLLM Quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart/)；[vLLM Benchmark CLI](https://docs.vllm.ai/en/stable/benchmarking/cli/) | Quickstart 离线/在线推理；Benchmark CLI | 固定模型与请求分布，保存原始压测结果 |
| 2 · 内存与解码 | [LLMs from Scratch · KV Cache 实现](https://github.com/rasbt/LLMs-from-scratch/tree/main/ch04/03_kv-cache)；[PagedAttention 论文](https://arxiv.org/abs/2309.06180)；[How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | 基础 KV cache；PagedAttention；Scaling Book 推理部分 | 手算权重/KV，解释 batch 和上下文影响 |
| 3 · 量化对照 | [ONNX Runtime 量化](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html)；[MIT 6.5940 · TinyML and Efficient Deep Learning Computing (2024)](https://hanlab.mit.edu/courses/2024-fall-65940) | ONNX Runtime 量化；MIT 量化课程选读 | 比较质量、模型大小与实际延迟 |
| 选修 · 服务优化 | [Speculative Decoding 论文](https://arxiv.org/abs/2211.17192)；[vLLM Disaggregated Prefilling](https://docs.vllm.ai/en/stable/features/disagg_prefill/)；[DistServe 论文](https://arxiv.org/abs/2401.09670) | 投机解码或 PD 分离二选一 | 包含传输、draft 与失败开销，完成下方基准报告 |

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
