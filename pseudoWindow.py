import pygame
from character import *
from setup import *


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
        self.ContentSize = (self.dim[0] - 2*self.borderSize, self.dim[1] - self.borderSize - self.menuSize)

        # Creates the "window" components for future displaying. Calculus are present to size and position Surf correctly within the Rects
        self.Content_Rect = pygame.Rect(self.coord, self.dim)
        self.Band_Rect = pygame.Rect(self.coord, (self.dim[0], self.menuSize))
        self.Content = pygame.Surface(self.ContentSize)
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

    def clicked(self, coords):
        print(coords)
        print(self.Cross)
        if self.Cross.collidepoint(coords):
            print("Left Click on CROSS")
            del self
            print("element removed from list")

