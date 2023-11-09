import random
import numpy as np
NUM_DIMENSIONS = 2
TARGET = []


def generate_color():
    red = random.randint(100, 200)
    green = random.randint(100, 200)
    blue = random.randint(100, 200)
    # Convierte los valores RGB en un código hexadecimal
    hex_color = "#{:02X}{:02X}{:02X}".format(red, green, blue)

    return hex_color


class Particle:
    def __init__(self, initial, target):

        global TARGET
        TARGET = target
        self.pos = []
        self.vel = []
        self.best_pos = []
        self.best_error = -1
        self.error = -1
        self.color = generate_color()
        for i in range(0, NUM_DIMENSIONS):
            self.vel.append(random.uniform(-1, 1))
            self.pos.append(initial[i])

    def update_velocity(self, global_best_position):
        w = 0.5
        c1 = 0.2
        c2 = 0.4

        for i in range(0, NUM_DIMENSIONS):
            update = [-1, 0, 1]
            r1 = round(random.choice(update))
            r2 = round(random.choice(update))
            cog_vel = c1*r1
            social_vel = c2*r2
            # cog_vel = c1*r1*(self.best_pos[i]-self.pos[i])
            # social_vel = c2*r2*(global_best_position[i]-self.pos[i])
            # self.vel[i] = normalize(w*self.vel[i]+cog_vel+social_vel)
            self.vel[i] = round(w*self.vel[i]+cog_vel+social_vel)

    def update_position(self, bounds, blueprint, empty_map):

        x = self.pos[0]+self.vel[0]
        y = self.pos[1]+self.vel[1]
        if blueprint[x][y] == 1:
            self.pos[0] = self.pos[0]
            self.pos[1] = self.pos[1]
            empty_map [x][y] = 1
        else:
            # print(int(blueprint[x][y]))
            self.pos[0] = x
            self.pos[1] = y
        return empty_map
    # def evaluate_fitness(self, fitness_function):
    def evaluate_fitness(self):
        self.error = fitness_function(self.pos)
        # print("ERROR------->", self.error)

        if self.error < self.best_error or self.best_error == -1:
            self.best_pos = self.pos
            self.best_error = self.error


def normalize(value):
    return 2 * (value + 1) / 1


def fitness_function(position):
    global TARGET
    x0 = float(TARGET[0])
    y0 = float(TARGET[1])
    # return (x0-position[0])**2 + (y0-position[1])**2
    # return (x0-3.14)**2 + (y0-2.72)**2 + np.sin(3*x0+1.41) + np.sin(4*y0-1.73)
    return (x0-position[0])**2 + (y0-position[1])**2 + np.sin(3*x0+1.41) + np.sin(4*y0-1.73)
