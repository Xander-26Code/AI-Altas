# 17 · GPU、算子与编译器

> 目标：能写一个数值正确的简单 GPU 算子，判断它受到计算、内存还是启动开销限制，并解释编译器优化的收益与边界。先修：张量运算、矩阵乘法、反向传播，以及 [硬件与系统基础](16-hardware-systems.md)。学习规划预算约 160–300 小时。理论与 CPU 编译实验可在普通电脑完成；CUDA/Triton 实验需要兼容 GPU。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

## 资源列表

核验日期：2026-09-30。GPU 指运行对应 GPU 实验的条件，阅读本身无需 GPU。

| 资源 | 语言 / 级别 / 费用 / 条件 | 建议范围与选择理由 |
| --- | --- | --- |
| [CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html) | 英文 / 进阶 / 免费 / GPU | Programming Model、SIMT kernels、异步执行与内存；适合查语义，初学无需通读高级特性。 |
| [Triton 官方教程](https://triton-lang.org/main/getting-started/tutorials/) | 英文 / 进阶 / 免费 / GPU | Vector Addition → Fused Softmax → Matrix Multiplication；每篇把实现、正确性与基准连接起来。注意这是算子语言，不是同名推理服务器。 |
| [机器学习编译课程（中文）](https://book-zh.mlc.ai/) | 中文 / 进阶 / 免费 / 可选GPU | 第 2、4、6、7 章；用 TensorIR、调度与计算图解释编译思想。课程代码与当前库 API 可能有版本差异。 |
| [Deep Learning Systems](https://dlsyscourse.org/) | 英文 / 进阶 / 免费 / 可选GPU | 自动微分、NDArray、硬件加速相关单元；适合从头搭小框架，理解框架内部责任。 |
| [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html) | 英文 / 进阶 / 免费 / GPU | Roofline、Memory Chart、指标解释；将性能猜测转换成证据。 |
| [Stanford CS336](https://cs336.stanford.edu/) | 英文 / 进阶 / 免费 / GPU | Resource Accounting、Kernels/Triton、Systems 作业；让算子优化回到语言模型训练。完整作业投入明显高于本章。 |
| [Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) | 英文 / 进阶 / 免费 / 可选GPU | eager/compiled 对比、graph break 与排错；建立应用代码和编译器之间的联系。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [GPU MODE lectures](https://github.com/gpu-mode/lectures) | 英文 · 进阶 | 免费 · GPU | GPU 入门选第 3、4、8、14 讲；分布式选第 17 讲 NCCL。视频、讲义和代码按需搭配。 |
| [MIT 6.5940 · TinyML and Efficient Deep Learning Computing (2024)](https://hanlab.mit.edu/courses/2024-fall-65940) | 英文 · 进阶 | 免费 · 可选GPU | 固定 2024 课程入口；选剪枝、量化与部署主题的讲义和作业，做精度、延迟和模型大小对照。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

GPU MODE 配 Triton 为实践主线；需要 CUDA C++ 时用 Programming Guide。编译器分支按兴趣选 MLC 或 Deep Learning Systems。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 编程模型 | [GPU MODE lectures](https://github.com/gpu-mode/lectures)；[CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html) | GPU MODE 第 3、4 讲；CUDA Programming Model | 运行向量加法并核对线程与内存访问 |
| 2 · 算子实现 | [Triton 官方教程](https://triton-lang.org/main/getting-started/tutorials/)；[GPU MODE lectures](https://github.com/gpu-mode/lectures) | Triton 向量加法、融合 softmax、矩阵乘法；GPU MODE 第 14 讲 | 建立多个 shape 的正确性与性能基线 |
| 3 · Profiling | [Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)；[GPU MODE lectures](https://github.com/gpu-mode/lectures) | Nsight Roofline/Memory Chart；GPU MODE 第 8 讲 | 用数据解释一个瓶颈并验证优化 |
| 选修 · 编译与框架 | [机器学习编译课程（中文）](https://book-zh.mlc.ai/)；[Deep Learning Systems](https://dlsyscourse.org/)；[Introduction to torch.compile](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html) | MLC TensorIR 或 DLSys 数组/自动微分；torch.compile 对照 | 选一个编译优化或框架内部实验 |
| 选修 · 高效模型 | [MIT 6.5940 · TinyML and Efficient Deep Learning Computing (2024)](https://hanlab.mit.edu/courses/2024-fall-65940)；[Stanford CS336](https://cs336.stanford.edu/) | MIT 量化/剪枝；CS336 systems 作业选读 | 完成一个与主项目相关的扩展 |

## 实践：给融合逐元素算子做一张性能说明书

1. 固定算子 `y = maximum(a*x+b, 0)`，先写 PyTorch 参考实现；设置负数、零、大数及非整块长度的输入。
2. 用 Triton 或 CUDA 实现一个版本；先使用 FP32，确认边界 mask 正确，再讨论低精度。
3. 测试小、中、大三组形状。记录硬件、软件版本、dtype、数据尺寸和是否包含 CPU/GPU 传输。
4. 先预热；GPU 计时使用事件或明确同步。单独报告首次调用，不把编译开销悄悄混入或删掉。
5. 对照参考实现报告最大绝对误差、相对误差及容差；使用多次重复的中位数比较性能。
6. 只改一个因素，例如块大小；解释它为什么对小输入无益，却可能影响大输入。

**验收**：至少 6 个形状包含一个非整块长度；数值检查通过；能手算最少搬运字节；报告三种规模的结果并承认未加速的情形。没有 GPU 时，可以完成 CPU 上 eager/compile 对比及 Roofline 手算，但不要把它写成 GPU 实测。

## 常见误区与下一步

- 看见更少的代码就假定更快：实际图、内存访问和 kernel 数量才决定代价。
- 只和自己写的慢基线比较：同时保留框架原生算子，防止得出误导结论。
- 用相同容差验证所有 dtype：误差标准应结合输入范围和下游任务制定。
- 把一个 shape 的速度推广到全部模型：布局、batch 和动态形状都会改变瓶颈。

继续学习 [分布式训练](18-distributed-training.md)，把单设备的数据移动模型扩展到多设备；偏部署方向进入 [推理与服务](19-inference-serving.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
