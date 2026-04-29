import pygame
import random

# Initialize pygame
pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader - Sprites")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Player
player_size = 40
player_x = WIDTH // 2
player_y = HEIGHT - 60
player_speed = 5

# Enemies
enemy_size = 30
enemy_list = []

for i in range(7):
    x = random.randint(0, WIDTH - enemy_size)
    y = random.randint(0, HEIGHT // 2)
    enemy_list.append([x, y])

# Score
score = 0
font = pygame.font.SysFont("Arial", 24)

# Collision check
def is_collision(px, py, ex, ey):
    return abs(px - ex) < 30 and abs(py - ey) < 30

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Draw enemies
    for enemy in enemy_list:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))

        # Check collision
        if is_collision(player_x, player_y, enemy[0], enemy[1]):
            score += 1

            # Move enemy to new random position
            enemy[0] = random.randint(0, WIDTH - enemy_size)
            enemy[1] = random.randint(0, HEIGHT // 2)

    # Display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()