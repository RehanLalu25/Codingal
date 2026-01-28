import pygame
from sys import exit

#game variables
GAME_WIDTH = 360
GAME_HEIGHT = 640

#bird class
bird_x = GAME_WIDTH/8
bird_y = GAME_HEIGHT/2
bird_width = 34
bird_height = 24



#game images
background_image = pygame.image.load("pteranadonbg")
def draw():
    window.blit(background_image,(0, 0))

pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("PY-BIRD")
clock = pygame.time.Clock()

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        exit()
    pygame.display.update()
    clock.tick(60)  #60 fps

