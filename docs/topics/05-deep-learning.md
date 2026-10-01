# 05 · 深度学习：理解与训练神经网络

> 目标：解释反向传播，独立实现训练循环，诊断训练失败，完成一个小模型项目。先修：[数学](01-math.md)、[编程](02-programming.md) 和 [机器学习](04-machine-learning.md)。**规划预算：120–220 小时**，用于完成先修后系统学习主教材、做练习并完成一个项目；不含补先修，不是领域掌握承诺。小型 MLP 可用 CPU，图像实验可选 GPU。

## 资源列表

“CPU/可选 GPU”指本页建议的学习实验，不表示能在 CPU 上高效复现教材内所有大规模训练。在线教材免费，训练服务费用另算。

- **[动手学深度学习](https://zh.d2l.ai/)**｜中文 · 入门 · 免费 · 可选GPU。作为中文主线；按第 3–7 章学回归、MLP、训练、CNN，再补第 10–11 章。
- **[PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)**｜英文 · 入门 · 免费 · CPU。建立标准训练循环；按 Tensors 到 Save & Load 全流程完成 FashionMNIST 示例。
- **[Deep Learning](https://www.deeplearningbook.org/)**｜英文 · 进阶 · 免费 · 无。补数值计算和训练原理；读第 4、6–8、11 章，作为参考而非追新工具。
- **[Practical Deep Learning for Coders](https://course.fast.ai/)**｜英文 · 入门 · 免费 · 可选GPU。喜欢先做作品可选此主线；先完成 Part 1 的模型训练与迁移学习。
- **[TensorFlow Playground](https://playground.tensorflow.org/)**｜英文 · 入门 · 免费 · CPU。交互观察决策边界；比较不同层数、噪声、学习率与正则化。
- **[Karpathy micrograd](https://github.com/karpathy/micrograd)**｜英文 · 进阶 · 免费 · CPU。看清自动微分；阅读 engine.py 的运算与 backward，再做二分类 demo。

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Karpathy · Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero) | 英文 · 入门 | 免费 · 可选GPU | 视频与 notebook 配套；深度学习先做 micrograd、makemore，再学 GPT 与 tokenizer。 |
| [Hands-On Machine Learning 第三版配套 notebook](https://github.com/ageron/handson-ml3) | 英文 · 进阶 | 部分免费 · 可选GPU | 选完整 ML 项目、分类、训练模型等 notebook；深度学习部分使用 Keras/TensorFlow，勿与 PyTorch 示例混装。 |
| [邱锡鹏 · 神经网络与深度学习](https://nndl.ai/) | 中文 · 进阶 | 免费 · CPU | 中文理论参考；从作者入口选神经网络与深度学习教材，按前馈网络、反向传播与优化主题选读。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

中文主线选 D2L；偏视频可换 fast.ai。Zero to Hero 用于手写实现，中文 NNDL 和 Deep Learning 作为理论参考。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 训练工具 | [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | Tensors 到 Save & Load | 独立跑通并改写一个训练循环 |
| 2 · 课程主线 | [动手学深度学习](https://zh.d2l.ai/)；[Practical Deep Learning for Coders](https://course.fast.ai/) | D2L 第 3–7 章；或 fast.ai Part 1 | 训练小型分类模型，做过拟合与正则对照 |
| 3 · 手写与排错 | [Karpathy · Neural Networks: Zero to Hero](https://github.com/karpathy/nn-zero-to-hero)；[Karpathy micrograd](https://github.com/karpathy/micrograd) | micrograd 和 makemore 的 MLP、梯度相关课 | 手写一个反向传播例子，比较自动微分结果 |
| 4 · 完成项目 | [动手学深度学习](https://zh.d2l.ai/) | 回到主课的训练与 CNN 练习 | 完成下方任务，保存学习率和误差分析 |
| 选修 · 理论与替代框架 | [邱锡鹏 · 神经网络与深度学习](https://nndl.ai/)；[Deep Learning](https://www.deeplearningbook.org/)；[Hands-On Machine Learning 第三版配套 notebook](https://github.com/ageron/handson-ml3) | 优化、正则与训练；Keras notebook 仅作框架分支 | 选择一个困惑的问题查证，不重复修三套主课 |

## 实践任务与验收

完成一个小型图像分类实验，例如 PyTorch 官方教程使用的 FashionMNIST；先做 MLP，再比较一个小 CNN。无需从零训练大型模型。

- [ ] 独立写出训练和验证循环，标注张量形状与标签格式。
- [ ] 手算一个标量梯度，与自动微分结果核对。
- [ ] 在少量样本上验证模型能拟合，再扩展到正式切分。
- [ ] 记录每轮训练/验证损失与主要指标，保存最佳验证检查点而非随意取最后一轮。
- [ ] 比较至少一个有明确假设的改动，保持数据切分、训练预算与其他设置可比。
- [ ] 在新进程加载模型进行预测，验证预处理一致。
- [ ] 报告错误样本、训练时间、参数量和设备；不把一次随机运行当成稳定结论。

进阶练习是自己实现一个仅支持加法、乘法和非线性的标量自动微分引擎，用有限差分验证。目标是理解依赖图，不是替代成熟框架。

## 常见误区

- **loss 下降就说明任务解决。** 仍需看独立数据、业务指标和错误分组。
- **模型越深一定越好。** 数据量、优化、预算和任务结构共同决定结果。
- **GPU 利用率低就继续买卡。** 先查数据加载、批次大小和计算瓶颈。
- **读取检查点等于恢复训练。** 优化器、调度器、步数及随机状态也可能影响续训。
- **所有网络都像人脑。** 神经网络是数学模型，生物类比不能替代计算解释。

下一步：选择 [自然语言处理](06-nlp.md) 或 [计算机视觉](07-computer-vision.md)；预测业务可读 [时间序列](08-time-series.md)。

---

资源核实：2026-09-30；已审阅推荐入口的介绍、目录或相关正文，未声明逐课完成或逐项运行。算力为本页练习建议，详见[核实记录](../research/foundations-sources.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)

