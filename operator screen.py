# Import neccessary libraries

import pygame
import os
import time

from character import *
from pseudoWindow import *
from Simon import *
from Carthage import *


# Ressource loading

mouse = pygame.image.load("ressources/img/curseur.png").convert_alpha()
mouse_pos = (500, 500)
pygame.mouse.set_visible(0)


# Carthage((100, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
# Simon((300, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
PseudoWindow((100, 100), (500, 500), color = (45, 177, 88, 1))
PseudoWindow((700, 100), (500, 500), color = (45, 177, 88, 1), closeCond = False)
    

# Boucle de jeu
running = True
while running:

    # Affichage du scrolling background
    clock.tick(FPS)



    # Gestion des événements pygame
    for event in pygame.event.get():

        # Manage key-press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # else:
            #     for trying in PseudoWindow.loadedPseudoWindows:
            #         trying.typeField.onTick( {"MOUSE_POS":[0,0], "MOUSE_BUTTONS":[], "ACTIVE_KEYS":[event.key]}, 1)


        # Manage pointer movement event
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        

        # Manage click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                print("Liste des fenêtres chargés :\n", PseudoWindow.loadedPseudoWindows)
                for cur in range(len(PseudoWindow.loadedPseudoWindows)):
                    if PseudoWindow.loadedPseudoWindows[cur].rectCross.collidepoint(mouse_pos) and PseudoWindow.loadedPseudoWindows[cur].closeCond:
                        del PseudoWindow.loadedPseudoWindows[cur]
                        print("element removed from list")
                        break
                #     elif instance.surfContent.get_rect().collidepoint(mouse_pos):
                #         print("Left Click on surfContent")

                """ ALED VALENTIN AAAAAAAAAAAAAAAAAAAAAAAA """

                for i in PseudoWindow.loadedPseudoWindows:
                    if i.rectContent.collidepoint(mouse_pos):
                        # On envoie les coordonnees relatives
                        i.clicked((mouse_pos[0] - i.coord[0] - i.borderSize, mouse_pos[1] - i.coord[1] - i.menuSize))


    # Resets the screen
    spyScreen.fill(black)

    # Draw every loaded "windows" on the screen, then the mouse
    for win in range(len(PseudoWindow.loadedPseudoWindows)):
        PseudoWindow.loadedPseudoWindows[win].show()
    spyScreen.blit(mouse, mouse_pos)

    # Rafraîchissement de l'affichage
    pygame.display.update()

pygame.quit()
