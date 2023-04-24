import pygame
import os
from ...Utilities.Mappers.CSVDataToActors import mapWorldCSVData, loadWorldFromCSV
from ...Actors.Characters.AgentCharacterActor import AgentCharacterActor
from ...Actors.Weapons.WeaponActor import *
from ...Actors.BulletActor import *
from ..loots.ArsenalUpdater import ArsenalUpdater
from random import randint
from ...Actors.World.SpriteSheetCutting import SpriteSheetCutter

class WorldActor:

    def __init__(self, levelId):
        (self.winWidth, self.winHeight) = pygame.display.get_window_size()
        self.scrollSpeedX = -20
        self.scrollXDistance = 0
        worldCSVData = loadWorldFromCSV(self, levelId)
        self.tileSize = int(self.winHeight/self.tHeight)
        self.agentSprites = {"FORWARD":[],
                             "UP":[],
                             "DOWN":[],
                             "BACK":[]}
        self.loadImages()
        self.background = (self.spritesSurfaces["BACKGROUND"], self.spritesSurfaces["BACKGROUND"].get_rect())
        self.arsenal = {"CLASSIC": WeaponActor(ClassicBullet, self.spritesSurfaces["KIWI_BULLET"], 0.5),
                        "TANK": WeaponActor(TankBullet, self.spritesSurfaces["CHICKEN"], 6),
                        "QUADRA": QuadraWeaponActor(ClassicBullet, self.spritesSurfaces["BLUE_BULLET"], 2),}
        self.agentCharacter = AgentCharacterActor(500, 300,self.agentSprites, self.arsenal["CLASSIC"], speed=self.tileSize)
        self.chunksList = {"LOADED":[],"ACTIVE":[],"ARCHIVED":[]}
        self.chunksList["LOADED"] = mapWorldCSVData(self, worldCSVData)
        self.chunksList["ACTIVE"] = self.chunksList["LOADED"][:2]
        self.chunksList["LOADED"] = self.chunksList["LOADED"][2:]
        self.bulletList = []
        self.lootList = []
        

    def loadImages(self):
        tileSize = self.tileSize

    
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(830, 415, 415, 415)
        dodoForwardSurface_k1 = pygame.transform.scale(img, (tileSize*10, tileSize*10))
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(830, 415, 415, 415)
        img = pygame.transform.scale(img, (tileSize*10,tileSize*10))
        dodoForwardSurface_k2 = pygame.transform.scale(img, (tileSize, tileSize))
        self.agentSprites["FORWARD"] = [dodoForwardSurface_k1, dodoForwardSurface_k2]
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(2075, 415, 415, 415)
        dodoUpSurface_K1 = pygame.transform.scale(img, (tileSize, tileSize))
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(2490, 415, 415, 415)
        dodoUpSurface_K2 = pygame.transform.scale(img, (tileSize, tileSize))
        self.agentSprites["UP"] = [dodoUpSurface_K1, dodoUpSurface_K2]
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(3320, 415, 415, 415)
        img = pygame.transform.scale(img, (tileSize*10,tileSize*10))
        dodoDownface_k1 = pygame.transform.scale(img, (tileSize, tileSize))
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(3735, 415, 415, 415)
        dodoDownSurface_k2 = pygame.transform.scale(img, (tileSize, tileSize))
        self.agentSprites["DOWN"] = [dodoDownface_k1, dodoDownSurface_k2]
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(4580, 415, 415, 415)
        dodoBackSurface_K1 = pygame.transform.scale(img, (tileSize, tileSize))
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(4995, 415, 415, 415)
        dodoBackSurface_K2 = pygame.transform.scale(img, (tileSize, tileSize))
        self.agentSprites["BACK"] = [dodoBackSurface_K1, dodoBackSurface_K2]


        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(830, 830, 415, 415)
        bulletFireSureface_K1 = pygame.transform.scale(img, (tileSize, tileSize))
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(1245, 830, 415, 415)
        bulletFireSureface_K2 = pygame.transform.scale(img, (tileSize, tileSize))
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(1660, 830, 415, 415)
        bulletFireSureface_K3 = pygame.transform.scale(img, (tileSize, tileSize))
        sheet = SpriteSheetCutter(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))
        img = sheet.cut(2075, 830, 415, 415)
        bulletSurface = pygame.transform.scale(img, (tileSize, tileSize))
        self.fireAnimSurfaces = {"K1":bulletFireSureface_K1,
                                 "K2":bulletFireSureface_K2,
                                 "K3":bulletFireSureface_K3,}
        
        
        
        
        img = pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Characters/robot_bird.png"))
        ennemySurface = pygame.transform.scale(img, (tileSize,tileSize))
        img = pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Backgrounds/japanese_night_city.png"))
        backgroundSurface = pygame.transform.scale(img, (self.winWidth*img.get_height()/self.winHeight,self.winHeight))
        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Tiles/Blocks/brick_wall.png"))
        wallSurface = pygame.transform.scale(img, (tileSize,tileSize))
        #img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Miscs/kiwi_fruit_bullet.png"))
        #bulletSurface = pygame.transform.scale(img, (tileSize/2,tileSize/2))
        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Miscs/chicken.png"))
        chicken = pygame.transform.scale(img, (tileSize*8,tileSize*8))
        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Miscs/blueBullet.png"))
        blueBullet = pygame.transform.scale(img, (tileSize,tileSize))
        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Miscs/drop.png"))
        redDrop = pygame.transform.scale(img, (tileSize,tileSize))
        self.spritesSurfaces = {#"DEFAULT_BULLET":bulletSurface,
                                "DEFAULT_ENNEMY":ennemySurface,
                                "DEFAULT_WALL":wallSurface,
                                "BACKGROUND":backgroundSurface,
                                "KIWI_BULLET":bulletSurface,
                                "CHICKEN":chicken,
                                "BLUE_BULLET":blueBullet,
                                "RED_DROP":redDrop}


    def onTick(self, inputs, dt):
        self.background[1].x += self.scrollSpeedX * dt * 4 
        self.scrollXDistance += self.scrollSpeedX * dt * 10  
        if self.scrollXDistance <= -self.tChunkWidth*self.tileSize:
            self.scrollXDistance += self.tChunkWidth*self.tileSize
            self.chunksList["ACTIVE"] = self.chunksList["ACTIVE"][1:] + self.chunksList["LOADED"][:1]
            self.chunksList["LOADED"] = self.chunksList["LOADED"][1:]
            print("newChunkActive")

        for bullet in self.bulletList:
            bullet.onTick(dt)
            #collision system - to split in CollisionSystem.testList(bulletList, ennemiesList)
            for chunk in self.chunksList["ACTIVE"]:
                collidedEnnemyId = bullet.hitBox.collidelist([ennemy.hitBox for ennemy in chunk.ennemiesList])
                if collidedEnnemyId != -1:
                    chunk.ennemiesList[collidedEnnemyId].shot(bullet.damage)
                    if chunk.ennemiesList[collidedEnnemyId].health <= 0:
                        chunk.ennemiesList.remove(chunk.ennemiesList[collidedEnnemyId])
                        if randint(1,3)==1:
                            self.lootList.append(ArsenalUpdater(self.agentCharacter, self.arsenal,bullet.sprite[1].x, bullet.sprite[1].y, self.spritesSurfaces["RED_DROP"], self.scrollSpeedX))
                        bullet.onHit(self.bulletList)
                        break
        
        for loot in self.lootList:
            loot.onTick(dt)
            if  loot.hitBox.colliderect(self.agentCharacter.hitBox):
                loot.onHit(self.lootList)

        for chunk in self.chunksList["ACTIVE"]:
            for ennemy in chunk.ennemiesList:
                bulletList = ennemy.onTick(dt)
                self.bulletList += bulletList
            bulletList = self.agentCharacter.onTick(inputs, dt)
            self.bulletList += bulletList

            for obstacle in chunk.obstaclesList:
                obstacle.onTick(dt)

    def draw(self, window):
        window.blit(self.background[0], self.background[1])
        self.agentCharacter.draw(window)
        for bullet in self.bulletList:
            bullet.draw(window)
        for chunk in self.chunksList["ACTIVE"]:
            for element in chunk.ennemiesList + chunk.obstaclesList:
                element.draw(window)
        for loot in self.lootList:
            loot.draw(window)



if __name__ == "__main__":
    world = WorldActor()
    world.loadLevelFromCSV(0)