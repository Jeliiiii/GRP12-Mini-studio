import csv


def mapWorldCSVData(self, worldCSVData):
    world = WorldActor()
    chunkList = []
    for chunkCSVData in worldCSVData:
        chunk = mapChunkCSVData(chunkCSVData)
        chunkList.append(chunk)
    world.chunkList = chunkList

def mapChunkCSVData(self, chunkCSVData):
    chunk = ChunkActor()
    ennemiesList = []
    obstaclesList = []
    for y, row in chunkCSVData:
        for x, tile in row:
            if tile != -1: # -1 = empty tile
                if tile > -1 and tile < 9:
                    obstacle = ObstacleActor(x, y, tile)
                elif tile >= 9 and tile <= 10:
                    pass #murs destructibles/ créables par l'opérateur
                elif tile == 11 and tile <= 14:
                    pass # 11 : shield faibles -> Destructibles
                elif tile == 12:
                    player = Character(window.screen,x*TILE_SIZE, y*TILE_SIZE, 40, 40, 15) #12 : joueur
                elif tile == 13 :
                    pass #13 : shield fort -> indestructible
                elif tile == 14 :
                    pass #14 : non utilisé
                elif tile == 15 : 
                    buffer.append(Basic(window, x*TILE_SIZE, y*TILE_SIZE, 5))
                    """ca fonctionne mais il y a beaucoup trop d'operations a chaque frame : ca fait lag une dinguerie"""
                    #enemy = Character(window.screen, x*TILE_SIZE, y*TILE_SIZE, 50, 100, 5) #15 : ennemi horizontal
                    pass
                elif tile == 16 : 
                    enemy = Character(window.screen, x*TILE_SIZE, y*TILE_SIZE, 50, 100, 5) #16 : ennemi vertical
                elif tile == 17 :
                    pass # 17 : mur électrifié
                elif tile >= 18 and tile <= 19 :
                    pass # inutilisé
                elif tile == 20 :
                    pass #Création de fin de niveau

                
        chunk = mapChunkCSVData(chunkCSVData)
        chunkList.append(chunk)
    world.chunkList = chunkList


def loadWorldFromCSV(self, levelId):
    import os
    csv_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../Assets/Levels/level0_data.csv"))
    with open(csv_file_path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        tHeight = 32
        tWidth = 401
        tChunkWidth = int((tHeight * 16) / 9) + ((tHeight * 16) % 9 > 0)
        """As a later improvement, we should turn this as a tool to create a header for each level_data.csv, 
        such as the first line of the file giving the total tWidth and tHeight of the level."""
        chunkData = [[None for _ in range (tChunkWidth)] for _ in range (self.tHeight)]
        worldChunkData = [chunkData for _ in range (int(tWidth/tChunkWidth) + (tWidth % tChunkWidth > 0))] # a list of empty lists representing each chunks
        
        for y, row in enumerate(reader):
            chunkId = -1
            for x, tile in enumerate(row):
                if(x%tChunkWidth == 0):
                    chunkId +=1
                
                worldChunkData[chunkId][y][x%tChunkWidth] = int(tile)
        """Generates line by line, increases the chunkId when x is a multiple of the chunkWidth 
        (meaning, it's the beginning of a new chunk)"""
    self.tHeight = tHeight
    self.tWidth = tWidth
    self.tChunkWidth = tChunkWidth