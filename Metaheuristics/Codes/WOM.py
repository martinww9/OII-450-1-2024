import random
import numpy as np

# Inicializar la población
def initialize_population(N, dimension, lower_bound, upper_bound):
    return (lower_bound + np.random.rand(N, dimension) * (upper_bound - lower_bound)).astype(np.float64)


# Fase de forrajeo (exploración)
def foraging_phase(i, population, fitness, r):
    better_positions = [k for k in range(len(fitness)) if fitness[k] < fitness[i] and k != i]
    if better_positions:  # Si existen mejores posiciones
        SFP = population[random.choice(better_positions)].astype(np.float64)  # Asegúrate de que SFP sea float
        I = random.randint(1, 2)  # Valor aleatorio 1 o 2
        # Cambiar el tipo de population[i] a float
        population[i] = population[i].astype(np.float64) + r * (SFP - I * population[i])
    return population[i]


# Fase de escape
def escape_phase(i, population, r, t, lower_bound, upper_bound):
    # Aquí se asegura que population sea un numpy array
    population = np.array(population) 

    # Cambiar el acceso a population[i, j] para que funcione con numpy
    new_position = population[i] + (1 - 2 * r) * (upper_bound - lower_bound) / t

    # Asegurarse de que los nuevos valores están dentro de los límites
    return np.clip(new_position, lower_bound, upper_bound)

# Wombat Optimization Algorithm (adaptado)
def iterarWOM(maxIter, t, dimension, population, bestSolution):
    population = np.array(population).astype(np.float64)  # Cambiar a float64

    lower_bound = -10  # Límite inferior
    upper_bound = 10   # Límite superior

    # Evaluar la función objetivo para la población actual
    fitness = np.sum(population**2, axis=1)  # Vectorizar la evaluación de fitness

    for it in range(maxIter):  # Cambié el bucle para que sea más claro
        t = 1 - (it / maxIter)  # Recalcular t en cada iteración
        t = max(t, 1e-10)  # Evitar la división por cero

        for i in range(population.shape[0]):
            r = random.uniform(0.0, 1.0)

            # Fase de forrajeo
            new_position = foraging_phase(i, population, fitness, r)

            # Evaluar nueva posición
            new_fitness = np.sum(new_position**2)
            if new_fitness < fitness[i]:
                population[i] = new_position
                fitness[i] = new_fitness

            # Fase de escape
            new_position = escape_phase(i, population, r, t, lower_bound, upper_bound)

            # Evaluar nueva posición
            new_fitness = np.sum(new_position**2)
            if new_fitness < fitness[i]:
                population[i] = new_position
                fitness[i] = new_fitness

    return population