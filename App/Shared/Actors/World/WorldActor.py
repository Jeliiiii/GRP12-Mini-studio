import pygame
import os
from random import randint
from ...Utilities.Mappers.CSVDataToActors import mapWorldCSVData, loadWorldFromCSV
from ...Actors.Characters.AgentCharacterActor import AgentCharacterActor
from ...Actors.Weapons.WeaponActor import *
from ...Actors.BulletActor import *
from ..loots.ArsenalUpdater import ArsenalUpdater
from random import randint

class WorldActor:

    def __init__(self, levelId):
        (self.winWidth, self.winHeight) = pygame.display.get_window_size()
        self.nextScene = None
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
        self.arsenal = {"CLASSIC": WeaponActor(ClassicBullet, self.spritesSurfaces["PURPLE_BULLET"], 0.5, self.firePurpleSurface_1),
                        "TANK": WeaponActor(TankBullet, self.spritesSurfaces["CHICKEN_BULLET"], 6, self.fireRedSurface_1),
                        "QUADRA": QuadraWeaponActor(ClassicBullet, self.spritesSurfaces["RED_BULLET"], 2, self.firePurpleSurface_1),}
        self.agentCharacter = AgentCharacterActor(500, 300,self.agentSprites, self.arsenal["CLASSIC"], speed=self.tileSize)
        self.chunksList = {"LOADED":[],"ACTIVE":[],"ARCHIVED":[]}
        self.chunksList["LOADED"] = mapWorldCSVData(self, worldCSVData)
        self.chunksList["ACTIVE"] = self.chunksList["LOADED"][:2]
        self.chunksList["LOADED"] = self.chunksList["LOADED"][2:]
        self.bulletListAlly = []
        self.bulletListEnnemy = []
        self.lootList = []
        self.gameOverTimer = 40
        self.gameOverSprite = None
        

    def loadImages(self):
        tileSize = self.tileSize

    
        sheet = pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/SpriteSheet.png"))


        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 414, 413, 413))
        dodoForwardSurface_K1 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 414, 413, 413))
        dodoForwardSurface_K2 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        self.agentSprites["FORWARD"] = [dodoForwardSurface_K1, dodoForwardSurface_K2]

        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1653, 414, 413, 413))
        dodoUpSurface_K1 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(2066, 414, 413, 413))
        dodoUpSurface_K2 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        self.agentSprites["UP"] = [dodoUpSurface_K1, dodoUpSurface_K2]
        
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(2479, 414, 413, 413))
        dodoDownSurface_k1 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(2892, 414, 413, 413))
        dodoDownSurface_k2 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        self.agentSprites["DOWN"] = [dodoDownSurface_k1, dodoDownSurface_k2]
        
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(3305, 414, 413, 413))
        dodoBackSurface_K1 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(3718, 414, 413, 413))
        dodoBackSurface_K2 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        self.agentSprites["BACK"] = [dodoBackSurface_K1, dodoBackSurface_K2]

#purple
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 827, 413, 413))
        bulletPurpleSureface_PK1 = pygame.transform.scale(surf, (tileSize*2, tileSize*2))

        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 1240, 413, 413))
        bulletPurpleSureface_PK2 = pygame.transform.scale(surf, (tileSize*2, tileSize*2))

        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 1653, 413, 413))
        bulletPurpleSureface_PK3 = pygame.transform.scale(surf, (tileSize*2, tileSize*2))

        self.firePurpleSurface_1 = {"K1":bulletPurpleSureface_PK1,
                                 "K2":bulletPurpleSureface_PK2,
                                 "K3":bulletPurpleSureface_PK3,}
        
#purple explosion
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 2066, 413, 413))
        purpleBulletSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        

#red
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 827, 413, 413))
        bulletRedSurface_PK1 = pygame.transform.scale(surf, (tileSize, tileSize))

        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 1240, 413, 413))
        bulletRedSurface_PK2 = pygame.transform.scale(surf, (tileSize, tileSize))

        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 1653, 413, 413))
        bulletRedSurface_PK3 = pygame.transform.scale(surf, (tileSize, tileSize))

        self.fireRedSurface_1 = {"K1":bulletRedSurface_PK1,
                                 "K2":bulletRedSurface_PK2,
                                 "K3":bulletRedSurface_PK3,}
        
#red explosion
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 2066, 413, 413))
        redBulletSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        
#Chicken bullet
        surf = pygame.surface.Surface((1500, 1000))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 2479, 1239, 826))
        chickenBulletSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))



        #static Ennemy
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 3718, 413, 413))
        staticEnnemySurface_PK1 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 4131, 413, 413))
        staticEnnemySurface_PK2 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 4544, 413, 413))
        staticEnnemySurface_PK3 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        self.staticEnnemySurface_1 = {"K1":staticEnnemySurface_PK1,
                                 "K2":staticEnnemySurface_PK2,
                                 "K3":staticEnnemySurface_PK3,}

        surf = pygame.surface.Surface((500, 1000))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 3718, 413, 826))
        MovingEnnemySurface_PK1 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        surf = pygame.surface.Surface((500, 1000))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 4131, 413, 826))
        MovingEnnemySurface_PK2 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        surf = pygame.surface.Surface((500, 1000))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 4544, 413, 826))
        MovingEnnemySurface_PK3 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        self.movingEnnemySurface_1 = {"K1":MovingEnnemySurface_PK1,
                                 "K2":MovingEnnemySurface_PK2,
                                 "K3":MovingEnnemySurface_PK3,}
        
        surf = pygame.surface.Surface((1000, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(2066, 3305, 826, 413))
        idleEnnemySurface_PK1 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        surf = pygame.surface.Surface((1000, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(2066, 4131, 826, 413))
        idleEnnemySurface_PK2 = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        self.idleEnnemySurface_1 = {"K1":idleEnnemySurface_PK1,
                                 "K2":idleEnnemySurface_PK2}

        #Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1, 2479, 413, 413))
        wallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        
        #Left Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(414, 2892, 413, 413))
        leftWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Left Corner Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(414, 2479, 413, 413))
        leftCornerWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Middle Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 2479, 413, 413))
        middleWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Right Corner Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 2479, 413, 413))
        rightCornerWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))


        #Right Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(1240, 2892, 413, 413))
        rightWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Right Laser Top Corner Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(414, 3718, 413, 413))
        rightLaserTopCornerWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Right Laser Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(414, 4131, 413, 413))
        rightLaserWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Right Laser Bot Corner Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(414, 4544, 413, 413))
        rightLaserBotCornerWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Left Laser Top Corner Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 3718, 413, 413))
        leftLaserTopCornerWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Left Laser Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 4131, 413, 413))
        leftLaserWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))

        #Left Laser Bot Corner Brick Wall
        surf = pygame.surface.Surface((500, 500))
        surf.set_colorkey((0,0,0))
        surf.blit(sheet, (0, 0),(827, 4544, 413, 413))
        leftLaserBotCornerWallSurface = pygame.transform.scale(surf, (tileSize*3, tileSize*3))
        
        img = pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Backgrounds/japanese_night_city.png"))
        backgroundSurface = pygame.transform.scale(img, (self.winWidth*img.get_height()/self.winHeight,self.winHeight))

        img= pygame.image.load(os.path.join(os.path.dirname(__file__),"../../Assets/Graphics/Miscs/drop.png"))
        redDrop = pygame.transform.scale(img, (tileSize,tileSize))

        self.spritesSurfaces = {"DEFAULT_WALL":wallSurface,
                                "LEFT_WALL":leftWallSurface,
                                "LEFT_CORNER_WALL":leftCornerWallSurface,
                                "LEFT_LASER_TOP_CORNER_WALL":leftLaserTopCornerWallSurface,
                                "LEFT_LASER_WALL":leftLaserWallSurface,
                                "LEFT_LASER_BOT_CORNER_WALL":leftLaserBotCornerWallSurface,
                                "MIDDLE_WALL":middleWallSurface,
                                "RIGHT_WALL" :rightWallSurface,
                                "RIGHT_CORNER_WALL":rightCornerWallSurface,
                                "RIGHT_LASER_TOP_CORNER_WALL":rightLaserTopCornerWallSurface,
                                "RIGHT_LASER_WALL":rightLaserWallSurface,
                                "RIGHT_LASER_BOT_CORNER_WALL":rightLaserBotCornerWallSurface,
                                "PURPLE_BULLET" :purpleBulletSurface,
                                "RED_BULLET" :redBulletSurface,
                                "CHICKEN_BULLET" :chickenBulletSurface,
                                "BACKGROUND":backgroundSurface,
                                "RED_DROP":redDrop,}


    def onTick(self, inputs, dt):
        self.background[1].x += self.scrollSpeedX * dt * 4 
        self.scrollXDistance += self.scrollSpeedX * dt * 10  
        if self.scrollXDistance <= -self.tChunkWidth*self.tileSize:
            self.scrollXDistance += self.tChunkWidth*self.tileSize
            self.chunksList["ACTIVE"] = self.chunksList["ACTIVE"][1:] + self.chunksList["LOADED"][:1]
            self.chunksList["LOADED"] = self.chunksList["LOADED"][1:]

        for bullet in self.bulletListAlly:
            bullet.onTick(dt)
            #collision system - to split in CollisionSystem.testList(bulletList, ennemiesList)
            for chunk in self.chunksList["ACTIVE"]:
                collidedEnnemyId = bullet.hitBox.collidelist([ennemy.hitBox for ennemy in chunk.ennemiesList])
                if collidedEnnemyId != -1:
                    chunk.ennemiesList[collidedEnnemyId].shot(bullet.damage)
                    if chunk.ennemiesList[collidedEnnemyId].health <= 0:
                        if 0 < chunk.ennemiesList[collidedEnnemyId].sprite[1][0] < self.winWidth :
                            if randint(1,3)==1:
                                self.lootList.append(ArsenalUpdater(self.agentCharacter, self.arsenal,bullet.sprite[1].x, bullet.sprite[1].y, self.spritesSurfaces["RED_DROP"], self.scrollSpeedX))
                        chunk.ennemiesList.remove(chunk.ennemiesList[collidedEnnemyId])
                        bullet.onHit(self.bulletListAlly)
                        break
                
            
        for bullet in self.bulletListEnnemy:
            bullet.onTick(dt)
            if  bullet.hitBox.colliderect(self.agentCharacter.hitBox):
                bullet.onHit(self.bulletListEnnemy)

        

        for chunk in self.chunksList["ACTIVE"]:
            for ennemy in chunk.ennemiesList:
                bulletList = ennemy.onTick(dt)
                self.bulletListEnnemy += bulletList
            bulletList = self.agentCharacter.onTick(inputs, dt)
            self.bulletListAlly += bulletList

            for obstacle in chunk.obstaclesList:
                obstacle.onTick(dt)
                for bullet in self.bulletListAlly:
                    if obstacle.hitBox.colliderect(bullet.hitBox):
                        try :
                            self.bulletListAlly.remove(bullet)
                        except :
                            pass
                for bullet in self.bulletListEnnemy:
                    if obstacle.hitBox.colliderect(bullet.hitBox):
                        try :
                            self.bulletListEnnemy.remove(bullet)
                        except :
                            pass
                #systeme collision dodo/obstacle
                """if  obstacle.hitBox.colliderect(self.agentCharacter.hitBox) == True:
                    self.onTick = self.gameOver"""
                
            for loot in self.lootList:
                loot.onTick(dt)
                if loot.hitBox.colliderect(self.agentCharacter.hitBox):
                    loot.onHit(self.lootList)

            

    def draw(self, window):
        window.blit(self.background[0], self.background[1])
        self.agentCharacter.draw(window)
        for bullet in self.bulletListAlly:
            bullet.draw(window)
        for bullet in self.bulletListEnnemy:
            bullet.draw(window)
        for chunk in self.chunksList["ACTIVE"]:
            for element in chunk.ennemiesList + chunk.obstaclesList:
                element.draw(window)
        for loot in self.lootList:
            loot.draw(window)
        self.agentCharacter.weapon.draw(window, (self.agentCharacter.sprite[1][0]+self.tileSize*2, self.agentCharacter.sprite[1][1]+0.39*self.tileSize))
        if self.gameOverSprite :
            window.blit(self.gameOverSprite)



    """def gameOver(self, input, dt):
        self.gameOverTimer -= 1
        if 30<= self.gameOverTimer < 40:
            self.gameOverSprite = (self.explosionList["K1"], self.explosionList["K1"].get_rect(topleft=AgentCharacterActor.sprite[1]))
        elif 20<= self.gameOverTimer < 30:
            self.gameOverSprite[1] = (self.explosionList["K2"])
        elif 10<= self.gameOverTimer < 20:
            self.gameOverSprite[1] = (self.explosionList["K3"])
        elif 0<= self.gameOverTimer < 10:
            self.gameOverSprite[1] = (self.explosionList["K4"])
        else:
            from ...Scenes.Menus.GameOverScene import GameOverScene
            self.nextScene = GameOverScene()"""
            


if __name__ == "__main__":
    world = WorldActor()
    world.loadLevelFromCSV(1)