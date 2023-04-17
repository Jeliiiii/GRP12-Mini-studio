import pygame
from character import *
# from level import *
import math
import csv
import os

pygame.init()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

clock = pygame.time.Clock()
FPS = 60
ROWS = 16
COLS = 150
TILE_SIZE = screen_height // ROWS
TILE_TYPES = 10
level = 0

black = (0, 0, 0)
white = (255, 255, 255)

pygame.font.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
screen = pygame.display.set_mode((1920, 1080), pygame.NOFRAME)
pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)
option = pygame.image.load("ressources/img/option.png").convert_alpha()
option_pos = (1600, 150)
mouse = pygame.image.load("ressources/img/curseur.png").convert_alpha()
mouse_pos = (0, 0)
pygame.mouse.set_visible(0)

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

        return
    
    def draw(self):
        for tile in self.obstacle_list:
            screen.blit(tile[0], tile[1])

#tiles liste
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"ressources/img/{x}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)

rect_width = 50
rect_height = 100
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rect_speed = 15
rect = Rectangle(screen, rect_x, rect_y, rect_width, rect_height, rect_speed)


test = Rectangle(screen, 1500, 500, rect_width, rect_height, rect_speed)

objectsList = [test]

keys = []

#Liste des balles à l'écran
bulletList = []

# Image background
bg = pygame.image.load("ressources/img/bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0
tiles = math.ceil(screen_width / bg_width) + 1

# Blit the background image
for i in range(0, tiles):
    screen.blit(bg, (i * bg_width, 0))


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
# world = World()
# player = world.process_data(world_data)



# Boucle de jeu
running = True
while running:
    # Affichage du scorlling background
    clock.tick(FPS)

    world.draw()

    # Gestion des événements pygame
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys.append(event.key)
        elif event.type == pygame.KEYUP:
            keys.remove(event.key)
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
        if event == pygame.MOUSEBUTTONDOWN == option:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 100))

    # Déplacement continu avec collisions
    if pygame.K_z in keys:
        rect.move_up()
    if pygame.K_s in keys:
        rect.move_down()
    if pygame.K_q in keys:
        rect.move_left()
    if pygame.K_d in keys:
        rect.move_right()

    #Tir
    if pygame.K_SPACE in keys:
        bulletList.append(Bullet(screen, rect.getCoordinates()[0], rect.getCoordinates()[1]+40, 20, 10, 30))

    # Effacement de l'écran
    # screen.fill(white)

    # Blit the background image with scrolling
    for i in range(0, tiles):
        screen.blit(bg, (i * bg_width + scroll, 0))

    #Scrolling background
    scroll -= 5

    #boucle du background
    if abs(scroll) > bg_width:
        scroll = 0

    # Dessin du rectangle
    rect.draw(black)

    test.draw(black)


    #Operations des balles
    for bullet in bulletList:
        #Déplacement
        bullet.go_on()
        #Check des collisions avec les objets de objectsList
        for object in objectsList:
            if bullet.rect.colliderect(test):
                bulletList.remove(bullet)
        #Destruction des balles une fois le field traversé sans avoir rien touché
        if bullet.getCoordinates()[0] == screen_width-20 :
            bulletList.remove(bullet)


    # Rafraîchissement de l'affichage
    screen.blit(mouse, mouse_pos)
    screen.blit(option, option_pos)
    # pygame.display.flip()

    pygame.display.update()

pygame.quit()
