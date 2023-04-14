import pygame


pygame.init()
pygame.font.init()
ecran = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)
option = pygame.image.load("ressources/img/option.png").convert_alpha()
option_pos = (1600, 150)
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
        if event == pygame.MOUSEBUTTONDOWN == option:
            pygame.draw.rect(ecran, (0, 0, 0), (0, 0, 100, 100))
    ecran.blit(mouse, mouse_pos)
    ecran.blit(option, option_pos)
    pygame.display.flip()
pygame.quit()

