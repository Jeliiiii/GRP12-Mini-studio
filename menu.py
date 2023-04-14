import pygame
import * from button

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.buttons = [Button(0,0,100,30,"Play",switchToAgent),Button(0,0,100,30,"Options",switchToOptions)]
        self.option = False
        self.running = True


    def menu(self):
        pause = True
        while pause:
            for event in pygame.event.get():

    def display(self):
        for b in buttons:
            b.display()

    def update(self, x,y):
        x = event.mouseClicked.x
        y = event.mouseClicked.y
        for b in buttons:
            if (b.isClicked(x,y)):
                b.callback()
                