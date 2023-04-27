from Shared.Actors.Characters.AgentCharacterActor import AgentCharacterActor
from Shared.Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from .MPScene import MPScene
from ...Actors.World.WorldActor import WorldActor
from Shared.Actors.operatorWindows.PseudoWindow import * # impoirte pseudoWindow et setup
from Shared.Actors.operatorWindows.Carthage import Carthage
from Shared.Actors.operatorWindows.Simon import Simon
# from Shared.Actors.operatorWindows.Tools import Tools
from Shared.Actors.operatorWindows.SpyWindow import *
from Shared.Actors.operatorWindows.ToolWindow import *

screenSize = pygame.display.get_desktop_sizes()
screenSize = (screenSize[0][0], screenSize[0][1])

class GameOperatorPovMPScene(MPScene):
    
    def __init__(self):
        # random.seed(time.time())
        super().__init__()
        self.role = 1
        self.timer = random.randint(50, 70)



        # Creates special windows for spying on the Actor's view, and it's control panel
        self.SpyingScreen = SpyWindow()
        self.ToolBelt = ToolWindow()

        # PseudoWindow((300, 300), (90, 90), color = (45, 177, 88, 1))
        # PseudoWindow((105, 105), (90, 90), color = (45, 177, 88, 1))

        # Simon((300, 100), (300, 300))
        # Carthage((100, 600), (300, 300))


    def updateScene(self, inputs, dt):
        super().updateScene(inputs, dt)
        if not self.data:
            self.data = {"MOUSE_POS":[0,0], "MOUSE_BUTTONS":[], "ACTIVE_KEYS":[]}
        windowsUpdated = []

        self.timer -= 1

        if self.timer == 0:
            self.timer = randint(50, 70)
            if self.timer % 2:
                Carthage((randint(0, screenSize[0] - 300), randint(0, screenSize[1] - 300)))
            else:
                simonGrid = randint(3, 6)
                simonDiff = randint(3, 6)
                Simon((randint(0, screenSize[0] - simonGrid * 50), randint(0, screenSize[1] - simonGrid * 50)), simonGrid, simonDiff)

        # Updates windows with priority of 0. Hard coded specifically for the SpyingScreen and ToolBelt
        self.SpyingScreen.onTick(self.data, dt)
        self.ToolBelt.onTick(inputs, dt)

        # Calls onTick() on every windows exactly once (despite changing priorities around)
        if PseudoWindow.loadedPseudoWindows:

            # print("Updating list of len() ", len(PseudoWindow.loadedPseudoWindows))

            for win in PseudoWindow.loadedPseudoWindows:
                # print("  ~ ", win.priority, " of class ", win.__class__.__name__)
                pass

            for prio in range(1, len(PseudoWindow.loadedPseudoWindows) + 1):
                # print("-Looking for priority of ", prio)

                for win in PseudoWindow.loadedPseudoWindows:

                    if win not in windowsUpdated and win.priority == prio:
                        # print("   * Found match ! Calling onTick() on ", win.priority, " class ", win.__class__.__name__)
                        win.onTick(inputs, dt)
                        windowsUpdated.append(win)

        # print("\n\n\n\n")

        # Spawns in pop-ups



    def drawScene(self, window):
        window.fill( "#111126" )
        img = pygame.image.load(os.path.join(os.path.dirname(__file__),"../Assets/Graphics/Backgrounds/spy_background.jpg"))
        window.blit(img, (0, 0))

        # Draws special windows of priority 0. Hard coded specifically for the SpyingScreen and ToolBelt
        self.SpyingScreen.draw()
        self.ToolBelt.draw()

        # Draws every windows that are loaded, by order if priority
        if PseudoWindow.loadedPseudoWindows:
            for prio in reversed(range(1, len(PseudoWindow.loadedPseudoWindows) + 1)):
                for win in PseudoWindow.loadedPseudoWindows:
                    if win.priority == prio:
                        win.draw()


    def switchMainMenuScene(self):
        from ..Menus.MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()