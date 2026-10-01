"""Learn y = w*x+b from synthetic data; no network or third-party packages."""
import json
import random


def make_data(size=200, seed=42):
    rng = random.Random(seed)
    return [(x, 3.0 * x + 2.0 + rng.gauss(0, 0.1))
            for x in [rng.uniform(-1, 1) for _ in range(size)]]


def loss_and_gradient(data, weight, bias):
    if not data:
        raise ValueError('data must not be empty')
    errors = [(weight * x + bias - y, x) for x, y in data]
    n = len(data)
    return (sum(e * e for e, _ in errors) / n,
            2 * sum(e * x for e, x in errors) / n,
            2 * sum(e for e, _ in errors) / n)


def fit(data, epochs=500, learning_rate=0.1):
    if epochs < 1 or learning_rate <= 0:
        raise ValueError('positive epochs and learning rate required')
    weight, bias = 0.0, 0.0
    initial = loss_and_gradient(data, weight, bias)[0]
    for _ in range(epochs):
        _, dw, db = loss_and_gradient(data, weight, bias)
        weight -= learning_rate * dw
        bias -= learning_rate * db
    return weight, bias, initial


def main():
    train, test = make_data(200, 42), make_data(80, 2026)
    weight, bias, initial = fit(train)
    print(json.dumps(dict(weight=weight, bias=bias, initial_train_mse=initial,
                          train_mse=loss_and_gradient(train, weight, bias)[0],
                          test_mse=loss_and_gradient(test, weight, bias)[0]), indent=2))


if __name__ == '__main__':
    main()
