import pygame 

class Window :
    def __init__(self):
        pygame.init()
        # obtenir les informations sur l'écran actuel.
        info = pygame.display.Info()
        # définir les dimensions de la fenêtre à la taille de l'écran actuel.
        self.width = info.current_w
        self.height = info.current_h
        # créer une fenêtre avec les dimensions définies et sans bordure
        self.screen = pygame.display.set_mode((self.width, self.height),pygame.NOFRAME)