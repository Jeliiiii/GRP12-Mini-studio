import pygame

class Rectangle:
    def __init__(self, screen, x, y, width, height, speed):
        # Initialise le rectangle avec une position, une taille et une vitesse
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move_up(self):
        # Déplace le rectangle vers le haut
        self.rect.move_ip(0, -self.speed)

    def move_down(self):
        # Déplace le rectangle vers le bas
        self.rect.move_ip(0, self.speed)

    def move_left(self):
        # Déplace le rectangle vers la gauche
        self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        # Déplace le rectangle vers la droite
        self.rect.move_ip(self.speed, 0)

    def draw(self, color):
        # Dessine le rectangle avec la couleur spécifiée
        pygame.draw.rect(self.screen, color, self.rect)

    def getCoordinates(self):
        # Renvoie les coordonnées du rectangle sous forme de liste [x, y]
        return [self.rect.x, self.rect.y]
