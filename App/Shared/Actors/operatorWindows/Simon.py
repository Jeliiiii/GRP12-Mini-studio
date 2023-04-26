from Shared.Actors.operatorWindows.PseudoWindow import *
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
    def __init__(self, coord=(0, 0), dim=(1, 1), gridSize=4, difficulty=5):
        self.size = 50 #ask Baptiste | ma réponse : poirte
        PseudoWindow.__init__(self, coord, (gridSize * self.size +10, gridSize * self.size +25), closeCond = False)
        self.squares = []
        self.replayCountDown = -1
        for i in range(gridSize):
            buffer = []
            for j in range(gridSize):
                buffer.append(SimPart(self.surfContent,
                                    i * self.size,
                                    j * self.size, 
                                    self.size,
                                    (i*20 + 50* j, i*20 + 50* j, i*20 + 50* j)
                                    ))
            self.squares.append(buffer)
        self.play(difficulty)


    def draw(self):
        super().draw()
        
        for row in self.squares:
            for square in row:
                if int(self.establishing/17) in square.gameValue and self.establishing!= -1 :
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

    
    def play(self, difficulty):
        #on défini ou vide les variables de jeu
        self.playingOrder = difficulty -1
        self.establishing = difficulty * 17
        self.lastDifficulty = difficulty
        self.clickCooldown = 5

        #on met le jeu en place
        for i in range(difficulty):
            rdm = (randint(0, len(self.squares)-1), randint(0, len(self.squares)-1))
            self.squares[rdm[0]][rdm[1]].gameValue.append(i) #on assigne un nombre à un carré random
        
    
    def replay(self):
        #j'ai mis cette fonction-ci par soucis de clareté, elle n'est pas nécéssaire
        self.replayCountDown
        for row in self.squares :
            for square in row:
                square.gameValue = []
        self.play(self.lastDifficulty)


    def onTick(self, inputs, dt):

        # Updates the cooldown every frame
        if self.clickCooldown != 0:
            self.clickCooldown -= 1
        
        mouse_pos = (inputs["MOUSE_POS"][0], inputs["MOUSE_POS"][1])

        # Test if the spy has cicked on a square with a valid cooldown
        if 1 in inputs["MOUSE_BUTTONS"] and self.clickCooldown == 0 and self.establishing == -1 and self.rectWhole.collidepoint(mouse_pos):
            
            # Calling super after passing the click condition, since PseudoWindow.onTick() removes the click upon detection, to compute it obly once
            super().onTick(inputs, dt)
            print("Got a click in Simon !")

            mouse_pos = (mouse_pos[0] - self.coord[0] - 5, mouse_pos[1] - self.coord[1] - 20)

            # Test each SimPart for the click
            for row in self.squares :
                for square in row:

                    # Test for colission with cursor
                    if square.rect.collidepoint(mouse_pos):
                        if self.playingOrder in square.gameValue:
                            self.playingOrder -= 1
                            square.clickedOn = [20, 1]
                            if self.playingOrder == -1:
                                PseudoWindow.loadedPseudoWindows.remove(self)
                        else :
                            square.clickedOn = [20, 0]
                            self.replayCountDown = 20

            self.clickCooldown = 10