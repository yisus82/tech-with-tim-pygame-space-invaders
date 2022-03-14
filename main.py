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


class Ship:
    """Ship class"""

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        """Draw the player"""
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        """Return the width of the ship"""
        return self.ship_img.get_width()

    def get_height(self):
        """Return the height of the ship"""
        return self.ship_img.get_height()


class Player(Ship):
    """Player class"""

    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACESHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


class Enemy(Ship):
    """Enemy class"""
    COLOR_MAP = {
        "red": (RED_SPACESHIP, RED_LASER),
        "green": (GREEN_SPACESHIP, GREEN_LASER),
        "blue": (BLUE_SPACESHIP, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        """Move the enemy"""
        self.y += vel


def main():
    """Main function"""
    run = True
    FPS = 60
    level = 0
    lives = 5
    enemies = []
    wave_length = 0
    enemy_vel = 1
    player_vel = 5
    player = Player(WIDTH / 2 - YELLOW_SPACESHIP.get_width() /
                    2, HEIGHT - YELLOW_SPACESHIP.get_height() - 50)
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

        # Draw enemies
        for enemy in enemies:
            enemy.draw(WINDOW)

        # Draw player
        player.draw(WINDOW)

        pygame.display.update()

    while run:
        clock.tick(FPS)

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        # Update player position
        keys = pygame.key.get_pressed()
        # Left
        if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - player_vel > 0:
            player.x -= player_vel
        # Right
        if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        # Up
        if keys[pygame.K_w] or keys[pygame.K_UP] and player.y - player_vel > 100:
            player.y -= player_vel
        # Down
        if keys[pygame.K_s] or keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel

        # Create enemies
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for _ in range(wave_length):
                enemy = Enemy(random.randint(50, WIDTH - 50),
                              random.randint(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)

        # Update enemies
        for enemy in enemies:
            enemy.move(enemy_vel)

        redraw_window()


main()
