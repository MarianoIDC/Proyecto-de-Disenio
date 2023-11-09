import time
import pygame
import sys
import math
import random
from maze import generate_blueprint
from pso_natan import Particle


def run_pso(num_particles, iterations, size):
    """
    Esta funcion corre el programa
    """
    # VARIABLES
    POINTS = 500
    BOUNDS = [(0, size), (0, size)]
    TARGET_POSITION = [size-1, size-1]
    err_best_g = -1                   # best error for group
    pos_best_g = []                   # best position for group

    # DEFINE SIZES
    MAIN_WIDTH = 800
    MAIN_HEIGHT = 600

    TERRAIN_WIDTH = 500
    TERRAIN_HEIGHT = 500

    PIXEL_WIDHT = 5
    PIXEL_HEIGHT = 5

    # DEFINE COLORS
    MAIN_WINDOW_BACKGROUND_COLOR = (27, 50, 95)
    TERRAIN_BACKGROUND_COLOR = (156, 196, 228)
    BLACK = (0, 0, 0)
    TARGET_COLOR = (127, 255, 0)

    pygame.init()
    # DEFINE THE MAIN WINDOW TITLE
    WINDOW_TITLE = "PARTICLE SWARM OPTIMIZATION - 2D"
    pygame.display.set_caption(WINDOW_TITLE)

    # CREATE THE MAIN WINDOW
    MAIN_WINDOW = pygame.display.set_mode((MAIN_WIDTH, MAIN_HEIGHT))
    # Llena el canvas con el color de fondo
    MAIN_WINDOW.fill(MAIN_WINDOW_BACKGROUND_COLOR)

    # CREATE THE SURFACE TO DRAW THE ALGORITHM
    TERRAIN = pygame.Surface((TERRAIN_WIDTH, TERRAIN_WIDTH))
    TERRAIN.fill(TERRAIN_BACKGROUND_COLOR)
    # MAIN_WINDOW.blit(TERRAIN, (10, 10))

    BLUEPRINT = generate_blueprint(points_number=POINTS, size = size)

    def draw_blueprint():
        """Function drwas the blueprint in the surface"""
        for fila in range(len(BLUEPRINT)):
            for col in range(len(BLUEPRINT[0])):
                if BLUEPRINT[fila][col] == 1:
                    pygame.draw.rect(
                        TERRAIN, BLACK, (col * PIXEL_WIDHT, fila * PIXEL_HEIGHT, PIXEL_WIDHT, PIXEL_HEIGHT))

    swarm = []
    for p in range(0, num_particles):
        # initial_r = [random.randint(0,100), random.randint(0,100)]
        initial_r = [1, 1]
        swarm.append(Particle(initial_r, target=TARGET_POSITION))

    running = True
    iteration = 0
    while running:
        # for evento in pygame.event.get():
        #     if evento.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()

        # Dibuja en el canvas

        MAIN_WINDOW.blit(TERRAIN, (10, 10))
        draw_blueprint()

        # draw the target
        pygame.draw.rect(TERRAIN, TARGET_COLOR, (
            TARGET_POSITION[0] * PIXEL_WIDHT, TARGET_POSITION[1] * PIXEL_HEIGHT, PIXEL_WIDHT*2, PIXEL_HEIGHT*2))

        for particle in swarm:
            pygame.draw.rect(TERRAIN, particle.color, (
                particle.position_i[0] * PIXEL_WIDHT, particle.position_i[1] * PIXEL_HEIGHT, PIXEL_WIDHT, PIXEL_HEIGHT))
            particle.evaluate()

            if particle.err_i < err_best_g or err_best_g == -1:
                pos_best_g = list(particle.position_i)
                err_best_g = float(particle.err_i)

            particle.update_velocity(pos_best_g)
            particle.update_position(BOUNDS)

        # Refresca la pantalla
        pygame.display.flip()
        iteration += 1
        # time.sleep(0.05)
        # if iteration >= iterations:
        #     running = False


run_pso(num_particles=15, iterations=10000000, size = 100)
