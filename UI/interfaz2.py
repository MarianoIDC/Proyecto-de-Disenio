import pygame
import sys
import random

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cuadrado en movimiento')

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Tamaño y posición inicial del cuadrado
square_size = 50
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2

# Velocidad del cuadrado
speed = 5

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mover el cuadrado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= speed
    if keys[pygame.K_RIGHT]:
        square_x += speed
    if keys[pygame.K_UP]:
        square_y -= speed
    if keys[pygame.K_DOWN]:
        square_y += speed

    # Limitar la posición del cuadrado para que no salga de la pantalla
    square_x = max(0, min(square_x, screen_width - square_size))
    square_y = max(0, min(square_y, screen_height - square_size))

    # Llenar la pantalla de negro
    screen.fill(black)

    # Dibujar el cuadrado
    pygame.draw.rect(screen, white, (square_x, square_y, square_size, square_size))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de Pygame
pygame.quit()
sys.exit()