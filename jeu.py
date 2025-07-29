# Example file showing a basic pygame "game loop"
import pygame, sys, random
from snake import Snake 
from apple import Apple 

class Jeu:
    def __init__(self):
        """Contructeur de la class
        """
        pygame.init()
        self.largeur = 1200
        self.hauteur = 900
        self.ecran = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Snake - Écran de démarrage")
        self.clock = pygame.time.Clock()
        self.ecran_debut = True
        self.Jeu_encours = False
        self.snake = Snake(self.largeur // 2, self.hauteur // 2)
        self.apple = Apple()
        
    def principale(self):
        """Page d'accueil du jeu
        """
        centre_x = self.ecran.get_width() // 2

        while self.ecran_debut:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.ecran_debut = False 
                        self.Jeu_encours = True
                        self.play()
                        

            # Couleur de fond (noir ici)
            self.ecran.fill((0, 0, 0))


            titre_rect = pygame.Rect(150, 50, self.ecran.get_width() - 300, self.ecran.get_height() - 100)
            pygame.draw.rect(self.ecran, (255, 255, 255), titre_rect, width=4, border_radius=10)

            # Affichage du titre et consignes
            self.message_debut("grand", "SNAKE", (centre_x, 200), (0, 255, 0))
            self.message_debut("petit", "Le but du jeu est de faire grandir le serpent", (centre_x - 100, 350), (0, 255, 0))
            self.message_debut("petit", "Pour cela, il doit manger des pommes !", (centre_x + 100,425), (0, 255, 0))
            self.message_debut("moyen", "Appuyez sur ENTRER pour commencer", (centre_x,550), (0, 255, 0))

            pygame.display.flip()
            self.clock.tick(60)  # 60 FPS

            
    def play(self):
        while self.Jeu_encours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.Jeu_encours = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.snake.changer_direction("GAUCHE")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.changer_direction("DROITE")
                    elif event.key == pygame.K_UP:
                        self.snake.changer_direction("HAUT")
                    elif event.key == pygame.K_DOWN:
                        self.snake.changer_direction("BAS")

            next_x = self.snake.x + self.snake.direction_x
            next_y = self.snake.y + self.snake.direction_y

            # Vérifier la collision avec la pomme à la prochaine position
            if [next_x, next_y] == [self.apple.x, self.apple.y]:
                self.snake.eatApple()
                self.apple.relocate()
                
            self.snake.deplacer()

            if self.snake.collision_avec_bords() or self.snake.collision_avec_soi_meme() :
                self.Jeu_encours = False

            self.afficher()

        pygame.quit()

    def afficher(self):
        self.ecran.fill((0, 0, 0))  # fond noir
        titre_rect = pygame.Rect(150, 50, self.ecran.get_width() - 300, self.ecran.get_height() - 100)
        pygame.draw.rect(self.ecran, (255, 255, 255), titre_rect, width=4, border_radius=0)
        self.snake.dessiner(self.ecran)
        self.apple.draw(self.ecran)
        pygame.display.flip()
        self.clock.tick(20)  # vitesse du jeu

    def message_debut(self, font, message, position, couleur):
        """Fonction de gestion des label pour la page d'accueil

        Args:
            font (string): Taille de la police (petit,moyen,grand)
            message (string): Contenu du message à afficher
            position (int,int): Position du text dans la page
            couleur (int,int,int): Couleur du text
        """
        
        if font == "petit":
            police = pygame.font.SysFont("arial", 20, True)
        elif font == "moyen":
            police = pygame.font.SysFont("arial", 25, True)
        elif font == "grand":
            police = pygame.font.SysFont("arial", 35, True)
        else:
            police = pygame.font.SysFont("arial", 30, True)

        texte = police.render(message, True, couleur)
        texte_rect = texte.get_rect(center=position)
        self.ecran.blit(texte, texte_rect)
