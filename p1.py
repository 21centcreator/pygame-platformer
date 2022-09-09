import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platformer')

#define game variables
tile_size = 50

#load images
bg_img = pygame.image.load('img/sky.png')
sun_img = pygame.image.load('img/sun.png')



run = True
while run:

    screen.blit(bg_img, (0, 0))
    screen.blit(sun_img, (200, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()