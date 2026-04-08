import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Add Custom Event")

# custom event
CHANGE_COLOR = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR, 1000)

class SpriteBox(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def change_color(self):
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        self.image.fill(color)

sprite1 = SpriteBox(100, 150, (255, 0, 0))
sprite2 = SpriteBox(350, 150, (0, 0, 255))

sprites = pygame.sprite.Group(sprite1, sprite2)

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_COLOR:
            sprite1.change_color()
            sprite2.change_color()

    sprites.draw(screen)
    pygame.display.update()

pygame.quit()