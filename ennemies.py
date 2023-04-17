import random
from character import *


class RectangleGenerator:
    def __init__(self, screen, speed, min_width, max_width, min_height, max_height, min_distance, max_distance):
        self.screen = screen
        self.speed = speed
        self.min_width = min_width
        self.max_width = max_width
        self.min_height = min_height
        self.max_height = max_height
        self.min_distance = min_distance
        self.max_distance = max_distance
        self.rectangles = []

    def generate(self):
        if len(self.rectangles) == 0 or self.screen.get_width() - self.rectangles[-1].getCoordinates()[0] > random.randint(self.min_distance, self.max_distance):
            width = random.randint(self.min_width, self.max_width)
            height = random.randint(self.min_height, self.max_height)
            x = 0 - width
            y = random.randint(0, self.screen.get_height() - height)
            self.rectangles.append(Rectangle(self.screen, x, y, width, height, self.speed))

    def move(self):
        for rectangle in self.rectangles:
            rectangle.move_right()
            if rectangle.getCoordinates()[0] >= self.screen.get_width():
                self.rectangles.remove(rectangle)

    def draw(self, color):
        for rectangle in self.rectangles:
            rectangle.draw(color)