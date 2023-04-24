class InitLevelState:

    def __init__(self):
        pass


    def InitLevelClientThreadMain(self):
        pass

    def InitLevelServThreadMain(self, threadLength):
        if threadLength > 2:
            self.lastGameState.startGame = 1