import pygame
from Utilities.charactersReferencesList import charactersReferencesList
from PseudoWindow import *


class TypingFieldActor:

    def __init__(self, x, y, font, fontSize, fontColor, value="", placeHolder="", active = True, maxLength=16, displayedWidth=9):
        self.font = font
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.value = value
        self.placeHolder = placeHolder
        self.maxLength = maxLength
        self.active = active
        self.hitBoxWidth = 3*self.fontSize/4*displayedWidth
        hitBoxHeight = self.fontSize+self.fontSize/4
        self.hitBox = pygame.Rect(x, y, self.hitBoxWidth, self.fontSize+self.fontSize/4)

        charRefs = charactersReferencesList()
        self.allowedChar = charRefs.strNumbers + charRefs.smallCharAlphabet + ["."]
        self.textSprite = self.font.render(self.value, fgcolor=self.fontColor, size=self.fontSize) # tuple : [0] = pygame.Surface, [1] = pygame.Rect
        if not self.active:
            self.textSprite[0].set_alpha(200)
        
        self.textPos = (x+self.fontSize/4, y+self.fontSize/4)
        (self.textSprite[1].x,self.textSprite[1].y) = (self.textPos[0], self.textPos[1])


    def isHovering(self, x, y):
        return self.hitBox.collidepoint(x, y)

    def onTick(self, inputs, dt):
        if self.active:
            '''if (not self.isHovering(inputs["MOUSE_POS"][0],inputs["MOUSE_POS"][1])) and (1 in inputs["MOUSE_BUTTONS"]):
                self.textSprite[0].set_alpha(200)
                self.active = False
                return'''
            print(inputs)
            if inputs["ACTIVE_KEYS"]:
                for key in inputs["ACTIVE_KEYS"]:
                    if key == pygame.K_BACKSPACE:
                        self.value = self.value[:-1]
                        inputs["ACTIVE_KEYS"].remove(pygame.K_BACKSPACE)
                    elif len(self.value) != self.maxLength:
                        if key == pygame.K_LSHIFT and pygame.K_SEMICOLON in inputs["ACTIVE_KEYS"]:
                            self.value += "."
                            inputs["ACTIVE_KEYS"].remove(pygame.K_SEMICOLON)
                        elif pygame.key.name(key) in self.allowedChar:
                            self.value += (pygame.key.name(key))
                            inputs["ACTIVE_KEYS"].remove(key)
                            print(self.value)
                self.textSprite = self.font.render(self.value, fgcolor=(self.fontColor), size=self.fontSize)
                (self.textSprite[1].x,self.textSprite[1].y) = (self.textPos[0], self.textPos[1])
        '''elif self.isHovering(inputs["MOUSE_POS"][0],inputs["MOUSE_POS"][1]) and (1 in inputs["MOUSE_BUTTONS"]):
            self.textSprite[0].set_alpha(255)
            self.active = True
            inputs["MOUSE_BUTTONS"].remove(1)
            print(self.active)'''

    def draw(self, window):
        pygame.draw.rect(window, "red", self.hitBox)
        window.blit(self.textSprite[0], self.textSprite[1])


class Carthage(PseudoWindow):
    def __init__(self, coord=(0, 0), dim=(1, 1), closeCondition=0, color=(128, 128, 128, 1), password = "carthage"):
        PseudoWindow.__init__(self, coord, dim, closeCondition, color)
        self.typeField = TypingFieldActor(10, 10, testFont, 40, (3, 53, 252), maxLength=8, active=True)
        self.password = password

    def show(self):
        pygame.draw.rect(spyScreen, self.color, self.Content_Rect, self.borderSize)
        pygame.draw.rect(spyScreen, self.color, self.Band_Rect)
        spyScreen.blit(self.Content, (self.coord[0] + self.borderSize, self.coord[1] + self.menuSize))

        pygame.draw.line(spyScreen, white, (self.dotRight, self.dotUp), (self.dotLeft, self.dotDown), 3)
        pygame.draw.line(spyScreen, white, (self.dotRight, self.dotDown), (self.dotLeft, self.dotUp), 3)

        self.typeField.draw(self.Content)
        if self.typeField.value == self.password :
            print("acces au 5e territoire")
            PseudoWindow.loadedPseudoWindows.remove(self)