import pygame
import random

class Apple:
    def __init__(self):
        self.taille_bloc = 10
        self.relocate()
        
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.taille_bloc, self.taille_bloc))

    def relocate(self):
        self.x = random.randrange(150+self.taille_bloc, 900-self.taille_bloc, self.taille_bloc)
        self.y = random.randrange(50+self.taille_bloc, 700-self.taille_bloc, self.taille_bloc)