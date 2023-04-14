# echo-client.py
import pygame
import socket
import pickle

pygame.init()
pygame.font.init()
 
RUNNING = True
INPUTS = thisdict = {
  "z": False,
  "q": False,
  "s": False,
  "d": False
}
HOST = '10.1.144.32'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

fenetre = pygame.display.set_mode((500,500))


class Rect:
    x = 10
    y = 10


def drawRect(rect):
    rect = pygame.draw.rect(
        fenetre,
        (255,0,0),
        pygame.Rect(rect.x, rect.y, 100, 100))

def boucle_principale():
    blitDisplay = drawRect
    rect = Rect()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))
        clock = pygame.time.Clock()
        with s:
            i = 1
            while RUNNING:
                fenetre.fill( (0,0,0) )
                
                rect = pickle.loads(s.recv(1024))
                print(rect.x)
                ## Exécute la fonction affecté à afficher (menu/jeu)
                blitDisplay(rect)
                
                
                pygame.display.update()
                i+=1
            pygame.quit()
            clock.tick(60)
 
boucle_principale()