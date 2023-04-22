import pygame

class BulletActor:
    def __init__(self, x, y, velX, velY, width=10, height=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = [velX, velY]
        self.damage = 5
            
    def onTick(self, dt):
        self.rect.x += self.velocity[0] * dt * 10
        self.rect.y += self.velocity[1] * dt * 10

    def draw(self, window):
        # Dessine le rectangle avec la couleur spécifiée
        pygame.draw.rect(window, "red", self.rect)