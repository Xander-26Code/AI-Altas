import math
import unittest
from examples.linear_regression import fit, loss_and_gradient, make_data
from examples.attention import attention
from examples.retrieval import Retriever, evaluate, DOCUMENTS
from examples.memory_budget import estimate


class RegressionTests(unittest.TestCase):
    def test_gradient_matches_finite_difference(self):
        data, w, b, eps = [(1, 3), (-2, -4), (0.5, 2)], 0.7, -0.3, 1e-6
        _, dw, db = loss_and_gradient(data, w, b)
        numerical_w = (loss_and_gradient(data, w + eps, b)[0] - loss_and_gradient(data, w - eps, b)[0]) / (2 * eps)
        numerical_b = (loss_and_gradient(data, w, b + eps)[0] - loss_and_gradient(data, w, b - eps)[0]) / (2 * eps)
        self.assertAlmostEqual(dw, numerical_w, places=5)
        self.assertAlmostEqual(db, numerical_b, places=5)

    def test_recovers_signal_and_generalizes(self):
        train = make_data(200, 42)
        w, b, initial = fit(train)
        self.assertAlmostEqual(w, 3.0, delta=0.08)
        self.assertAlmostEqual(b, 2.0, delta=0.04)
        self.assertLess(loss_and_gradient(make_data(200, 111), w, b)[0], 0.03)
        self.assertGreater(initial, 1)

    def test_empty_rejected(self):
        with self.assertRaises(ValueError):
            fit([])


class AttentionTests(unittest.TestCase):
    def test_causal_invariance(self):
        q = [[1.,0.],[0.,1.],[1.,1.]]
        v = [[1.,2.],[3.,4.],[5.,6.]]
        before, weights = attention(q, q, v)
        after, _ = attention(q, q[:2] + [[999., -333.]], v[:2] + [[12345., 777.]])
        self.assertEqual(before[:2], after[:2])
        self.assertEqual(weights[0], [1.,0.,0.])
        for row in weights:
            self.assertAlmostEqual(sum(row), 1)

    def test_uniform_attention_is_mean(self):
        out, _ = attention([[0.,0.]], [[1.,2.],[3.,4.]], [[2.],[6.]], causal=False)
        self.assertEqual(out, [[4.]])

    def test_numerical_stability(self):
        out, weights = attention([[1000.]], [[1000.]], [[2.]])
        self.assertTrue(math.isfinite(out[0][0]))
        self.assertEqual(weights, [[1.]])

    def test_bad_dimensions_rejected(self):
        with self.assertRaises(ValueError):
            attention([[1.,2.]], [[1.]], [[1.]])


class RetrievalTests(unittest.TestCase):
    def test_unknown_or_empty_returns_no_evidence(self):
        index = Retriever(DOCUMENTS)
        self.assertEqual(index.search(''), [])
        self.assertEqual(index.search('xyzunknownterm'), [])

    def test_metric_uses_all_relevant_documents(self):
        index = Retriever([{'id':'a','text':'apple'}, {'id':'b','text':'banana'}])
        metrics = evaluate(index, [('apple', {'a','b'})], 1)
        self.assertEqual(metrics['recall_at_k'], 0.5)
        self.assertEqual(metrics['mrr_at_k'], 1.0)

    def test_misses_do_not_inflate_mrr(self):
        index = Retriever([{'id':'a','text':'apple'}])
        result = evaluate(index, [('banana', {'a'})])
        self.assertEqual(result['mrr_at_k'], 0)
        self.assertEqual(result['recall_at_k'], 0)

    def test_invalid_k_and_ids(self):
        with self.assertRaises(ValueError):
            Retriever(DOCUMENTS).search('GPU', 0)
        with self.assertRaises(ValueError):
            Retriever([DOCUMENTS[0], DOCUMENTS[0]])


class MemoryTests(unittest.TestCase):
    def test_known_kv_size(self):
        self.assertEqual(estimate()['kv_cache_gib'], 0.5)

    def test_batch_and_context_scale_cache_not_weights(self):
        a, b = estimate(), estimate(batch=4, sequence=8192)
        self.assertEqual(a['weights_gib'], b['weights_gib'])
        self.assertEqual(b['kv_cache_gib'], a['kv_cache_gib'] * 8)

    def test_quantization_does_not_shrink_kv_implicitly(self):
        a, b = estimate(), estimate(weight_bits=4)
        self.assertEqual(b['weights_gib'], a['weights_gib'] / 4)
        self.assertEqual(a['kv_cache_gib'], b['kv_cache_gib'])

    def test_invalid_size(self):
        with self.assertRaises(ValueError):
            estimate(batch=0)


if __name__ == '__main__':
    unittest.main()
