# Import neccessary libraries

import pygame
from character import *
import math
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


# Creating "window" class, an UI element of the spy's screen

class PseudoWindow:
    # Stores every "window" to make them interactive in main loop
    loadedPseudoWindows = []

    def __init__(self, coord=(0, 0), dim=(1, 1), closeCondition=0, color=(128, 128, 128, 1), borderSize=6, menuSize=13):
        # Saves the object caracteristics
        self.coord = coord
        self.dim = dim
        self.closeCond = closeCondition
        self.color = color
        self.borderSize = borderSize
        self.menuSize = menuSize*2 if menuSize > 10 else 20

        # Creates the "window" components for future displaying. Calculus are present to size and position Surf correctly within the Rects
        self.Content_Rect = pygame.Rect(self.coord, self.dim)
        self.Band_Rect = pygame.Rect(self.coord, (self.dim[0], self.menuSize))
        self.Content = pygame.Surface((self.dim[0] - 2*self.borderSize, self.dim[1] - self.borderSize - self.menuSize))
        self.Content.fill(white)

        # Determine needed coordinates to draw the line of the cross and create it's hitbox
        self.dotUp = self.coord[0] + self.menuSize // 8
        self.dotDown = self.dotUp + self.menuSize - self.menuSize // 4
        self.dotRight = self.coord[0] + self.dim[0] - self.borderSize - self.menuSize // 8
        self.dotLeft = self.dotRight - self.menuSize + self.menuSize // 8

        self.Cross = pygame.Rect((self.dotLeft, self.dotUp), (self.dotRight - self.dotLeft, self.dotDown - self.dotUp))

        PseudoWindow.loadedPseudoWindows.append(self)

    def __del__(self):
        print("Called destructor on \"window\"")

    def __str__(self):
        return f"coordinates: {self.coord}, dimensions: {self.dim}, close method: {self.closeCond}, color: {self.color}, border size: {self.borderSize}, menu size: {self.menuSize}"

    def show(self):
        pygame.draw.rect(spyScreen, self.color, self.Content_Rect, self.borderSize)
        pygame.draw.rect(spyScreen, self.color, self.Band_Rect)
        spyScreen.blit(self.Content, (self.coord[0] + self.borderSize, self.coord[1] + self.menuSize))

        pygame.draw.line(spyScreen, white, (self.dotRight, self.dotUp), (self.dotLeft, self.dotDown), 3)
        pygame.draw.line(spyScreen, white, (self.dotRight, self.dotDown), (self.dotLeft, self.dotUp), 3)

PseudoWindow((100, 100), (300, 300), color = (45, 177, 88, 1), menuSize = 16, borderSize = 8)
    

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
                    if PseudoWindow.loadedPseudoWindows[cur].Cross.collidepoint(mouse_pos):
                        print("Left Click on CROSS")
                        del PseudoWindow.loadedPseudoWindows[cur]
                        print("element removed from list")
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
