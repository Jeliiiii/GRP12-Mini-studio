from character import *
   


class ennemy(Rectangle):
    def __init__(self, screen, x, y, width, height, speed):
        Rectangle.__init__(self, screen, x, y, width, height, speed)

    def go_on(self):
        self.move_left()
        self.draw((0, 0, 0))


