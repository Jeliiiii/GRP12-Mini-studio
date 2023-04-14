import pygame
import socket
import pickle

RUNNING = True
INPUTS = thisdict = {
  "z": False,
  "q": False,
  "s": False,
  "d": False
}
HOST = '10.1.144.32'  # The server's hostname or IP address
PORT = 65432  # The port used by the server

pygame.init()
pygame.font.init()

fenetre = pygame.display.set_mode((500,500))
 
myfont = pygame.font.SysFont('Helvetic', 20)


class Rect:
    x = 10
    y = 10
 
def gerer_events_principale(rect):
    global RUNNING
    global INPUTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                INPUTS["z"] = True
            if event.key == pygame.K_q:
                INPUTS["q"] = True
            if event.key == pygame.K_s:
                INPUTS["s"] = True
            if event.key == pygame.K_d:
                INPUTS["d"] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                INPUTS["z"] = False
            if event.key == pygame.K_q:
                INPUTS["q"] = False
            if event.key == pygame.K_s:
                INPUTS["s"] = False
            if event.key == pygame.K_d:
                INPUTS["d"] = False
###
        if INPUTS["z"] and rect.y >= 10:
            rect.y -= 10
            print("Moved on Z", rect.y)
        
        if INPUTS["q"] and rect.x >= 10:
            rect.x -= 10
            print("Moved on Q", rect.x)
        
        if INPUTS["s"] and rect.y <= 390:
            rect.y += 10
            print("Moved on S", rect.y)
        
        if INPUTS["d"] and rect.x <= 390: 
            rect.x += 10
            print("Moved on D", rect.x)

    return rect
 
def drawRect(rect):
    rect = pygame.draw.rect(
        fenetre,
        (255,0,0),
        pygame.Rect(rect.x, rect.y, 100, 100))

 
def boucle_principale():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        print("Server loaded")
        conn, addr = s.accept()
        print(f"Connected by {addr}")

        blitDisplay = drawRect
        rect = Rect()
        clock = pygame.time.Clock()
        with conn:
            while RUNNING:
                conn.sendall(pickle.dumps(rect))
                fenetre.fill( (0,0,0) )
                
                rect = gerer_events_principale(rect)
                
                ## Exécute la fonction affecté à afficher (menu/jeu)
                blitDisplay(rect)
                
                pygame.display.update()
                clock.tick(60)
                
            pygame.quit()
    
 
 
boucle_principale()

class Server():

    def __init__(self, port):
        self.PORT = port  # The port used by the server
        self.HOST = socket.gethostname()  # The server's hostname or IP address
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.serverSocket:
            self.serverSocket.bind((HOST, PORT))
            self.serverSocket.listen(2)
            print("Server loaded")

    def send(self, clientSocket, data):
        data = pickle.dumps(data)
        header = pickle.dumps(len(data))
        clientSocket.sendall(header, data)
        pass

    def sendAll(self, data):
        for clientSocket in self.clientSockets:
            self.send(clientSocket, data)

    def receive(self):
        pass

    def acceptConnections(self, connAmount):
        while(len(self.clientSockets) < connAmount):
            conn, addr = s.accept(connAmount)
            self.clientSockets = [[conn, addr],[conn, addr]] = [conn, conn]


    def main():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen(1)
            print("Server loaded")
            self.acceptConnection(2)
            
            
            print(f"Connected by {addr}")


if (__name__ == "__main__"):
    server = Server(65432)


# serializedGameState = dumps(GameState)
# header = encode(len(serializedGameState)) + encode(len(type))
# serializedGameState = header + type + serializedGameState



# header = decode(recv(8))
# type = decode(recv(8))
# gameState = recv(header)
