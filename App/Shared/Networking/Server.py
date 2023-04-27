
if(__name__ != "__main__"):
    import socket
    from threading import Thread, active_count
    from queue import Queue
    from Shared.Networking.Socket import Socket
    from .ServerStates.InitLevelState import InitLevelState
    from pygame import time


class Server(Socket):
    """
    In functions naming:
        CT = ClientThread
        ST = ServerThread
    """


    def __init__(self):
        super().__init__()
        print("[SERVER] - Socket Initialized")

    def start(self, HOST, PORT):
        print("[SERVER] - Starting Server")
        try:
            PORT = int(PORT)
            print("Port : ", PORT)
        except:
            print("Invalid PORT")
            return
        self.RUNNING = True
        
        self.socket.bind((HOST, PORT))
        self.socket.listen()
        print("[SERVER] - Server Hosted on ", HOST, "; Port:", PORT)

        self.serverState = InitLevelState()
        self.eventsQueue = Queue()
        self.serverClock = time.Clock()
        self.main()

    def close(self):
        self.RUNNING = False

    def handleConnections(self):
        print("[SERVER] - Waiting for Connections...")
        while self.RUNNING:
            clientSocket, addr = self.socket.accept()
            if len(self.serverState.clientsThreads) == 0:
                roleDataAlias = self.serverState.agentData
            elif len(self.serverState.clientsThreads) == 1:
                roleDataAlias = self.serverState.operatorData
            else:
                roleDataAlias = self.serverState.operatorData
            print(f'[SERVER] - Connection to {addr} Accepted')
            newClient = Thread(target=self.onNewClient, args=(clientSocket, roleDataAlias)).start()
            self.serverState.clientsThreads.append(newClient)

    def onNewClient(self, clientSocket, roleDataAlias):
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
            self.send(clientSocket, (self.serverState.globalData, roleDataAlias))
        clientSocket.close()
        return

    def serverUpdate(self):
        if self.serverState.nextGameState:
            self.serverState = self.serverState.nextGameState

    def main(self):
        Thread(target= self.handleConnections).start()
        
        while self.RUNNING:
            dt = self.serverClock.tick() / 1000
            event = (-1, None)
            if not self.eventsQueue.empty():
                event = self.eventsQueue.get()
                self.eventsQueue.task_done()

            self.serverState.stateUpdate(event)
            self.serverUpdate()
            

if __name__ == "__main__":
    server = Server()
    server.start(socket.gethostname(), 65534)