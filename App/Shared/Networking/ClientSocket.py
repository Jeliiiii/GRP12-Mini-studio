if(__name__ != "__main__"):
    import socket
    from Shared.Networking import Socket

class ClientSocket(Socket.Socket):

    def __init__(self):
        super().__init__()

    def joinServer(self, SERVER_HOST, PORT):
        try:
            self.socket.connect((SERVER_HOST, PORT))
            print("[CLIENT] - Connected to server: ", SERVER_HOST)
        except:
            print(f"[CLIENT] - Connection to {SERVER_HOST} couldn't be established")

    def disconnect(self):
        self.send(self.socket, 0, 3) #type = 3 -> disconnect type

if __name__ == "__main__":
    clientSocket = ClientSocket()
    clientSocket.joinServer(socket.gethostname(), 65534)