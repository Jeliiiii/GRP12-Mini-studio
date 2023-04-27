from threading import Thread
from Shared.Networking.Server import Server
import socket
from ...Networking.ClientSocket import ClientSocket
from Shared.Actors.UI.ButtonActor import ButtonActor
from .MenuScene import MenuScene
from ..Multiplayer.WaitingScreenMPScene import WaitingScreenMPScene
import pygame
import time
from Shared.Actors.UI.FormsActors.TypingFieldActor import TypingFieldActor


class HostInterfaceScene(MenuScene):
    
    def __init__(self):
        super().__init__("HostInterface")

        (windowWidth, windowHeight) = pygame.display.get_window_size()
        HOST = socket.gethostname()
        PORT = 5000

        self.menu.buttonsList=[ButtonActor("Host", lambda: self.hostAndJoinServer()),
                               ButtonActor("Back", self.switchMainMenuScene)
                                ]
        
        
        buttonsAmount = self.menu.getButtonsAmount()
        buttonsFontSize = windowHeight/16
        buttonsFont = pygame.freetype.Font("App\Shared\Assets\Graphics\Fonts\Square.ttf")
        key=1
        for button in self.menu.buttonsList:
            
            button.renderDefaultSprite(buttonsFont, buttonsFontSize, "white")
            button.moveSpriteOnCenter(windowWidth/2, (key*4)*windowHeight/16)
            key+=2

        self.portTypingField = TypingFieldActor(windowWidth/2, windowHeight/3+200, buttonsFont, buttonsFontSize, "white", active=True)
        self.HUD = [self.menu, self.portTypingField]

        self.fieldLabel = buttonsFont.render("IP Address :", fgcolor = "white", size=buttonsFontSize)
        self.fieldLabel[1].x = windowWidth/2 - 250
        self.fieldLabel[1].y = windowHeight/2 - 40

    def updateScene(self, inputs, dt):
        self.menu.handleMouse(inputs["MOUSE_POS"][0], inputs["MOUSE_POS"][1], inputs["MOUSE_BUTTONS"])
        self.HUD[1].onTick(inputs, dt)

    def drawScene(self, window):
        window.fill( "#111126" )
        window.blit(self.fieldLabel[0], self.fieldLabel[1])
        for actor in self.HUD:
            actor.draw(window)




    def hostAndJoinServer(self):
        Thread(target=Server().start, args=(socket.gethostname(), self.HUD[1].value)).start()
        time.sleep(2)
        self.clientSocket = ClientSocket()
        self.clientSocket.joinServer(socket.gethostname(), self.HUD[1].value)
        self.sceneSwitcher(WaitingScreenMPScene(clientSocket = self.clientSocket))



    def switchMainMenuScene(self):
        from .MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()