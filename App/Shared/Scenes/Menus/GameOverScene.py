from Shared.Actors.UI.ButtonActor import ButtonActor
from .MenuScene import MenuScene
import pygame
import os


class GameOverScene(MenuScene):
    def __init__(self):
        super().__init__("GameOver")

        (windowWidth, windowHeight) = pygame.display.get_window_size()

        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Backgrounds/GameOver.png"))
        self.backGround = pygame.transform.scale(img, (windowWidth, windowHeight))

        self.menu.buttonsList=[ButtonActor("Back to menu", self.switchMainMenuScene)]

        buttonsAmount = self.menu.getButtonsAmount()
        buttonsFontSize = windowHeight/16
        buttonsFont = pygame.freetype.Font("App\Shared\Assets\Graphics\Fonts\Square.ttf")

        self.menu.buttonsList[0].renderDefaultSprite(buttonsFont, buttonsFontSize, "white")
        self.menu.buttonsList[0].moveSpriteOnCenter(windowWidth/2, windowHeight/2)


    def updateScene(self, inputs, dt):
        self.menu.handleMouse(inputs["MOUSE_POS"][0], inputs["MOUSE_POS"][1], inputs["MOUSE_BUTTONS"])


    def drawScene(self, window):
        window.blit()
        self.menu.draw(window)


    def switchMainMenuScene(self):
        from .MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()
