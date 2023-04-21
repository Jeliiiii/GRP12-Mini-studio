import pygame
import csv
from character import *
from setup import *


ROWS = 32
COLS = 401
TILE_SIZE = window.hauteur // ROWS
TILE_TYPES = 21
level = 3

#tiles liste
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"ressources/img/tiles/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)


class Block(Rectangle):
    def __init__(self, data, window):
        Rectangle.__init__(self, window.screen, data[1].x, data[1].y, window.hauteur/32, window.hauteur/32, 5)
        self.data = data
        self.destructible = False

    def go_on(self):
        self.move_left()
        self.data[1][0] = self.getCoordinates()[0]
        self.draw()

    def draw(self):
        self.screen.blit(self.data[0], self.data[1])



class World():
    def __init__(self):
        pass

    def process_data(self, data, objectsList):
        #parcourir chaque valeur dans le fichier de données de niveau
        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    img = img_list[tile]
                    img_rect = img.get_rect()
                    img_rect.x = x*TILE_SIZE
                    img_rect.y = y*TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 8:
                        objectsList[0].append(Block(tile_data, window))
                    elif tile >= 9 and tile <= 10:
                        pass #murs destructibles/ créables par l'opérateur
                    elif tile == 11 and tile <= 14:
                        pass # 11 : shield faibles -> Destructibles
                    elif tile == 12:
                        player = Character(window.screen,x*TILE_SIZE, y*TILE_SIZE, 40, 40, 15) #12 : joueur
                    elif tile == 13 :
                        pass #13 : shield fort -> indestructible
                    elif tile == 14 :
                        pass #14 : non utilisé
                    elif tile == 15 : 
                        buffer.append(Basic(window, x*TILE_SIZE, y*TILE_SIZE, 5))
                        """ca fonctionne mais il y a beaucoup trop d'operations a chaque frame : ca fait lag une dinguerie"""
                        #enemy = Character(window.screen, x*TILE_SIZE, y*TILE_SIZE, 50, 100, 5) #15 : ennemi horizontal
                        pass
                    elif tile == 16 : 
                        enemy = Character(window.screen, x*TILE_SIZE, y*TILE_SIZE, 50, 100, 5) #16 : ennemi vertical
                    elif tile == 17 :
                        pass # 17 : mur électrifié
                    elif tile >= 18 and tile <= 19 :
                        pass # inutilisé
                    elif tile == 20 :
                        pass #Création de fin de niveau

        return player
    

#créer un liste de tile vide
world_data = []
for row in range(ROWS):
    r = [-1] * COLS
    world_data.append(r)
#charger des données de niveau et créer un monde (pour lire le dossier csv)
with open(f"level{level}_data.csv", newline="") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for x, row in enumerate(reader):
        for y, tile in enumerate(row):
            world_data[x][y] =  int(tile)
world = World()
player = world.process_data(world_data, objectsList)

