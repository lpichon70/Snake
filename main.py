# Example file showing a basic pygame "game loop"
import pygame, sys, random

class Jeu:
    def __init__(self):
        pygame.init()
        self.ecran = pygame.display.set_mode((1200, 900))
        pygame.display.set_caption("Snake - Écran de démarrage")
        self.Jeu_encours = True
        self.clock = pygame.time.Clock()
        self.ecran_debut = True
        
    def principale(self):

        centre_x = self.ecran.get_width() // 2

        while self.ecran_debut:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.ecran_debut = False  # Quitter l'écran d'accueil

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

    def message_debut(self, font, message, position, couleur):
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

# Lancer le jeu
if __name__ == '__main__':
    jeu = Jeu()
    jeu.principale()
    pygame.quit()