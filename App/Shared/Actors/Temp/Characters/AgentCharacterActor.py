import pygame
from ..DefaultPawnActor import DefaultPawnActor
from ..Weapons.WeaponActor import WeaponActor


class AgentCharacterActor(DefaultPawnActor):
    def __init__(self, x, y, surface, weapon, speed=50):
        super().__init__(x, y, surface)
        self.speed = speed
        self.weapon = weapon

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

        self.weapon.onTick(dt)
        self.move(dt)

        return bulletList
