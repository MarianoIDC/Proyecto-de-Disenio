import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def generate_blueprint(rows, cols, density=0.3):
    blueprint = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if random.random() < density:
                blueprint[i][j] = 'X'  # 'X' represents a building block

    return blueprint

def save_blueprint_to_dataframe(blueprint, file_path):
    df = pd.DataFrame(blueprint)
    df.to_csv(file_path, index=False)

def save_blueprint_to_matrix(blueprint, file_path):
    matrix = np.array(blueprint)
    np.save(file_path, matrix)


def print_blueprint(blueprint):
    for row in blueprint:
        print(' '.join(row))

def plot_blueprint(blueprint):
    rows = len(blueprint)
    cols = len(blueprint[0])

    plt.figure(figsize=(cols, rows))
    plt.imshow([[1 if cell == 'X' else 0 for cell in row] for row in blueprint], cmap='binary', interpolation='nearest')
    plt.title('Build Blueprint')
    plt.show()

if __name__ == "__main__":
    rows = 100
    cols = 100
    density = 0.4
    
    build_blueprint = generate_blueprint(rows, cols, density)
    print_blueprint(build_blueprint)
    
    save_blueprint_to_dataframe(build_blueprint, 'build_blueprint.csv')
    save_blueprint_to_matrix(build_blueprint, 'build_blueprint_matrix.txt')
    plot_blueprint(build_blueprint)
    
