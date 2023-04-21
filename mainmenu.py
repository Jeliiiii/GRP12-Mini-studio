import pygame
from window import *

class MainMenu:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.Font(None, 50)
        self.play_button = pygame.Rect(570, 300, 400, 200) # Crée un rectangle pour le bouton "play"
        self.quit_button = pygame.Rect(100, 700, 200, 100)

    def draw(self):
        self.window.screen.fill((255, 255, 255)) # Efface l'écran
        # Dessine le texte "Birds of Chaos" centré en haut de l'écran
        text = self.font.render("Birds of Chaos", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.window.width/2, self.window.height/4))
        self.window.screen.blit(text, text_rect)

        # Dessine le bouton "play"
        pygame.draw.rect(self.window.screen, (0, 255, 0), self.play_button)
        text = self.font.render("Play", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.play_button.center)
        self.window.screen.blit(text, text_rect)
        
        # Dessine le bouton "quit"
        pygame.draw.rect(self.window.screen, (255, 0, 0), self.quit_button)
        text = self.font.render("Quitter", True, (0, 0, 0))
        text_rect = text.get_rect(center=self.quit_button.center)
        self.window.screen.blit(text, text_rect)

        pygame.display.flip()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifie si le bouton "play" a été cliqué
                if self.play_button.collidepoint(event.pos):
                    return True # Retourne True pour indiquer que le jeu doit être lancé
        return False # Retourne False sinon
    
    
    def quit_game(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.collidepoint(event.pos):
                   return True
        return False 
