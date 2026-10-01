# 18 · 分布式训练

> 目标：能区分训练加速与模型装载问题，选出合适的并行策略，验证多进程结果，并从检查点恢复训练。先修：PyTorch 训练循环、梯度累积、优化器状态，以及 [GPU 与系统基础](17-gpu-kernels-compilers.md)。学习规划预算约 120–240 小时。CPU 可完成双进程通信与一致性实验；完整 GPU 性能实验通常需要至少两张兼容 GPU。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

多卡训练不是把设备数量写成 8。你需要决定数据、参数、梯度、优化器状态和激活分别放在哪里，谁在什么时候通信，以及某个进程失败后如何恢复。正确性先于加速比。

## 学习顺序

1. **通信原语**：用几个短数组手算 broadcast、all-reduce、all-gather、reduce-scatter、all-to-all。
2. **DDP**：进程组、rank、数据分片、梯度平均；与单进程等效 batch 对齐。
3. **状态分片**：显存账本、ZeRO/FSDP、分组粒度、参数重组、激活重计算。
4. **模型并行**：TP、PP、EP 与拓扑；先做纸上切分，再运行现成教学例子。
5. **恢复与测量**：完整 checkpoint、吞吐、通信占比和失败恢复。

## 先明确你在拆什么

**数据并行复制模型、切分样本。** 每个 rank 对自己的 batch 做前向和反向，随后同步梯度。设两份等大的 batch 的平均梯度为 g₁、g₂，全局平均梯度为 (g₁+g₂)/2；本地 batch 不等大时，简单平均这两个数不再等价，必须考虑样本权重。`DistributedDataParallel` 通常采用每设备一个进程；经典 `DataParallel` 的单进程路径并不等同于 DDP。DDP 也不会替你自动切分全部输入数据，需要正确的 sampler 与每轮设置。[PyTorch DDP 教程](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)是实践入口。

对于纯数据并行，若每 rank 的 micro-batch 为 b，数据并行度为 D，累积 A 次才更新，则有效 batch 为 b×D×A。增加卡数而保持 b、A 不变，会改变优化过程；比较多卡与单卡时，要先固定全局 batch、损失归一化和优化器步数。

**状态分片解决的是常驻副本开销。** 一个教学用混合精度 Adam 账本可以按每参数 16 字节估算：低精度权重 2、低精度梯度 2、FP32 主权重 4、两份 FP32 动量 8。实际框架可能使用不同梯度或权重表示，应以测量为准。7B 参数据此约 112 GB；8 路完整分片的常驻状态理想值约 14 GB/卡，但激活、临时 all-gather、通信 buffer 与碎片还没算进去。

ZeRO-1 分优化器状态，ZeRO-2 再分梯度，ZeRO-3 再分参数；FSDP 在相关思路上按模块组织参数分片与重组。它们减少常驻状态，并不意味着每层计算不再需要对应参数。分片过细会增加小通信，分片过粗会抬高瞬时峰值。当前 [FSDP2 教程](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)采用 `fully_shard`，不要把旧包装器 API 与新教程混用。激活重计算则少保存中间结果、在反向时重新计算，消耗额外算力换显存。

**模型并行拆的是计算。** TP 把一个矩阵的行或列分到多卡，层内频繁交换结果，因而更依赖快速互联；PP 把连续层交给不同 stage，通过 micro-batch 让多个 stage 同时工作，但仍有流水线气泡与负载不均。EP 把 MoE 专家放到不同设备，token 路由产生 all-to-all，热门专家会造成倾斜。DP、TP、PP 可以组合；EP 与数据并行分组可能共享维度，不应机械地把所有并行度都相乘来算卡数。

**通信时间包含固定开销和传输开销。** 在理想 ring all-reduce 模型中，N 个 rank、每 rank 梯度大小 M、链路有效带宽 B、每步启动延迟 α，可粗略估计：

$$
t_{\mathrm{allreduce}}\approx2(N-1)\alpha+\frac{2(N-1)}{N}\frac{M}{B}
$$

这不是所有拓扑与 NCCL 算法的统一公式，却能解释为什么小张量受延迟影响、卡数增加后通信不一定变短。通信和反向计算可重叠，最终要看训练 step 时间，而不只是单次通信时间。各原语的数据语义见 [NCCL Collective Operations](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)。

## 核心知识表

| 方法 | 拆分对象 | 主要收益 | 主要代价 |
| --- | --- | --- | --- |
| DDP | 样本 | 增加数据处理能力 | 模型状态仍复制；同步梯度 |
| FSDP / ZeRO | 参数、梯度、优化器状态 | 降低每卡常驻状态 | 重组参数、通信与峰值管理 |
| TP | 层内张量 | 超大单层可分布计算 | 频繁层内通信，依赖互联 |
| PP | 模型层 | 分担模型与激活 | 气泡、stage 负载、micro-batch 调度 |
| EP | MoE 专家 | 分担专家参数与计算 | token all-to-all 与路由倾斜 |
| 激活 checkpointing | 保存的中间激活 | 降低激活显存 | 重算前向，与存盘恢复不是一回事 |
| 训练 checkpoint | 训练状态与进度 | 故障后继续 | I/O、状态完整性、分片重载 |

## 精选资源

核验日期：2026-09-30；均为免费的一手文档。完整多卡示例的算力费用不包含在“免费”中。

| 资源 | 语言 / 级别 / 条件 | 重点与理由 |
| --- | --- | --- |
| [PyTorch DDP](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html) | 英文 / 进阶 / 可选GPU | 进程初始化、梯度同步、保存加载；先建立可对齐的最小实现。CPU 可用合适的通信后端学习原语。 |
| [PyTorch FSDP2](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) | 英文 / 进阶 / GPU | `fully_shard`、通信时机、内存管理；清楚区分当前 API 与旧 FSDP 教程。 |
| [PyTorch Tensor Parallel](https://docs.pytorch.org/tutorials/intermediate/TP_tutorial.html) | 英文 / 进阶 / GPU | Rowwise/ColwiseParallel、DeviceMesh 与布局；知道张量切分后在哪个位置通信。 |
| [DeepSpeed ZeRO](https://www.deepspeed.ai/tutorials/zero/) | 英文 / 进阶 / GPU | 三阶段状态分片；把 JSON 配置对应回显存账本。 |
| [NCCL 集合通信](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html) | 英文 / 进阶 / GPU | 对照图例理解 reduce-scatter 与 all-gather；学习通信语义的可靠入口。 |
| [PyTorch Distributed Checkpoint](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html) | 英文 / 进阶 / 可选GPU | 保存、加载、分片重排；理解加载为什么需要目标模型的状态布局。 |
| [DeepSpeed Pipeline Parallelism](https://www.deepspeed.ai/tutorials/pipeline/) | 英文 / 进阶 / GPU | micro-batch、层切分、stage 平衡；展示模型结构和调度的关系。 |
| [DeepSpeed MoE](https://www.deepspeed.ai/tutorials/mixture-of-experts/) | 英文 / 进阶 / GPU | 专家分组与并行组合；避免把专家参数量误当成每个 token 的实际计算量。 |

## 实践：先证明双进程训练算得对

1. 用固定随机种子的合成回归数据、小型 MLP 和 SGD，建立单进程基线；保存初始参数。
2. 启动两进程版本。普通电脑可选择 CPU/Gloo；GPU 环境按官方教程选择后端。将同一全局 batch 切成等大的两份。
3. 比较第一次更新后的参数与损失。关闭 dropout 等额外随机性，明确损失采用 sum 还是 mean；不要用“最终大概收敛”代替一致性检查。
4. 训练若干步后保存模型、优化器、学习率调度、随机数状态、数据位置及配置；关闭进程，再加载并继续。
5. 与连续训练相同步数的结果对比。记录容差与不能逐位复现的原因；不同硬件上的浮点归约顺序可能不同。
6. 可选 GPU 扩展：固定全局 batch，比较一张与两张卡的每步时间、样本/秒、峰值显存，写出扩展效率。CPU 功能实验不能作为 GPU 加速结论。

**验收**：一步更新在预设容差内对齐；每轮各 rank 样本不意外重复；故障恢复后步数、学习率与数据进度正确；能解释参数、梯度和优化器状态各存在哪里。

## 常见误区与下一步

- 显存估算只算权重：训练状态、激活和临时重组同样重要。
- 多卡更慢就立即换框架：先排查小 batch、数据加载、通信与同步点。
- 保存 `model.state_dict()` 就认为能继续原训练：优化器、随机性和样本顺序也影响轨迹。
- 把激活重计算与恢复检查点混用：二者解决的问题不同。

接着看 [推理与服务](19-inference-serving.md)，理解为什么训练中的最佳并行方案未必适合在线解码；用 [MLOps](20-mlops.md)管理实验与恢复流程。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
