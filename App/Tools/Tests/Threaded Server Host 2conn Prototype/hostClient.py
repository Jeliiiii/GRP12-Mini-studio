import pygame
import pickle
import socket
from threading import Thread
from queue import Queue

class Client:

    def __init__(self):
        
        self.RUNNING = True
        self.BG_COLORS = ["black", "red", "yellow2", "blue"]
        self.colorId = 0
        self.SERVER_STATE = False
        self.clientSocket = None

    def onNewClient(self, clientSocket, serverSocket, eventsQueue):
        print("New Client Thread Loaded")
        while True:
            try:
                data = clientSocket.recv(1024)
            except:
                pass
            if data:
                print("[SERVER] - Event Received : ", pickle.loads(data))
                eventsQueue.put(pickle.loads(data))
                data = None

    def hostThreadedServer(self, args):
        print("Creating Server")
        HOST = socket.gethostname()
        PORT = 60540
        eventsQueue = Queue()
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
            serverSocket.bind((HOST, PORT))
            serverSocket.listen(2)
            serverSocket.setblocking(False)
            print("Server loaded")

            while True:
                try:
                    clientSocket, addr = serverSocket.accept()
                    print(f'[SERVER] Accepted Connection to : {clientSocket}, {addr}')
                    Thread(target=self.onNewClient, args=(clientSocket, serverSocket, eventsQueue)).start()
                except socket.error:
                    pass
                if not eventsQueue.empty():
                    print("[SERVER] - ", eventsQueue.get())
                    eventsQueue.task_done()
                    


    def joinServer(self, ip, port):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSocket.connect((socket.gethostname(), 60540))
        print("[CLIENT] - Connected to server")
        self.clientSocket.sendall(pickle.dumps(self.BG_COLORS[self.colorId]))
            
    def eventsHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.RUNNING = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    self.RUNNING = False
                if event.key == pygame.K_d:
                    self.colorId += 1 
                    if(self.colorId == 4):
                        self.colorId = 0
                    if self.SERVER_STATE:
                        self.clientSocket.sendall(pickle.dumps(self.BG_COLORS[self.colorId]))
                if event.key == pygame.K_q:
                    self.colorId -= 1 
                    if(self.colorId == -1):
                        self.colorId = 3
                    if self.SERVER_STATE:
                        self.clientSocket.sendall(pickle.dumps(self.BG_COLORS[self.colorId]))

                if event.key == pygame.K_h:
                    print(self.SERVER_STATE)
                    if self.SERVER_STATE == False:
                        self.SERVER_STATE = True
                        self.serverThread = Thread(target=self.hostThreadedServer, args=(self.SERVER_STATE,))
                        self.serverThread.start()
                    else:
                        self.SERVER_STATE = False
                        self.serverThread.join()
                        print("Server Closed")
                if event.key == pygame.K_j:
                    print("Joining Server...")
                    self.joinServer(socket.gethostname(),60540)
                    

    def main(self):
        pygame.init()
        window = pygame.display.set_mode((500,500))
        clock = pygame.time.Clock()
        while self.RUNNING:
            self.eventsHandler()
            window.fill( self.BG_COLORS[self.colorId] )
            
            pygame.display.update()
            clock.tick(60)

        pygame.quit()





if( __name__ == "__main__"):
    client = Client()
    client.main()