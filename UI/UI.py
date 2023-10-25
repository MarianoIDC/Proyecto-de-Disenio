import time
import pygame
import sys
import math
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
BACKGROUND_COLOR = (255, 255, 255)
PARTICLE_COLOR = (0, 0, 255)
TARGET_COLOR = (255, 0, 0)
PARTICLE_RADIUS = 5
TARGET_RADIUS = 8
PARTICLE_COUNT = 20
MAX_VELOCITY = 5
TARGET_X = 400
TARGET_Y = 200
OPTIMAL_VALUE = 0  # Change this to the function minimum you want to find

# Initialize the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PSO Visualization")

# Particle class
class Particle:
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.velocity_x = random.uniform(-MAX_VELOCITY, MAX_VELOCITY)
        self.velocity_y = random.uniform(-MAX_VELOCITY, MAX_VELOCITY)
        self.best_x = self.x
        self.best_y = self.y

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y
        # Update best position
        if self.fitness() < self.fitness(self.best_x, self.best_y):
            self.best_x = self.x
            self.best_y = self.y

    def fitness(self, x=None, y=None):
        if x is None or y is None:
            x = self.x
            y = self.y
        return (x - TARGET_X) ** 2 + (y - TARGET_Y) ** 2  # Change this function

particles = [Particle() for _ in range(PARTICLE_COUNT)]

screen.fill(BACKGROUND_COLOR)
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    time.sleep(0.05)
    for particle in particles:
        particle.move()
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(particle.x), int(particle.y)), PARTICLE_RADIUS)
        pygame.draw.circle(screen, TARGET_COLOR, (TARGET_X, TARGET_Y), TARGET_RADIUS)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
