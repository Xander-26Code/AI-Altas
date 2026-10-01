# 23 · 推荐系统与信息检索

> 目标：理解从海量候选到少量结果的流程，能够设计不泄漏未来信息的离线评估。先修：[机器学习](04-machine-learning.md)、[数据工程](03-data.md)。具备先修后，系统学习主教材、做练习并完成一个项目，建议预留 **100–180 小时**。补先修另计；小数据可用 CPU。

## 资源列表

| 资源 | 语言 / 难度 / 费用 / 算力 | 为什么选、读哪部分 |
|---|---|---|
| [信息检索导论](https://nlp.stanford.edu/IR-book/) | 英文 / 入门 / 免费在线版 / CPU | 原作者教材；优先读倒排、评分与评估 |
| [TensorFlow Recommenders](https://www.tensorflow.org/recommenders) | 英文，可切中文 / 进阶 / 免费 / CPU | 官方示例串起数据、召回和排序；安装时核对依赖版本 |
| [Faiss](https://faiss.ai/) | 英文 / 进阶 / 免费 / 可选 GPU | 从精确索引学起，再比较近似索引；无需一开始用 GPU |
| [MovieLens](https://grouplens.org/datasets/movielens/) | 英文 / 入门 / 免费获取、受数据条款约束 / CPU | 提供适合小实验的数据；在项目中记下具体版本并遵守原许可 |
| [TorchRec](https://meta-pytorch.org/torchrec/overview.html) | 英文 / 进阶 / 免费 / 可选 GPU | 理解大 embedding 表、分片和分布式推荐训练 |

## 按资源安排学习顺序

信息检索和推荐共享评估方法，但项目不同。先学检索基础，再在文本检索与用户推荐中选一个。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · 检索基础 | [信息检索导论](https://nlp.stanford.edu/IR-book/) | 倒排、评分、检索评估 | 实现关键词基线和相关性标注 |
| 2 · 任务分支 | [TensorFlow Recommenders](https://www.tensorflow.org/recommenders)；[MovieLens](https://grouplens.org/datasets/movielens/) | 推荐选 TFR 的召回/排序和 MovieLens；纯检索可跳过 | 按时间切分，建立热门或简单检索基线 |
| 3 · 向量召回 | [Faiss](https://faiss.ai/) | 精确索引，再选 ANN 索引 | 比较 recall、内存和检索延迟 |
| 选修 · 大规模推荐 | [TorchRec](https://meta-pytorch.org/torchrec/overview.html) | embedding 表、分片与训练接口 | 估算表大小和通信，不强行启动大规模训练 |

## 实践：推荐结果有没有超越热门榜

使用一个固定版本的 MovieLens 数据，按全局时间边界构造训练、验证和测试，确保每次预测只使用当时可见的信息。先写热门榜，再实现物品协同过滤；有余力再做双塔。明确新用户、新物品的处理策略，并始终在同一候选集比较。

验收材料应包含：时间边界、用户覆盖率、Recall@10、NDCG@10、热门/长尾子组表现、推理延迟和 5 个案例解释。如果负采样测试而不是全量候选测试，报告里必须写明采样策略，不能直接和全量指标比较。

也可以先运行本仓库 [检索实验](../projects/02-retrieval.md)：它不需要下载数据或调用模型，用小型中文知识库把召回、拒答和评估接起来。

## 易踩的坑

- 先按完整数据统计热度，再划分训练测试，会引入未来信息。
- 向量相似度高不保证内容相关，ANN 搜索正确也不保证 embedding 学得好。
- 推荐指标上升可能牺牲多样性、覆盖率或长期目标，需明确业务权衡。
- RAG 引用错误时，先检查候选文档和切块，不能只调生成模型。

下一步：[RAG](12-rag.md)、[图学习](24-graphs.md)、[因果推断](25-causal-probabilistic.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
