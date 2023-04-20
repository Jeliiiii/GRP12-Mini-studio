import pygame

class ButtonActor:

    def __init__(self, text, callback):
        self.text = text 
        self.onClick = callback       
        self.displaySize = "normal"

    def renderDefaultSprite(self, font, fontSize, fontColor):
        """
        Creates a sprite that can be drawn. Assigns a tuple (pygame.Surface, pygame.Rect) to self.sprite.
        """
        self.font = font
        self.fontColor = fontColor
        self.fontSize = fontSize
        self.sprite = font.render(self.text, fgcolor=self.fontColor, size=self.fontSize)

    def moveSpriteOnCenter(self, x, y):
        """
        Moves the sprite to given x,y coordinates - coordinates represent the center of the sprite.
        """
        self.sprite[1].centerx = x
        self.sprite[1].centery = y

    def isHovering(self, x, y):
        return self.sprite[1].collidepoint(x, y)

    def handleMouse(self, x, y, mouseInputs):
        if self.isHovering(x, y):
            if self.displaySize != "big":
                self.displaySize = "big"
            clicking = (1 in mouseInputs)
            if clicking:
                self.onClick()
                if clicking:
                    mouseInputs.remove(1)
        elif self.displaySize != "normal":
            self.displaySize = "normal"

    def draw(self, window):
        window.blit(self.sprite[0], self.sprite[1])


    # def generateSprite(self, text, font, fontSize):

    # def moveButton(self, x, y):
    #     self.sprite[1].center(x,y)
    #     self.hitbox.center(x,y)
    
    # def 

    # def setButtonHitBox(self, windowWidth, heightPosition, font, widthPosition="CENTERED"):
    #     """
    #     Parameters:
    #     heightPosition is the position of the middle of the button on the screen
    #     font must have a size method that takes a string as argument and returns a tuple with the width/height needed for the text.
    #     """
    #     (textWidth, textHeight) = font.size(self.text)
    #     widthPadding = textWidth/3
    #     heightPadding = textHeight/2
    #     buttonWidth = 2*widthPadding + textWidth
    #     buttonHeight = 2*heightPadding + textHeight

    #     if widthPosition == "CENTERED":
    #         x = windowWidth/2-buttonWidth/2
    #         y = heightPosition-buttonHeight/2

    # def setButtonPos

    # def isHovered(self, x, y):
    #     return self.hitbox.isCoordIn(x, y)