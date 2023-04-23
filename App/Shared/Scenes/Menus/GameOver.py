import socket
from Shared.Actors.UI.ButtonActor import ButtonActor
from .MenuScene import MenuScene
import pygame

class GameOverScene(Scene):
    def __init__(self):
        super().__init__("GameOver")
    
        self.menu.buttonsList=[ButtonActor("Back to menu", self.switchMainMenuScene)]


    def updateScene(self, inputs, dt):
        self.menu.handleMouse(inputs["MOUSE_POS"][0], inputs["MOUSE_POS"][1], inputs["MOUSE_BUTTONS"])
        self.HUD[1].onTick(inputs, dt)

    def drawScene(self, window):
        window.fill( "#111126" )
        self.menu.draw(window)

    def switchMainMenuScene(self):
        from .MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()


 