from Shared.Scenes.Menus.MenuScene import MenuScene

class JoinInterfaceScene(MenuScene):

    def __init__(self):
        pass




    def switchMainMenuScene(self):
        from .MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()