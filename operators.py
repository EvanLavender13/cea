import numpy as np


### Selection


def select_linear(nhood, fitness):
    n = nhood.shape[0]
    r = n * (n + 1) / 2
    sorted_idx = np.argsort(fitness)

    # TODO: which way should I do this?
    probs = np.arange(n, 0, -1) / r
    # probs  = np.array([1 / (i + 1) for i in range(n)])
    # probs /= np.sum(probs)
    for i in range(n): yield np.random.choice(sorted_idx, size=2, replace=False, p=probs)


### Recombination


def recomb_singlepoint(a, b):
    n = a.shape[0]
    idx = np.random.randint(1, n)
    c = np.concatenate([a[:idx], b[idx:]])
    return c


### Mutation


def something():
    print("a")


### Replacement


def replace_all():
    print("a")


### Neighborhood


def nhood_linear(x, y, dimensions, n=5):
    z = n // 4
    xmax, ymax = dimensions

    # center point
    yield [x, y] 

    # add horizontal / column points
    for i in range(y - 1, y - z - 1, -1): yield [x, (ymax + i) % ymax]
    for i in range(y + 1, y + z + 1):     yield [x, (ymax + i) % ymax]
    
    # add vertical / row points
    for j in range(x - 1, x - z - 1, -1): yield [(xmax + j) % xmax, y]
    for j in range(x + 1, x + z + 1):     yield [(xmax + j) % xmax, y]


def nhood_get(population, fitness, nhood_idx):
    nhood_idx = list(nhood_idx)
    nhood     = np.array([population[x][y] for x, y in nhood_idx])
    nhood_fit = np.array([fitness[x][y]    for x, y in nhood_idx])
    return nhood, nhood_fit