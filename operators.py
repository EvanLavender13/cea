import numpy as np


### Selection


def select_linear(nhood, fitness):
    n = nhood.shape[0]
    r = n * (n + 1) / 2
    sorted_idx = np.argsort(fitness)

    # TODO: which way should I do this?
    probs = np.arange(1, n + 1) / r
    # probs  = np.array([1 / (i + 1) for i in range(n)])
    # probs /= np.sum(probs)
    # print(fitness)
    # print(sorted_idx)
    # print(probs)
    return np.random.choice(sorted_idx, size=2, p=probs)


def select_roulette(nhood, fitness):
    n = nhood.shape[0] - 1
    sorted_idx = np.argsort(fitness[1:])
    print(fitness[1:])
    print(sorted_idx)
    probs = 1.0 - (fitness[1:] / np.sum(fitness[1:]))
    probs /= np.sum(probs)
    print(probs)

    return 1


### Recombination


def recomb_singlepoint(a, b):
    n = a.shape[0]
    idx = np.random.randint(1, n)
    c = np.concatenate([a[:idx], b[idx:]])
    return c


def recomb_ordered(a, b):
    n = a.shape[0]
    c = -np.ones(n, dtype=int)
    i, j = sorted(np.random.choice(n, size=2, replace=False))
    c[i:j] = a[i:j]
    for k in b:
        if k not in c:
            for l in range(n):
                if c[l] == -1: 
                    c[l] = k
                    break
    return c


### Mutation

# TODO
def mutate_uniform(a, low=0.0, high=1.0):
    n = a.shape[0]
    return n


def mutate_gaussian(a, sigma=0.1):
    return a + sigma * np.random.randn()


def mutate_swap(a):
    n = a.shape[0]
    i, j = np.random.choice(n, size=2, replace=False)
    a[i], a[j] = a[j], a[i]
    return a


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


### Sampling


def sample_uniform(low, high, shape):
    return np.random.uniform(low, high, shape)


def sample_gaussian(shape, sigma=1.0):
    return 1.0 * np.random.randn(*shape)


def sample_intlist(low, high, shape):
    return np.random.random_integers(low, high, shape)


def sample_intperm(n, shape):
    a = np.zeros(shape, dtype=int)
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            a[x][y] = np.random.permutation(n)
    return a