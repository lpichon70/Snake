import pygame

class Snake:
    def __init__(self, x, y, taille_bloc=10):
        """Constructeur de la classe

        Args:
            x (int): Coordonnée sur l'axe x
            y (int): Coordonnée sur l'axe y
            taille_bloc (int): Taille du serpent
        """
        self.x = x
        self.y = y
        self.taille_bloc = taille_bloc
        self.direction_x = taille_bloc
        self.direction_y = 0
        self.positions = []
        self.taille = 1

    def changer_direction(self, direction):
        """Fonction qui permet de changer la direction du serpent

        Args:
            direction (string): Chaîne de caractère à choix pour orienter le serpent : GAUCHE/DROITE/HAUT/BAS
        """
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
        """Fait avancer le serpent en fonction de la direction
        """
        self.x += self.direction_x
        self.y += self.direction_y
        self.positions.append([self.x, self.y])
        if len(self.positions) > self.taille:
            del self.positions[0]

    def collision_avec_bords(self):
        """Gestion de la collision avec les bords

        Returns:
            Bool: Retourne True ou Fasle en fonction de si le serpent touche un mur ou non
        """
        return (
            self.x < (150+self.taille_bloc) or self.x >= (1050-self.taille_bloc) or
            self.y < (50+self.taille_bloc) or self.y >= (750-self.taille_bloc) 
        )
    
    def eatApple(self):
        """Ajoute 1 à la taille du serpent
        """
        self.taille += 1

    def collision_avec_soi_meme(self):
        """Gestion de la collision avec soi même

        Returns:
            Bool: Retourne True ou Fasle en fonction de si le serpent touche une parti de son corp
        """
        return [self.x, self.y] in self.positions[:-1]

    def dessiner(self, surface):
        """Dessine le serpent

        Args:
            surface (pygame.display): Surface utilisé pour le jeu (fenêtre du jeu)
        """
        for pos in self.positions:
            pygame.draw.rect(surface, (0, 255, 0), (pos[0], pos[1], self.taille_bloc, self.taille_bloc))