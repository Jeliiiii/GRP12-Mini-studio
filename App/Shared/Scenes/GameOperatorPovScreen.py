from threading import Thread
from Shared.Networking.Server import Server
import socket
from Shared.Actors.UI.ButtonActor import ButtonActor
from .Menus.MenuScene import MenuScene
import pygame
from Components.operatorWindows.PseudoWindow import * #importe la pseudowindow et le setup
from Components.operatorWindows.Simon import Simon
from Components.operatorWindows.Carthage import Carthage

class GameOperatorPovScene(MenuScene):
    
    def __init__(self):
        super().__init__("HostInterface")

        (windowWidth, windowHeight) = pygame.display.get_window_size()
        HOST = socket.gethostname()
        PORT = 5000

        self.menu.buttonsList=[ButtonActor("Host", lambda: Thread(target=Server().start, args=(HOST, PORT)).start()),
                               ButtonActor("Back", self.switchMainMenuScene)
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


    def switchMainMenuScene(self):
        from .Menus.MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()