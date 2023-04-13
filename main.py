import pygame

pygame.init()
ecran = pygame.display.set_mode((810, 540), pygame.RESIZABLE)

pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)

jouer = True

option = pygame.draw.rect(ecran, (255, 255, 255), (0, 0, 50, 50))
clem = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pos_clem = (0, 0)

largeur = 10
hauteur = 10
couleur = (20, 180, 20)

while jouer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jouer = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            jouer = False
        if event.type == pygame.MOUSEMOTION:
            pos_clem = event.pos
            x, y = event.pos
            '''pygame.draw.rect(ecran, couleur, (x, y, largeur, hauteur))'''
    ecran.blit(clem, pos_clem)        
    pygame.display.flip()

pygame.quit()