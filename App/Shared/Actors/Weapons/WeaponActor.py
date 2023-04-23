
class WeaponActor:
    def __init__(self, bullet, bulletSurface, shootCooldownRef):
        self.bullet = bullet
        self.bulletSurface = bulletSurface
        self.shootCooldownRef = shootCooldownRef
        self.shootCooldownRemaining = 0

    def fire(self, x, y, velX, velY):
        bulletList = [self.bullet(x, y, self.bulletSurface, velX=velX, velY=velY)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList
    
    def fireDouble(self, x, y, velX, velY):
        bulletList = [self.bullet(x, y, self.bulletSurface, velX=velX, velY=velY),self.bullet(x, y, self.bulletSurface, velX=velX, velY=-velY)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList
    
    def onTick(self, dt):
        if self.shootCooldownRemaining != 0:
            self.shootCooldownRemaining -= dt
            if self.shootCooldownRemaining < 0:
                self.shootCooldownRemaining = 0


class QuadraWeaponActor(WeaponActor):
    def __init__(self, bullet, bulletSurface, shootCooldownRef):
        super().__init__(bullet, bulletSurface, shootCooldownRef)

    def fire(self, x, y, velX, velY):
        bulletList = [self.bullet(x, y, self.bulletSurface, velX=velX, velY=60),
                    self.bullet(x, y, self.bulletSurface, velX=velX, velY=-60),
                    self.bullet(x, y, self.bulletSurface, velX=velX, velY=20),
                    self.bullet(x, y, self.bulletSurface, velX=velX, velY=-20)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList