from ...DefaultPawnActor import DefaultPawnActor
from random import randint
import pygame

class EnnemyActor(DefaultPawnActor):
    def __init__(self, x, y, surface, weapon, velX=0, velY=0):
        super().__init__(x, y, surface, velX=velX, velY=velY)
        self.winHeight = 720
        self.weapon = weapon
        self.health = 10

    def shot(self, damage):
        self.health -= damage

    def onTick(self, dt, windowSize):
        super().onTick(dt)
        bulletList = []
        
        
        if self.hitBox.y <= 0 :
            self.hitBox.y = self.sprite[1].x = 0
            self.velocity[1] = -self.velocity[1]
        elif self.hitBox.y >= self.winHeight :
            self.hitBox.y = self.sprite[1].y = self.winHeight
            self.velocity[1] = -self.velocity[1]

        if self.weapon.shootCooldownRemaining == 0 and self.isInWindow(windowSize):
            bulletList = self.weapon.fireDouble(self.hitBox.x, self.hitBox.centery, -70, 40)
        self.weapon.onTick(dt)
        return bulletList



# class EnnemyBullet(Rectangle):
#     def __init__(self, screen, x, y, width, height, speed):
#         Rectangle.__init__(self, screen, x, y, width, height, speed)
            
#     def go_on(self):
#         self.move_right()
#         self.draw((255, 255, 255))


