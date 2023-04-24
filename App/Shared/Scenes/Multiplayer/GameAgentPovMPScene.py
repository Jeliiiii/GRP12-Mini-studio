from ..Scene import Scene
from ...Actors.World.WorldActor import WorldActor

class GameAgentPovMPScene(Scene):
    
    def __init__(self):
        super().__init__()
        print("AgentPov Loaded")

    def updateScene(self, inputs, dt):
        super().updateScene(inputs, dt)

    def drawScene(self, window):
        pass

