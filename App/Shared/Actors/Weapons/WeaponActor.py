
class WeaponActor:
    def __init__(self, bullet, bulletSurface, shootCooldownRef, fireKeys):
        self.bullet = bullet
        self.bulletSurface = bulletSurface
        self.shootCooldownRef = shootCooldownRef
        self.shootCooldownRemaining = 0
        self.fireKeys = fireKeys
        self.shooting = 0

    def fire(self, x, y, velX, velY):
        self.shooting = 6
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

    def draw(self, window, coords):
        if self.shooting == 5 or self.shooting == 6:
            window.blit(self.fireKeys["K1"], coords)
        elif self.shooting == 4 or self.shooting == 3:
            window.blit(self.fireKeys["K2"], coords)
        elif self.shooting == 2 or self.shooting == 1:
            window.blit(self.fireKeys["K3"], coords)



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