import random

def generate_maze(rows, cols):
    maze = [['1' for _ in range(cols)] for _ in range(rows)]
    stack = []
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze[x][y] == '1'
    
    def get_neighbors(x, y):
        neighbors = [(x+2, y), (x-2, y), (x, y+2), (x, y-2)]
        random.shuffle(neighbors)
        return [(nx, ny) for nx, ny in neighbors if is_valid(nx, ny)]
    
    def carve_path(x, y):
        maze[x][y] = '0'
        stack.append((x, y))
        
        while stack:
            x, y = stack[-1]
            neighbors = get_neighbors(x, y)
            
            if neighbors:
                nx, ny = neighbors[0]
                maze[(x + nx) // 2][(y + ny) // 2] = '0'
                maze[nx][ny] = '0'
                stack.append((nx, ny))
            else:
                stack.pop()
    
    start_x, start_y = 0, 0
    carve_path(start_x, start_y)
    
    return maze

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

if __name__ == "__main__":
    rows = 1000
    cols = 1000
    
    maze = generate_maze(rows, cols)
    print_maze(maze)