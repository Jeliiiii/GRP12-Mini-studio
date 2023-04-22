from Shared.Actors.Characters.AgentCharacterActor import AgentCharacterActor
from Shared.Actors.Characters.Ennemies.EnnemyActor import EnnemyActor
from .Scene import Scene
import pygame

class GameAgentPovScene(Scene):
    
    def __init__(self):
        super().__init__()
        (windowWidth, windowHeight) = pygame.display.get_window_size()

        self.character = AgentCharacterActor(100,100, 30, 30, speed=70)
        self.bulletList = []
        self.ennemiesList = [EnnemyActor(600, 300, 20, 100, -5, 0), EnnemyActor(700, 400, 20, 100, -5, 0)]

    def updateScene(self, inputs, dt):
        for bullet in self.bulletList:
            bullet.onTick(dt)
            #collision system - to split in CollisionSystem.testList(bulletList, ennemiesList)
            collidedEnnemyId = bullet.rect.collidelist([ennemy.rect for ennemy in self.ennemiesList])
            if collidedEnnemyId != -1:
                self.ennemiesList[collidedEnnemyId].shot(bullet.damage)
                if self.ennemiesList[collidedEnnemyId].health <= 0:
                    self.ennemiesList.remove(self.ennemiesList[collidedEnnemyId])
                self.bulletList.remove(bullet)


        for ennemy in self.ennemiesList:
            bulletList = ennemy.onTick(dt)
            self.bulletList += bulletList
        bulletList = self.character.onTick(inputs, dt)
        self.bulletList += bulletList


    def drawScene(self, window):
        window.fill( "#111126" )
        self.character.draw(window)
        for bullet in self.bulletList:
            bullet.draw(window)
        for ennemy in self.ennemiesList:
            ennemy.draw(window)


    def switchMainMenuScene(self):
        from .Menus.MainMenuScene import MainMenuScene
        self.nextScene = MainMenuScene()