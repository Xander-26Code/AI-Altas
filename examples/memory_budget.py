"""Illustrative weight + KV-cache estimate; this is NOT a capacity benchmark."""
import argparse
import json


def estimate(parameters_b=7, weight_bits=16, layers=32, kv_heads=8,
             head_dim=128, sequence=4096, batch=1, kv_bytes=2):
    values = [parameters_b, weight_bits, layers, kv_heads, head_dim, sequence, batch, kv_bytes]
    if any(v <= 0 for v in values):
        raise ValueError('all model and workload parameters must be positive')
    weights = parameters_b * 1_000_000_000 * weight_bits / 8
    kv = 2 * layers * kv_heads * head_dim * sequence * batch * kv_bytes
    return dict(weights_gib=weights / 2**30, kv_cache_gib=kv / 2**30,
                subtotal_gib=(weights + kv) / 2**30,
                excluded='activations, runtime, temporary buffers, quantization metadata, fragmentation; actual engine layout may differ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--parameters-b', type=float, default=7)
    parser.add_argument('--weight-bits', type=int, default=16)
    parser.add_argument('--layers', type=int, default=32)
    parser.add_argument('--kv-heads', type=int, default=8)
    parser.add_argument('--head-dim', type=int, default=128)
    parser.add_argument('--sequence', type=int, default=4096)
    parser.add_argument('--batch', type=int, default=1)
    parser.add_argument('--kv-bytes', type=int, default=2)
    args = parser.parse_args()
    print(json.dumps(estimate(**vars(args)), indent=2))
