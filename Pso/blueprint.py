import random
from PIL import Image

def generate_blueprint(rows, cols, density=0.3):
    blueprint = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if random.random() < density:
                blueprint[i][j] = 'X'  # 'X' represents a building block

    return blueprint

def save_maze_as_bitmap(maze, file_path):
    width = len(maze[0])
    height = len(maze)
    cell_size = 20  # Adjust the cell size as needed
    
    image = Image.new('RGB', (width * cell_size, height * cell_size), 'white')
    pixels = image.load()
    
    for i in range(height):
        for j in range(width):
            color = 'black' if maze[i][j] == 'X' else 'white'
            for x in range(i * cell_size, (i + 1) * cell_size):
                for y in range(j * cell_size, (j + 1) * cell_size):
                    pixels[y, x] = (0, 0, 0) if color == 'black' else (255, 255, 255)
    image.save(file_path)

def print_blueprint(blueprint):
    for row in blueprint:
        print(' '.join(row))

if __name__ == "__main__":
    rows = 100
    cols = 100
    density = 0.2
    
    build_blueprint = generate_blueprint(rows, cols, density)
    print_blueprint(build_blueprint)
    save_maze_as_bitmap(build_blueprint, 'bp.bmp')