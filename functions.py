import numpy as np

def rastrigin(x, A=10):
    n = x.shape[0]
    return A * n + np.sum(x ** 2 - A * np.cos(2 * np.pi * x))