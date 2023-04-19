import pygame
from character import *
import math
from window import *
from weapons import *
from ennemies import *
from rectangle import *
from mainmenu import *

pygame.init()


window = Window()



clock = pygame.time.Clock()
FPS = 60

black = (0, 0, 0)
white = (255, 255, 255)

pygame.font.init()
pygame.display.set_caption("Birds Of Chaos")
icon = pygame.image.load("ressources/img/dodo.png").convert_alpha()
pygame.display.set_icon(icon)
mouse = pygame.image.load("ressources/img/curseur.png").convert_alpha()
mouse_pos = (0, 0)
pygame.mouse.set_visible(0)



rect = Character(window.screen, rect_x, rect_y, rect_width, rect_height, rect_speed)


#Liste des objets à l'écran
#objectsList = [Basic(window, window.largeur+20, 100, 50, 50, 5)]
objectsList = [Idle(window, window.width+20, 100, 50, 50, 5)]

keys = []

#Liste des balles à l'écran
bulletList = []

# Image background
bg = pygame.image.load("ressources/img/bg.png").convert()
bg_width = bg.get_width()
bg_rect = bg.get_rect()

scroll = 0
tiles = math.ceil(window.width / bg_width) + 1

# Blit the background image
for i in range(0, tiles):
    window.screen.blit(bg, (i * bg_width, 0))

#On initialise la variable de cooldown du shoot
shootCd = 0

is_hit = False

main_menu = MainMenu(window)

# Boucle du programme
running = True

# Boucle du jeu
play = False

# Boucle du menu
menu = True

# On entre dans la boucle du programme (Le programme se lance)
while running:
    
    # Affichage du scorlling background
    clock.tick(FPS)
    
    # On entre dans la boucle du menu
    if menu == True:
        
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = event.pos
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            if main_menu.handle_events(events):
                print("Starting game...")
                menu = False
                play = True

            main_menu.draw()
            
            
            
    # On entre dans la boucle de jeu
    if play == True:
        
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
        if pygame.K_SPACE in keys and shootCd == 0:
            bulletList.append(classic.bullet(window.screen, rect.getCoordinates()[0], rect.getCoordinates()[1]+40, 20, 10, 30, "ally"))
            shootCd = classic.tear
        
        if shootCd > 0:
            shootCd -= 1

        # Effacement de l'écran
        # screen.fill(white)

        # Blit the background image with scrolling
        for i in range(0, tiles):
            window.screen.blit(bg, (i * bg_width + scroll, 0))

        #Scrolling background
        scroll -= 5

        #boucle du background
        if abs(scroll) > bg_width:
            scroll = 0

        # Dessin du rectangle
        rect.draw(white)


        #On active les go_on
        for object in objectsList:
            object.go_on()
            if object.doing: #point mystere
                for referencial in objectsList:
                    if object != referencial :
                        if object.rect.colliderect(referencial):
                            if object.doing == object.move_up:
                                object.doing = object.move_down
                            else :
                                object.doing = object.move_up
                if object.tearRemaining==0:
                    object.tearRemaining = object.tearTimer
                    if type(object)== Basic:
                        bulletList.append(object.bullet.bullet(window.screen, object.getCoordinates()[0], object.getCoordinates()[1]+40, 20, 10, 30, "ennemy"))
                    elif type(object)== Idle:
                        bulletList.append(object.bullet.bullet(window.screen, object.getCoordinates()[0], object.getCoordinates()[1]+40, 10, 20, 10, "ennemy"))


        #Operations des balles
        for bullet in bulletList:
            #Déplacement
            bullet.go_on()
            #Check des collisions avec les objets de objectsList
            for object in objectsList:
                if bullet.rect.colliderect(object) and object.side!=bullet.side:
                    bulletList.remove(bullet)
                    objectsList.remove(object)
            if bullet.rect.colliderect(rect) and is_hit == False:
                print("game over")#game over a set ici
                is_hit = True
            #Destruction des balles une fois le field traversé sans avoir rien touché
            if bullet.getCoordinates()[0] == window.width+20 :
                bulletList.remove(bullet)

    # Rafraîchissement de l'affichage
    window.screen.blit(mouse, mouse_pos)
    pygame.display.flip()
    pygame.display.update()
            

pygame.quit()

