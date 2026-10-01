"""Single-head scaled dot-product attention, including a causal mask."""
import json
import math


def attention(query, key, value, causal=True):
    if not query or not key or not value or len(key) != len(value):
        raise ValueError('non-empty Q/K/V required, and K/V lengths must match')
    dim, value_dim = len(key[0]), len(value[0])
    if dim == 0 or value_dim == 0:
        raise ValueError('feature dimensions must be positive')
    if any(len(row) != dim for row in query + key) or any(len(row) != value_dim for row in value):
        raise ValueError('inconsistent feature dimensions')
    if causal and len(query) != len(key):
        raise ValueError('this educational causal implementation requires equal Q/K lengths')
    output, weights = [], []
    for i, q in enumerate(query):
        scores = [sum(a * b for a, b in zip(q, k)) / math.sqrt(dim) for k in key]
        allowed = [j for j in range(len(key)) if not causal or j <= i]
        maximum = max(scores[j] for j in allowed)
        row = [math.exp(s - maximum) if j in allowed else 0.0 for j, s in enumerate(scores)]
        total = sum(row)
        row = [x / total for x in row]
        output.append([sum(row[j] * value[j][d] for j in range(len(key))) for d in range(value_dim)])
        weights.append(row)
    return output, weights


if __name__ == '__main__':
    q = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
    values = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]
    result, weights = attention(q, q, values)
    print(json.dumps(dict(output=result, attention_weights=weights), indent=2))
