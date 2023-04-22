from ...Weapons.WeaponActor import WeaponActor
from ...BulletActor import BulletActor
from random import randint
import pygame

class EnnemyActor:
    def __init__(self, x, y, width, height, velX, velY):
        self.rect = pygame.Rect(x, y, width, height)
        self.winHeight = 720
        self.weapon = WeaponActor(25, BulletActor, 0.7)
        self.side = "ennemy"
        self.velocity = [velX, velY]
        self.health = 10

    def shot(self, damage):
        self.health -= damage

    def onTick(self, dt):
        bulletList = []
        self.rect.x += self.velocity[0] * dt * 10
        self.rect.y += self.velocity[1] * dt * 10
        
        if self.rect.y <= 0 :
            self.rect.y = 0
            self.velocity[1] = -self.velocity[1]
        elif self.rect.y >= self.winHeight :
            self.rect.y = self.winHeight
            self.velocity[1] = -self.velocity[1]

        if self.weapon.shootCooldownRemaining == 0:
            bulletList = self.weapon.fireDouble(self.rect.x, self.rect.y, -70, 40)
        self.weapon.onTick(dt)
        return bulletList

    def draw(self, window):
        #dessine le personnage sur l'écran.
        pygame.draw.rect(window, "red", self.rect)


# class EnnemyBullet(Rectangle):
#     def __init__(self, screen, x, y, width, height, speed):
#         Rectangle.__init__(self, screen, x, y, width, height, speed)
            
#     def go_on(self):
#         self.move_right()
#         self.draw((255, 255, 255))


