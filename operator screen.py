# Import neccessary libraries

import pygame
import math
import os
import time

from character import *
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


# Font delcaration

defaultFont = pygame.font.Font(size = 50)


# "window" class, the main UI element of the spy's screen

class PseudoWindow:
    # Stores every "window" to make them interactive in main loop
    loadedPseudoWindows = []

    def __init__(self, coord=(0, 0), dim=(1, 1), color=(128, 128, 128, 1), borderSize=6, menuSize=26):
        # Saves the object caracteristics
        self.coord = coord
        self.dim = dim
        self.color = color
        self.borderSize = 5
        self.menuSize = 20

        # Creates the "window" components for future displaying. Calculus are present to size and position Surf correctly within the Rects
        self.rectBorder = pygame.Rect(self.coord, self.dim)
        self.rectMenu = pygame.Rect(self.coord, (self.dim[0], self.menuSize))
        self.surfContent = pygame.Surface((self.dim[0] - 2*self.borderSize, self.dim[1] - self.borderSize - self.menuSize))
        self.rectContent = pygame.Surface.get_rect()
        self.surfContent.fill(white)
        self.Cross = pygame.Surface((16, 16))
        # self.Cross.fill((255, 0, 0))

        PseudoWindow.loadedPseudoWindows.append(self)

    def __del__(self):
        print("Called destructor on \"window\"")

    def __str__(self):
        return f"coordinates: {self.coord}, dimensions: {self.dim}, close method: {self.closeCond}, color: {self.color}, border size: {self.borderSize}, menu size: {self.menuSize}"

    def show(self):
        pygame.draw.rect(spyScreen, self.color, self.rectBorder, self.borderSize)
        pygame.draw.rect(spyScreen, self.color, self.rectMenu)
        pygame.draw.rect(spyScreen, (255, 0, 0), self.Cross.get_rect())
        spyScreen.blit(self.surfContent, (self.coord[0] + self.borderSize, self.coord[1] + self.menuSize))
        # spyScreen.blit(self.Cross, (self.coord[0] + self.dim[0] - self.borderSize - 18, self.coord[1] + 2))

# Carthage((100, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
# Simon((300, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
PseudoWindow((600, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
    

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
                    if PseudoWindow.loadedPseudoWindows[cur].Cross.get_rect().collidepoint(mouse_pos):
                        del PseudoWindow.loadedPseudoWindows[cur]
                        print("element removed from list")
                #     elif instance.surfContent.get_rect().collidepoint(mouse_pos):
                #         print("Left Click on surfContent")
                for i in PseudoWindow.loadedPseudoWindows:
                    if i.Content_Rect.collidepoint(mouse_pos):
                        i.clicked((mouse_pos[0] - i.coord[0] - i.borderSize, mouse_pos[1] - i.coord[1] - i.menuSize))   # On envoie les coordonnees relatives



    # Resets the screen
    spyScreen.fill(black)

    # Draw every loaded "windows" on the screen, then the mouse
    for win in range(len(PseudoWindow.loadedPseudoWindows)):
        PseudoWindow.loadedPseudoWindows[win].show()
    spyScreen.blit(mouse, mouse_pos)

    # Rafraîchissement de l'affichage
    pygame.display.update()

pygame.quit()
