import pygame
import csv
from main import *

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
                    img_rect.x = x * TILE_SIZE
                    img_rect.y = y * TILE_SIZE
                    tile_data = (img, img_rect)
                    if tile >= 0 and tile <= 10:
                        self.obstacle_list.append(tile_data)
                    elif tile >= 11 and tile <= 14:
                        pass#décoration
                    elif tile == 12:#joueur
                        player = Rectangle("player", x * TILE_SIZE, y * TILE_SIZE)
                        # health_bar = HealthBar(10, 10, player.health, player.health)
                    elif tile == 15:#enemis horizontaux
                        # player = Rectangle("enemi", x * TILE_SIZE, y * TILE_SIZE)
                        pass
                    elif tile == 16:#enemis verticaux
                        # player = Rectangle("enemi", x * TILE_SIZE, y * TILE_SIZE)
                        pass
                    elif tile == 17:#mur mortel
                        # death_wall = DeathWall("player", x * TILE_SIZE, y * TILE_SIZE)
                        pass
                    elif tile == 18:#vitre cassable par l'acteur
                        # glass = Glass("player", x * TILE_SIZE, y * TILE_SIZE)
                        pass
                    elif tile == 19:#Bonus
                        # item_box = ItemBox("player", x * TILE_SIZE, y * TILE_SIZE)
                        pass
                    elif tile == 20:#exit
                        pass

        return player#,health_bar
    
    def draw(self):
        for tile in self.obstacle_list:
            screen.blit(tile[0], tile[1])