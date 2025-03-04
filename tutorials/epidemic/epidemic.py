#! /usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import sys
import json


__copyright__ = """

    Copyright 2020 Vytautas Jancauskas

    This file is part of EasyVVUQ

    EasyVVUQ is free software: you can redistribute it and/or modify
    it under the terms of the Lesser GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    EasyVVUQ is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Lesser GNU General Public License for more details.

    You should have received a copy of the Lesser GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
__license__ = "LGPL"


class Population:
    def __init__(self, grid_size, n, duration, mortality):
        self.grid_size = int(grid_size)
        self.n = int(n)
        self.duration = int(duration)
        self.mortality = mortality
        self.x = np.random.randint(0, self.grid_size, (self.n, 2))
        self.ill = np.array([self.duration] + [0] * (self.n - 1))
        self.immune = np.array([0] * self.n)
        self.n_history = []
        self.ill_history = []
        self.immune_history = []

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
        to_delete = np.argwhere(np.logical_and(
            self.ill == 1, np.random.random(self.n) < self.mortality))
        self.ill[np.argwhere(self.ill > 0)] -= 1
        self.x = np.delete(self.x, to_delete, axis=0)
        self.ill = np.delete(self.ill, to_delete)
        self.immune = np.delete(self.immune, to_delete)
        self.n -= len(to_delete)
        self.n_history.append(self.n)
        self.ill_history.append(np.count_nonzero(self.ill))
        self.immune_history.append(np.count_nonzero(self.immune))

    def status(self, i, j):
        find = np.argwhere((np.array([i, j]) == self.x).prod(axis=1) == 1)
        return self.ill[find[0]][0], self.immune[find[0]][0]

    def run(self):
        ill = []
        immune = []
        population_size = []
        n_ill = 1
        while n_ill:
            self.move()
            n_ill = np.count_nonzero(self.ill)
            n_immune = np.count_nonzero(self.immune)
            ill.append(n_ill)
            immune.append(n_immune)
            population_size.append(population.n)
        return ill, immune, population_size

    def get_im(self):
        im = []
        for i in range(self.grid_size):
            im_row = []
            for j in range(self.grid_size):
                try:
                    ill, immune = self.status(i, j)
                    if ill:
                        illness = 1.0 - ill / float(self.duration)
                        im_row.append([1, illness, illness])
                    elif immune:
                        im_row.append([0, 1, 0])
                    else:
                        im_row.append([1, 1, 1])
                except IndexError:
                    im_row.append([0, 0, 0])
            im.append(im_row)
        return np.array(im)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as fd:
        parameters = json.load(fd)
    population = Population(parameters['grid_size'], parameters['n'],
                            parameters['duration'], parameters['mortality'])
    ill, immune, population_size = population.run()
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
