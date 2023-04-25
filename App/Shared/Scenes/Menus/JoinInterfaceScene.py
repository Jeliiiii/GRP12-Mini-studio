from Shared.Networking.ClientSocket import ClientSocket
import socket
from Shared.Actors.UI.ButtonActor import ButtonActor
from .MenuScene import MenuScene
import pygame
from Shared.Actors.UI.FormsActors.TypingFieldActor import TypingFieldActor

class JoinInterfaceScene(MenuScene):
    
    def __init__(self):
        super().__init__("HostInterface")

        (windowWidth, windowHeight) = pygame.display.get_window_size()
        HOST = socket.gethostname()
        PORT = 5000

        self.menu.buttonsList=[ButtonActor("Join", self.connectToServer),
                               ButtonActor("Back", self.switchMainMenuScene)
                                ]
        
        
        
        buttonsAmount = self.menu.getButtonsAmount()
        buttonsFontSize = windowHeight/16
        buttonsFont = pygame.freetype.Font("App\Shared\Assets\Graphics\Fonts\ethnocentric rg.ttf")
        key=0
        for button in self.menu.buttonsList:
            button.renderDefaultSprite(buttonsFont, buttonsFontSize, "white")
            button.moveSpriteOnCenter(windowWidth/2, (key+2)*windowHeight/(buttonsAmount*2))
            key+=1

        
        self.ipTypingField = TypingFieldActor(windowWidth/2, windowHeight/3+200, buttonsFont, buttonsFontSize, "white", active=True)
        self.portTypingField = TypingFieldActor(windowWidth/2, windowHeight/3, buttonsFont, buttonsFontSize, "white", maxLength=5, active=False, value="4437")
        self.HUD = [self.menu, self.ipTypingField, self.portTypingField]


    def updateScene(self, inputs, dt):
        self.menu.handleMouse(inputs["MOUSE_POS"][0], inputs["MOUSE_POS"][1], inputs["MOUSE_BUTTONS"])
        self.HUD[1].onTick(inputs, dt)

    def drawScene(self, window):
        window.fill( "#111126" )
        for actor in self.HUD:
            actor.draw(window)


    def switchMainMenuScene(self):
        from .MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()

    def connectToServer(self):
        ClientSocket().joinServer( self.HUD[1].value, self.HUD[2].value)