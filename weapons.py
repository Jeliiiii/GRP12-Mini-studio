import pygame
from rectangle import *

class Weapon:
    def __init__(self, tear, bullet):
        self.tear = tear
        self.bullet = bullet



class Bullet(Rectangle):
    def __init__(self, screen, x, y, width, height, speed, side):
        Rectangle.__init__(self, screen, x, y, width, height, speed)
        self.side =side
            
    def go_on(self):
        if self.side == "ally":
            self.move_right()
        else :
            self.move_left()
        self.draw((255, 255, 255))

classic = Weapon(15, Bullet)