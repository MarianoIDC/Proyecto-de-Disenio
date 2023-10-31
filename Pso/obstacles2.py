import time
import pygame
import numpy as np

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 10
OBSTACLE_SIZE = 10

RED = (255,0,0)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PSO Obstacle Avoidance")

# PSO parameters
num_particles = 30
num_dimensions = 2  # 2D space (x, y)
max_iterations = 100
c1 = 1.5  # Cognitive parameter
c2 = 1.5  # Social parameter
w = 0.7  # Inertia weight

# Define the environment
# obstacles = [(100, 100), (400, 200), (600, 300)]  # Obstacle locations

obstacles = []

for i in range(1, 200):
    obstacles.append((np.random.randint(1,700),np.random.randint(1,500)))


# Initialize particles
particles = np.random.rand(num_particles, num_dimensions) * (WIDTH, HEIGHT)
velocities = np.zeros((num_particles, num_dimensions))
best_positions = particles.copy()
best_scores = np.full(num_particles, np.inf)

# Function to calculate the fitness of a particle
def fitness(particle):
    # Calculate the distance to obstacles
    distance_to_obstacles = [np.sqrt((particle[0] - obs[0])**2 + (particle[1] - obs[1])**2) for obs in obstacles]
    return sum(distance_to_obstacles)

running = True
iteration = 0
screen.fill(WHITE)
while running:
    time.sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for i in range(num_particles):
        particle = particles[i]
        score = fitness(particle)

        if score < best_scores[i]:
            best_scores[i] = score
            best_positions[i] = particle

        global_best = best_positions[np.argmin(best_scores)]

        # Update velocity and position
        r1, r2 = np.random.rand(2)
        velocities[i] = w * velocities[i] + c1 * r1 * (best_positions[i] - particle) + c2 * r2 * (global_best - particle)
        particles[i] += velocities[i]

        # Ensure particles stay within the window
        particles[i] = np.clip(particles[i], 0, (WIDTH, HEIGHT))

    

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, RED, pygame.Rect(obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))

    # Draw particles
    for particle in particles:
        pygame.draw.circle(screen, BLACK, (int(particle[0]), int(particle[1])), 5)

    pygame.display.flip()
    iteration += 1

    if iteration >= max_iterations:
        running = False

pygame.quit()