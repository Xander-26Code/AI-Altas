# AI 知识地图

27 个专题按学习关系组织。先修列是建议，不是入学要求；能完成自测和实践时，可以跳过已掌握的部分。每个专题包含原创导读、主线、精选资源与实践设计，并非完整教材。

![基础、模型、应用与系统](assets/atlas.svg)

## 怎么走

- 基础路线：编程与数学 → 数据与机器学习 → 深度学习 → 一个领域项目。
- 应用路线：编程 → 模型接口 → 检索与 RAG → 工具工作流 → 评估与运维。
- 系统路线：编程与训练基础 → 硬件系统 → 算子 / 分布式 / 推理主攻 → 生产验证。

具体阶段与时间预算见 [学习路线](roadmaps/README.md)。

## 基础与算法

| 专题 | 核心内容 | 建议先修 |
|---|---|---|
| 01 · [数学基础](topics/01-math.md) | 线性代数、微积分、概率统计、优化与信息论 | 从这里开始 |
| 02 · [编程与计算机基础](topics/02-programming.md) | Python、数据结构、Git、Linux、SQL 与软件工程 | 从这里开始 |
| 03 · [数据工程与数据质量](topics/03-data.md) | 采集、清洗、标注、切分、数据治理与数据版本 | [编程与计算机基础](topics/02-programming.md) |
| 04 · [机器学习](topics/04-machine-learning.md) | 回归、分类、树模型、聚类、降维与泛化 | [数学基础](topics/01-math.md)、[编程与计算机基础](topics/02-programming.md)、[数据工程与数据质量](topics/03-data.md) |
| 05 · [深度学习](topics/05-deep-learning.md) | 自动微分、反向传播、优化、网络结构与训练诊断 | [机器学习](topics/04-machine-learning.md) |
| 06 · [自然语言处理](topics/06-nlp.md) | 文本表示、序列建模、语言模型与语言任务 | [深度学习](topics/05-deep-learning.md) |
| 07 · [计算机视觉](topics/07-computer-vision.md) | 分类、检测、分割、视觉表示与三维视觉 | [深度学习](topics/05-deep-learning.md) |
| 08 · [时间序列与异常检测](topics/08-time-series.md) | 预测、时序切分、统计基线与分布漂移 | [机器学习](topics/04-machine-learning.md) |

## 模型与应用

| 专题 | 核心内容 | 建议先修 |
|---|---|---|
| 09 · [大语言模型](topics/09-llm.md) | Tokenizer、Transformer、位置编码、预训练与 MoE | [深度学习](topics/05-deep-learning.md)、[自然语言处理](topics/06-nlp.md) |
| 10 · [生成模型与多模态](topics/10-generative-multimodal.md) | VAE、GAN、扩散、flow matching、视觉语言、音频视频 | [深度学习](topics/05-deep-learning.md) |
| 11 · [AI 应用开发](topics/11-ai-applications.md) | API、结构化输出、流式、缓存、工具调用与产品设计 | [编程与计算机基础](topics/02-programming.md) |
| 12 · [检索增强生成](topics/12-rag.md) | 切块、embedding、混合召回、重排、引用与权限 | [AI 应用开发](topics/11-ai-applications.md)、[推荐与信息检索](topics/23-recommendation-search.md) |
| 13 · [Agent 与工作流](topics/13-agents.md) | 工具、规划、状态、记忆、MCP、边界与评估 | [AI 应用开发](topics/11-ai-applications.md) |
| 14 · [微调与对齐](topics/14-finetuning-alignment.md) | SFT、LoRA、QLoRA、RLHF、DPO 与偏好学习 | [大语言模型](topics/09-llm.md)、[数据工程与数据质量](topics/03-data.md) |
| 15 · [评估、安全与负责任 AI](topics/15-evaluation-safety.md) | 评测、数据污染、红队、隐私、公平与可观测性 | [机器学习](topics/04-machine-learning.md) |

## AI Infra

| 专题 | 核心内容 | 建议先修 |
|---|---|---|
| 16 · [硬件与系统基础](topics/16-hardware-systems.md) | CPU、GPU、内存、OS、网络、存储与性能模型 | [编程与计算机基础](topics/02-programming.md) |
| 17 · [GPU、算子与编译器](topics/17-gpu-kernels-compilers.md) | CUDA、Triton、算子融合、roofline、图优化与编译 | [硬件与系统基础](topics/16-hardware-systems.md)、[深度学习](topics/05-deep-learning.md) |
| 18 · [分布式训练](topics/18-distributed-training.md) | DDP、FSDP、ZeRO、TP、PP、EP、通信与容错 | [硬件与系统基础](topics/16-hardware-systems.md)、[深度学习](topics/05-deep-learning.md) |
| 19 · [推理与模型服务](topics/19-inference-serving.md) | KV Cache、批处理、量化、推测解码、PD 分离与 SLO | [大语言模型](topics/09-llm.md)、[硬件与系统基础](topics/16-hardware-systems.md) |
| 20 · [MLOps 与生产系统](topics/20-mlops.md) | 实验、流水线、版本、部署、监控、回滚与成本 | [数据工程与数据质量](topics/03-data.md)、[机器学习](topics/04-machine-learning.md) |
| 21 · [端侧 AI](topics/21-edge-ai.md) | 移动端、浏览器、ONNX、量化、隐私与设备约束 | [深度学习](topics/05-deep-learning.md)、[推理与模型服务](topics/19-inference-serving.md) |

## 交叉领域

| 专题 | 核心内容 | 建议先修 |
|---|---|---|
| 22 · [强化学习与机器人](topics/22-rl-robotics.md) | MDP、控制、模仿、离线 RL、具身智能与世界模型 | [数学基础](topics/01-math.md)、[深度学习](topics/05-deep-learning.md) |
| 23 · [推荐与信息检索](topics/23-recommendation-search.md) | 倒排、BM25、向量检索、召回、排序与在线实验 | [数据工程与数据质量](topics/03-data.md)、[机器学习](topics/04-machine-learning.md) |
| 24 · [图学习与知识表示](topics/24-graphs.md) | 图算法、知识图谱、GNN、图评测与结构化关系 | [深度学习](topics/05-deep-learning.md) |
| 25 · [因果推断与概率建模](topics/25-causal-probabilistic.md) | 贝叶斯、图模型、因果识别、干预与不确定性 | [数学基础](topics/01-math.md)、[机器学习](topics/04-machine-learning.md) |
| 26 · [AI for Science](topics/26-ai-for-science.md) | 分子、蛋白质、材料、科学机器学习与神经算子 | [深度学习](topics/05-deep-learning.md)、[图学习与知识表示](topics/24-graphs.md) |
| 27 · [经典 AI 与规划优化](topics/27-classical-ai.md) | 搜索、博弈、逻辑、约束求解、进化计算与神经符号 | [编程与计算机基础](topics/02-programming.md) |

## 当前覆盖深度

所有 27 个入口均提供学习导读与资源；仓库内可运行实验只有回归、检索、attention 和显存估算四项。微调、GPU、分布式、机器人与科学计算实验需要按任务书或外部课程另行完成。

| 相关方向 | 当前入口 | 尚未单独展开的部分 |
|---|---|---|
| 语音、音乐、视频、3D | [生成与多模态](topics/10-generative-multimodal.md)、[视觉](topics/07-computer-vision.md) | 独立音频课程、实时视频工程和空间重建完整路线 |
| 联邦学习、隐私计算、可解释性 | [安全](topics/15-evaluation-safety.md)、[端侧](topics/21-edge-ai.md)、[因果](topics/25-causal-probabilistic.md) | 差分隐私推导、密码协议与联邦训练实作 |
| AutoML、元学习、持续学习 | [机器学习](topics/04-machine-learning.md)、[深度学习](topics/05-deep-learning.md) | 独立算法课程和灾难性遗忘实验 |
| 医疗、金融、法律、教育等行业 AI | [AI for Science](topics/26-ai-for-science.md)、[评估](topics/15-evaluation-safety.md) | 行业规范、领域知识与真实部署验证，不能仅靠通用 AI 课程替代 |
| 多智能体博弈、神经符号、进化计算 | [强化学习](topics/22-rl-robotics.md)、[经典 AI](topics/27-classical-ai.md) | 研究级专题与更多可运行案例 |

这些是后续可扩展方向，不作为已经完成的独立课程宣传。贡献新分支时，先补先修、主教材、实践与验收，再加入目录。

[资源目录](resources.md) · [项目任务](projects/README.md) · [调研与来源](research/README.md)
