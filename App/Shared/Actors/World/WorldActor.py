import pygame


#TILE_SIZE = window.hauteur // ROWS
TILE_TYPES = 21
level = 0

class WorldActor:

    def __init__(self):
        self.scrollSpeed = 1
        self.loadedChunks = []
        self.activeChunks = []
        self.archivedChunks = []




if __name__ == "__main__":
    world = WorldActor()
    world.loadLevelFromCSV(0)