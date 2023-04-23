import csv
from ...Actors.World.ChunkActor import ChunkActor
from ...Actors.DefaultPawnActor import DefaultPawnActor
from ...Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from ...Actors.Characters.AgentCharacterActor import AgentCharacterActor
from ...Actors.Weapons.WeaponActor import WeaponActor
from ...Actors.BulletActor import ClassicBullet

def mapWorldCSVData(world, worldCSVData):
    chunkList = []
    for chunkId, chunkCSVData in enumerate(worldCSVData):
        chunk = mapChunkCSVData(world, chunkCSVData, 0 if chunkId == 0 else 1)
        chunkList.append(chunk)
    return chunkList

def mapChunkCSVData(world, chunkCSVData, offsetChunk):
    tileSize = world.tileSize
    chunk = ChunkActor()
    ennemiesList = []
    obstaclesList = []
    for y, row in enumerate(chunkCSVData):
        for x, tile in enumerate(row):
            if tile != -1: # -1 = empty tile
                if tile > -1 and tile < 11:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["DEFAULT_WALL"], velX=world.scrollSpeedX))
                elif tile == 11 and tile <= 14:
                    pass # 11 : shield faibles -> Destructibles
                elif tile == 13 :
                    pass #13 : shield fort -> indestructible
                elif tile == 14 :
                    pass #14 : non utilisé
                elif tile == 15 : 
                    ennemiesList.append(EnnemyActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["DEFAULT_ENNEMY"], WeaponActor(ClassicBullet, world.spritesSurfaces["KIWI_BULLET"], 0.5), velX=world.scrollSpeedX))
                    #enemy = Character(window.screen, x*TILE_SIZE, y*TILE_SIZE, 50, 100, 5) #15 : ennemi horizontal
                    pass
                elif tile == 16 : 
                    ennemiesList.append(EnnemyActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["DEFAULT_ENNEMY"], WeaponActor(ClassicBullet, world.spritesSurfaces["KIWI_BULLET"], 0.5), velX=world.scrollSpeedX, velY=world.scrollSpeedX)) #16 : ennemi vertical
                elif tile == 17 :
                    pass # 17 : mur électrifié
                elif tile >= 18 and tile <= 19 :
                    pass # inutilisé
                elif tile == 12:
                    pass
                elif tile == 20 :
                    pass #Création de fin de niveau
    chunk.obstaclesList = obstaclesList
    chunk.ennemiesList = ennemiesList
    return chunk           
        
        
    


def loadWorldFromCSV(world, levelId):
    import os
    csv_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f"../../Assets/Levels/level{levelId}_data.csv"))
    with open(csv_file_path, newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        tHeight = 32
        tWidth = 401
        tChunkWidth = int((tHeight * 16) / 9) + ((tHeight * 16) % 9 > 0)
        """As a later improvement, we should turn this as a tool to create a header for each level_data.csv, 
        such as the first line of the file giving the total tWidth and tHeight of the level."""
        chunkData = [[None for _ in range (tChunkWidth)] for _ in range (tHeight)]
        worldChunkData = [chunkData for _ in range (int(tWidth/tChunkWidth) + (tWidth % tChunkWidth > 0))] # a list of empty lists representing each chunks
        
        for y, row in enumerate(reader):
            chunkId = -1
            for x, tile in enumerate(row):
                if(x%tChunkWidth == 0):
                    chunkId +=1
                
                worldChunkData[chunkId][y][x%tChunkWidth] = int(tile)
        """Generates line by line, increases the chunkId when x is a multiple of the chunkWidth 
        (meaning, it's the beginning of a new chunk)"""
    world.tHeight = tHeight
    world.tWidth = tWidth
    world.tChunkWidth = tChunkWidth
    return worldChunkData