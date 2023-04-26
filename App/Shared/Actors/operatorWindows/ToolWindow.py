from Shared.Actors.operatorWindows.PseudoWindow import *


class ToolWindow(PseudoWindow):

    # Used to not make default __init__ values a kilometer long
    screenSize = (pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1])

    def __init__(self, coord=(screenSize[0] * 0.2, screenSize[1] * 0.77), dim=(screenSize[0] * 0.6, screenSize[1] * 0.15), color=(128, 128, 128, 1), closeCond = False):
        super().__init__(coord, dim, color, closeCond)
        self.priority = 0
        PseudoWindow.loadedPseudoWindows.remove(self)

    def draw(self):
        super().draw()

    def onTick(self, inputs, dt):
        pass