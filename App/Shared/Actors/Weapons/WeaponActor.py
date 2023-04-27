
class WeaponActor:
    def __init__(self, bullet, bulletSurface, shootCooldownRef, fireKeys):
        self.bullet = bullet
        self.bulletSurface = bulletSurface
        self.shootCooldownRef = shootCooldownRef
        self.shootCooldownRemaining = 0
        self.fireKeys = fireKeys
        self.shooting = 0

    def fire(self, x, y, velX, velY):
        self.shooting = 12
        bulletList = [self.bullet(x, y, self.bulletSurface, velX=velX, velY=velY)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList
    
    def onTick(self, dt):
        if self.shootCooldownRemaining != 0:
            self.shootCooldownRemaining -= dt
            if self.shootCooldownRemaining < 0:
                self.shootCooldownRemaining = 0
        if self.shooting!=0:
            self.shooting -=1

    def draw(self, window, coords):
        if 12 >= self.shooting > 8:
            window.blit(self.fireKeys["K1"], coords)
        elif 8 >= self.shooting > 4:
            window.blit(self.fireKeys["K2"], coords)
        elif 4 >= self.shooting > 0:
            window.blit(self.fireKeys["K3"], coords)



class QuadraWeaponActor(WeaponActor):
    def __init__(self, bullet, bulletSurface, shootCooldownRef, fireKeys):
        super().__init__(bullet, bulletSurface, shootCooldownRef, fireKeys)

    def fire(self, x, y, velX, velY):
        bulletList = [self.bullet(x, y, self.bulletSurface, velX=velX, velY=60),
                    self.bullet(x, y, self.bulletSurface, velX=velX, velY=-60),
                    self.bullet(x, y, self.bulletSurface, velX=velX, velY=20),
                    self.bullet(x, y, self.bulletSurface, velX=velX, velY=-20)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList
    


class DoubleWeaponActor(WeaponActor):
    def __init__(self, bullet, bulletSurface, shootCooldownRef, fireKeys):
        super().__init__(bullet, bulletSurface, shootCooldownRef, fireKeys)

    def fire(self, x, y, velX, velY):
        bulletList = [self.bullet(x, y, self.bulletSurface, velX=velX, velY=velY),self.bullet(x, y, self.bulletSurface, velX=velX, velY=-velY)]
        self.shootCooldownRemaining = self.shootCooldownRef
        return bulletList