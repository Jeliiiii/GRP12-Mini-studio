import pygame 

class Window :
    def __init__(self):
        pygame.init()
        info = pygame.display.Info()
        self.largeur = info.current_w
        self.hauteur = info.current_h
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))