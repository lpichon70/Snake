import pygame

class Snake:
    def __init__(self, x, y, taille_bloc=10):
        self.x = x
        self.y = y
        self.taille_bloc = taille_bloc
        self.direction_x = taille_bloc
        self.direction_y = 0
        self.positions = []
        self.taille = 3

    def changer_direction(self, direction):
        if direction == "GAUCHE" and self.direction_x == 0:
            self.direction_x = -self.taille_bloc
            self.direction_y = 0
        elif direction == "DROITE" and self.direction_x == 0:
            self.direction_x = self.taille_bloc
            self.direction_y = 0
        elif direction == "HAUT" and self.direction_y == 0:
            self.direction_x = 0
            self.direction_y = -self.taille_bloc
        elif direction == "BAS" and self.direction_y == 0:
            self.direction_x = 0
            self.direction_y = self.taille_bloc

    def deplacer(self):
        self.x += self.direction_x
        self.y += self.direction_y
        self.positions.append([self.x, self.y])
        if len(self.positions) > self.taille:
            del self.positions[0]

    def collision_avec_bords(self):
        return (
            self.x < 150 or self.x >= 1050 or
            self.y < 50 or self.y >= 850 
        )
    
    def eatApple(self):
        self.taille += 1
        

    def collision_avec_soi_meme(self):
        return [self.x, self.y] in self.positions[:-1]

    def dessiner(self, surface):
        for pos in self.positions:
            pygame.draw.rect(surface, (0, 255, 0), (pos[0], pos[1], self.taille_bloc, self.taille_bloc))