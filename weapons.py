import pygame
from character import *

class weapon:
    def __init__(self, tear, bullet):
        self.tear = tear
        self.bullet = bullet



class Bullet(Rectangle):
    def __init__(self, screen, x, y, width, height, speed):
        Rectangle.__init__(self, screen, x, y, width, height, speed)
            
    def go_on(self):
        self.move_right()
        self.draw((255, 255, 255))

classic = weapon(15, Bullet)