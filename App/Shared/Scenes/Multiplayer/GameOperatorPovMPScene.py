from Shared.Actors.Characters.AgentCharacterActor import AgentCharacterActor
from Shared.Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from ..Scene import Scene
from ...Actors.World.WorldActor import WorldActor
import pygame
import os

class GameOperatorPovMPScene(Scene):
    
    def __init__(self):
        super().__init__()
        print("OperatorPov Loaded")

    def updateScene(self, inputs, dt):
        pass


    def drawScene(self, window):
        pass
