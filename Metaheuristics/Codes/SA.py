import random
import math
import numpy as np


def iterarSA(maxIter, iter, dimension, population, best, lb, ub, t, fitness_func):
    population = np.array(population)
    bestSolution = np.array(best)
    new_population = population.copy()

    for i in range(len(population)):
        candidate = population[i].copy()
        idx = np.random.randint(dimension)
        candidate[idx] = 1 - candidate[idx]
        _, candidate_fitness = fitness_func(candidate)
        _, current_fitness = fitness_func(population[i])

        if candidate_fitness < current_fitness:  # Minimización
            new_population[i] = candidate
        else:
            acceptance_probability = math.exp((current_fitness - candidate_fitness) / t) if t > 0 else 0
            if random.random() < acceptance_probability:
                new_population[i] = candidate

        # Limita los valores dentro de lb y ub
        for j in range(dimension):
            if new_population[i][j] < lb[j]:
                new_population[i][j] = lb[j]
            elif new_population[i][j] > ub[j]:
                new_population[i][j] = ub[j]

    # Enfriamiento
    t = t * (1 - (iter / maxIter))
    return np.array(new_population)
