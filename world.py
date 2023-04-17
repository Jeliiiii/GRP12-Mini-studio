import pygame
import csv
from character import *
from window import *
from ennemies import *

window = Window()
ROWS = 16
COLS = 150
TILE_SIZE = window.hauteur // ROWS
TILE_TYPES = 21
level = 0

#tiles liste
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"ressources/img/tiles/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

class World():
    def __init__(self):
        self.obstacle_list = []

    def process_data(self, data):
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
                        self.obstacle_list.append(tile_data) #Sol + murs
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
                        enemy = Character(window.screen, x*TILE_SIZE, y*TILE_SIZE, 50, 100, 5) #15 : ennemi horizontal
                    elif tile == 16 : 
                        enemy = Character(window.screen, x*TILE_SIZE, y*TILE_SIZE, 50, 100, 5) #16 : ennemi vertical
                    elif tile == 17 :
                        pass # 17 : mur électrifié
                    elif tile >= 18 and tile <= 19 :
                        pass # inutilisé
                    elif tile == 20 :
                        pass #Création de fin de niveau

        return player
    
    def draw(self):
        for tile in self.obstacle_list:
            window.screen.blit(tile[0], tile[1])

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
print(world_data)
world = World()
player = world.process_data(world_data)