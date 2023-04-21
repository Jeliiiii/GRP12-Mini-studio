# Import neccessary libraries

import pygame
from character import *
import math
from time import sleep
import os


# Changes pyhton3 working directory. This is a fix fro a problem only present on Baptiste's machine

print("!!!!! working directory is about to change !!!!!")
os.chdir("C:\\Users\\BAPTISTE\\Desktop\\GRP12-Mini-studio")
os.getcwd()


# Initialization of diverse pygame functionnalities

pygame.init()
pygame.font.init()


# Setting up screen size

userScreenInfo = pygame.display.Info()
spyScreen_dimension = (userScreenInfo.current_w//2, userScreenInfo.current_h//2)
spyScreen = pygame.display.set_mode(spyScreen_dimension, pygame.NOFRAME)
pygame.display.set_caption("Birds Of Chaos")


# Setting up 

clock = pygame.time.Clock()
FPS = 60


# Some color declaration

black = (0, 0, 0)
white = (255, 255, 255)


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

PseudoWindow((100, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
# PseudoWindow((200, 30), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
    

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

        # Manage pointer movement event
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos

        # Manage click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed(3)[0]:
                print(PseudoWindow.loadedPseudoWindows)
                for cur in range(len(PseudoWindow.loadedPseudoWindows)):
                    if PseudoWindow.loadedPseudoWindows[cur].Cross.get_rect().collidepoint(mouse_pos):

                        del PseudoWindow.loadedPseudoWindows[cur]
                        print("element removed from list")
                #     elif instance.surfContent.get_rect().collidepoint(mouse_pos):
                #         print("Left Click on surfContent")
                #     else:
                #         print("Left Click somewhere else")
                #         PseudoWindow.loadedPseudoWindows[cur].show()


    # Resets the screen
    spyScreen.fill(black)

    # Draw every loaded "windows" on the screen, then the mouse
    for win in range(len(PseudoWindow.loadedPseudoWindows)):
        PseudoWindow.loadedPseudoWindows[win].show()
    spyScreen.blit(mouse, mouse_pos)

    # Rafraîchissement de l'affichage
    pygame.display.update()

pygame.quit()
