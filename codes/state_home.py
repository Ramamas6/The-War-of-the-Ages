"""
Manages the home page of the game
"""

import pygame

class Accueil :

    def __init__ (self, screen) :
        self.background = pygame.transform.scale(pygame.image.load("../assets/bg_accueil.jpg"), (screen.get_width(), screen.get_height()))
        # Titre
        self.titre = (pygame.font.SysFont("algerian", 180, bold=True)).render ("Towns Age", 1, (255,0,0))
        self.titre_rect = self.titre.get_rect ()
        self.titre_rect.x = (screen.get_width() // 2) - (self.titre_rect.width // 2)
        self.titre_rect.y = 50
        # Boutons
        self.continuer = pygame.transform.scale(pygame.image.load("../assets/continuer.png"), (450, 188))
        self.continuer_rect = self.continuer.get_rect ()
        self.nouvelle_partie = pygame.transform.scale(pygame.image.load("../assets/nouvelle_partie.png"), (450, 188))
        self.nouvelle_partie_rect = self.nouvelle_partie.get_rect ()
        self.quitter = pygame.transform.scale(pygame.image.load("../assets/quitter.png"), (450, 188))
        self.quitter_rect = self.quitter.get_rect ()
        # Boutons X
        self.continuer_rect.x = (screen.get_width() // 2) - (self.continuer_rect.width // 2)
        self.nouvelle_partie_rect.x = self.continuer_rect.x
        self.quitter_rect.x = self.continuer_rect.x
        # Boutons Y
        self.continuer_rect.y = self.titre_rect.y + self.titre_rect.height
        self.nouvelle_partie_rect.y = self.continuer_rect.y + self.nouvelle_partie_rect.height + 20
        self.quitter_rect.y = self.nouvelle_partie_rect.y + self.quitter_rect.height + 20

    def afficher (self, screen, etape) :
        # Fond
        screen.blit(self.background, (0, 0))
        # Titre
        if (etape == "GameOver") :
            self.titre = (pygame.font.SysFont("algerian", 180, bold=True)).render ("Game Over", 1, (255,0,0))
            screen.blit(self.titre, self.titre_rect)
        elif (etape == "Victory") :
            self.titre = (pygame.font.SysFont("algerian", 180, bold=True)).render ("Victoire", 1, (255,0,0))
            screen.blit(self.titre, self.titre_rect)
        else :
            self.titre = (pygame.font.SysFont("algerian", 180, bold=True)).render ("Towns Age", 1, (255,0,0))
            screen.blit(self.titre, self.titre_rect)
        # Boutons
        if (etape == "Home") :
            self.continuer = pygame.transform.scale(pygame.image.load("../assets/continuer.png"), (450, 188))
            screen.blit(self.continuer, self.continuer_rect)
        else :
            self.continuer = pygame.transform.scale(pygame.image.load("../assets/continuer_non.png"), (450, 188))
            screen.blit(self.continuer, self.continuer_rect)
        screen.blit(self.nouvelle_partie, self.nouvelle_partie_rect)
        screen.blit(self.quitter, self.quitter_rect)

# _______________________________________________________________________________________________________________________________ #

def accueil (main) :
    main.accueil.afficher (main.screen, main.etape) # Affiche l'accueil
    pygame.display.flip() # Met à jour la fenêtre
    while (True) :
        # Evenements
        for event in pygame.event.get() :
            # Fenêtre fermée
            if (event.type == pygame.QUIT) :
                pygame.quit()
                return False
            # Bouton
            elif (event.type == pygame.KEYDOWN) :
                main.pressed_button[event.key] = True
                if (event.key == pygame.K_ESCAPE) :
                    return main.menu.menu(main)
            elif (event.type == pygame.KEYUP) :
                main.pressed_button[event.key] = False

            # Souris bouton gauche (1) : bouton droit = 3
                # Appuyé
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) :
                if (main.accueil.continuer_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "continuer"
                elif (main.accueil.nouvelle_partie_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "nouv"
                elif (main.accueil.quitter_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "quitter"
                else :
                    main.pressed_button[event.button] = ""
                # Laché
            elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1) :
                if (main.accueil.continuer_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "continuer") :
                    main.pressed_button[event.button] = ""
                    if (main.etape == "Home") :
                        main.etape = "Continue"
                        return True
                elif (main.accueil.nouvelle_partie_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "nouv") :
                    main.pressed_button[event.button] = ""
                    main.etape = "NewGame"
                    return True
                elif (main.accueil.quitter_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "quitter") :
                    main.pressed_button[event.button] = ""
                    pygame.quit()
                    return False
                else :
                    main.pressed_button[event.button] = ""
