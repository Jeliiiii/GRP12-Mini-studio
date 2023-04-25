

class DefaultPawnActor:

    def __init__(self, x, y, surface, velX=0, velY=0):

        self.sprite = (surface, surface.get_rect(topleft=(x, y)))
        self.hitBox = self.sprite[1]

        self.velocity = [velX, velY]
        
    def isInWindow(self, windowSize):
        if self.hitBox.x > 0 and self.hitBox.x < windowSize[0] and self.hitBox.y > 0 and self.hitBox.y < windowSize[1]:
            return True

    def shot(self, damage):
        self.health -= damage
        return self.health

    def move(self, dt):
        self.hitBox.x += self.velocity[0] * dt * 10
        self.hitBox.y += self.velocity[1] * dt * 10
        (self.sprite[1].x, self.sprite[1].y) = (self.hitBox.x, self.hitBox.y)

    def onTick(self, dt):
        self.move(dt)

    def draw(self, window):
        window.blit(self.sprite[0], self.sprite[1])

if __name__ == "__main__":
    import pygame