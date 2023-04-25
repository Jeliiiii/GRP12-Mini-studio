import pygame

class SpriteSheetCutter:
        def __init__(self, file):
            self.sheet = pygame.image.load(file).convert()

        def cut(self, x, y, w, h, scale = 1):
            sprite = pygame.Surface([w, h])
            sprite.blit(self.sheet, (0, 0), (x, y, w, h))
            sprite.set_colorkey((255, 255, 255))
            return sprite