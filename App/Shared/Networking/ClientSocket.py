
import socket
from Shared.Networking.Socket import Socket

class ClientSocket(Socket):

    def __init__(self):
        super().__init__()

    def joinServer(self, SERVER_HOST, PORT):
        try:
            PORT = int(PORT)
            print("Joining through ")
            self.socket.connect((SERVER_HOST, PORT))
            print("[CLIENT] - Connected to server: ", SERVER_HOST)
        except:
            print(f"[CLIENT] - Connection to {SERVER_HOST} couldn't be established")
        

    def disconnect(self):
        self.send(self.socket, "DISCONNECT") #type = 3 -> disconnect type

if __name__ == "__main__":
    clientSocket = ClientSocket()
    clientSocket.joinServer(socket.gethostname(), 65534)