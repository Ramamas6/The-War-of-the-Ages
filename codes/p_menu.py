"""
Manages the "escape" page of the game
"""

import pygame

class Menu :

    def __init__ (self, screen) :
        # Titre
        self.titre = (pygame.font.SysFont("algerian" , 150, bold=True)).render ( "Menu principal", 1 , (255,0,0) )
        self.titre_rect = self.titre.get_rect ()
        self.titre_rect.x = (screen.get_width() // 2) - (self.titre_rect.width // 2)
        self.titre_rect.y = 50
        # Boutons
        self.accueil = pygame.transform.scale(pygame.image.load("../assets/accueil.png"), (450, 188))
        self.accueil_rect = self.accueil.get_rect ()
        self.a_remplacer = pygame.transform.scale(pygame.image.load("../assets/a_remplacer.png"), (450, 188))
        self.a_remplacer_rect = self.a_remplacer.get_rect ()
        self.quitter = pygame.transform.scale(pygame.image.load("../assets/quitter.png"), (450, 188))
        self.quitter_rect = self.quitter.get_rect ()
        # Boutons X
        self.accueil_rect.x = (screen.get_width() // 2) - (self.accueil_rect.width // 2)
        self.a_remplacer_rect.x = self.accueil_rect.x
        self.quitter_rect.x = self.accueil_rect.x
        # Boutons Y
        self.accueil_rect.y = self.titre_rect.y + self.titre_rect.height
        self.a_remplacer_rect.y = self.accueil_rect.y + self.a_remplacer_rect.height + 20
        self.quitter_rect.y = self.a_remplacer_rect.y + self.quitter_rect.height + 20


    def afficher (self, main) :
        # Fond d'écran
        if (main.etape < 4) :
            main.screen.blit(main.accueil.background, (0, 0))
        # Titre
        main.screen.blit(self.titre, self.titre_rect)
        # Boutons
        main.screen.blit(self.accueil, self.accueil_rect)
        main.screen.blit(self.a_remplacer, self.a_remplacer_rect)
        main.screen.blit(self.quitter, self.quitter_rect)


    def menu (self, main) :
        self.afficher (main) # Affiche le menu
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
                        return True
                elif (event.type == pygame.KEYUP) :
                    main.pressed_button[event.key] = False

                # Souris bouton gauche
                    # Appuyé
                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) :
                    if (self.accueil_rect.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "accueil"
                    elif (self.a_remplacer_rect.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "a_remplacer"
                    elif (self.quitter_rect.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "quitter"
                    else :
                        main.pressed_button[event.button] = ""
                    # Laché
                elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1) :
                    if (self.accueil_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "accueil") :
                        main.pressed_button[event.button] = ""
                        main.etape = 1
                        return True
                    elif (self.a_remplacer_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "a_remplacer") :
                        main.pressed_button[event.button] = ""
                        main.etape = 1
                        return True
                    elif (self.quitter_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "quitter") :
                        main.pressed_button[event.button] = ""
                        pygame.quit()
                        return False
                    else :
                        main.pressed_button[event.button] = ""




