from ..DefaultPawnActor import DefaultPawnActor
from random import randint

class ArsenalUpdater(DefaultPawnActor):
    def __init__(self, agent, arsenal, x, y, surface, velX=0, velY=0):
        super().__init__(x, y, surface, velX=velX, velY=velY)
        self.agent = agent
        self.arsenal = arsenal
        self.damage = 0

    def onTick(self, dt):
        super().onTick(dt)

    def onHit(self, bulletList):
        keys = list(self.arsenal.keys())
        print(type(keys))
        self.agent.weapon = self.arsenal[f"{keys[randint(0, len(keys)-1)]}"]
        bulletList.remove(self)