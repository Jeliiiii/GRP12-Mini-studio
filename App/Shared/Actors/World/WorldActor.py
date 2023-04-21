import pygame
import csv
import os






#TILE_SIZE = window.hauteur // ROWS
TILE_TYPES = 21
level = 0

class WorldActor:

    def __init__(self):
         #Height in tiles unit
         #width in tiles unit - 16:9 sceen ratio round to the upper value
        pass
        

    def loadLevelFromCSV(self, levelId):
        #créer un liste de tile vide
        # worldData = []
        # for row in range(self.TROWS):
        #     r = [-1] * self.TCOLS_PER_CHUNK
        #     worldData.append(r)
        #charger des données de niveau et créer un monde (pour lire le dossier csv)
        csv_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Assets/Levels/level0_data.csv"))
        print(csv_file_path)
        with open(csv_file_path, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")

            #initializing tHeight/tWidth/tChunkWidth
            for i, row in enumerate(reader): 
                pass
            self.tHeight = i+1
            self.tWidth = len(row)
            self.tChunkWidth = round(self.tHeight * 16 / 9)
            self.worldChunkData = []
            """As a later improvement, we should turn this as a tool to create a header for each level_data.csv, 
            such as the first line of the file giving the total tWidth and tHeight of the level."""

            for y, row in enumerate(reader):
                for x, tile in enumerate(row):
                    if y==0 and x % self.tChunkWidth == 0:
                        self.worldChunkData.append([])
                    self.worldChunkData[63%x][y][x%self.tChunkWidth] = int(tile)
            print(self.worldChunkData)
            self.tLevelWidth = x

if __name__ == "__main__":
    world = WorldActor()
    world.loadLevelFromCSV(0)