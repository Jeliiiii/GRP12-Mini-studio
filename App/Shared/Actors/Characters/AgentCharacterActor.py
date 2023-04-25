import pygame
from ..DefaultPawnActor import DefaultPawnActor
from ..Weapons.WeaponActor import WeaponActor


class AgentCharacterActor(DefaultPawnActor):
    def __init__(self, x, y, surfaceList, weapon, speed=50):
        self.surfaceList = surfaceList
        self.sprite =  [surfaceList["FORWARD"][0], surfaceList["FORWARD"][0].get_rect()]
        super().__init__(x, y)
        self.speed = speed
        self.weapon = weapon
        self.animCooldown = 1000
        print("init")

    def onTick(self, inputs, dt):
        bulletList = []
        self.velocity = [0,0,0]
        if pygame.K_z in inputs["ACTIVE_KEYS"]:
            self.velocity[1] = -self.speed
        if pygame.K_s in inputs["ACTIVE_KEYS"]:
            self.velocity[1] = self.speed
        if pygame.K_q in inputs["ACTIVE_KEYS"]:
            self.velocity[0] = -self.speed
        if pygame.K_d in inputs["ACTIVE_KEYS"]:
            self.velocity[0] = self.speed
        if pygame.K_SPACE in inputs["ACTIVE_KEYS"]:
            if self.weapon.shootCooldownRemaining <= 0:
                bulletList = self.weapon.fire(self.hitBox.x, self.hitBox.y, 100, 0)
        
        self.animation()
        self.weapon.onTick(dt)
        self.move(dt)

        return bulletList

    def animation(self):
        self.animCooldown -=1

        if self.velocity[1] < 0:
            if self.animCooldown == 1000:
                print(10)
                self.sprite[0] = self.surfaceList["UP"][0]
            elif self.animCooldown == 500:
                print(5)
                self.sprite[0] = self.surfaceList["UP"][1]
            elif self.animCooldown == 1:
                print(0)
                self.animCooldown = 1000

        elif self.velocity[1] > 0:
            if self.animCooldown == 1000:
                print(10)
                self.sprite[0] = self.surfaceList["DOWN"][0]
            elif self.animCooldown == 500:
                print(5)
                self.sprite[0] = self.surfaceList["DOWN"][1]
            elif self.animCooldown == 1:
                print(0)
                self.animCooldown = 1000

        elif self.velocity[0] < 0:
            if self.animCooldown == 1000:
                print(10)
                self.sprite[0] = self.surfaceList["BACK"][0]
            elif self.animCooldown == 500:
                print(5)
                self.sprite[0] = self.surfaceList["BACK"][1]
            elif self.animCooldown == 1:
                print(0)
                self.animCooldown = 1000

        else :
            if self.animCooldown == 1000:
                print(10)
                self.sprite[0] = self.surfaceList["FORWARD"][0]
            elif self.animCooldown == 500:
                print(5)
                self.sprite[0] = self.surfaceList["FORWARD"][1]
            elif self.animCooldown == 1:
                print(0)
                self.animCooldown = 1000