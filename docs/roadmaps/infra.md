# 路线 E · AI Infra

先修：能写与调试 Python，理解模型训练和推理；C/C++、操作系统和网络知识有帮助。规划 **500–900 小时**，每周 8–12 小时约 **10–27 个月**。如果从系统零基础开始，需另留补课时间。这里的目标是完成有可信证据的优化项目。

| 阶段 | 内容 | 投入 | 产出 | 主资源与范围 |
|---|---|---|---|---|
| 系统与性能模型 | [硬件系统](../topics/16-hardware-systems.md) | 100–180 小时 | 测量方法、带宽/计算预算、CPU 基线 | [MLSysBook](https://mlsysbook.ai/) 基础卷 → OSTEP 内存/并发 → [Scaling Book](https://jax-ml.github.io/scaling-book/) Roofline |
| 算子与编译 | [GPU 与编译器](../topics/17-gpu-kernels-compilers.md) | 140–240 小时 | 数值正确、覆盖多个 shape 的算子优化 | [GPU MODE](https://github.com/gpu-mode/lectures) 第 3、4、8、14 讲 → Triton 向量加法/softmax/matmul → Nsight profiling |
| 训练或推理主攻 | [分布式训练](../topics/18-distributed-training.md) 或 [推理服务](../topics/19-inference-serving.md) 选一条深入 | 140–260 小时 | 等效 batch 验证或固定请求分布的服务压测 | 训练：DDP → FSDP2 或 ZeRO → Distributed Checkpoint；推理：vLLM Quickstart → Benchmark CLI → Scaling Book 推理部分；链接见左列专题 |
| 生产约束 | [MLOps](../topics/20-mlops.md)、[端侧](../topics/21-edge-ai.md) 选读 | 60–100 小时 | 容错、可观测、恢复与资源边界 | [MLOps Zoomcamp](https://github.com/DataTalksClub/mlops-zoomcamp) 部署、监控选读；做端侧则改选 [MIT 6.5940](https://hanlab.mit.edu/courses/2024-fall-65940) 量化/部署与一种运行时 |
| 综合实验 | 对照、回归和报告 | 60–120 小时 | 一份可被别人复现的性能报告 | 使用前面同一套代码和环境完成独立对照，按服务压测或训练恢复任务交付 |

## 从没有 GPU 的阶段开始

先完成 [显存估算](../projects/04-memory.md)，手算张量字节数并验证单位；再用 CPU 测量数据读取、序列化或批处理开销。这些能训练性能分析方法，但不能替代 CUDA 算子的真实运行与 profiling。

有兼容 GPU 后，从小算子开始。每次优化同时记录正确性、shape、dtype、预热、同步方式、软件版本和设备。吞吐上升时，检查尾延迟和质量是否变差。

## 两个可选毕业项目

- **推理方向**：[服务压测](../projects/06-serving.md)，比较不同负载与 batch 策略，报告 TTFT、TPOT、吞吐和失败率。
- **训练方向**：固定全局 batch，对比单进程与 DDP/FSDP，记录 loss 一致性、通信和检查点恢复。

完成一种配置的优化不代表掌握所有 GPU 或分布式系统；继续在不同设备、模型与负载上积累经验。

[全部路线](README.md) · [环境与算力](../guides/environment.md)
