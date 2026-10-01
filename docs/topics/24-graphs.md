# 24 · 图学习与知识表示

> 目标：把关系结构建模为图，区分知识图谱、图算法与图神经网络。先修：[线性代数](01-math.md)、[机器学习](04-machine-learning.md)、[深度学习](05-deep-learning.md)。具备先修后，系统学习主教材、做练习并完成一个项目，建议预留 **100–180 小时**。补先修另计，不代表掌握全部图学习方法。

## 资源列表

| 资源 | 语言 / 难度 / 费用 / 算力 | 建议读法 |
|---|---|---|
| [NetworkX 文档](https://networkx.org/documentation/stable/) | 英文 / 入门 / 免费 / CPU | 先练图构造、路径和中心性；让数据结构变得直观 |
| [W3C RDF Primer](https://www.w3.org/TR/rdf11-primer/) | 英文 / 入门 / 免费 / 无 | 阅读三元组、IRI 与 Turtle，理解交换格式；这是入门说明文档 |
| [Stanford CS224W](https://cs224w.stanford.edu/) | 英文 / 进阶 / 免费公开资料 / 可选 GPU | 图学习主线；选择与当前基础匹配的公开讲义和作业 |
| [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/) | 英文 / 进阶 / 免费 / 可选 GPU | 跟 Introduction by Example 做小图，再学 mini-batch 与采样 |
| [Open Graph Benchmark](https://ogb.stanford.edu/) | 英文 / 研究 / 免费 / 可选 GPU | 观察官方切分和 evaluator，避免自定义切分使结果不可比 |

## 按资源安排学习顺序

先学图结构，再按图神经网络或知识图谱分支深入。CS224W 是图学习主课，RDF 是知识表示分支。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 图操作 | [NetworkX 文档](https://networkx.org/documentation/stable/) | 图构造、路径、中心性 | 给小图建立非神经基线 |
| 2 · 图学习 | [Stanford CS224W](https://cs224w.stanford.edu/) | 消息传递、图表示和对应公开作业 | 解释节点/边/图任务的数据切分 |
| 3 · 实现与评估 | [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/en/latest/)；[Open Graph Benchmark](https://ogb.stanford.edu/) | PyG 小图、batch、采样；OGB 划分与评估器 | 跑一个小图任务并核对官方指标 |
| 选修 · 知识表示 | [W3C RDF Primer](https://www.w3.org/TR/rdf11-primer/) | RDF 三元组、IRI 和 Turtle | 把一个小知识集表示成图并验证查询 |

## 实践：引用网络分类

选择公开小型引用图，记录数据许可和官方切分。做三个基线：只预测最多类别；仅用节点特征的 MLP；同时使用图结构的 GCN。保持训练轮数预算和调参次数尽量一致，比较宏平均 F1、各类别表现与峰值内存。

验收需提供：图的节点/边数量、切分说明、三种模型的多种子结果，以及两项消融——随机打乱边、移除节点特征。若 GCN 没有胜出，应解释结构噪声、同配性或超参数影响，而不是删除失败结果。增加节点重编号检查，确认预测没有意外依赖编号。

知识图谱方向可以给 30 个 AI 概念手工建立“先修于/用于/实现于”关系，加上每条边的证据。比较普通词法检索与一跳扩展检索；这也是改进本 Wiki 知识导航的可贡献项目。

## 易踩的坑

- 一张图画得复杂不代表关系质量高，错误实体合并会污染所有下游路径。
- GraphRAG 不是对所有语料都有效，应先确认问题需要跨实体关系。
- 某个图 benchmark 的好成绩不能证明对新图、新时间段或新关系泛化。

下一步：[推荐与检索](23-recommendation-search.md)、[AI for Science](26-ai-for-science.md)、[经典 AI](27-classical-ai.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
