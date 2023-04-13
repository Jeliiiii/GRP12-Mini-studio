import pygame

pygame.init()
ecran = pygame.display.set_mode((810, 540), pygame.RESIZABLE)

pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)

jouer = True

pygame.display.flip()

while jouer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jouer = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            jouer = False

pygame.quit()