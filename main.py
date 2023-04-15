import pygame
from character import *

pygame.init()


screen_width = 1920
screen_height = 1080


black = (0, 0, 0)
white = (255, 255, 255)

pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)
option = pygame.image.load("ressources/img/option.png").convert_alpha()
option_pos = (1600, 150)
mouse = pygame.image.load("ressources/img/curseur.png").convert_alpha()
mouse_pos = (0, 0)
pygame.mouse.set_visible(0)


rect_width = 50
rect_height = 100
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect_speed = 1
rect = Rectangle(screen, rect_x, rect_y, rect_width, rect_height, rect_speed)


keys = []

running = True
while running:
    # Gestion des événements pygame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys.append(event.key)
        elif event.type == pygame.KEYUP:
            keys.remove(event.key)
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        if event == pygame.MOUSEBUTTONDOWN == option:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 100))

    # Déplacement continu avec collisions
    if pygame.K_UP in keys:
        rect.move_up()
    if pygame.K_DOWN in keys:
        rect.move_down()
    if pygame.K_LEFT in keys:
        rect.move_left()
    if pygame.K_RIGHT in keys:
        rect.move_right()

    # Effacement de l'écran
    screen.fill(white)

    # Dessin du rectangle
    rect.draw(black)

    # Rafraîchissement de l'affichage
    screen.blit(mouse, mouse_pos)
    screen.blit(option, option_pos)
    pygame.display.flip()

# Fermeture de pygame
pygame.quit()


