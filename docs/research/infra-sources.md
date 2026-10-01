# AI Infra 选材与核验记录

本记录对应专题 16–21。资源检索与内容核对日期为 **2026-09-30**；学习预算在后续审阅中调整。结构化清单见 [resources-infra.json](../assets/data/resources-infra.json)：共 **41 个独特 URL**，其中 40 项为 `content-reviewed`，1 项为 `search-verified`。

## 核验口径

- `content-reviewed`：打开一手网页并核对与推荐有关的正文、课程目录或 API/章节入口；不表示完整学完课程、运行全部作业或复现论文结果。论文条目此次核对的是 arXiv 摘要、作者与元数据，没有完成全文逐页审查。
- `search-verified`：官方搜索索引能确认标题、地址和相关内容，但正文抓取未成功；不能等同于正文复核。
- 本组未下载模型、安装大型依赖、购买算力、运行 GPU 任务。因此专题中的性能算例均标为理论/教学估算，实践部分是供读者完成的实验方案，不能当作仓库已完成的性能测量。
- 搜索阶段用课程/项目官方域名寻找入口，再打开推荐 URL。对涉及易过期的信息，优先链接当前文档，不写未经环境验证的版本兼容、固定提速倍数或硬件购买建议。
- 文档费用只指公开阅读材料。教材、直播班、硬件、托管服务和云计算资源可能收费，不能由“开源”推出所有使用成本为零。

## 已有路线的结构观察

以下优缺点是基于公开主页和目录的编辑判断，而非课程质量排名；没有用 star 数量替代内容评价。

| 参考路线 | 本次确认的结构 | 适合借鉴 | 对本 Wiki 读者的局限与调整 |
| --- | --- | --- | --- |
| [lvy010/AI-wiki](https://github.com/lvy010/AI-wiki) | 聚合 Course、Paper、Blog、Book；包含 FlashAttention、Triton、CUDA、vLLM、量化、推测解码等主题 | 适合有背景的读者按问题快速发现系统材料；课程、论文与工程文章相互补充 | 资源型入口对零基础读者缺少明确依赖与退出条件。本 Wiki 将资源拆进六个专题，补先修、知识解释、实验验收和硬件条件，不复制原文或整份清单。 |
| [Stanford CS336](https://cs336.stanford.edu/) | 从语言模型组件到系统、并行、推理、缩放、数据和评测；Systems 作业连接 profiling 与实现 | 以可以构建的语言模型贯穿算法与系统，资源计量先于盲目优化 | 公开课程已要求 ML/DL 基础且实现强度高；不适合作为零基础几周速成路线。本 Wiki 只把选定单元作为进阶主教材，并另补 OS/网络/存储。 |
| [Deep Learning Systems](https://dlsyscourse.org/) | 从自动微分与框架内部到设备级算法，配合实现型作业 | 有助于理解张量库、执行与反向传播背后的系统责任 | 重心是深度学习框架构建，不覆盖全部线上发布/成本/端侧问题。当前学期材料可能按进度发布，应从课程页选择实际可用材料。 |
| [机器学习编译课程](https://book-zh.mlc.ai/) | 张量程序抽象 → 端到端执行 → 自动优化 → 框架整合 → GPU → 图优化 | 中文材料能降低编译方向门槛；围绕 IR 和变换，比直接堆工具名更有解释力 | TensorIR/TVM 教学示例具有版本背景；把概念与最新运行指令分开，运行时核对依赖，不承诺复制即用。 |
| [Made With ML](https://madewithml.com/courses/mlops/) | Design、Data、Model、Develop、Utilities、Test、Reproducibility、Production | 从问题设计到测试、部署和监控形成项目闭环 | 具体课程栈不必全部照搬；先让小模型实现版本追溯和回滚，再按需要引入平台，避免把工具安装误当学习结果。 |

## 本 Wiki 的组织决策

1. **按依赖建立六个层级**：硬件/OS/网络/存储 → GPU/算子/编译器 → 分布式训练 → 推理服务 → MLOps → 端侧。MLOps 与端侧也允许从应用方向直接进入，不要求每个读者完成所有系统主题。
2. **把“知道名词”与“完成实验”分开**：每篇包含目标、先修、预算、概念解释、关键表格、精选资源、实践步骤、验收和下一步。验收重视正确性、可复查测量与失败案例，不预设必须获得某个加速倍数。
3. **统一预算口径**：在已有先修基础上，系统学习主教材、练习和一个项目；不含补先修，不等于掌握整个领域。专题预算依次为 120–220、160–300、120–240、100–200、100–180、80–160 小时。删除每个学习步骤的精确小时分配，避免造成虚假的进度承诺；共享材料不应机械重复计时。
4. **给出普通设备入口**：硬件基础、MLOps 可用 CPU；GPU/分布式/推理给出手算、CPU 功能实验或调度模拟替代。模拟结果明确不冒充真实设备性能。
5. **避免技术口号**：参数文件大小不等于运行内存；FSDP 不消除激活与瞬时重组；量化、PD 分离、统一内存与编译均不承诺普遍提速。

## 分组核验摘要

### 16 · 硬件与系统基础

| 一手来源 | 实际核对范围 |
| --- | --- |
| [CS:APP 作者站](https://csapp.cs.cmu.edu/) | 作者与课程背景，数据表示、内存层次、网络与并发范围；作者站不等于教材全文免费。 |
| [OSTEP](https://pages.cs.wisc.edu/~remzi/OSTEP/) | 免费章节 PDF、虚拟化/并发/持久化主线与作业入口。 |
| [CS144](https://cs144.github.io/) | 课程主页、网络教材与实验导航；没有将注册学生服务当成公众可用权益。 |
| [Brendan Gregg Linux Performance](https://www.brendangregg.com/linuxperf.html) | USE、Off-CPU、火焰图等性能方法入口。 |
| [Linux 内存概念](https://docs.kernel.org/admin-guide/mm/concepts.html) | NUMA、页缓存、匿名内存、回收。 |
| [Apache Parquet](https://parquet.apache.org/docs/overview/) | 列式格式、规范与实现，以及不同实现的兼容性限制。 |

### 17 · GPU、算子与编译器

| 一手来源 | 实际核对范围 |
| --- | --- |
| [CUDA Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html) | Programming Model、SIMT Kernels、异步执行和内存章节导航。 |
| [Triton Tutorials](https://triton-lang.org/main/getting-started/tutorials/) | 向量加法、融合 softmax、矩阵乘法与后续算子教学。 |
| [中文 MLC](https://book-zh.mlc.ai/) | TensorIR、自动程序优化、GPU 与计算图优化章节。 |
| [DL Systems](https://dlsyscourse.org/) | 课程描述、实现型学习目标、作业与当前学期信息。 |
| [Nsight Compute](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) | Roofline、Memory Chart 和匹配指令路径的测量解释。 |
| [CS336](https://cs336.stanford.edu/) | Resource Accounting、Kernels/Triton、Parallelism、Inference、Systems 作业。 |
| [torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) | 编译路径、graph break 与排错；不将首次调用当稳态。 |

### 18 · 分布式训练

| 一手来源 | 实际核对范围 |
| --- | --- |
| [DDP](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) | 多进程训练、初始化与保存加载。 |
| [FSDP2](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) | `fully_shard`、通信行为与旧 API 差异；明确区分 FSDP1。 |
| [Tensor Parallel](https://docs.pytorch.org/tutorials/intermediate/TP_tutorial.html) | 行列切分、布局、SequenceParallel 与 loss_parallel。 |
| [ZeRO](https://www.deepspeed.ai/tutorials/zero/) | 优化器、梯度、参数的分阶段分片。 |
| [NCCL Collectives](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) | 各集合通信原语及 rank 对数据布局的影响；根目录空响应后改用已打开的具体子页。 |
| [Distributed Checkpoint](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html) | 模型/优化器状态及 resharding 所需布局。 |
| [Pipeline](https://www.deepspeed.ai/tutorials/pipeline/) | micro-batch、迭代器与 stage 负载均衡。 |
| [MoE](https://www.deepspeed.ai/tutorials/mixture-of-experts/) | Expert groups 与并行组合。 |

### 19 · 推理与服务

| 一手来源 | 实际核对范围 |
| --- | --- |
| [vLLM Quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart/) | 离线 batch 与在线服务，CPU/GPU 安装入口。 |
| [PagedAttention](https://arxiv.org/abs/2309.06180) | 原论文摘要、作者、KV 碎片和分页设计的问题定义。 |
| [Speculative Decoding](https://arxiv.org/abs/2211.17192) | 原论文摘要与采样分布保持的目标，不宣称复现提速结果。 |
| [vLLM PD 分离](https://docs.vllm.ai/en/stable/features/disagg_prefill/) | 独立调整 TTFT/ITL、KV connector 和 experimental 标记。 |
| [vLLM Benchmark CLI](https://docs.vllm.ai/en/stable/benchmarking/cli/) | 工作负载、客户端延迟、指标术语、结果与请求记录保存。 |
| [ONNX 量化](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) | scale/zero point、动态/静态量化、校准与调试；同时关联端侧专题。 |
| [DistServe](https://arxiv.org/abs/2401.09670) | 原论文摘要及 SLO/goodput 的研究目标。 |

### 20 · MLOps

| 一手来源 | 实际核对范围 |
| --- | --- |
| [Made With ML](https://madewithml.com/courses/mlops/) | 生命周期目录、Testing、Versioning、CI/CD 与 Monitoring。 |
| [MLflow Registry](https://www.mlflow.org/docs/latest/registry/) | **仅 search-verified**：官方搜索索引给出 lineage、versioning、aliasing、tags；打开正文为空，另一个域名尝试不可达。 |
| [DVC `.dvc` Files](https://doc.dvc.org/user-guide/project-structure/dvc-files) | 元数据、哈希、路径、remote；早先尝试的数据版本总览地址未成功，改用实际打开的官方子页。 |
| [KServe](https://kserve.github.io/website/docs/intro) | 控制面/数据面、模型服务资源与安装路径。 |
| [Prometheus](https://prometheus.io/docs/practices/histograms/) | 直方图、摘要及无法直接聚合已有分位数的限制。 |
| [OpenTelemetry](https://opentelemetry.io/docs/concepts/observability-primer/) | 日志、指标、追踪及可观测性基础。 |
| [scikit-learn Persistence](https://scikit-learn.org/stable/model_persistence.html) | 持久化格式、代码执行与依赖兼容问题。 |

### 21 · 端侧、移动端与浏览器

| 一手来源 | 实际核对范围 |
| --- | --- |
| [ONNX Runtime Mobile](https://onnxruntime.ai/docs/tutorials/mobile/) | Execution Provider、子图分割、延迟/功耗/体积的目标设备测量。 |
| [MLX](https://ml-explore.github.io/mlx/build/html/index.html) | Quick Start、Lazy Evaluation、Unified Memory 与示例目录。 |
| [Transformers.js WebGPU](https://huggingface.co/docs/transformers.js/en/guides/webgpu) | 设备选择与 pipeline 示例；页面历史浏览器支持比例不作为当前数值引用。 |
| [LiteRT](https://developers.google.com/edge/litert/overview) | 模型转换、CompiledModel、CPU/GPU/NPU 与参考应用。 |
| [Core ML Tools](https://apple.github.io/coremltools/docs-guides/source/overview-coremltools.html) | 模型转换、模型包、macOS 验证与 Apple 设备部署。 |
| [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/) | WASM/GPU 后端算子范围及客户端/服务端选型。 |

## 待持续维护的边界

MLflow 正文需要在后续可访问时复核；外链能打开不代表每个深层下载、视频或练习依赖均有效。当前页、稳定版文档和 GitHub 默认分支会继续变化，适合在准备实际实验时记录版本或 commit。旧 ONNX mobile performance tuning 页面明确仅适用于旧运行时，故未列为学习入口。课程在读、文档迁移、浏览器支持与 GPU 后端都应定期复查，不将本次核验写成长期可用保证。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
