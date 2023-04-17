import pygame
from window import *

window = Window()

rect_width = 50
rect_height = 100
rect_x = (window.largeur - rect_width) // 2
rect_y = (window.hauteur - rect_height) // 2
rect_speed = 15
class Character:
    def __init__(self, screen, x, y, width, height, speed):
        """
        Initialise la classe Character avec les paramètres suivants:
        - screen: l'objet Pygame représentant l'écran de jeu
        - x, y: la position de départ du personnage
        - width, height: la taille du personnage
        - speed: la vitesse de déplacement du personnage
        """
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.side = "ally"

    def move_up(self):
        #Déplace le personnage vers le haut.
        self.rect.move_ip(0, -self.speed)
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        #Déplace le personnage vers le bas.
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()

    def move_left(self):
        #Déplace le personnage vers la gauche.
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        #Déplace le personnage vers la droite.
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()

    def draw(self, color):
        #dessine le personnage sur l'écran.
        pygame.draw.rect(self.screen, color, self.rect)

    def getCoordinates(self):
        #renvoie les coordonnées actuelles du personnage.
        return [self.rect.x, self.rect.y]




