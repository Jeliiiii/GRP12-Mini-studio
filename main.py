import pygame
import os
x= 0
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()
pygame.font.init()
ecran = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)
option = pygame.image.load("ressources/img/option.png").convert_alpha()
option_pos = (1700, 50)
mouse = pygame.image.load("ressources/img/curseur.png").convert_alpha()
mouse_pos = (0, 0)
pygame.mouse.set_visible(0)

jouer = True

while jouer:
    pygame.draw.rect(ecran, (255, 255, 255), (0, 0, 1920, 1080))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jouer = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            jouer = False
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        if event == pygame.MOUSEBUTTONDOWN in pygame.MOUSEMOTION(0, 0, 50, 50):
            pygame.draw.rect(ecran, (255, 255, 255), (0, 0, 50, 50))
    ecran.blit(mouse, mouse_pos)
    ecran.blit(option, option_pos)
    pygame.display.flip()

pygame.quit()