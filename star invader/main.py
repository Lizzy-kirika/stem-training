import pygame

pygame.init()
screen= pygame.display.set_mode((800,600))

background= pygame.image.load("background.ping")
icon=pygame.image.load("spaceship.png")

pygame.display.set_icon(icon)
pygame.display.set_caption("space Wars")

while True:
    screen.blit(background,(0,0))
    pygame.display.update()