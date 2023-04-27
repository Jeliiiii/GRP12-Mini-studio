from Shared.Actors.operatorWindows.PseudoWindow import *
from Shared.Actors.World.WorldActor import *

# Used to not make default __init__ values a kilometer long
screenSize = (pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1])

class SpyWindow(PseudoWindow):


    def __init__(self, coord=(screenSize[0] * 0.1, screenSize[1] * 0.07), dim=(screenSize[0] * 0.8, screenSize[0] * 0.8 * (9/24)), color=(128, 128, 128, 1), closeCond = False):
        super().__init__(coord, dim, color, closeCond)
        self.priority = 0
        self.worldSpectated = WorldActor(0, winSize=self.dim)
        PseudoWindow.loadedPseudoWindows.remove(self)

    def draw(self):
        super().draw()
        temp = pygame.Surface(screenSize)
        self.worldSpectated.draw(temp)
        temp = pygame.transform.scale(temp, (self.surfContent.get_width(), screenSize[0] * 0.8 * (9/16)))
        # self.surfContent.blit(temp, (0, 0))
        spyScreen.blit(temp, (0, 0))

    def onTick(self, inputs, dt):
        self.worldSpectated.onTick(inputs, dt)