import pygame

class WeaponActor:
    def __init__(self, bullet, shootCooldownRef):
        self.bullet = bullet
        self.shootCooldownRef = shootCooldownRef
        self.shootCooldownRemaining = 0

    def fire(self, x, y, velX, velY):
        bulletList = [self.bullet(x, y, velX, velY)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList
    
    def fireDouble(self, x, y, velX, velY):
        bulletList = [self.bullet(x, y, velX, velY),self.bullet(x, y, velX, -velY),self.bullet(x, y, velX, 0)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList
    
    def onTick(self, dt):
        if self.shootCooldownRemaining != 0:
            self.shootCooldownRemaining -= dt
            if self.shootCooldownRemaining < 0:
                self.shootCooldownRemaining = 0


