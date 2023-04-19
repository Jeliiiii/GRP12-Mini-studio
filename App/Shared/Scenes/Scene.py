class Scene:

    def __init__(self):
        self.nextScene = None

    def sceneSwitcher(self, nextScene):
        self.nextScene = nextScene

    def quit(self):
        self.nextScene = "QUIT_CLIENT"