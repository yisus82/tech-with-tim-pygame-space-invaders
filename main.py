import os
import random
import time

import pygame

# region Setup PyGame display
WIDTH = 750
HEIGHT = 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")
# endregion

# region Load images
# Enemy spaceships
BLUE_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_blue_small.png"))
GREEN_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_green_small.png"))
RED_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_red_small.png"))

# Player spaceship
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_yellow.png"))

# Enemy lasers
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_green.png"))
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))

# Player laser
YELLOW_LASER = pygame.image.load(
    os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BACKGROUND = pygame.image.load(os.path.join("assets", "background_black.png"))
# endregion


def main():
    """Main function"""
    run = True
    FPS = 60
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


main()
