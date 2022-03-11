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
    os.path.join("assets/images", "pixel_ship_blue_small.png"))
GREEN_SPACESHIP = pygame.image.load(
    os.path.join("assets/images", "pixel_ship_green_small.png"))
RED_SPACESHIP = pygame.image.load(
    os.path.join("assets/images", "pixel_ship_red_small.png"))

# Player spaceship
YELLOW_SPACESHIP = pygame.image.load(
    os.path.join("assets/images", "pixel_ship_yellow.png"))

# Enemy lasers
BLUE_LASER = pygame.image.load(os.path.join(
    "assets/images", "pixel_laser_blue.png"))
GREEN_LASER = pygame.image.load(
    os.path.join("assets/images", "pixel_laser_green.png"))
RED_LASER = pygame.image.load(os.path.join(
    "assets/images", "pixel_laser_red.png"))

# Player laser
YELLOW_LASER = pygame.image.load(
    os.path.join("assets/images", "pixel_laser_yellow.png"))

# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(
    os.path.join("assets/images", "background_black.png")), (WIDTH, HEIGHT))
# endregion

# region Load fonts
pygame.font.init()
MAIN_FONT = pygame.font.Font(os.path.join("assets/fonts", "prstart.ttf"), 20)
# endregion


def main():
    """Main function"""
    run = True
    FPS = 60
    level = 1
    lives = 5
    clock = pygame.time.Clock()

    def redraw_window():
        """Redraw the window"""
        # Background
        WINDOW.blit(BACKGROUND, (0, 0))

        # Draw texts
        lives_label = MAIN_FONT.render(f"Lives: {lives}", 1, (255, 255, 255))
        level_label = MAIN_FONT.render(f"Level: {level}", 1, (255, 255, 255))
        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False


main()
