# Import neccessary libraries

import pygame
from character import *
import math
import os
from pseudoWindow import *
from Simon import *
from carthage import *


# Changes pyhton3 working directory. This is a fix fro a problem only present on Baptiste's machine

"""print("!!!!! working directory is about to change !!!!!")
os.chdir("C:\\Users\\BAPTISTE\\Desktop\\GRP12-Mini-studio")
os.getcwd()"""



# Setting up 

clock = pygame.time.Clock()
FPS = 60


# Ressource loading

mouse = pygame.image.load("ressources/img/curseur.png").convert_alpha()
mouse_pos = (500, 500)
pygame.mouse.set_visible(0)


Carthage((100, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
Simon((300, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
#PseudoWindow((600, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
    

# Boucle de jeu
running = True
while running:
    # Affichage du scrolling background
    clock.tick(FPS)




    #--TEST--



    # Gestion des événements pygame
    for event in pygame.event.get():

        # Manage key-press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                for trying in PseudoWindow.loadedPseudoWindows:
                    trying.typeField.onTick( {"MOUSE_POS":[0,0], "MOUSE_BUTTONS":[], "ACTIVE_KEYS":[event.key]}, 1)


        # Manage pointer movement event
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        

        # Manage click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                for i in PseudoWindow.loadedPseudoWindows:
                    if i.Content_Rect.collidepoint(mouse_pos):
                        i.clicked((mouse_pos[0] - i.coord[0] - i.borderSize, mouse_pos[1] - i.coord[1] - i.menuSize))#on envoie les coordonnees relatives
                """for cur in range(len(PseudoWindow.loadedPseudoWindows)):
                    if PseudoWindow.loadedPseudoWindows[cur].Cross.collidepoint(mouse_pos):
                        print("Left Click on CROSS")
                        del PseudoWindow.loadedPseudoWindows[cur]
                        print("element removed from list")"""
                #     elif instance.Content.get_rect().collidepoint(mouse_pos):
                #         print("Left Clikc on Content")
                #     else:
                #         print("Left Click somewhere else")



    # Resets the screen
    spyScreen.fill(black)

    # Draw every loaded "windows" on the screen, then the mouse
    for win in range(len(PseudoWindow.loadedPseudoWindows)):
        PseudoWindow.loadedPseudoWindows[win].show()
    spyScreen.blit(mouse, mouse_pos)

    # Rafraîchissement de l'affichage
    pygame.display.update()

pygame.quit()
