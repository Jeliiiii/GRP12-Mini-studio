from pseudoWindow import *
from random import randint

class SimPart:
    def __init__(self, surface, x, y, size, color):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.surface = surface
        self.gameValue = []
        self.clickedOn = [0, 0]
    
    def draw(self, color):
        pygame.draw.rect(self.surface, color, self.rect)


class Simon(PseudoWindow):
    def __init__(self, coord=(0, 0), dim=(1, 1), closeCondition=0, color=(128, 128, 128, 1), gridSize=4):
        self.size = 50 #ask Baptiste
        PseudoWindow.__init__(self, coord, dim, closeCondition, color)
        self.squares = []
        self.replayCountDown = -1
        for i in range(gridSize):
            buffer = []
            for j in range(gridSize):
                buffer.append(SimPart(self.Content,
                                    i * self.size,
                                    j * self.size, 
                                    self.size,
                                    (i*20 + 50* j, i*20 + 50* j, i*20 + 50* j)
                                    ))
            self.squares.append(buffer)
        self.play(5)



    def show(self):
        pygame.draw.rect(spyScreen, self.color, self.Content_Rect, self.borderSize)
        pygame.draw.rect(spyScreen, self.color, self.Band_Rect)
        spyScreen.blit(self.Content, (self.coord[0] + self.borderSize, self.coord[1] + self.menuSize))

        pygame.draw.line(spyScreen, white, (self.dotRight, self.dotUp), (self.dotLeft, self.dotDown), 3)
        pygame.draw.line(spyScreen, white, (self.dotRight, self.dotDown), (self.dotLeft, self.dotUp), 3)
        
        for row in self.squares:
            for square in row:
                if int(self.establishing/60) in square.gameValue and self.establishing!= -1 :
                    square.draw((252, 3, 198))
                elif self.establishing == -1 and square.clickedOn[0] != 0:
                    if square.clickedOn[1] == 1 :
                        square.draw((50, 125, 168))
                    else :
                        square.draw((135, 24, 37))
                    square.clickedOn[0] -= 1
                    if square.clickedOn[0] == 0 :
                        square.clickedOn[1] = 0
                else :
                    square.draw(square.color)
        if self.establishing > -1:
            self.establishing -= 1
        if self.replayCountDown == -1:
            pass
        elif self.replayCountDown == 0 :
            self.replayCountDown -=1
            self.replay()
        else :
            self.replayCountDown -=1

    
    def play(self, difficultie):
        #on défini ou vide les variables de jeu
        self.playingOrder = difficultie -1
        self.establishing = difficultie * 60
        self.lastDifficultie = difficultie

        #on met le jeu en place
        for i in range(difficultie):
            rdm = (randint(0, len(self.squares)-1), randint(0, len(self.squares)-1))
            self.squares[rdm[0]][rdm[1]].gameValue.append(i) #on assigne un nombre à un carré random
        
    
    def replay(self):
        #j'ai mis cette fonction-ci par soucis de clareté, elle n'est pas nécéssaire
        self.replayCountDown
        for row in self.squares :
            for square in row:
                square.gameValue = []
        self.play(self.lastDifficultie)


    def clicked(self, coords):
        if self.Cross.collidepoint(coords):
            print("Left Click on CROSS")
            del self
            print("element removed from list")
        
        for row in self.squares :
            for square in row:
                if square.rect.collidepoint(coords):
                    if self.playingOrder in square.gameValue :
                        self.playingOrder -= 1
                        square.clickedOn = [20, 1]
                        if self.playingOrder == -1:
                            print("congrats")
                            PseudoWindow.loadedPseudoWindows.remove(self)
                    else :
                        square.clickedOn = [20, 0]
                        self.replayCountDown = 20