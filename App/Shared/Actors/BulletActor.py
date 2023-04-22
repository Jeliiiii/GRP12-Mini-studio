import pygame
from .DefaultPawnActor import DefaultPawnActor

class BulletActor(DefaultPawnActor):
    def __init__(self, x, y, surface, velX=0, velY=0):
        super().__init__(x, y, surface, velX=velX, velY=velY)
        self.damage = 5

    def onTick(self, dt):
        super().onTick(dt)
