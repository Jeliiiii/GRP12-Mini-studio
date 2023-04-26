from ...Actors.operatorWindows.setup import *
from time import sleep
# Creating "window" class, an UI element of the spy's screen

class PseudoWindow:
    # Stores every "window" to make them interactive in main loop
    loadedPseudoWindows = []

    def __init__(self, coord = (0, 0), dim = (330, 300), color = (128, 128, 128, 1), closeCond = True):
        # Saves the object caracteristics
        self.coord = coord
        self.dim = dim
        self.color = color
        self.borderSize = 5
        self.menuSize = 20
        self.closeCond = closeCond
        self.priority = 1

        
        """
        Creates the "window" components. surfComponent are here to blit images within them, while rectComponent are used as hitboxes
        """
        # Hitbox for the entire window
        self.rectWhole = pygame.Rect(self.coord, self.dim)

        # Hitbox of the menu, or band on the top
        self.rectMenu = pygame.Rect(self.coord, (self.dim[0], self.menuSize))

        # Hitbox and Surface for the inside of the window
        self.surfContent = pygame.Surface((self.dim[0] - 2*self.borderSize, self.dim[1] - self.borderSize - self.menuSize)) # Inside of the window
        self.surfContent.fill(white)
        self.rectContent = self.surfContent.get_rect(topleft = (self.coord[0] + self.borderSize, self.coord[1] + self.menuSize))

        # Hitbox and surface for the cross to close the window
        self.surfCross = pygame.Surface((16, 16))
        self.rectCross = self.surfCross.get_rect(topright = (self.coord[0] + self.dim[0] - self.borderSize, self.coord[1] + (self.menuSize - self.surfCross.get_height()) // 2))

        # Adding the new instance to the list and updates priority of the other
        if PseudoWindow.loadedPseudoWindows:
            for instance in PseudoWindow.loadedPseudoWindows:
                instance.priority += 1
        PseudoWindow.loadedPseudoWindows.append(self)

    def __del__(self):
        # print("/!\\ Thank you for calling del ! Here is target priority : ", self.priority)
        if PseudoWindow.loadedPseudoWindows:
            for instance in PseudoWindow.loadedPseudoWindows:
                if instance.priority > self.priority:
                    instance.priority -= 1

    
    # Essentially makes selected windows on number 1 priority, and shift the other windows accrodingly
    def focusOn(self):
        # print("Thank you for calling focusOn() ! Here is target priority : ", self.priority)
        if PseudoWindow.loadedPseudoWindows and self.priority != 1:
            for instance in PseudoWindow.loadedPseudoWindows:
                if instance.priority != self.priority and instance.priority + 1 <= self.priority:
                    instance.priority += 1
        self.priority = 1

    def draw(self):

        # Draws the effective border to the window
        pygame.draw.rect(spyScreen, self.color, self.rectWhole)

        # Draw the top band to look like a menu
        pygame.draw.rect(spyScreen, self.color, self.rectMenu)

        """ TEMPORARY DISPLAYING """
        # self.surfContent.fill(white)
        # self.surfContent.blit(defaultFont.render(f"{self.priority}", True, (160, 50, 200)), (10, 10))

        # Blit the Content of the window
        spyScreen.blit(self.surfContent, (self.rectContent.x, self.rectContent.y))

        # Blit the Cross of the window
        if self.closeCond:
            self.surfCross.fill((255, 0, 0))
        else:
            self.surfCross.fill((70, 70, 70))
        spyScreen.blit(self.surfCross, self.rectCross.topleft)


    # Update a window. Called every frame and for every window
    def onTick(self, inputs, dt):
        mouse_pos = (inputs["MOUSE_POS"][0], inputs["MOUSE_POS"][1])

        # Test if the click append within the window region
        if 1 in inputs["MOUSE_BUTTONS"] and self.rectWhole.collidepoint(mouse_pos):
            inputs["MOUSE_BUTTONS"].remove(1)

            print("====> Click detected !")

            
            # Necessary loop to get the index of object within list of loaded objects
            for cur in range(len(PseudoWindow.loadedPseudoWindows)):

                # Filter to only act on targeted object via it's index
                if PseudoWindow.loadedPseudoWindows[cur] == self:

                    # print("====> Testing click on ", self.priority, ", ", self.__class__.__name__, " of index ", cur)

                    # Manages priorities
                    if self.rectWhole.collidepoint(mouse_pos):
                        # print("====> Rearraging priorities...")
                        for instance in PseudoWindow.loadedPseudoWindows:
                            if instance.priority != self.priority and instance.priority + 1 <= self.priority:
                                instance.priority += 1
                        self.priority = 1

                    # Another filter to make sure actions are tested on a single window every time
                    if self.priority == 1:

                        # Closes the window if the Cross region was clicked
                        if self.rectCross.collidepoint(mouse_pos) and self.closeCond:
                            for target in range(len(PseudoWindow.loadedPseudoWindows)):
                                print(len(PseudoWindow.loadedPseudoWindows) ,target)
                                if PseudoWindow.loadedPseudoWindows[target] == self:
                                    del PseudoWindow.loadedPseudoWindows[target]
                                    return

                    else:
                        # print("====> No cillision found...")
                        inputs["MOUSE_BUTTONS"].append(1)
        else:
            # print("====> Passing...")
            pass