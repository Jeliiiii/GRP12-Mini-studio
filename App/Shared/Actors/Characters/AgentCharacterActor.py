import pygame
from ..Weapons.WeaponActor import WeaponActor
from ..BulletActor import BulletActor

class AgentCharacterActor:
    def __init__(self, x, y, width, height, speed=100):
        """
        Initializes the AgentCharacterActor class with the following 
        Parameters:
        - screen: l'objet Pygame représentant l'écran de jeu
        - x, y: la position de départ du personnage
        - width, height: la taille du personnage
        - speed: la vitesse de déplacement du personnage
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.weapon = WeaponActor(15, BulletActor, 0.5)


    def move(self, dt):
        self.rect.x += self.velocity[0] * dt * 10
        self.rect.y += self.velocity[1] * dt * 10

    def onTick(self, inputs, dt):
        bulletList = []
        self.velocity = [0,0]
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
                bulletList = self.weapon.fire(self.rect.x, self.rect.y, 100, 0)

        self.weapon.onTick(dt)
        self.move(dt)

        return bulletList

    def draw(self, window):
        #dessine le personnage sur l'écran.
        pygame.draw.rect(window, "red", self.rect)


        # Déplacement par seconde -> Déplacement par tick (tick variable)
        # 1 seconde   -> tick (variable)