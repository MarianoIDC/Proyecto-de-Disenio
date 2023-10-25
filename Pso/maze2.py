from PIL import Image
import random

def generate_maze(rows, cols):
    maze = [['#' for _ in range(cols)] for _ in range(rows)]
    stack = []
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == '#'
    
    def get_neighbors(x, y):
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        random.shuffle(neighbors)
        return [(nx, ny) for nx, ny in neighbors if is_valid(nx, ny)]
    
    def carve_path(x, y):
        maze[x][y] = ' '
        stack.append((x, y))
        
        while stack:
            x, y = stack[-1]
            neighbors = get_neighbors(x, y)
            
            if neighbors:
                nx, ny = neighbors[0]
                maze[(x + nx) // 2][(y + ny) // 2] = ' '
                maze[nx][ny] = ' '
                stack.append((nx, ny))
            else:
                stack.pop()
    
    start_x, start_y = 0, 0
    carve_path(start_x, start_y)
    
    return maze

def save_maze_as_bitmap(maze, file_path):
    width = len(maze[0])
    height = len(maze)
    cell_size = 20  # Adjust the cell size as needed
    
    image = Image.new('RGB', (width * cell_size, height * cell_size), 'white')
    pixels = image.load()
    
    for i in range(height):
        for j in range(width):
            color = 'black' if maze[i][j] == '#' else 'white'
            for x in range(i * cell_size, (i + 1) * cell_size):
                for y in range(j * cell_size, (j + 1) * cell_size):
                    pixels[y, x] = (0, 0, 0) if color == 'black' else (255, 255, 255)

    image.save(file_path)

if __name__ == "__main__":
    rows = 40
    cols = 20
    
    maze = generate_maze(rows, cols)
    # print_maze(maze)
    
    save_maze_as_bitmap(maze, 'maze.bmp')
