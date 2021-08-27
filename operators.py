import numpy as np


### Selection


def select_linear(nhood, fitness):
    n = nhood.shape[0] - 1
    # r = n * (n + 1) / 2
    sorted_idx = np.argsort(fitness[1:])

    # TODO: which way should I do this?
    # probs = np.arange(n, 0, -1) / r
    # print(fitness[1:])
    # print(sorted_idx)
    # print(probs)
    probs  = np.array([1 / (i + 1) for i in range(n)])
    probs /= np.sum(probs)
    # print(probs)
    return np.random.choice(sorted_idx, p=probs)


### Recombination


def recomb_singlepoint(a, b):
    n = a.shape[0]
    idx = np.random.randint(1, n)
    c = np.concatenate([a[:idx], b[idx:]])
    return c


### Mutation


def mutate_gaussian(mu, sigma=0.1):
    n = mu.shape[0]
    return mu + sigma * np.random.randn(n)


### Replacement


def replace_always():
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
    nhood     = np.array([population[x][y] for x, y in nhood_idx])
    nhood_fit = np.array([fitness[x][y]    for x, y in nhood_idx])
    return nhood, nhood_fit


def nhood_set(population, nhood, nhood_idx):
    for i, (x, y) in enumerate(nhood_idx): population[x][y] = nhood[i]