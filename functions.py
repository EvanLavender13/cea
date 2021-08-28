import numpy as np


### https://en.wikipedia.org/wiki/Test_functions_for_optimization


def ackley(p):
    x, y = p
    a = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x ** 2 + y ** 2)))
    b = -np.exp(0.5 * np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)) + np.e + 20.0
    return a + b


def easom(p):
    x, y = p
    exp = np.exp(-((x - np.pi) ** 2 + (y - np.pi) ** 2))
    return -np.cos(x) * np.cos(y) * exp


def himmelblau(p):
    x, y = p
    return (x ** 2 + y - 11) ** 2 + (x + y ** 2 - y) ** 2


def holder_table(p):
    x, y = p
    exp = np.exp(np.abs(1 - (np.sqrt(x ** 2 + y ** 2) / np.pi)))
    return -np.abs(np.sin(x) * np.cos(y) * exp)


def rastrigin(x, A=10):
    n = x.shape[0]
    return A * n + np.sum(x ** 2 - A * np.cos(2 * np.pi * x))


def rosenbrock(p, a=1, b=100):
    x, y = p
    return (a - x) ** 2 + b * (y - x ** 2) ** 2