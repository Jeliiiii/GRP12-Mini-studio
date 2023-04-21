import pygame
from window import *
from setup import *


rect_width = 50
rect_height = 50
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
        self.img = pygame.image.load("ressources/img/dodo/0.png")
        self.img = pygame.transform.scale(self.img, (50, 50))

    def move_up(self):
        #Déplace le personnage vers le haut.
        self.rect.move_ip(0, -self.speed)
        if self.rect.top < 0:
            self.rect.top = 0
        #comprend la collision mais bug a cose du scrolling (ex: quand tu mantient d il se stop mais quand tu lache il traverse)
        for tile in objectsList[0]:
            if self.rect.colliderect(tile.rect):
                if self.speed > 0:
                    self.rect.top = tile.rect.left
                break

    def move_down(self):
        #Déplace le personnage vers le bas.
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()

        for tile in objectsList[0]:
            if self.rect.colliderect(tile.rect):
                if self.speed > 0:
                    self.rect.bottom = tile.rect.left
                break

    def move_left(self):
        #Déplace le personnage vers la gauche.
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0

        for tile in objectsList[0]:
            if self.rect.colliderect(tile.rect):
                if self.speed > 0:
                    self.rect.left = tile.rect.left
                break

    def move_right(self):
        #Déplace le personnage vers la droite.
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()
        
        for tile in objectsList[0]:
            if self.rect.colliderect(tile.rect):
                if self.speed > 0:
                    self.rect.right = tile.rect.left
                break
        
    """def move_right(self):
    #Déplace le personnage vers la droite.
    self.rect.move_ip(self.speed, 0)
    if self.rect.right > self.screen.get_width():
        self.rect.right = self.screen.get_width()
    
    for tile in objectsList[0]:
        if self.rect.colliderect(tile.rect):
            self.rect.left = tile.rect.right
            break"""

    def check_collisions(self, objectsList):
        for tile in objectsList[0]:
            if self.rect.colliderect(tile.rect):
                self.show_loss_window()
                break


    def draw(self):
        #dessine le personnage sur l'écran.
        #pygame.draw.rect(self.screen, color, self.rect)
        self.screen.blit(self.img, self.rect)

    def getCoordinates(self):
        #renvoie les coordonnées actuelles du personnage.
        return [self.rect.x, self.rect.y]




rect = Character(window.screen, rect_x, rect_y, rect_width, rect_height, rect_speed)