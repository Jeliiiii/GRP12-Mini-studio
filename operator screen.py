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

    def __init__(self, coord = (0, 0), dim = (1, 1), color = (128, 128, 128, 1), closeCond = True):
        # Saves the object caracteristics
        self.coord = coord
        self.dim = dim
        self.color = color
        self.borderSize = 5
        self.menuSize = 20
        self.closeCond = closeCond
        # self.priority = ???

        
        """
        Creates the "window" components. surfComponent are here to blit images within them, while rectComponent are used as hitboxes
        """
        # Hitbox for the entire window
        self.rectWhole = pygame.Rect(self.coord, self.dim)

        # Hitbox of the menu, or band on the top
        self.rectMenu = pygame.Rect(self.coord, (self.dim[0], self.menuSize))

        # Hitbox and Surface for the inside of the window
        self.surfContent = pygame.Surface((self.dim[0] - 2*self.borderSize, self.dim[1] - self.borderSize - self.menuSize)) # Inside of the window
        self.surfContent.fill(white)
        self.rectContent = self.surfContent.get_rect(topleft = (self.coord[0] + self.borderSize, self.coord[1] + self.menuSize))

        # Hitbox and surface for the cross to close the window
        self.surfCross = pygame.Surface((16, 16))
        if self.closeCond:
            self.surfCross.fill((255, 0, 0))
        else:
            self.surfCross.fill((70, 70, 70))
        self.rectCross = self.surfCross.get_rect(topright = (self.coord[0] + self.dim[0] - self.borderSize, self.coord[1] + (self.menuSize - self.surfCross.get_height()) // 2))

        # Adding the new instance to the list
        PseudoWindow.loadedPseudoWindows.append(self)

    def __del__(self):
        print("/!\\ Called destructor /!\\")

    # def __str__(self):
    #     return f"coordinates: {self.coord}, dimensions: {self.dim}, close method: {self.closeCond}, color: {self.color}, border size: {self.borderSize}, menu size: {self.menuSize}"

    def show(self):
        # Draws the effective border to the window
        pygame.draw.rect(spyScreen, self.color, self.rectWhole)

        # Draw the top band to look like a menu
        pygame.draw.rect(spyScreen, self.color, self.rectMenu)

        # Blit the Content of the window
        # spyScreen.blit(self.surfContent, (self.coord[0] + self.borderSize, self.coord[1] + self.menuSize))
        spyScreen.blit(self.surfContent, (self.rectContent.x, self.rectContent.y))

        # Blit the Cross of the window
        spyScreen.blit(self.surfCross, (self.rectCross.x, self.rectCross.y))


# Carthage((100, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
# Simon((300, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
PseudoWindow((100, 100), (300, 300), color = (45, 177, 88, 1))
PseudoWindow((110, 100), (300, 300), color = (45, 177, 88, 1), closeCond = False)
    

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

                # for i in PseudoWindow.loadedPseudoWindows:
                #     if i.Content_Rect.collidepoint(mouse_pos):
                #         i.clicked((mouse_pos[0] - i.coord[0] - i.borderSize, mouse_pos[1] - i.coord[1] - i.menuSize))   # On envoie les coordonnees relatives



    # Resets the screen
    spyScreen.fill(black)

    # Draw every loaded "windows" on the screen, then the mouse
    for win in range(len(PseudoWindow.loadedPseudoWindows)):
        PseudoWindow.loadedPseudoWindows[win].show()
    spyScreen.blit(mouse, mouse_pos)

    # Rafraîchissement de l'affichage
    pygame.display.update()

pygame.quit()
