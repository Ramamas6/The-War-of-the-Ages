import pygame

class Base :

    def __init__ (self, screen) :
        self.epoque_nom = ["Préhistoire", "Moyen-Age", "Renaissance", "Age industriel", "Age moderne", "Age futuriste"]
        self.new()

        # Graphiques
        self.image = pygame.transform.scale(pygame.image.load("../assets/base/0.png"), (700, 700))
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = screen.get_height() - self.rect.height
        self.rectx = 500

        self.recolte = pygame.transform.scale(pygame.image.load("../assets/base/0_recolte.png"), (100, 100))
        self.recolte_rect = self.recolte.get_rect()
        self.recolte_rect.x = 3000
        self.recolte_rect.y = screen.get_height() - 200

        self.fermer = pygame.transform.scale(pygame.image.load("../assets/fermer.png"), (100, 100))
        self.fermer_rect = self.fermer.get_rect()
        self.fermer_rect.x = screen.get_width() - 150
        self.fermer_rect.y = 50

        self.plus_vie = pygame.transform.scale(pygame.image.load("../assets/base/plus_oui.png"), (200, 200))
        self.plus_vie_rect = self.plus_vie.get_rect()
        self.plus_vie_rect.x = (screen.get_width() // 2) - 250
        self.plus_vie_rect.y = 200

        self.fois_vie = pygame.transform.scale(pygame.image.load("../assets/base/fois_oui.png"), (200, 200))
        self.fois_vie_rect = self.fois_vie.get_rect()
        self.fois_vie_rect.x = (screen.get_width() // 2) + 50
        self.fois_vie_rect.y = 200

        self.help_vie = pygame.transform.scale(pygame.image.load("../assets/base/interrogation.png"), (60, 100))
        self.help_vie_rect = self.help_vie.get_rect()
        self.help_vie_rect.x = (screen.get_width() // 2) - 30
        self.help_vie_rect.y = 250

        self.defense = pygame.transform.scale(pygame.image.load("../assets/base/defense.png"), (450, 188))
        self.defense_rect = self.defense.get_rect()
        self.defense_rect.x = (screen.get_width() // 2) - (self.defense_rect.width // 2)
        self.defense_rect.y = 450

        self.ameliorer_oui = pygame.transform.scale(pygame.image.load("../assets/ameliorer_oui.png"), (450, 188))
        self.ameliorer_non = pygame.transform.scale(pygame.image.load("../assets/ameliorer_non.png"), (450, 188))
        self.ameliorer_rect = self.ameliorer_oui.get_rect()
        self.ameliorer_rect.x = self.defense_rect.x
        self.ameliorer_rect.y = 650

        self.plus_oui = pygame.transform.scale(pygame.image.load("../assets/plus_oui.png"), (100, 100))
        self.plus_non = pygame.transform.scale(pygame.image.load("../assets/plus_non.png"), (100, 100))

        self.revenus = pygame.rect.Rect(120, 250, 450, 188)
        self.up_recolte = pygame.rect.Rect(120, 450, 450, 188)
        self.down_recolte = pygame.rect.Rect(120, 650, 450, 188)

    def new (self) :
        self.epoque_nbr = 0
        self.max_health = 100
        self.health = 100
        self.health_base = 100
        self.health_ajout = 0
        self.health_multiply = 0
        self.damages = 0
        self.recoltex = 3000

    def calcul_health (self) :
        self.max_health = int ((self.health_base + self.health_ajout) * (1 + 0.1*self.health_multiply))
        self.health = self.max_health - self.damages

    def damage (self, attaque) :
        self.damages += attaque

##

def game_base_afficher (main) :
    pygame.draw.rect(main.screen, (150, 150, 150), [5, 5, main.screen.get_width() - 10, main.screen.get_height() - 10])
    main.screen.blit(main.game.base.fermer, main.game.base.fermer_rect)
    # Revenus passifs
    if (2 * (main.game.base.epoque_nbr + 1) >= main.game.revenus_passifs and main.game.monnaie >= (1 + main.game.revenus_passifs) ** 4) :
        main.screen.blit(main.game.base.plus_oui, main.game.base.revenus)
    else :
        main.screen.blit(main.game.base.plus_non, main.game.base.revenus)
    txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Revenus réguliers : " + str(main.game.revenus_passifs), 1, (0,0,0))
    main.screen.blit(txt, (main.game.base.revenus.x - 100, main.game.base.revenus.y - 60))

    # Quantitée de récolte
    if (5 * (main.game.base.epoque_nbr + 1) >= main.game.ressources and main.game.monnaie >= main.game.ressources ** 3) :
        main.screen.blit(main.game.base.plus_oui, main.game.base.up_recolte)
    else :
        main.screen.blit(main.game.base.plus_non, main.game.base.up_recolte)
    txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Récoltes : " + str(1 + main.game.ressources), 1, (0,0,0))
    main.screen.blit(txt, (main.game.base.up_recolte.x - 100, main.game.base.up_recolte.y - 60))

    # Distance de récolte
    if (main.game.base.recoltex > 2900 - 100 * main.game.base.epoque_nbr and main.game.monnaie >= (1 + (3000 - main.game.base.recoltex) * 10)) :
        main.screen.blit(main.game.base.plus_oui, main.game.base.down_recolte)
    else :
        main.screen.blit(main.game.base.plus_non, main.game.base.down_recolte)
    txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Distance de récolte : " + str(main.game.base.recoltex // 10), 1, (0,0,0))
    main.screen.blit(txt, (main.game.base.down_recolte.x - 100, main.game.base.down_recolte.y - 60))

    # Points de vie
    if (main.game.monnaie >= main.game.base.health_ajout ** 2) :
        main.game.base.plus_vie = pygame.transform.scale(pygame.image.load("../assets/base/plus_oui.png"), (200, 200))
    else :
        main.game.base.plus_vie = pygame.transform.scale(pygame.image.load("../assets/base/plus_non.png"), (200, 200))
    main.screen.blit(main.game.base.plus_vie, main.game.base.plus_vie_rect)
    if (main.game.monnaie >= 2**main.game.base.health_multiply) :
        main.game.base.fois_vie = pygame.transform.scale(pygame.image.load("../assets/base/fois_oui.png"), (200, 200))
    else :
        main.game.base.fois_vie = pygame.transform.scale(pygame.image.load("../assets/base/fois_non.png"), (200, 200))
    main.screen.blit(main.game.base.fois_vie, main.game.base.fois_vie_rect)
    main.screen.blit(main.game.base.help_vie, main.game.base.help_vie_rect)
    # Défenses
    main.screen.blit(main.game.base.defense, main.game.base.defense_rect)
    txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Défenses", 1, (0,0,0))
    main.screen.blit (txt, (main.game.base.defense_rect.x + 100, main.game.base.defense_rect.y + 60))
    # Améliorer
    if (main.game.xp >= main.game.xp_suiv and main.game.monnaie >= 99 + (main.game.base.epoque_nbr + 1) ** 8) :
        main.screen.blit(main.game.base.ameliorer_oui, main.game.base.ameliorer_rect)
    else :
        main.screen.blit(main.game.base.ameliorer_non, main.game.base.ameliorer_rect)
    txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Passer à l'age suivant", 1, (0,0,0))
    main.screen.blit(txt, (main.game.base.ameliorer_rect.x + 10, main.game.base.ameliorer_rect.y + 60))

    main.game.afficher_bandeau (main.screen)

##

def game_base (main) :
    while (True) :
        game_base_afficher (main)
        # Détails du bandeau
        a = pygame.mouse.get_pos()
        style = (pygame.font.SysFont("arial" , 50, bold=True))
        if (main.game.bandeau_monnaie_rect.collidepoint(a)):
            txt = style.render("Monnaie : " + str(main.game.monnaie), 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_monnaie_rect.x, main.game.bandeau_monnaie_rect.y + 100))
        elif (main.game.bandeau_xp_rect.collidepoint(a)):
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("XP : " + str(main.game.xp), 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_xp_rect.x, main.game.bandeau_xp_rect.y + 100))
        elif (main.game.bandeau_tetes_rect.collidepoint(a)):
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Soldats : 1 - Outils : 2", 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_tetes_rect.x, main.game.bandeau_tetes_rect.y + 100))
        elif (main.game.base.revenus.collidepoint(a)) :
            txt = style.render("Coût : " + str((1 + main.game.revenus_passifs) ** 4), 1, (0,0,0))
            main.screen.blit(txt, main.game.base.revenus)
        elif (main.game.base.up_recolte.collidepoint(a)) :
            txt = style.render("Coût : " + str(main.game.ressources ** 3), 1, (0,0,0))
            main.screen.blit(txt, main.game.base.up_recolte)
        elif (main.game.base.down_recolte.collidepoint(a)) :
            txt = style.render("Coût : " + str(1 + (3000 - main.game.base.recoltex) * 10), 1, (0,0,0))
            main.screen.blit(txt, main.game.base.down_recolte)
        elif (main.game.base.plus_vie_rect.collidepoint(pygame.mouse.get_pos())):
            txt = (pygame.font.SysFont("arial",30,bold=True)).render("Coût : "+str(main.game.base.health_ajout**2),1,(0,0,0))
            main.screen.blit(txt, (main.game.base.plus_vie_rect.x, main.game.base.plus_vie_rect.y + 150))
            txt = (pygame.font.SysFont("arial" , 30, bold=True)).render("Augmente la base de vie de 1" , 1, (0,0,0))
            main.screen.blit(txt, (main.game.base.plus_vie_rect.x, main.game.base.plus_vie_rect.y + 200))
        elif (main.game.base.fois_vie_rect.collidepoint(pygame.mouse.get_pos())):
            txt = (pygame.font.SysFont("arial",30,bold=True)).render("Coût : "+str(2**main.game.base.health_multiply),1,(0,0,0))
            main.screen.blit(txt, (main.game.base.fois_vie_rect.x, main.game.base.fois_vie_rect.y + 150))
            txt = (pygame.font.SysFont("arial" , 30, bold=True)).render("Augmente la multiplication de vie de 0.1", 1, (0,0,0))
            main.screen.blit(txt, (main.game.base.fois_vie_rect.x, main.game.base.fois_vie_rect.y + 200))
        elif (main.game.base.help_vie_rect.collidepoint(pygame.mouse.get_pos())):
            txt = (pygame.font.SysFont("arial",30,bold=True)).render("La vie de votre base est égale à :",1,(0,0,0))
            main.screen.blit(txt, (main.game.base.help_vie_rect.x - 200, main.game.base.help_vie_rect.y + 100))
            txt = "(100 * epoque^5 + ajout de vie) x (multiplication de vie + 1)"
            txt = (pygame.font.SysFont("arial",30,bold=True)).render(txt,1,(0,0,0))
            main.screen.blit(txt, (main.game.base.help_vie_rect.x - 200, main.game.base.help_vie_rect.y + 150))
        elif (main.game.base.ameliorer_rect.collidepoint(pygame.mouse.get_pos())):
            st = pygame.font.SysFont("arial",30,bold=True)
            txt = (st.render("Coût : " + str(99 + (main.game.base.epoque_nbr + 1) ** 8),1,(0,0,0)))
            main.screen.blit(txt, (main.game.base.ameliorer_rect.x + 460, main.game.base.ameliorer_rect.y + 35))
            txt = (st.render("Augmente la base de vie",1,(0,0,0)))
            main.screen.blit(txt, (main.game.base.ameliorer_rect.x + 460, main.game.base.ameliorer_rect.y + 70))
            txt = (st.render("Permet de nouvelles améliorations",1,(0,0,0)))
            main.screen.blit(txt, (main.game.base.ameliorer_rect.x + 460, main.game.base.ameliorer_rect.y + 110))

        pygame.display.flip() # Met à jour la fenêtre

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
                if (main.game.base.fermer_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "fermer"
                elif (main.game.base.plus_vie_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "plus_vie"
                elif (main.game.base.fois_vie_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "fois_vie"
                elif (main.game.base.ameliorer_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "ameliorer"
                elif (main.game.base.revenus.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "revenus"
                elif (main.game.base.up_recolte.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "up_recolte"
                elif (main.game.base.down_recolte.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "down_recolte"
                # Laché
            elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1) :
                if (main.game.base.fermer_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "fermer") :
                    main.pressed_button[event.button] = ""
                    return True
                elif (main.game.base.plus_vie_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "plus_vie") :
                    main.pressed_button[event.button] = ""
                    if (main.game.monnaie >= main.game.base.health_ajout ** 2) :
                        main.game.monnaie -= main.game.base.health_ajout ** 2
                        main.game.base.health_ajout += 1
                elif (main.game.base.fois_vie_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "fois_vie") :
                    main.pressed_button[event.button] = ""
                    if (main.game.monnaie >= 2**main.game.base.health_multiply) :
                        main.game.monnaie -= 2**main.game.base.health_multiply
                        main.game.base.health_multiply += 1
                elif (main.game.base.revenus.collidepoint(event.pos) and main.pressed_button[event.button] == "revenus") :
                    main.pressed_button[event.button] = ""
                    if (2 * (main.game.base.epoque_nbr + 1) >= main.game.revenus_passifs and main.game.monnaie >= (1 + main.game.revenus_passifs) ** 4) :
                        main.game.monnaie -= (1 + main.game.revenus_passifs) ** 4
                        main.game.revenus_passifs += 1
                elif (main.game.base.up_recolte.collidepoint(event.pos) and main.pressed_button[event.button] == "up_recolte") :
                    main.pressed_button[event.button] = ""
                    if (5 * (main.game.base.epoque_nbr + 1) >= main.game.ressources and main.game.monnaie >= main.game.ressources ** 3) :
                        main.game.monnaie -= main.game.ressources ** 3
                        main.game.ressources += 1
                elif (main.game.base.down_recolte.collidepoint(event.pos) and main.pressed_button[event.button] == "down_recolte") :
                    main.pressed_button[event.button] = ""
                    if (main.game.base.recoltex > 2900 - 100 * main.game.base.epoque_nbr and main.game.monnaie >= (1 + (3000 - main.game.base.recoltex) * 10)) :
                        main.game.monnaie -= (1 + (3000 - main.game.base.recoltex) * 10)
                        main.game.base.recoltex -= 10
                elif (main.game.base.ameliorer_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "ameliorer") :
                    main.pressed_button[event.button] = ""
                    if (main.game.base.epoque_nbr < 5) :
                        (c_xp, c_or) = (main.game.xp_suiv, 99 + (main.game.base.epoque_nbr + 1) ** 8)
                        if (main.game.xp >= c_xp and main.game.monnaie >= c_or) :
                            a = main.game_confirmer ("Coût : "+ main.game.transforme_nbr(c_xp) + " xp et " + main.game.transforme_nbr(c_or) + " or")
                            if (a) :
                                main.game.evoluer (c_xp, c_or)
                                return True




