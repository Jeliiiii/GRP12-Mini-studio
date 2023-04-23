from setup import *
from time import sleep
# Creating "window" class, an UI element of the spy's screen

class PseudoWindow:
    # Stores every "window" to make them interactive in main loop
    loadedPseudoWindows = []

    def __init__(self, coord = (0, 0), dim = (1, 1), color = (128, 128, 128, 1), closeCond = True):
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
        if self.closeCond:
            self.surfCross.fill((255, 0, 0))
        else:
            self.surfCross.fill((70, 70, 70))
        self.rectCross = self.surfCross.get_rect(topright = (self.coord[0] + self.dim[0] - self.borderSize, self.coord[1] + (self.menuSize - self.surfCross.get_height()) // 2))

        # Adding the new instance to the list and updates priority of the other
        if PseudoWindow.loadedPseudoWindows:
            for instance in PseudoWindow.loadedPseudoWindows:
                instance.priority += 1
        PseudoWindow.loadedPseudoWindows.append(self)

    def __del__(self):
        print("/!\\ Thank you for calling del ! Here is target priority : ", self.priority)
        if PseudoWindow.loadedPseudoWindows:
            for instance in PseudoWindow.loadedPseudoWindows:
                if instance.priority > self.priority:
                    instance.priority -= 1

    # def __str__(self):
    #     return f"coordinates: {self.coord}, dimensions: {self.dim}, close method: {self.closeCond}, color: {self.color}, border size: {self.borderSize}, menu size: {self.menuSize}"

    # Essentially makes selected windows on number 1 priority, and shift the other windows accrodingly
    def focusOn(self):
        print("Thank you for calling focusOn() ! Here is target priority : ", self.priority)
        if PseudoWindow.loadedPseudoWindows and self.priority != 1:
            for instance in PseudoWindow.loadedPseudoWindows:
                if instance.priority != self.priority and instance.priority + 1 <= self.priority:
                    instance.priority += 1
        self.priority = 1

    def show(self):

        # Draws the effective border to the window
        pygame.draw.rect(spyScreen, self.color, self.rectWhole)

        # Draw the top band to look like a menu
        pygame.draw.rect(spyScreen, self.color, self.rectMenu)

        """ TEMPORARY DISPLAYING """
        self.surfContent.fill(white)
        self.surfContent.blit(defaultFont.render(f"{self.priority}", True, (160, 50, 200)), (10, 10))

        # Blit the Content of the window
        spyScreen.blit(self.surfContent, (self.rectContent.x, self.rectContent.y))

        # Blit the Cross of the window
        spyScreen.blit(self.surfCross, (self.rectCross.x, self.rectCross.y))


    def clicked(self, coords):
        print("coords : ", coords, ", self.rectCross : ", self.rectCross)
        if self.rectCross.collidepoint(coords):
            print("Left Click on CROSS")
            del self
            print("element removed from list")
