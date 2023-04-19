from rectangle import *
from random import randint
from weapons import *


class EnnemyBullet(Rectangle):
    def __init__(self, screen, x, y, width, height, speed):
        Rectangle.__init__(self, screen, x, y, width, height, speed)
            
    def go_on(self):
        self.move_right()
        self.draw((255, 255, 255))


class Basic(Rectangle):
    def __init__(self, window, x, y, speed):
        Rectangle.__init__(self, window.screen, x, y, 50, 50, speed)
        self.height = window.hauteur
        self.left = 0
        self.doing = 0
        self.bullet = Weapon(25, Bullet)
        self.tearTimer = 20
        self.tearRemaining = self.tearTimer
        self.side = "ennemy"

    def go_on(self):
        self.move_left()
        self.draw((0, 0, 0))

        if self.left == 0:
            if self.getCoordinates()[1]-20*self.speed < 0 :
                self.doing = self.move_down
            elif self.getCoordinates()[1]+20*self.speed > self.height :
                self.doing = self.move_up
            elif randint(1,2)==1:
                self.doing = self.move_up
            else:
                self.doing = self.move_down
            self.left = 20
        else:
            self.doing()
            self.left-=1
            if self.left == 0:
                self.doing = 0

        self.tearRemaining -= 1



class Idle(Rectangle):
    def __init__(self, window, x, y, speed):
        Rectangle.__init__(self, window.screen, x, y, 50, 50, speed)
        self.height = window.height
        self.left = 40
        self.doing = self.move_down
        self.bullet = Weapon(25, VerticalBullet)
        self.tearTimer = 20
        self.tearRemaining = self.tearTimer
        self.side = "ennemy"

    def go_on(self):
        self.move_left()
        self.draw((0, 0, 0))

        if self.left == 0:
            if self.doing == self.move_up:
                self.doing = self.move_down
            else :
                self.doing = self.move_up
            self.left = 40
        else:
            self.doing()
            self.left -=1

        self.tearRemaining -= 1