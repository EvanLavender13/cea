import numpy as np


### Selection


def select_linear(nhood, fitness):
    print(nhood)
    print(fitness)

    return nhood


### Neighborhoods


def linear_nhood(x, y, dimensions, n=5):
    idx = 0
    z = n // 4
    xmax, ymax = dimensions

    neighborhood = np.zeros((n, 2), dtype=int)
    neighborhood[idx] = [x, y] # center point
    idx += 1

    # add horizontal / column points
    for i in range(y - 1, y - z - 1, -1):
        neighborhood[idx] = [x, (ymax + i) % ymax]
        idx += 1
    for i in range(y + 1, y + z + 1):
        neighborhood[idx] = [x, (ymax + i) % ymax]
        idx += 1
    
    # add vertical / row points
    for j in range(x - 1, x - z - 1, -1):
        neighborhood[idx] = [(xmax + j) % xmax, y]
        idx += 1
    for j in range(x + 1, x + z + 1):
        neighborhood[idx] = [(xmax + j) % xmax, y]
        idx += 1

    return neighborhood


def get_nhood(population, fitness, nhood_idx):
    nhood     = np.array([population[x][y] for x, y in nhood_idx])
    nhood_fit = np.array([fitness[x][y]    for x, y in nhood_idx])
    return nhood, nhood_fit