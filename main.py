import sys
import pygame
from game_of_life import GameOfLife

# Create a pygame instance with caption
pygame.init()
pygame.display.set_caption("** THE GAME OF LIFE **")

# Dimension of window
WIDTH = 1280
HEIGHT = 640

# Define actual screen to display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create instance of GameOfLife
conway_gol = GameOfLife(screen, scale=10)

# Define clock speed
clock = pygame.time.Clock()
fps = 60

# To hold window screen until we close it
while True:
    clock.tick(fps)
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    conway_gol.run()

    pygame.display.update()
