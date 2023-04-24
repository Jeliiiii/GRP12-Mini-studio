if(__name__ != "__main__"):
    import socket
    from threading import Thread, active_count
    from queue import Queue
    from Shared.Networking.Socket import Socket

class Server(Socket):
    """
    In functions naming:
        CT = ClientThread
        ST = ServerThread
    """

    def __init__(self):
        super().__init__()
        print("[SERVER] - Socket Initialized")
        self.serverState = initLevel()
        
    def handleConnections(self, clientsThreads):
        print("[SERVER] - Waiting for Connections...")
        while self.RUNNING:
            clientSocket, addr = self.socket.accept()
            if len(clientsThreads) == 0:
                clientRole = "OPERATOR"
            elif len(clientsThreads) == 1:
                clientRole = "AGENT"
            else:
                clientRole = "SPECTATOR"
            print(f'[SERVER] - Connection to {addr} Accepted')
            newClient = Thread(target=self.onNewClient, args=(clientSocket, clientRole)).start()
            clientsThreads.append(newClient)

    def onNewClient(self, clientSocket, role):
        connected = True
        print("[SERVER] - New Client Thread Opened")
        while connected:
            data = self.recv(clientSocket)
            if data:
                if data != "DISCONNECT":
                    print("[SERVER] - Event Received : ", data)
                    self.eventsQueue.put(data)
                    data = None
                else:
                    print("[SERVER] - Client Disconnecting Request / Closing Connection / Closing Thread")
                    break
        clientSocket.close()
        return
    
    def main(self):
        clientsThreads = []
        Thread(target= lambda : self.handleConnections(clientsThreads)).start()
        while self.RUNNING:
            if not self.eventsQueue.empty():
                print("[SERVER] - Event Used : ", self.eventsQueue.get())
                self.eventsQueue.task_done()

    def initLevelST(self):
        pass
    

    def close(self):
        self.RUNNING = False


    def start(self, HOST, PORT):
        print("[SERVER] - Starting Server")
        try:
            PORT = int(PORT)
            print("Port : ", PORT)
        except:
            print("Invalid PORT")
            return
        self.RUNNING = True
        self.eventsQueue = Queue()

        self.socket.bind((HOST, PORT))
        self.socket.listen()
        print("[SERVER] - Server Hosted on ", HOST, "; Port:", PORT)
        self.main()



if __name__ == "__main__":
    server = Server()
    server.start(socket.gethostname(), 65534)