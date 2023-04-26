from Shared.Actors.Characters.AgentCharacterActor import AgentCharacterActor
from Shared.Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from .Scene import Scene
from ..Actors.World.WorldActor import WorldActor
import pygame
import os 

class GameAgentPovScene(Scene):
    
    def __init__(self):
        super().__init__()
        self.world = WorldActor(0)

        

    def updateScene(self, inputs, dt):

        #
        #
        #receive
        #
        #
        

        self.world.onTick(inputs, dt)
        
            


    def drawScene(self, window):
        window.fill( "#111126" )
        self.world.draw(window)
        if self.world.nextScene:
            self.nextScene = self.world.nextScene


    def switchMainMenuScene(self):
        from .Menus.MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()