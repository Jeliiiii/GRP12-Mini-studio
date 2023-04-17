from rectangle import *
from random import randint


class Basic(Rectangle):
    def __init__(self, window, x, y, width, height, speed):
        Rectangle.__init__(self, window.screen, x, y, width, height, speed)
        self.height = window.hauteur
        self.left = 0
        self.doing = 0

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



class Idle(Rectangle):
    def __init__(self, window, x, y, width, height, speed):
        Rectangle.__init__(self, window.screen, x, y, width, height, speed)
        self.height = window.hauteur
        self.left = 40
        self.doing = self.move_down

    def go_on(self):
        self.move_left()
        self.draw((0, 0, 0))

        if self.left == 0:
            if self.doing == self.move_up:
                self.doing = self.move_down
                print('%s'%(self.doing))
            else :
                self.doing = self.move_up
                print('%s'%(self.doing))
            self.left = 40
        else:
            self.doing()
            self.left -=1