
import time

import numpy as np

from operators import nhood_get

def cea_gen(population, fitness, dimensions, f_evaluate, f_nhood, f_select, f_recomb, f_mutate):
    start = time.time()
    dimx, dimy = dimensions

    rangex = range(dimx)
    rangey = range(dimy)

    pb_mutate = 0.1 # TODO: make parameter

    frame   = np.zeros(dimensions)
    pop_new = np.zeros_like(population)
    for x in rangex:
        for y in rangey:
            nhood_idx = list(f_nhood(x, y, dimensions))
            nhood, nhood_fit = nhood_get(population, fitness, nhood_idx)
            a, b = f_select(nhood, nhood_fit)
            c = f_recomb(nhood[a], nhood[b])
            p = np.random.random()
            if p < pb_mutate: c = f_mutate(c)
            pop_new[x][y] = c # TODO: replacement policies?

    population[:] = pop_new
    fitness = f_evaluate(population)
    end = time.time()
    return population, fitness
    