"""

Main Documentation
https://www.youtube.com/watch?v=xE  Qv9YdvRiA&ab_channel=PyShine
"""


import time
import random
import math
import numpy as np
import csv
import os
import _thread
import matplotlib.pyplot as plt
import random

initial = [random.randint(-400, 400), random.randint(-400, 400)]
bounds = [(-400, 400), (-400, 400)]

colors = np.array([
    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229),

    (31, 119, 180), (174, 199, 232), (255, 127,  14), (255, 187, 120),
    (44, 160,  44), (152, 223, 138), (214,  39,  40), (255, 152, 150),
    (148, 103, 189), (197, 176, 213), (140,  86,  75), (196, 156, 148),
    (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
    (188, 189,  34), (219, 219, 141), (23, 190, 207), (158, 218, 229)

]) / 255.


class Particle:
    def __init__(self, initial):
        self.pos = []
        self.vel = []
        self.best_pos = []
        self.best_error = -1
        self.error = -1
        for i in range(0, num_dimensions):
            self.vel.append(random.uniform(-1, 1))
            self.pos.append(initial[i])

    def update_velocity(self, global_best_position):
        w = 0.5
        c1 = 1
        c2 = 2

        for i in range(0, num_dimensions):
            r1 = random.random()
            r2 = random.random()

            cog_vel = c1*r1*(self.best_pos[i]-self.pos[i])
            social_vel = c2*r2*(global_best_position[i]-self.pos[i])
            self.vel[i] = w*self.vel[i]+cog_vel+social_vel

    def update_position(self, bounds):
        for i in range(0, num_dimensions):
            self.pos[i] = self.pos[i]+self.vel[i]

            if self.pos[i] > bounds[i][1]:
                self.pos[i] = bounds[i][1]

            if self.pos[i] < bounds[i][0]:
                self.pos[i] = bounds[i][0]

    # def evaluate_fitness(self, fitness_function):
    def evaluate_fitness(self):
        self.error = fitness_function(self.pos)
        # print("ERROR------->", self.error)

        if self.error < self.best_error or self.best_error == -1:
            self.best_pos = self.pos
            self.best_error = self.error


def fitness_function(x):
    x0, y0 = getXY('target.csv')
    x0 = float(x0)
    y0 = float(y0)
    total = 0
    total += (x0-x[0])**2 + (y0-x[1])**2
    return total
# def fitness_function(x):
#     x0, y0 = getXY('target.csv')
#     x0 = float(x0)
#     y0 = float(y0)
#     f1 = (x[0] - 3.14) ** 2
#     f2 = (x[1] - 2.72) ** 2
#     f3 = np.sin(3 * x[0] + 1.41)
#     f4 = np.sin(4 * x[1] + 1.73)

#     z = f1 + f2 + f3 + f4

#     return z


def getXY(filename):
    lat = 0
    long = 0
    # with open(filename) as csvDataFile:
    # 	csvReader = csv.reader(csvDataFile)
    # 	for row in csvReader:
    # 		lat = row[0]
    # 		long= row[1]
    # return lat,long
    return 250, 360


class Interactive_PSO():
    # def __init__(self, fitness_function, initial, bounds, num_particles, iterations):
    def __init__(self, initial, bounds, num_particles, iterations):
        global num_dimensions

        self.iterartions = iterations
        num_dimensions = len(initial)
        global_best_error = -1
        global_best_position = []
        self.gamma = 0.0001
        active_flag = 0
        swarm = []
        for i in range(0, num_particles):
            initial_r = [random.randint(-400, 400), random.randint(-400, 400)]
            swarm.append(Particle(initial_r))
        x, y = getXY('target.csv')
        plt.plot(float(x), float(y),  color='k', marker='X')
        i = 0
        # while True:
        while (i < iterations or (active_flag==1 and round(global_best_error)>100)):
            # print(str(active_flag)+'aaaaa'+str(round(global_best_error)))
            active_flag = 1
            # print('x'+','+'y',file = open('pos.csv','w'))
            for j in range(0, num_particles):
                swarm[j].evaluate_fitness()
                # print('global_best_position', swarm[j].error, global_best_error)

                if swarm[j].error < global_best_error or global_best_error == -1:
                    global_best_position = list(swarm[j].pos)
                    global_best_error = float(swarm[j].error)
                    plt.title("PyShine Interactive PSO, Particles:{}, Error:{}, Iterations:{}".format(
                        num_particles, round(global_best_error, 1), i))

                if i % 2 == 0:
                    global_best_error = -1
                    global_best_position = list([swarm[j].pos[0]+self.gamma*(swarm[j].error)*random.random(
                    ), swarm[j].pos[1]+self.gamma*(swarm[j].error)*random.random()])

            pos_0 = {}
            pos_1 = {}
            for j in range(0, num_particles):
                pos_0[j] = []
                pos_1[j] = []

            for j in range(0, num_particles):
                swarm[j].update_velocity(global_best_position)
                swarm[j].update_position(bounds)

                pos_0[j].append(swarm[j].pos[0])
                pos_1[j].append(swarm[j].pos[1])
                # print(str(swarm[j].pos[0])+','+str(swarm[j].pos[1]),file = open('pos.csv','a'))
                plt.xlim([-500, 500])
                plt.ylim([-500, 500])

            for j in range(0, num_particles):
                plt.plot(pos_0[j], pos_1[j],  color=colors[j], marker='o')
            plt.pause(0.05)
            # plt.clf()
            i += 1
        for j in range(0, num_particles):
            plt.plot(pos_0[j], pos_1[j],  color=colors[j], marker='o')
        plt.plot(float(x), float(y),  color='k', marker='X')
        plt.show()
        print('Results')
        print('Best Position:', global_best_position)
        print('Best Error:', global_best_error)
        print('Interations', str(i))
        plt.close('all')


# let say 2 particles and 50 iterations
# Interactive_PSO(fitness_function, initial, bounds,num_particles=5, iterations=1000)
Interactive_PSO(initial, bounds,num_particles=5, iterations=1000)
# if __name__ == "__Interactive_PSO__":
#     Interactive_PSO(fitness_function, initial, bounds, num_particles=5, iterations=1000)
