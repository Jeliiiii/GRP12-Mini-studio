import socket
from threading import Thread
from Shared.Networking.Server import Server
from .MenuScene import MenuScene
from Shared.Actors.UI.ButtonActor import ButtonActor

import pygame

class MainMenuScene(MenuScene):
    
    def __init__(self):
        super().__init__("MainMenu")

        (windowWidth, windowHeight) = pygame.display.get_window_size()

        self.menu.buttonsList=[ButtonActor("Play", self.switchGameAgentPovScene),
                               ButtonActor("Spy", self.switchGameOperatorPovScene),
                               ButtonActor("Host", self.switchHostInterfaceScene),
                               ButtonActor("Join", self.switchJoinInterfaceScene),
                               ButtonActor("Quit", self.quit)
                                ]
        
        
        buttonsAmount = self.menu.getButtonsAmount()
        buttonsFontSize = windowHeight/16
        buttonsFont = pygame.freetype.Font("App\Shared\Assets\Graphics\Fonts\Square.ttf")
        key=0
        for button in self.menu.buttonsList:
            button.renderDefaultSprite(buttonsFont, buttonsFontSize, "white")
            button.moveSpriteOnCenter(windowWidth/2, (key+2)*windowHeight/(buttonsAmount*2))
            key+=1




    def updateScene(self, inputs, dt):
        self.menu.handleMouse(inputs["MOUSE_POS"][0], inputs["MOUSE_POS"][1], inputs["MOUSE_BUTTONS"])


    def drawScene(self, window):
        window.fill( "#111126" )
        self.menu.draw(window)




    def switchGameAgentPovScene(self):
        from ..GameAgentPovScene import GameAgentPovScene
        self.nextScene = GameAgentPovScene()

    def switchHostInterfaceScene(self):
        from .HostInterfaceScene import HostInterfaceScene
        self.nextScene = HostInterfaceScene()

    def switchJoinInterfaceScene(self):
        from .JoinInterfaceScene import JoinInterfaceScene
        self.nextScene = JoinInterfaceScene()

    def switchGameOperatorPovScene(self):
        from ..GameOperatorPovScene import GameOperatorPovScene
        self.nextScene = GameOperatorPovScene()