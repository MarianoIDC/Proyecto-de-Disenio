
import random

NUM_DIMENSIONS = 2
TARGET = [0,0]

class Particle:
    def __init__(self, initial):
        self.pos = []
        self.vel = []
        self.best_pos = []
        self.best_error = -1
        self.error = -1
        for i in range(0, NUM_DIMENSIONS):
            self.vel.append(random.uniform(-1, 1))
            self.pos.append(initial[i])

    def update_velocity(self, global_best_position):
        w = 0.5
        c1 = 1
        c2 = 2

        for i in range(0, NUM_DIMENSIONS):
            r1 = random.random()
            r2 = random.random()

            cog_vel = c1*r1*(self.best_pos[i]-self.pos[i])
            social_vel = c2*r2*(global_best_position[i]-self.pos[i])
            self.vel[i] = w*self.vel[i]+cog_vel+social_vel

    def update_position(self, bounds):
        for i in range(0, NUM_DIMENSIONS):
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


def fitness_function(position):
    # x0, y0 = getXY('target.csv')
    x0 = float(TARGET[1])
    y0 = float(TARGET[2])
    # total = 0
    # total += (x0-x[0])**2 + (y0-x[1])**2
    # return total
    return (x0-position[0])**2 + (y0-position[1])**2


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
