from .Scene import Scene
from ..Actors.World.WorldActor import WorldActor

class GameAgentPovScene(Scene):
    
    def __init__(self):
        super().__init__()
        self.world = WorldActor(1)

    def updateScene(self, inputs, dt):
        self.world.onTick(inputs, dt)


    def drawScene(self, window):
        window.fill( "#111126" )
        self.world.draw(window)


    def switchMainMenuScene(self):
        from .Menus.MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()