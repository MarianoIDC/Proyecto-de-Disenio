"""Module to create random values"""
import random
import numpy as np

def generate_blueprint(density, size):
    """function that creates a blueprint"""

    blueprint = np.zeros((size, size))

    for i in range(size):
        for j in range(size):
            if random.random() < density:
                blueprint[i][j] = 1  # '1' represents a building block
    for i in range(size):
        blueprint[i][0] = 1
        blueprint[i][size-1] = 1
        blueprint[0][i] = 1
        blueprint[size-1][i] = 1
    blueprint[size-1][size-1] = 0
    # print(blueprint)
    return blueprint

def empty_blueprint(size):
    """function that creates an empty blueprint"""
    blueprint = np.zeros((size, size))
    for i in range(size):
        blueprint[i][0] = 1
        blueprint[i][size-1] = 1
        blueprint[0][i] = 1
        blueprint[size-1][i] = 1
    return blueprint

# generate_blueprint(0.3, 50)