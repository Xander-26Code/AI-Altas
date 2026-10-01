# 25 · 概率建模与因果推断

> 目标：表达不确定性，区分预测、干预与反事实问题。先修：[概率统计](01-math.md)、[机器学习](04-machine-learning.md)。具备先修后，系统学习主教材、做练习并完成一个项目，建议预留 **140–260 小时**。补先修另计；入门实验用 CPU。

## 资源列表

| 资源 | 语言 / 难度 / 费用 / 算力 | 建议读法 |
|---|---|---|
| [Probabilistic Machine Learning](https://probml.github.io/pml-book/) | 英文 / 进阶 / 免费在线资料、纸书另售 / CPU | 作者书籍入口；按概率、图模型和推断主题选章 |
| [Stanford CS228 Notes](https://ermongroup.github.io/cs228-notes/) | 英文 / 进阶 / 免费 / 无 | 把表示、推断、学习分开理解，先做小图手算 |
| [PyMC 学习入口](https://www.pymc.io/projects/docs/en/stable/learn.html) | 英文 / 进阶 / 免费 / CPU | 以简单回归做后验和预测检查；诊断收敛再看参数 |
| [Causal Inference: What If](https://miguelhernan.org/whatifbook) | 英文 / 进阶 / 免费作者电子资料 / CPU | 从随机与观测研究的识别假设读起 |
| [DoWhy v0.13 文档](https://www.pywhy.org/dowhy/v0.13/) | 英文 / 进阶 / 免费 / CPU | 将建模、识别、估计与反驳检查区分开；此链接固定版本 |
| [EconML](https://www.pywhy.org/EconML/) | 英文 / 进阶 / 免费 / CPU | 探索异质效应与 double machine learning，不把软件输出当因果证明 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Seeing Theory](https://seeing-theory.brown.edu/) | 英文 · 入门 | 免费 · CPU | 用概率、条件概率、分布与贝叶斯推断交互页面辅助理解；站点已归档，作为补充。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

概率建模先走 PML → CS228/PyMC；因果推断再走 What If → DoWhy。已有概率背景可从因果分支开始。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 概率基础 | [Probabilistic Machine Learning](https://probml.github.io/pml-book/)；[Seeing Theory](https://seeing-theory.brown.edu/) | PML 概率部分；Seeing Theory 仅补直觉 | 做概率模拟并解释后验与预测的区别 |
| 2 · 推断与建模 | [Stanford CS228 Notes](https://ermongroup.github.io/cs228-notes/)；[PyMC 学习入口](https://www.pymc.io/projects/docs/en/stable/learn.html) | CS228 表示/推断；PyMC 入门与预测检查 | 提交一个含诊断的贝叶斯小模型 |
| 3 · 因果识别 | [Causal Inference: What If](https://miguelhernan.org/whatifbook) | What If 的识别假设与研究设计 | 先画因果图并写假设，再决定能否估计 |
| 4 · 因果实验 | [DoWhy v0.13 文档](https://www.pywhy.org/dowhy/v0.13/) | DoWhy 建模、识别、估计、反驳 | 用合成数据检验已知效应 |
| 选修 · 异质效应 | [EconML](https://www.pywhy.org/EconML/) | EconML 对应方法与使用条件 | 检查交叉拟合和识别前提，不只输出效应数值 |

## 实践：在已知真相的数据中识别偏差

自行生成 2,000 条合成记录。让历史活跃度 Z 同时影响是否收到处理 X 和结果 Y，并把真实处理效应固定为 2。比较简单均值差、控制 Z 的回归与一种加权估计。再增加一个没有放进模型的混杂变量，观察估计偏差。

验收包括：数据生成方程、随机种子、因果图、目标量、估计结果与不确定性区间；明确写出哪些假设由模拟器保证、哪些在真实数据里无法直接证明。至少展示一个“置信区间很窄但估计错了”的设定。

概率建模扩展：给小样本二项数据设两个不同先验，比较后验预测。说明小数据时先验影响为何更大，观测增加后如何变化。不要只报告一个均值而隐藏整个分布。

## 易踩的坑

- 随意控制更多变量可能引入选择偏差，变量越多不是越安全。
- SHAP 等归因解释不自动等价于干预效果。
- 因果发现算法输出的图依赖假设与数据质量，不能替代领域判断。
- 高预测准确率、统计显著和实际可行动的效果，是三件不同的事。

下一步：[推荐实验](23-recommendation-search.md)、[数据质量](03-data.md)、[评估与安全](15-evaluation-safety.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
