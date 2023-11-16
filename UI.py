import csv
import datetime
import time
import pygame
import sys
import math
import random
from maze import generate_blueprint, empty_blueprint
# from pso_natan import Particle
from PSO import Particle


def run_pso(iterations, size, num_particles):
    """
    Esta funcion corre el programa
    """
    # VARIABLES
    POINTS = 500
    BOUNDS = [(0, size), (0, size)]
    TARGET_POSITION = [size-2, size-2]
    err_best_g = -1                   # best error for group
    pos_best_g = []                   # best position for group

    # DEFINE SIZES
    TERRAIN_WIDTH = size*8
    TERRAIN_HEIGHT = size*8

    MAIN_WIDTH = TERRAIN_WIDTH+400
    MAIN_HEIGHT = TERRAIN_HEIGHT+100

    PIXEL_WIDHT = 8
    PIXEL_HEIGHT = 8

    # DEFINE COLORS
    MAIN_WINDOW_BACKGROUND_COLOR = (27, 50, 95)
    TERRAIN_BACKGROUND_COLOR = (255,255,255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    TARGET_COLOR = (127, 255, 0)
    RED = (255, 0, 0)
    DRON = (255, 228, 196)

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

    # BLUEPRINT = generate_blueprint(points_number=POINTS, size = size)
    BLUEPRINT = generate_blueprint(density=0.2, size=size)

    def save_log(pos_best_g, err_best_g, iteration, explore, swarm, elapsed_seconds):
        """Function to save the results"""
        current_time = datetime.datetime.now()
        data = [
            ['Dron#','Dron Amount', 'Best Postion Global', 'Best Error Global', 'Iterations', 'Iteration', 'Size',
                'Total Percentage Explore', 'Individual Error', 'Individual Position', 'Elapsed Time(s)']
        ]
        count = 1
        for particle in swarm:
            data.append([count, num_particles,pos_best_g, err_best_g, iterations, iteration,
                        size, explore, particle.error, particle.pos, elapsed_seconds])
            count += 1
        csv_file = './results/Data_log_{}-{}-{}_{}-{}-{}.csv'.format(
            current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
        # Abre el archivo CSV en modo escritura
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def draw_blueprint(blueprint):
        """Function drwas the blueprint in the surface"""
        for fila in range(len(blueprint)):
            for col in range(len(blueprint[0])):
                if blueprint[col][fila] == 1:
                    pygame.draw.rect(
                        TERRAIN, BLACK, (col * PIXEL_WIDHT, fila * PIXEL_HEIGHT, PIXEL_WIDHT, PIXEL_HEIGHT))

    def percetange_explore(map):
        """function to retrieve the explore percentage"""
        count = 0
        map_size = len(map[0])
        for i in range(map_size):
            for j in range(map_size):
                if map[i][j] == 1:
                    count += 1
        percentage = round((count/(map_size**2))*100)
        # print("Percentaje of the map cover: {}".format(percentage))
        return percentage
    PERCENTAGE_MAP = empty_blueprint(size=size)
    EMPTY_MAP = empty_blueprint(size=size)
    swarm = []
    for p in range(0, num_particles):
        # initial_r = [random.randint(0,100), random.randint(0,100)]
        initial_r = [1, 1]
        swarm.append(Particle(initial_r, target=TARGET_POSITION))
    # draw_blueprint(BLUEPRINT)
    draw_blueprint(EMPTY_MAP)
    running = True
    iteration = 0

    font = pygame.font.Font(None, 36)  # Choose a font and font size
    text_color = (255, 255, 255)  # White

    start_time = pygame.time.get_ticks()
    # while running:

    def draw_button(x, y, text):
        button_text = font.render(text, True, BLACK)
        button_rect = button_text.get_rect(center=(x, y))
        pygame.draw.rect(MAIN_WINDOW, WHITE, button_rect, border_radius=5)
        MAIN_WINDOW.blit(button_text, button_rect)
    while True:
        if running:
            explore = percetange_explore(PERCENTAGE_MAP)
            current_time = pygame.time.get_ticks()  # Tiempo actual en milisegundos
            # Convertir a segundos
            elapsed_seconds = (current_time - start_time) // 1000

            MAIN_WINDOW.fill(MAIN_WINDOW_BACKGROUND_COLOR)

            timer_surface = font.render("Elapsed Time: {} s".format(
                elapsed_seconds), True, text_color)
            MAIN_WINDOW.blit(timer_surface, (10, 10))

            iteration_surface = font.render("Iterations: {} of {}".format(
                iteration, iterations), True, text_color)
            # Position the text surface
            MAIN_WINDOW.blit(iteration_surface, (10, 50))

            percentage_surface = font.render(
                "Percentage: {}%".format(explore), True, text_color)
            # Position the text surface
            MAIN_WINDOW.blit(percentage_surface, (10, 100))

            dron_surface = font.render(
                "Drones: {} units".format(num_particles), True, text_color)
            # Position the text surface
            MAIN_WINDOW.blit(dron_surface, (10, 150))

            size_surface = font.render(
                "Size: {}x{}".format(size, size), True, text_color)
            # Position the text surface
            MAIN_WINDOW.blit(size_surface, (10, 200))

            MAIN_WINDOW.blit(TERRAIN, (350, 10))

            # draw the target
            pygame.draw.rect(TERRAIN, TARGET_COLOR, (
                TARGET_POSITION[0] * PIXEL_WIDHT, TARGET_POSITION[1] * PIXEL_HEIGHT, PIXEL_WIDHT, PIXEL_HEIGHT))

            for particle in swarm:
                x_particle = particle.pos[0]
                y_particle = particle.pos[1]

                PERCENTAGE_MAP[x_particle][y_particle] = 1

                pygame.draw.rect(TERRAIN, particle.color, (
                    x_particle * PIXEL_WIDHT, y_particle * PIXEL_HEIGHT, PIXEL_WIDHT, PIXEL_HEIGHT))
                particle.evaluate_fitness()
                particle.update_velocity(pos_best_g)
                EMPTY_MAP = particle.update_position(
                    size, BLUEPRINT, EMPTY_MAP)
                draw_blueprint(EMPTY_MAP)
                if explore >= 80:
                    running = False
                if particle.error < err_best_g or err_best_g == -1:
                    pos_best_g = list(particle.pos)
                    err_best_g = float(particle.error)
                if particle.pos[0] == TARGET_POSITION[0] and particle.pos[1] == TARGET_POSITION[1]:
                    running = False
            iteration += 1
        else:
            draw_button(100, 250, "Save Log")
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                # save_log(pos_best_g, err_best_g, iteration, explore, swarm, elapsed_seconds)
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                # Check if the mouse click is within the button area
                button_rect = font.render(
                    "Save Loog", True, BLACK).get_rect(center=(100, 250))
                if button_rect.collidepoint(evento.pos):
                    save_log(pos_best_g, err_best_g, iteration,
                             explore, swarm, elapsed_seconds)
                    # print("Data saved!")

        # Refresca la pantalla
        pygame.display.flip()

        time.sleep(0.05)
        if iteration > iterations:
            running = False

# run_pso(num_particles=25, iterations=500, size=50)
