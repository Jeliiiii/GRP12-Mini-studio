from .MPScene import MPScene
from .GameAgentPovMPScene import GameAgentPovMPScene
from .GameOperatorPovMPScene import GameOperatorPovMPScene

class WaitingScreenMPScene(MPScene):
    
    def __init__(self, clientSocket=None):
        super().__init__(clientSocket)
        self.role = -1
        
    def updateScene(self, inputs, dt):
        super().updateScene(inputs, dt)
        if self.data[0][0] == 1:
            globalData = self.data[0]
            roleData = self.data[1]

            if globalData[0]:
                if roleData[0] == 0: #0 = "AGENT"
                    self.sceneSwitcher(GameAgentPovMPScene())
                elif roleData[0] == 1: #1 = "OPERATOR"
                    self.sceneSwitcher(GameOperatorPovMPScene())
                #else: self.sceneSwitcher(GameSpectatorPovMPScene()) #Any = "SPECTATOR"

    def drawScene(self, window):
        pass