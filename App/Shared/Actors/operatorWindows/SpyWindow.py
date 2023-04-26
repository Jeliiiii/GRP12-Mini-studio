from Shared.Actors.operatorWindows.PseudoWindow import *


class SpyWindow(PseudoWindow):

    # Used to not make default __init__ values a kilometer long
    screenSize = (pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1])

    def __init__(self, coord=(screenSize[0] * 0.1, screenSize[1] * 0.07), dim=(screenSize[0] * 0.8, screenSize[0] * 0.8 * (9/24)), color=(128, 128, 128, 1), closeCond = False):
        super().__init__(coord, dim, color, closeCond)
        self.priority = 0
        PseudoWindow.loadedPseudoWindows.remove(self)

    def draw(self):
        super().draw()

    def onTick(self, inputs, dt):
        pass