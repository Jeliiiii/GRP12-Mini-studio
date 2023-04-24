from .MPScene import MPScene
from .GameAgentPovMPScene import GameAgentPovMPScene
from .GameOperatorPovMPScene import GameOperatorPovMPScene


class WaitingScreenMPScene(MPScene):
    
    def __init__(self, clientSocket=None):
        super().__init__(clientSocket)
        self.data.startGame = 0

    def updateScene(self, inputs, dt):
        super().__init__()
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