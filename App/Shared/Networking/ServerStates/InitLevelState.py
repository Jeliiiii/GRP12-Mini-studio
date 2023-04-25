class InitLevelState:

    def __init__(self):
        self.nextGameState = None
        self.startGame = 0

    def serverMain(self, event):
        if self.clientsThreads > 2:
            self.startGame = 1