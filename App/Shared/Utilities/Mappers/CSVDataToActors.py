import csv
from ...Actors.World.ChunkActor import ChunkActor
from ...Actors.DefaultPawnActor import DefaultPawnActor
from ...Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from ...Actors.Characters.AgentCharacterActor import AgentCharacterActor
from ...Actors.Weapons.WeaponActor import WeaponActor, DoubleWeaponActor
from ...Actors.BulletActor import ClassicBullet, TankBullet

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
                if tile == 0:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["MIDDLE_WALL"], velX=world.scrollSpeedX))
                elif tile == 1:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["LEFT_CORNER_WALL"], velX=world.scrollSpeedX))
                elif tile == 2:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["RIGHT_CORNER_WALL"], velX=world.scrollSpeedX))
                elif tile == 3:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["LEFT_WALL"], velX=world.scrollSpeedX))
                elif tile == 4:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["DEFAULT_WALL"], velX=world.scrollSpeedX))
                elif tile == 5:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["RIGHT_WALL"], velX=world.scrollSpeedX))
                elif tile == 6:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["LEFT_LASER_TOP_CORNER_WALL"], velX=world.scrollSpeedX))
                elif tile == 7:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["LEFT_LASER_WALL"], velX=world.scrollSpeedX))
                elif tile == 8:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["LEFT_LASER_BOT_CORNER_WALL"], velX=world.scrollSpeedX))
                elif tile == 9:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["RIGHT_LASER_TOP_CORNER_WALL"], velX=world.scrollSpeedX))
                elif tile == 10:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["RIGHT_LASER_WALL"], velX=world.scrollSpeedX))
                elif tile == 11:
                    obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["RIGHT_LASER_BOT_CORNER_WALL"], velX=world.scrollSpeedX))
                elif tile == 12:
                    pass#obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["TOP_GLASS_WALL"], velX=world.scrollSpeedX))
                elif tile == 13:
                    pass#obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["GLASS_WALL"], velX=world.scrollSpeedX))
                elif tile == 14:
                    pass#obstaclesList.append(DefaultPawnActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.spritesSurfaces["BOT_GLASS_WALL"], velX=world.scrollSpeedX))
                elif tile == 15 : #static enemy shooting left (wall)
                    ennemiesList.append(EnnemyActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.staticEnnemySurface_1, DoubleWeaponActor(ClassicBullet, world.spritesSurfaces["ENNEMY_BULLET"], 0.5, world.firePurpleSurface_1), velX=world.scrollSpeedX, bulletVelY=40))
                elif tile == 16 : # enemy shooting left
                    ennemiesList.append(EnnemyActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.movingEnnemySurface_1, WeaponActor(ClassicBullet, world.spritesSurfaces["ENNEMY_BULLET"], 0.5, world.firePurpleSurface_1), velX=world.scrollSpeedX))
                elif tile == 17 : #Enemy shooting under
                    ennemiesList.append(EnnemyActor(x*tileSize+(offsetChunk*world.tChunkWidth*tileSize), y*tileSize, world.idleEnnemySurface_1, WeaponActor(TankBullet, world.spritesSurfaces["IDLE_BULLET"], 0.5, world.firePurpleSurface_1), velX=world.scrollSpeedX, velY=world.scrollSpeedX, bulletVelX=world.scrollSpeedX, bulletVelY= 50)) 
                elif tile == 18  : # player spawn, unused actually
                    pass 
                elif tile == 19 : # Operator Wall 
                    pass 
                elif tile == 20 : # level end
                    pass 


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
        worldChunkData = [[[None for _ in range (tChunkWidth)] for _ in range (tHeight)] for _ in range (int(tWidth/tChunkWidth) + (tWidth % tChunkWidth > 0))] # a list of empty lists representing each chunks
        
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