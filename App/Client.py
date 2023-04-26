import pygame
from Shared.Scenes.Menus.MainMenuScene import MainMenuScene

import os
print("!!!!!!\n!!!!!!\nWORKING DIRECTORY MANUALLY CHANGED\n!!!!!!\n!!!!!!")
os.chdir("C:\\Users\\BAPTISTE\\Desktop\\GRP12-Mini-studio")

class Client:

    def __init__(self):
        self.inputs = {"MOUSE_POS":[0,0], "MOUSE_BUTTONS":[], "ACTIVE_KEYS":[]}
        self.server = None
        self.clientSocket = None
        self.initWindow()

    def initWindow(self):
        pygame.init()
        desktopSize = pygame.display.get_desktop_sizes()
        print(desktopSize)
        pygame.display.set_caption("Birds of Chaos")
        # self.window = pygame.display.set_mode(desktopSize[0], pygame.FULLSCREEN)
        x = 0
        y = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
        self.window = pygame.display.set_mode((1000, 900))
        self.clock = pygame.time.Clock()
        self.currentScene = MainMenuScene()

    def updateInputsEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key not in self.inputs["ACTIVE_KEYS"]:
                    self.inputs["ACTIVE_KEYS"].append(event.key)
            elif event.type == pygame.KEYUP:
                if event.key in self.inputs["ACTIVE_KEYS"]:
                    self.inputs["ACTIVE_KEYS"].remove(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button not in self.inputs["MOUSE_BUTTONS"]:
                    self.inputs["MOUSE_BUTTONS"].append(event.button)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button in self.inputs["MOUSE_BUTTONS"]:
                    self.inputs["MOUSE_BUTTONS"].remove(event.button)
            elif event.type == pygame.MOUSEMOTION:
                (self.inputs["MOUSE_POS"][0],self.inputs["MOUSE_POS"][1]) = event.pos
            elif event.type == pygame.QUIT:
                self.running = False

    def updateClient(self):
        #Inputs Events Control
        if pygame.K_F11 in self.inputs["ACTIVE_KEYS"]:
            pygame.display.toggle_fullscreen()
            self.inputs["ACTIVE_KEYS"].remove(pygame.K_F11)
        #Scenes Switch Management
        if self.currentScene.nextScene:
            self.currentScene = self.currentScene.nextScene

    def main(self):
        while self.currentScene != "QUIT_CLIENT":
            dt = self.clock.tick(60)/1000 #time since last frame in seconds

            #Get Inputs
            self.updateInputsEvents()

            #Scene Manager
            self.currentScene.updateScene(self.inputs,dt)
            self.currentScene.drawScene(self.window)

            #Client Manager
            self.updateClient()

            pygame.display.update()

        pygame.quit()

if( __name__ == "__main__"):
    client = Client()
    client.main()