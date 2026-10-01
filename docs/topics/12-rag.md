# 12 · RAG 与知识系统

> 目标：建立能够检索、引用、拒答并遵守文档权限的知识问答系统；能区分检索失败与生成失败。
> 先修：Python、基本文本处理、向量相似度、HTTP；了解语言模型上下文。建议规划 80–140 小时。这是完成先修后系统学习主教材、练习和一个项目的规划预算，不含补先修，不等于掌握整个领域。

## 资源列表

资料阅读免费；数据库托管和模型服务可能收费。先用本地小数据确认正确性。核实日期：2026-09-30。

| 资源 | 语言 / 级别 | 费用 / 算力 | 为什么推荐、读哪部分 |
| --- | --- | --- | --- |
| [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) | 英文 / 进阶 | 免费 / 无 | 读参数记忆与非参数记忆、RAG-Sequence/Token；区分原始训练方法和今日应用管线。 |
| [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) | 英文 / 进阶 | 免费 / 可选GPU | 读完整双阶段检索例子，先复现召回再加CrossEncoder；用于定位相关性与延迟取舍。 |
| [Elasticsearch: Reciprocal Rank Fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) | 英文 / 进阶 | 免费 / CPU | 先读RRF公式与手算示例，再研究查询实现；融合分数不同量纲的检索列表。 |
| [pgvector](https://github.com/pgvector/pgvector) | 英文 / 进阶 | 免费 / CPU | 读距离函数、HNSW/IVFFlat和过滤部分；适合把向量检索与已有Postgres数据模型结合。 |
| [Faiss Wiki](https://github.com/facebookresearch/faiss/wiki) | 英文 / 进阶 | 免费 / 可选GPU | 先读相似度搜索和索引选择，再在固定向量集比较准确率、延迟与内存。 |
| [BEIR](https://github.com/beir-cellar/beir) | 英文 / 进阶 | 免费 / 可选GPU | 读数据格式和评估示例，学习跨数据集检索评估；先选小子集，不急着跑全套。 |
| [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | 英文 / 进阶 | 免费 / 无 | 读证据位置实验和评估协议；为自己的模型重做位置对照，不直接套用旧模型结论。 |

### 补充课程与实作资源

| 资源 | 语言 · 难度 | 获取 · 算力 | 用法与阅读范围 |
|---|---|---|---|
| [Datawhale · LLM Universe](https://github.com/datawhalechina/llm-universe) | 中文 · 入门 | 免费 · CPU | 选第一部分 API、知识库、RAG、评估与优化；进阶部分仍有在编内容。核对依赖版本，API 费用另计。 |
| [DataTalks.Club · LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | 英文 · 进阶 | 免费 · CPU | 选 RAG、Vector Search、Evaluation、Monitoring 和项目；先完成普通检索基线，再扩展 agentic 流程。 |

以上新增入口核实于 2026-10-01；资料免费不含硬件与 API 费用。

## 按资源安排学习顺序

中文选 LLM Universe 第一部分，英文选 LLM Zoomcamp。先跑检索与评估，再引入混合检索和生成优化。

按顺序完成主线，每步完成右列产出后再推进；选修不计入必做清单。页首时长包含所选主线、练习与本页项目，不包含把全部资料逐一学完。

| 阶段 | 使用资源 | 阅读 / 练习范围 | 完成后应留下什么 |
|---|---|---|---|
| 1 · RAG 主课 | [Datawhale · LLM Universe](https://github.com/datawhalechina/llm-universe)；[DataTalks.Club · LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) | 文档加载、清洗、切片、检索问答与评估 | 建一份带来源的知识库和问题集 |
| 2 · 提升检索 | [Sentence Transformers: Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)；[Elasticsearch: Reciprocal Rank Fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion) | Retrieve & Re-Rank，再读 RRF 公式与示例 | 比较单路召回、融合、重排的效果 |
| 3 · 索引与评估 | [pgvector](https://github.com/pgvector/pgvector)；[Faiss Wiki](https://github.com/facebookresearch/faiss/wiki)；[BEIR](https://github.com/beir-cellar/beir) | pgvector 或 Faiss 二选一；BEIR 数据格式与评估 | 在固定数据上记录召回率、耗时和内存 |
| 4 · 生成诊断 | [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)；[Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172) | 原始 RAG 方法；Lost in the Middle 实验协议 | 检查引用、无答案情况和证据位置敏感性 |

## 实践：给本 Wiki 建一个可验证的问答器

选择 30 篇公开文档，保存来源与版本，构造 50 道问题：30 道单文档题、10 道需要两份证据的题、10 道语料没有答案的题。每道可回答题标注证据 ID，而不只写标准答案。将问题划为开发集和最终测试集。

依次运行：关键词基线、向量检索、两者 RRF 融合、融合加重排。每次只改变一个环节，保存前 10 条候选。随后接生成器，要求输出答案和证据 ID；验证这些 ID 确实来自当前请求的授权候选。对摘要式答案人工检查每条关键主张是否有支持。

另外复制两份内容相似但权限不同的测试文档，分别授予用户甲和乙访问；加入一份旧版本和一份新版；最后删除其中一份。检查切换用户、命中缓存、更新索引和引用跳转后的行为。练习采用虚构信息，避免引入真实敏感资料。

**验收标准**：交付数据清单、50 题标注集、4 组检索对照表、失败分类和运行配置；测试集至少有一组明确超越关键词基线，若没有则保留基线并解释原因；越权文档不能进入模型上下文；10 道无答案题逐项记录拒答；删除后不再返回已删除文档。对照结果应真实填写，不能为了“达标”改写标注。

## 常见误区

- **“有引用就不会幻觉。”** 引用可能存在但不支持结论，必须检查主张与证据的对应关系。
- **“上下文越长越好。”** 更多内容可能增加干扰；[Lost in the Middle](https://arxiv.org/abs/2307.03172) 提醒我们关注证据位置与使用能力。
- **“换向量数据库就能提高语义质量。”** 数据解析、embedding、查询和排序通常也需要独立排查。
- **“RAG 与微调只能选一个。”** RAG 适合更新可追溯知识；微调适合改变任务行为，两者可以组合。

## 下一步

动态查询与多步检索进入 [Agents](13-agents.md)；为知识系统建立持续回归，进入 [评估与安全](15-evaluation-safety.md)。

[返回知识地图](../map.md) · [选择学习路线](../roadmaps/README.md)
