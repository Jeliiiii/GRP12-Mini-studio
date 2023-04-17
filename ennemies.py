from character import *
   


class ennemy(Character):
    def __init__(self, screen, x, y, width, height, speed):
        Character.__init__(self, screen, x, y, width, height, speed)

    def go_on(self):
        self.move_left()
        self.draw((255, 255, 255))