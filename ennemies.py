from rectangle import *
from random import randint
from weapons import *
from copy import deepcopy




class Basic(Rectangle):
    def __init__(self, window, x, y, speed):
        Rectangle.__init__(self, window.screen, x, y, 50, 50, speed)
        self.height = window.hauteur
        self.left = 0
        self.doing = 0
        self.tearTimer = 20
        self.tearRemaining = self.tearTimer
        self.side = "ennemy"
        self.lastCollid = -1

    

    def go_on(self, objectsList):
        self.move_left()
        self.draw((0, 0, 0))
        self.bullet = Weapon(25, Bullet(self.screen, self.rect.x, self.rect.y, 20, 10, 10, "ennemy"))#on met a jour la bullet (pas opti)

        
        
        #check collisions au décor

        testUp = deepcopy(self.rect)
        testDown = deepcopy(self.rect)

        testUp[1] = self.getCoordinates()[1] -20
        testDown[1] = self.getCoordinates()[1] +20

        collider = testUp.collidelist(objectsList[0])

        
        if collider != -1 :
            self.switchDir()
        else :
            collider = testDown.collidelist(objectsList[0])
            if collider != -1 :
                self.switchDir()


        #check collisions entre ennemies

        if self.rect in objectsList[1]:
            myself = objectsList[1].index(self.rect)
        else :
            myself = -1

        
        collider = testUp.collidelist(objectsList[1])

        if collider != -1 and collider!= myself: #si je touches quelque chose qui n'est pas moi
            self.switchDir()
        else :
            collider = testDown.collidelist(objectsList[1])
            if collider != -1 and collider!= myself:
                self.switchDir()

        #choice
        if self.doing == 0:
            if self.getCoordinates()[1]-20*self.speed < 0 :
                self.doing = self.move_down
            elif self.getCoordinates()[1]+20*self.speed > self.height :
                self.doing = self.move_up
            elif randint(1,2)==1:
                self.doing = self.move_down
            else :
                self.doing = self.move_up
            self.left = 20
        else:
            self.doing()
            self.left-=1
            if self.left == 0:
                self.doing = 0

        self.tearRemaining -= 1
        if self.tearRemaining == 0:
            self.shoot(objectsList)
            self.tearRemaining = self.tearTimer


    def switchDir(self):
        if self.doing == self.move_up:
            self.doing = self.move_down
        else :
            self.doing = self.move_up


    def shoot(self, objectsList):
        objectsList[2].append(self.bullet.bullet)



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