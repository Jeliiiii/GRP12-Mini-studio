


class GameLoopState:

    def __init__(self, clientsThreads = [], data=(1,(0,),(1,))):
        self.nextGameState = None
        self.clientsThreads = clientsThreads
        self.isGameRunning = data[0]

        self.globalData = (self.isGameRunning,) 
        #first item is the role id : 0=agent, 1=operator
        self.agentData = data[1]
        self.operatorData = data[2]




    def stateUpdate(self, event):
        if(event[0] == 0):
            self.operatorData = event[1]