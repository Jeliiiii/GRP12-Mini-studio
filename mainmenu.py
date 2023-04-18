import pygame
from window import *

rect_casejeu_width = 400
rect_casejeu_height = 50

rect_caseoption_width = 400
rect_cas
_height = 50
class MainMenu :
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.font = pygame.font.Font(None,50)
        self.play_button = pygame.Rect(200,200,100,100)
        