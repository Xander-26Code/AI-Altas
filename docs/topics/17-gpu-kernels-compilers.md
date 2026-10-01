# 17 · GPU、算子与编译器

> 目标：能写一个数值正确的简单 GPU 算子，判断它受到计算、内存还是启动开销限制，并解释编译器优化的收益与边界。先修：张量运算、矩阵乘法、反向传播，以及 [硬件与系统基础](16-hardware-systems.md)。学习规划预算约 160–300 小时。理论与 CPU 编译实验可在普通电脑完成；CUDA/Triton 实验需要兼容 GPU。
> 时间口径：具备先修后，系统学习主教材、完成练习与一个项目的规划预算；不包含补先修，也不等于掌握整个领域。实际投入受基础、实验条件和项目深度影响。

GPU 不会因为代码中出现“并行”就自动变快。线程如何访问内存、数据能否复用、计算形状是否适合硬件、启动与同步是否频繁，都会影响执行时间。本章从性能模型出发，再走到代码。

## 学习顺序

1. **先算账**：张量尺寸、字节数、FLOPs、算术强度；手算逐元素加法与矩阵乘法。
2. **理解执行与内存**：grid、block、warp、寄存器、共享内存、全局内存；画出线程和数据的映射。
3. **实现与验证**：向量加法 → 归约/softmax → 分块矩阵乘；至少自己完成一个。
4. **编译与 profiling**：计算图、IR、融合、布局、图中断；比较 eager 与编译后的完整调用。
5. **写优化报告**：提交形状覆盖、精度检查和测量条件。

## 性能模型先于优化技巧

设算子工作量为 F FLOPs，从所分析存储层搬运的数据为 Q 字节，算术强度 I=F/Q。简化 Roofline 上界为：

$$
P\leq\min(P_{\mathrm{peak}},B\times I),\qquad
t\geq\max(F/P_{\mathrm{peak}},Q/B)
$$

这里的峰值必须匹配实际精度和指令路径。假设设备有效带宽为 1 TB/s，FP32 向量加法每个元素读两个数、写一个数，共 12 字节，仅做 1 次加法，因此 I≈1/12 FLOP/byte；带宽对应上界约 83 GFLOP/s。即使计算峰值是 100 TFLOP/s，这个算子也不会因为浮点单元更多而自动接近峰值。真实执行还受缓存、占用率、同步和启动影响。[Nsight Compute Profiling Guide](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)给出了 Roofline 与分层内存分析方法。

**分块提高复用，但会消耗片上资源。** 方阵乘法约需 2n³ FLOPs；若 A、B 各读一次，C 写一次，FP32 的理想数据量为 12n² 字节，算术强度约 n/6。这是理想复用模型，朴素实现可能反复读取相同数据。分块让一组线程把数据搬入共享内存或寄存器后复用；块过大又可能占满寄存器，使同一 SM 能驻留的线程组减少。优化目标是缩短时间，并不是把 occupancy 数字单独推到最大。

**合并访存与减少搬运是不同问题。** 相邻线程访问相邻地址，能让内存事务利用得更充分；算子融合则可以消除中间张量写回与再次读取。例如 `y = relu(a*x+b)` 分成多次 kernel 时，会产生额外启动和中间结果；融合可减少这些成本，但更大的融合也可能增加寄存器压力。[CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html)是核对执行、内存与同步语义的依据。

**编译器把“做什么”转成“如何执行”。** 前端捕获计算图，IR 表达数据依赖与循环，优化阶段做融合、常量传播、布局变换和调度，后端生成目标代码。静态形状有利于专门优化，动态形状可能需要 guard、多个编译版本或退回普通执行。`torch.compile` 的第一次调用可能包含编译工作，应分别测冷启动和稳态；若额外编译 2 秒，每次只节省 1 毫秒，需要约 2000 次调用才能抵消初始成本。[PyTorch 编译教程](https://docs.pytorch.org/tutorials/intermediate/torch_compile_tutorial.html)还解释了 graph break 的限制。

## 核心知识表

| 概念 | 要回答的问题 | 典型失败 |
| --- | --- | --- |
| SIMT、warp、分支 | 哪些线程同时执行？分歧如何影响利用？ | 每个线程走不同分支，执行资源空转 |
| HBM、共享内存、寄存器 | 哪些值被重复使用，放在哪里？ | 溢出到 local memory，搬运反而增加 |
| 归约与同步 | 谁生产结果，谁消费，何时可见？ | 读到未完成写入的数据或线程死锁 |
| tiling、布局、向量化 | 索引如何映射到线程与内存？ | 对某个矩阵形状快，换形状就失效 |
| 融合与 IR | 可以消掉哪些中间结果？ | 图中断、动态控制流、过度融合 |
| 混合精度与 Tensor Core | 输入/累加精度及形状是否合适？ | 精度回退或错误对比不匹配的峰值 |
| profiling | 是 kernel 慢还是调度/传输慢？ | 只测异步提交时间，没有等待完成 |

FlashAttention 可作为后续案例：通过分块和在线 softmax 减少注意力中间矩阵的物化与显存访问。它的核心是 IO 与计算调度的改变；不能从名称推断任意序列长度、形状和硬件上都有固定收益。

## 精选资源

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
