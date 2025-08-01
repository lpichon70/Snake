import pygame
import random

class Apple:
    def __init__(self):
        """Constructeur de la classe
        """
        self.taille_bloc = 10
        self.relocate()
        
    def draw(self, surface):
        """Dessine la pomme

        Args:
            surface (pygame.display): Surface utilisé pour le jeu (fenêtre du jeu)
        """
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.taille_bloc, self.taille_bloc))

    def relocate(self):
        """Change les coordonnées de la pomme
        """
        self.x = random.randrange(150+self.taille_bloc, 900-self.taille_bloc, self.taille_bloc)
        self.y = random.randrange(50+self.taille_bloc, 700-self.taille_bloc, self.taille_bloc)