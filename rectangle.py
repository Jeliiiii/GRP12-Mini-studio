import pygame

class Rectangle:
    def __init__(self, screen, x, y, width, height, speed):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move_up(self):
        self.rect.move_ip(0, -self.speed)
        

    def move_down(self):
        self.rect.move_ip(0, self.speed)
        

    def move_left(self):
        self.rect.move_ip(-self.speed, 0)
        

    def move_right(self):
        self.rect.move_ip(self.speed, 0)
        

    def draw(self, color):
        pygame.draw.rect(self.screen, color, self.rect)

    def getCoordinates(self):
        return [self.rect.x, self.rect.y]
