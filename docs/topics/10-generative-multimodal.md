# 10 · 生成模型与多模态

> 目标：理解模型如何生成图像、音频和视频，能区分表示学习、跨模态对齐与条件生成，并完成一个可复现的小实验。
> 先修：概率分布、梯度下降、CNN / Transformer、PyTorch。建议规划 100–200 小时。这是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。

## 资源列表

阅读均免费；表中的算力指建议的动手环境，论文“无”表示阅读无需硬件。真实模型的显存需要取决于分辨率、长度、精度、批大小和实现。核实日期：2026-09-30。

| 资源 | 语言 / 级别 | 费用 / 算力 | 为什么推荐、读哪部分 |
| --- | --- | --- | --- |
| [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course/unit1/1) | 英文 / 进阶 | 免费 / 可选GPU | 先完成Unit 1最小去噪实验，再读条件控制；避免一开始下载大型文生图模型。 |
| [Diffusers Documentation](https://huggingface.co/docs/diffusers/index) | 英文 / 进阶 | 免费 / GPU | 读Quickstart、pipeline与scheduler概念，再按硬件读优化；理解模型和采样器可以分别选择。 |
| [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) | 英文 / 进阶 | 免费 / 无 | 读正向加噪、反向过程与训练目标；把损失和采样算法分别写成伪代码。 |
| [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747) | 英文 / 研究 | 免费 / 无 | 读条件概率路径与向量场回归，先用二维线性路径理解训练，再研究ODE采样。 |
| [CLIP: Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) | 英文 / 进阶 | 免费 / 无 | 读图文配对训练和zero-shot分类方法，思考检索相似度与精细视觉推理的区别。 |
| [Whisper: Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) | 英文 / 进阶 | 免费 / 无 | 读数据、任务构造和鲁棒性实验；关注语言、噪声与分布变化，不把一个总分当通用结论。 |
| [DiT: Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748) | 英文 / 研究 | 免费 / 无 | 读latent patch与Transformer骨干设计；理解扩散训练方式和网络结构是不同维度。 |
| [Video Diffusion Models](https://arxiv.org/abs/2204.03458) | 英文 / 研究 | 免费 / 无 | 读视频架构与时间扩展方法；重点观察时序一致性为何超出单帧生成问题。 |

## 按资源安排学习顺序

生成方向先做 Diffusion Course；跨模态方向可在共同基础后转 CLIP 或 Whisper，不要求同时做图像、音频与视频。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 最小去噪 | [Hugging Face Diffusion Course](https://huggingface.co/learn/diffusion-course/unit1/1) | Unit 1 及其 notebook | 在小数据上训练并观察去噪过程 |
| 2 · 对照原文 | [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)；[Diffusers Documentation](https://huggingface.co/docs/diffusers/index) | DDPM 训练/采样；Diffusers pipeline 与 scheduler | 记录采样器、步数和种子对输出的影响 |
| 3 · 完成一个分支 | [CLIP: Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)；[Whisper: Robust Speech Recognition via Large-Scale Weak Supervision](https://arxiv.org/abs/2212.04356) | 图文选 CLIP 的训练与分类；语音选 Whisper 任务与实验 | 提交下方生成或检索实验之一 |
| 选修 · 扩展阅读 | [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)；[DiT: Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748)；[Video Diffusion Models](https://arxiv.org/abs/2204.03458) | Flow Matching、DiT 或 Video Diffusion 三选一 | 用对照表说明它改变了训练目标、骨干还是数据维度 |

## 实践：两个低成本实验，选一条完成

**A · CPU 路线：二维 flow matching。** 用固定种子采样二维高斯噪声与双月形数据，定义小 MLP，输入坐标和时间，拟合线性条件路径的速度。用 10、50、100 步 Euler 积分生成散点图。保存训练损失、轨迹和每种步数耗时，并解释数值误差。训练目标下降但最终分布不对时，优先检查路径方向、时间输入和积分步长。

**B · GPU 路线：小图像去噪。** 使用课程的最小图像实验，固定数据切分和 16 个噪声种子，训练小去噪网络。只改变一个变量，例如训练噪声日程或采样步数。保存完整样本网格，不只选最佳图片；记录依赖版本、模型权重、分辨率和 GPU 峰值显存。

两条路线都增加一个**多模态诊断练习**：准备 20 对自制图片与描述，包含颜色交换、数量变化、否定句和文字标签。用现有图文编码器做检索，列出最易混淆的配对，并说明检索分数为什么不能证明事实正确。可在 CPU 上小批量运行。

**验收标准**：提交可重跑配置、至少一次受控对照、完整样本和失败分析；解释“训练一次采样一个 $t$”与“生成多步积分”的区别；能指出至少两类自动指标未覆盖的错误。二维分布成功并不意味着完成了真实文生图模型训练。

## 常见误区

- **“扩散模型从数据库拼贴图片。”** 生成机制不是简单检索，但可能记忆训练样本；需要另做相似度与数据来源审查。
- **“步数越多一定越好。”** 采样器、模型训练方式和条件强度会改变结果，必须实验。
- **“看懂图片就能可靠数数。”** 粗语义识别与精确空间推理是不同能力。
- **“语音识别只比较一个平均 WER。”** 口音、噪声、语言和说话人分组可能暴露平均值掩盖的问题。
- **“视频就是独立生成许多图片。”** 这样通常缺乏时序一致性，也没有解决运动建模。

## 下一步

做图文知识库，进入 [RAG](12-rag.md)；做可靠交互产品，进入 [AI 应用开发](11-ai-applications.md)；多模态模型同样需要 [评估与安全](15-evaluation-safety.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
