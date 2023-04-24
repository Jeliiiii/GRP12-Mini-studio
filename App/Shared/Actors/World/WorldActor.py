import pygame
import os
from ...Utilities.Mappers.CSVDataToActors import mapWorldCSVData, loadWorldFromCSV
from ...Actors.Characters.AgentCharacterActor import AgentCharacterActor
from ...Actors.Weapons.WeaponActor import WeaponActor
from ...Actors.BulletActor import BulletActor

class WorldActor:

    def __init__(self, levelId):
        (self.winWidth, self.winHeight) = pygame.display.get_window_size()
        self.scrollSpeedX = -20
        self.scrollXDistance = 0
        worldCSVData = loadWorldFromCSV(self, levelId)
        self.tileSize = int(self.winHeight/self.tHeight)
        self.loadImages()
        self.background = (self.spritesSurfaces["BACKGROUND"], self.spritesSurfaces["BACKGROUND"].get_rect())
        self.agentCharacter = AgentCharacterActor(500, 300,self.spritesSurfaces["CHARACTER"], WeaponActor(BulletActor, self.spritesSurfaces["KIWI_BULLET"], 0.5), speed=self.tileSize)
        self.chunksList = {"LOADED":[],"ACTIVE":[],"ARCHIVED":[]}
        self.chunksList["LOADED"] = mapWorldCSVData(self, worldCSVData)
        self.scrollLoadedChunksToActive(2)
        self.bulletList = []

    def loadImages(self):
        tileSize = self.tileSize
        img = pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Characters/dodo_sideview.png"))
        characterSurface = pygame.transform.scale(img, (tileSize, tileSize))

        img = pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Characters/robot_bird.png"))
        ennemySurface = pygame.transform.scale(img, (tileSize,tileSize))
        img = pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Backgrounds/japanese_night_city.png"))
        backgroundSurface = pygame.transform.scale(img, (self.winWidth*img.get_height()/self.winHeight,self.winHeight))
        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Tiles/Blocks/brick_wall.png"))
        wallSurface = pygame.transform.scale(img, (tileSize,tileSize))
        
        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Miscs/kiwi_fruit_bullet.png"))
        bulletSurface = pygame.transform.scale(img, (tileSize/2,tileSize/2))
        

        self.spritesSurfaces = {"CHARACTER":characterSurface,
                                "DEFAULT_ENNEMY":ennemySurface,
                                "DEFAULT_WALL":wallSurface,
                                "BACKGROUND":backgroundSurface,
                                "KIWI_BULLET":bulletSurface}

    def scrollLoadedChunksToActive(self, amountToScroll):
        self.chunksList["ACTIVE"] = self.chunksList["ACTIVE"][amountToScroll:] + self.chunksList["LOADED"][:amountToScroll]
        self.chunksList["LOADED"] = self.chunksList["LOADED"][amountToScroll:]

    def onTick(self, inputs, dt):
        self.background[1].x += self.scrollSpeedX * dt * 4 
        self.scrollXDistance += self.scrollSpeedX * dt * 10  
        if self.scrollXDistance <= -self.tChunkWidth*self.tileSize:
            self.scrollXDistance += self.tChunkWidth*self.tileSize
            self.scrollLoadedChunksToActive(1)

        for bullet in self.bulletList:
            bullet.onTick(dt)
            if bullet.isInWindow((self.winWidth, self.winHeight)):
                #collision system - to split in CollisionSystem.testList(bulletList, ennemiesList)
                for chunk in self.chunksList["ACTIVE"]:
                    collidedEnnemyId = bullet.hitBox.collidelist([ennemy.hitBox for ennemy in chunk.ennemiesList])
                    if collidedEnnemyId != -1:
                        chunk.ennemiesList[collidedEnnemyId].shot(bullet.damage)
                        if chunk.ennemiesList[collidedEnnemyId].health <= 0:
                            chunk.ennemiesList.remove(chunk.ennemiesList[collidedEnnemyId])
                            self.bulletList.remove(bullet)
                            break
            else:
                self.bulletList.remove(bullet)

        for chunk in self.chunksList["ACTIVE"]:
            for ennemy in chunk.ennemiesList:
                bulletList = ennemy.onTick(dt,(self.winWidth, self.winHeight))
                self.bulletList += bulletList

            for obstacle in chunk.obstaclesList:
                obstacle.onTick(dt)

        bulletList = self.agentCharacter.onTick(inputs, dt)
        self.bulletList += bulletList

    def draw(self, window):
        window.blit(self.background[0], self.background[1])
        self.agentCharacter.draw(window)
        for bullet in self.bulletList:
            bullet.draw(window)
        for chunk in self.chunksList["ACTIVE"]:
            for element in chunk.ennemiesList + chunk.obstaclesList:
                element.draw(window)



if __name__ == "__main__":
    world = WorldActor()
    world.loadLevelFromCSV(0)