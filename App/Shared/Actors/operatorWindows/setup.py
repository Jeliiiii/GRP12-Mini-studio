import pygame
import random
random.seed()
import time
import os

# Initialization of diverse pygame functionnalities

pygame.init()
pygame.font.init()


# Setting up screen size

userScreenInfo = pygame.display.Info()
spyScreen_dimension = (userScreenInfo.current_w, userScreenInfo.current_h)
spyScreen = pygame.display.set_mode(spyScreen_dimension, pygame.NOFRAME)
pygame.display.set_caption("Birds Of Chaos")


# Some color declaration

black = (0, 0, 0)
white = (255, 255, 255)


# Font delcaration

defaultFont = pygame.font.Font(size = 50)
testFont = pygame.freetype.Font("App/Shared/Assets/Graphics/Fonts/Square.ttf")


# Setting up 

clock = pygame.time.Clock()
FPS = 60