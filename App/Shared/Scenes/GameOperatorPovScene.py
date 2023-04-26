from Shared.Actors.Characters.AgentCharacterActor import AgentCharacterActor
from Shared.Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from .Scene import Scene
from ..Actors.World.WorldActor import WorldActor
from Shared.Actors.operatorWindows.PseudoWindow import * # impoirte pseudoWindow et setup
from Shared.Actors.operatorWindows.Carthage import Carthage
from Shared.Actors.operatorWindows.Simon import Simon
# from Shared.Actors.operatorWindows.Tools import Tools
from Shared.Actors.operatorWindows.SpyWindow import *
from Shared.Actors.operatorWindows.ToolWindow import *

class GameOperatorPovScene(Scene):
    
    def __init__(self):
        # random.seed(time.time())
        super().__init__()
        self.world = WorldActor(1)
        self.timer = random.randint(20000, 30000)



        # Creates special windows for spying on the Actor's view, and it's control panel
        self.SpyScreen = SpyWindow()
        self.ToolBelt = ToolWindow()

        # PseudoWindow((300, 300), (90, 90), color = (45, 177, 88, 1))
        # PseudoWindow((105, 105), (90, 90), color = (45, 177, 88, 1))

        Simon((300, 100), (300, 300))
        Carthage((100, 600), (300, 300))


    def updateScene(self, inputs, dt):
        
        windowsUpdated = []

        # Updates windows with priority of 0. Hard coded specifically for the SpyScreen and ToolBelt
        self.SpyScreen.onTick(inputs, dt)
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

        # Draws special windows of priority 0. Hard coded specifically for the SpyScreen and ToolBelt
        self.SpyScreen.draw()
        self.ToolBelt.draw()

        # Draws every windows that are loaded, by order if priority
        if PseudoWindow.loadedPseudoWindows:
            for prio in reversed(range(1, len(PseudoWindow.loadedPseudoWindows) + 1)):
                for win in PseudoWindow.loadedPseudoWindows:
                    if win.priority == prio:
                        win.draw()


    def switchMainMenuScene(self):
        from .Menus.MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()