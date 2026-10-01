# 项目 02 · 无需模型的中文检索与评估

目标：理解检索是怎样提供证据的。源码为 `examples/retrieval.py`，包含 8 条原创短文档和演示查询。使用中文字符二元组、英文词元、TF-IDF 与余弦相似度；不调用生成模型。

```bash
python3 examples/retrieval.py --query "如何减少模型幻觉"
python3 examples/retrieval.py --query "xyzunknownterm"
python3 examples/retrieval.py --evaluate --top-k 3
```

输出含文档 ID、证据文本和相似度；无共享词元时返回没有匹配证据。相似度不是答案正确率，也不是校准过的置信度。内置查询用于演示指标计算，不能当作独立质量测试集。

## 做成自己的实验

1. 准备有授权的 20–50 篇短文，保留来源和 ID。
2. 单独编写至少 30 个测试问题，包含改写、多答案和库外问题，人工标记相关文档。
3. 用开发集选择 tokenization、top-k 和拒答条件；锁定测试集。
4. 比较词法检索与一个可用的 embedding 基线，记录 Recall@k、MRR、库外拒答与延迟。

验收时要解释：召回了多个相关文档时 Recall 如何计算；正确结果在第 1 和第 3 名时 MRR 有何差别；没有命中的查询为什么也必须计入平均值。

该脚本没有实现生成、权限过滤和生产索引。把它扩展成 RAG 时，按 [RAG 章节](../topics/12-rag.md) 加入引用验证和独立的答案质量评估。

[项目目录](README.md) · [推荐搜索](../topics/23-recommendation-search.md)
