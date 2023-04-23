import pygame
from .DefaultPawnActor import DefaultPawnActor

class ClassicBullet(DefaultPawnActor):
    def __init__(self, x, y, surface, velX=0, velY=0):
        super().__init__(x, y, surface, velX=velX, velY=velY)
        self.damage = 5

    def onTick(self, dt):
        super().onTick(dt)

    def onHit(self, bulletList):
        bulletList.remove(self)


class TankBullet(DefaultPawnActor):
    def __init__(self, x, y, surface, velX=0, velY=0):
        super().__init__(x, y, surface, velX=velX, velY=velY)
        self.damage = 50
        self.durability = 5

    def onTick(self, dt):
        super().onTick(dt)

    def onHit(self, bulletList):
        if self.durability == 0:
            bulletList.remove(self)
        else :
            self.durability-=1
