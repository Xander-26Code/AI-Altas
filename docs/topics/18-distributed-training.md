# 18 · 分布式训练

> 目标：能区分训练加速与模型装载问题，选出合适的并行策略，验证多进程结果，并从检查点恢复训练。先修：PyTorch 训练循环、梯度累积、优化器状态，以及 [GPU 与系统基础](17-gpu-kernels-compilers.md)。学习规划预算约 120–240 小时。CPU 可完成双进程通信与一致性实验；完整 GPU 性能实验通常需要至少两张兼容 GPU。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

## 资源列表

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

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [GPU MODE lectures](https://github.com/gpu-mode/lectures) | 英文 · 进阶 | 免费 · GPU | GPU 入门选第 3、4、8、14 讲；分布式选第 17 讲 NCCL。视频、讲义和代码按需搭配。 |
| [How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | 英文 · 进阶 | 免费 · 无 | 先 Roofline，再训练并行与推理部分；用题目练内存、通信和延迟估算，注意 TPU 与 GPU 差异。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

先 DDP，再按显存或计算瓶颈选一种分片；多种并行策略不要求一次全部实现。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 通信与 DDP | [NCCL 集合通信](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)；[PyTorch DDP](https://docs.pytorch.org/tutorials/intermediate/ddp_tutorial.html)；[GPU MODE lectures](https://github.com/gpu-mode/lectures) | NCCL 图例、GPU MODE 第 17 讲；DDP 教程 | 验证双进程与单进程等效 batch 的结果 |
| 2 · 状态分片 | [PyTorch FSDP2](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html)；[DeepSpeed ZeRO](https://www.deepspeed.ai/tutorials/zero/) | FSDP2 与 ZeRO 对照阅读，实现二选一 | 记录参数、梯度、优化器状态的显存变化 |
| 3 · 恢复能力 | [PyTorch Distributed Checkpoint](https://docs.pytorch.org/tutorials/recipes/distributed_checkpoint_recipe.html) | Distributed Checkpoint 保存、加载与重分片 | 中断再恢复并核对继续训练结果 |
| 选修 · 扩展并行 | [PyTorch Tensor Parallel](https://docs.pytorch.org/tutorials/intermediate/TP_tutorial.html)；[DeepSpeed Pipeline Parallelism](https://www.deepspeed.ai/tutorials/pipeline/)；[DeepSpeed MoE](https://www.deepspeed.ai/tutorials/mixture-of-experts/)；[How to Scale Your Model](https://jax-ml.github.io/scaling-book/) | TP、PP、MoE 按目标选一；Scaling Book 估算通信 | 先纸面估算，再在可用硬件验证 |

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
