"""Character-bigram TF-IDF retrieval over an original tiny Chinese corpus.

This is evidence retrieval, not an LLM/RAG answer generator. The self-check
queries are demonstrations, not a held-out benchmark of real retrieval quality.
"""
import argparse
import collections
import json
import math
import re

DOCUMENTS = [
    {'id':'rag', 'text':'检索增强生成通过查找外部资料，为回答提供引用和证据。减少模型幻觉需要验证引用是否支持结论；没有证据时应拒答。'},
    {'id':'lora', 'text':'LoRA 微调冻结底座权重，训练低秩适配器。它减少可训练参数，但模型权重和激活仍然占用显存。'},
    {'id':'kv', 'text':'KV Cache 保存注意力的键和值，减少自回归推理的重复计算。长上下文和高并发会增加缓存显存。'},
    {'id':'split', 'text':'训练集用于拟合参数，验证集用于选择超参数，测试集用于最终评估。先划分数据，再在训练集拟合预处理，避免数据泄漏。'},
    {'id':'gpu', 'text':'GPU 算子优化需要测量计算、内存带宽和启动开销。比较性能前应预热、同步并验证数值正确性。'},
    {'id':'agent', 'text':'Agent 工具调用需要输入校验、权限限制、超时与最大步数。执行带副作用的动作时还需要防止重复执行。'},
    {'id':'rl', 'text':'强化学习通过状态、动作和奖励学习策略，关注长期回报。评估应使用独立回合和多个随机种子。'},
    {'id':'causal', 'text':'因果推断研究干预会如何改变结果。观测相关性不等于因果效应，需要检查混杂和识别假设。'},
]
DEMO_QUERIES = [('如何减少模型幻觉', {'rag'}), ('什么是数据泄漏', {'split'}),
                ('微调为什么仍然占显存', {'lora'}), ('因果效应如何识别', {'causal'})]


def tokenize(text):
    # Adjacent Chinese character pairs avoid a dependency on a word segmenter.
    tokens = []
    for part in re.findall(r'[\u4e00-\u9fff]+|[a-z0-9]+', text.lower()):
        if re.fullmatch(r'[\u4e00-\u9fff]+', part):
            tokens.extend(part[i:i + 2] for i in range(len(part) - 1))
            if len(part) == 1:
                tokens.append(part)
        else:
            tokens.append(part)
    return tokens


class Retriever:
    def __init__(self, documents):
        if not documents:
            raise ValueError('documents must not be empty')
        if len({d['id'] for d in documents}) != len(documents):
            raise ValueError('document IDs must be unique')
        self.documents = documents
        counts = [collections.Counter(tokenize(d['text'])) for d in documents]
        df = collections.Counter(t for c in counts for t in c)
        self.idf = {t: math.log((1 + len(counts)) / (1 + n)) + 1 for t, n in df.items()}
        self.vectors = [self.vector(c) for c in counts]

    def vector(self, counts):
        raw = {t: n * self.idf[t] for t, n in counts.items() if t in self.idf}
        norm = math.sqrt(sum(v * v for v in raw.values()))
        return {t: v / norm for t, v in raw.items()} if norm else {}

    def search(self, query, k=3):
        if k <= 0:
            raise ValueError('k must be positive')
        q = self.vector(collections.Counter(tokenize(query)))
        results = []
        for doc, vec in zip(self.documents, self.vectors):
            score = sum(v * vec.get(t, 0) for t, v in q.items())
            if score > 0:
                results.append(dict(**doc, score=score))
        return sorted(results, key=lambda r: (-r['score'], r['id']))[:k]


def evaluate(retriever, queries, k=3):
    if not queries:
        raise ValueError('queries must not be empty')
    recalls, reciprocal_ranks = [], []
    for query, relevant in queries:
        if not relevant:
            raise ValueError('recall requires at least one relevant document')
        ids = [r['id'] for r in retriever.search(query, k)]
        recalls.append(len(set(ids) & relevant) / len(relevant))
        ranks = [i + 1 for i, ident in enumerate(ids) if ident in relevant]
        reciprocal_ranks.append(1 / min(ranks) if ranks else 0)
    return {'recall_at_k': sum(recalls) / len(recalls),
            'mrr_at_k': sum(reciprocal_ranks) / len(reciprocal_ranks), 'k': k, 'queries': len(queries)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--query', default='如何减少模型幻觉')
    parser.add_argument('--top-k', type=int, default=3)
    parser.add_argument('--evaluate', action='store_true')
    args = parser.parse_args()
    retriever = Retriever(DOCUMENTS)
    result = evaluate(retriever, DEMO_QUERIES, args.top_k) if args.evaluate else retriever.search(args.query, args.top_k)
    print(json.dumps(result or {'message':'没有匹配证据；此示例不生成答案'}, ensure_ascii=False, indent=2))
