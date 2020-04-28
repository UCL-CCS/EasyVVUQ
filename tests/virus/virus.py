import numpy as np
from scipy.spatial.distance import cdist
import scipy.stats as stats
import matplotlib.pyplot as plt
import sys
import json


class Population:
    def __init__(self, grid_size, n, duration, mortality):
        self.grid_size = grid_size
        self.n = n
        self.duration = duration
        self.mortality = mortality
        self.x = np.random.randint(0, grid_size, (n, 2))
        self.ill = np.array([duration] + [0] * (n - 1))
        self.immune = np.array([0] * n)

    def move(self):
        self.x += np.random.randint(-1, 2, (self.n, 2))
        self.x = np.remainder(self.x, self.grid_size)
        for i, x1 in enumerate(self.x):
            for j, x2 in enumerate(self.x):
                if i != j:
                    if ((x1 == x2).all() and
                        self.ill[j] > 0 and
                            self.ill[i] == 0 and not self.immune[i]):
                        self.ill[i] = self.duration
                        self.immune[i] = 1
        to_delete = []
        for i, status in enumerate(self.ill):
            if status > 1:
                self.ill[i] -= 1
            elif status == 1:
                self.ill[i] = 0
                if np.random.random() < self.mortality:
                    if self.n > 0:
                        to_delete.append(i)
        self.x = np.delete(self.x, to_delete, axis=0)
        self.ill = np.delete(self.ill, to_delete)
        self.immune = np.delete(self.immune, to_delete)
        self.n -= len(to_delete)

    def status(self, i, j):
        find = np.argwhere((np.array([i, j]) == self.x).prod(axis=1) == 1)
        if len(find) > 0:
            return self.ill[find[0]][0]
        else:
            return -1

    def count_ill(self):
        return np.count_nonzero(self.ill)

    def count_immune(self):
        return np.count_nonzero(self.immune)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fd:
        parameters = json.load(fd)
    population = Population(parameters['grid_size'], parameters['n'],
                            parameters['duration'], parameters['mortality'])
    ill = []
    immune = []
    population_size = []
    while True:
        population.move()
        ill.append(population.count_ill())
        immune.append(population.count_immune())
        population_size.append(population.n)
        if not population.count_ill():
            break
    if len(sys.argv) < 3:
        plt.plot(ill, label="Sick Individuals")
        plt.plot(immune, label="Immune Individuals")
        plt.plot(population_size, label="Population")
        plt.xlabel("Time")
        plt.ylabel("Count")
        plt.legend()
        plt.show()
    else:
        iteration = 0
        with open(sys.argv[2], 'w') as fd:
            fd.write("iteration,ill,immune,population\n")
            for a, b, c in zip(ill, immune, population_size):
                fd.write("{},{},{},{}\n".format(iteration, a, b, c))
                iteration += 1
