from ...DefaultPawnActor import DefaultPawnActor
from random import randint
import pygame

class EnnemyActor(DefaultPawnActor):
    def __init__(self, x, y, surfaceList, weapon, velX=0, velY=0, bulletVelX = -70, bulletVelY = 0):
        self.surfaceList = surfaceList
        self.sprite =  [surfaceList["K1"], surfaceList["K1"].get_rect(topleft=(x, y))]
        super().__init__(x, y, None, velX=velX, velY=velY)
        self.winHeight = 720
        self.weapon = weapon
        self.health = 10
        self.animCooldown = 12
        self.bulletVelX = bulletVelX
        self.bulletVelY = bulletVelY

    def shot(self, damage):
        self.health -= damage

    def onTick(self, dt):
        super().onTick(dt)
        bulletList = []
        
        if self.hitBox.y <= 0 :
            self.hitBox.y = self.sprite[1].x = 0
            self.velocity[1] = -self.velocity[1]
        elif self.hitBox.y >= self.winHeight :
            self.hitBox.y = self.sprite[1].y = self.winHeight
            self.velocity[1] = -self.velocity[1]

        if self.weapon.shootCooldownRemaining == 0:
            bulletList = self.weapon.fire(self.hitBox.x, self.hitBox.centery, self.bulletVelX, self.bulletVelY)
        self.weapon.onTick(dt)
        return bulletList
    
    def animation(self):
        if 12 >= self.shooting > 8:
            self.sprite[0]= self.surfaceList[0]
        elif 8 >= self.shooting > 4:
            self.sprite[1]= self.surfaceList[1]
        elif 4 >= self.shooting > 0:
            self.sprite[2]= self.surfaceList[2]




# class EnnemyBullet(Rectangle):
#     def __init__(self, screen, x, y, width, height, speed):
#         Rectangle.__init__(self, screen, x, y, width, height, speed)
            
#     def go_on(self):
#         self.move_right()
#         self.draw((255, 255, 255))


