import pygame

class Rectangle:
    def __init__(self, screen, x, y, width, height, speed):
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move_up(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.top < 0:
            self.rect.top = 0

    def move_down(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > self.screen.get_height():
            self.rect.bottom = self.screen.get_height()

    def move_left(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.left < 0:
            self.rect.left = 0

    def move_right(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.right > self.screen.get_width():
            self.rect.right = self.screen.get_width()

    def draw(self, color):
        pygame.draw.rect(self.screen, color, self.rect)

    def getCoordinates(self):
        return [self.rect.x, self.rect.y]



class Bullet(Rectangle):
    def __init__(self, screen, x, y, width, height, speed):
        Rectangle.__init__(self, screen, x, y, width, height, speed)
            
    def go_on(self):
        self.move_right()
        self.draw((255, 255, 255))
