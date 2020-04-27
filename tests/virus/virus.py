import numpy as np
from scipy.spatial.distance import cdist
import scipy.stats as stats
import matplotlib.pyplot as plt
import sys
import json


class Population:
    def __init__(self, grid_size, n, duration):
        self.grid_size = grid_size
        self.n = n
        self.duration = duration
        self.x = np.random.randint(0, grid_size, (n, 2))
        self.ill = np.array([duration] + [0] * (n - 1))
        self.immune = np.array([0] * n)

    def move(self):
        self.x += np.random.randint(-1, 2, (self.n, 2))
        self.x = np.remainder(self.x, self.grid_size)
        for i, x1 in enumerate(self.x):
            for j, x2 in enumerate(self.x):
                if i != j:
                    if (x1 == x2).all() and self.ill[j] > 0 and self.ill[i] == 0 and not self.immune[i]:
                        self.ill[i] = self.duration
                        self.immune[i] = 1
        self.ill += np.array([-1] * self.n)
        self.ill = np.clip(self.ill, 0, self.duration)

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

    def __str__(self):
        lines = '\n'.join([''.join(['.' if self.status(i, j) < 0
                                        else str(self.status(i, j))
                                        for j in range(self.grid_size)])
                               for i in range(self.grid_size)])
        return str(lines)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fd:
        parameters = json.load(fd)
    population = Population(parameters['grid_size'], parameters['n'], parameters['duration'])
    ill = []
    immune = []
    for i in range(parameters['iterations']):
        population.move()
        ill.append(population.count_ill())
        immune.append(population.count_immune())
    if len(sys.argv) < 3:
        plt.plot(ill, label="Sick Individuals")
        plt.plot(immune, label="Immune Individuals")
        plt.xlabel("Time")
        plt.ylabel("Count")
        plt.legend()
        plt.show()
    else:
        with open(sys.argv[2], 'w') as fd:
            fd.write("ill,immune")
            for a, b in zip(ill, immune):
                fd.write("{},{}".format(a, b))
