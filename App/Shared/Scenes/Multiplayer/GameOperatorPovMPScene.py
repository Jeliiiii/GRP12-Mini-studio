from Shared.Actors.Characters.AgentCharacterActor import AgentCharacterActor
from Shared.Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from .Scene import Scene
from ..Actors.World.WorldActor import WorldActor
import pygame
import os
from Shared.Components.operatorWindows.PseudoWindow import * #impoirte pseudoWindow et setup
from Shared.Components.operatorWindows.Carthage import Carthage
from Shared.Components.operatorWindows.Simon import Simon

class GameOperatorPovScene(Scene):
    
    def __init__(self):
        super().__init__()
        self.world = WorldActor(1)


        Simon((100, 100), (300, 300), color = (45, 177, 88, 1)),
        #Carthage((100, 100), (300, 300), color = (45, 177, 88, 1)),
        #PseudoWindow((100, 100), (90, 90), color = (45, 177, 88, 1))


        # self.character = AgentCharacterActor(100,100, characterSprite, speed=70)
        # self.bulletList = []
        # self.ennemiesList = [EnnemyActor(600, 500, ennemySprite, velX=-10, velY=0), EnnemyActor(600, 100, ennemySprite, velX=-20, velY=0)]

    def updateScene(self, inputs, dt):
        if PseudoWindow.loadedPseudoWindows:
            for window in PseudoWindow.loadedPseudoWindows:
                window.onTick(inputs, dt)



    def drawScene(self, window):
        window.fill( "#111126" )
        if PseudoWindow.loadedPseudoWindows:
            for prio in reversed(range(1, len(PseudoWindow.loadedPseudoWindows) + 1)):
                for win in range(len(PseudoWindow.loadedPseudoWindows)):
                    if PseudoWindow.loadedPseudoWindows[win].priority == prio:
                        PseudoWindow.loadedPseudoWindows[win].draw()


    def switchMainMenuScene(self):
        from .Menus.MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()