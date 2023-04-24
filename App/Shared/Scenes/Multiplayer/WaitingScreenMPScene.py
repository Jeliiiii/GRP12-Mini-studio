from ..Scene import Scene
from ..Multiplayer.GameAgentPovMPScene import GameAgentPovMPScene
from ..Multiplayer.GameOperatorPovMPScene import GameOperatorPovMPScene


class WaitingScreenMPScene(Scene):
    
    def __init__(self, clientSocket=None):
        super().__init__()
        self.clientSocket = clientSocket
        self.data = None

    def updateScene(self, inputs, dt):
        self.clientSocket.send(self.clientSocket.socket, inputs)
        self.data = self.clientSocket.recv(self.clientSocket.socket)
        if self.data.startGame:
            if self.data.role == 0: #0 = "AGENT"
                self.sceneSwitcher(GameAgentPovMPScene())
            elif self.data.role == 1: #1 = "OPERATOR"
                self.sceneSwitcher(GameOperatorPovMPScene())
            #else: self.sceneSwitcher(GameSpectatorPovMPScene()) #Any = "SPECTATOR"

    def drawScene(self, window):
        data = self.clientSocket.recv(self.clientSocket.socket)
        if data:
            print("[CLIENT] - Draw GameState", data)