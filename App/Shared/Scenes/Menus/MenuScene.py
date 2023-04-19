from Shared.Actors.UI.MenuActor import MenuActor
from Shared.Scenes.Scene import Scene


class MenuScene(Scene):
    
    def __init__(self, title=''):
        super().__init__()
        self.menu = MenuActor(title)