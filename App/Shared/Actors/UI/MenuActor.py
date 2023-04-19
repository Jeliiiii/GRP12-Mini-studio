from Shared.Actors.UI.ButtonActor import ButtonActor

class MenuActor:

    def __init__(self, title):
        self.buttonsList = []
        self.title = title

    def getButtonsAmount(self):
        return len(self.buttonsList)

    def addButton(self, text, action):
        newButton = ButtonActor(text, action)

    def addRect(self, x, y, width, height):
        self.buttonsList.append(ButtonActor(x,y,width, height))

    def addButtons(self, *buttons: ButtonActor):
        for button in buttons:
            self.addButton(button)

    def setButtonsInListPositions(self):
        for button in self.buttonsList:
            button.move

    def handleMouse(self, x, y, mouseInputs):
        clicking = (1 in mouseInputs)
        for button in self.buttonsList:
            button.handleMouse(x, y, clicking)
        if clicking:
            mouseInputs.remove(1)


    def draw(self, window):
        for button in self.buttonsList:
            button.draw(window)