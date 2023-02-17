"""
Manage the game
"""

import pygame
import time
from p_base import *
from p_emplacement import *
from p_soldats import *
from p_ennemi import *


class Timer :

    def __init__ (self) :
        self.temps = 0
        self.temps0 = 0
        self.temps1 = time.time()
        self.stop = False

    def actualise (self, vitesse) :
        if (self.stop) :
            self.temps1 = time.time()
            self.stop = False
        else :
            t = time.time()
            self.temps0 += ((t - self.temps1) * vitesse)
            self.temps1 = t
            self.temps = int(self.temps0)

    def restart (self) :
        self.temps = 0
        self.temps0 = 0
        self.temps1 = int(time.time())


    def pause (self, vitesse) :
        if (not self.stop) :
            self.actualise (vitesse)
            self.stop = True


##

class Game :

    def __init__ (self, screen) :
        # Graphiques
        self.background = pygame.image.load("../assets/map.jpg")
        self.background_rect = self.background.get_rect()
        self.transforme_bg(screen)
        self.background_rect.x = 0
        self.background_rect.y = 0

        self.bandeau_monnaie = pygame.transform.scale(pygame.image.load("../assets/monnaie.png"), (200, 100))
        self.bandeau_monnaie_rect = self.bandeau_monnaie.get_rect()
        self.bandeau_monnaie_rect.x = 20
        self.bandeau_monnaie_rect.y = 10

        self.bandeau_xp = pygame.transform.scale(pygame.image.load("../assets/xp.png"), (100, 100))
        self.bandeau_xp_rect = self.bandeau_xp.get_rect()
        self.bandeau_xp_rect.x = 240 + self.bandeau_monnaie_rect.width
        self.bandeau_xp_rect.y = 10

        self.bandeau_tetes = pygame.transform.scale(pygame.image.load("../assets/tetes.png"), (300, 100))
        self.bandeau_tetes_rect = self.bandeau_tetes.get_rect()
        self.bandeau_tetes_rect.x = 20 + self.bandeau_xp_rect.x + self.bandeau_xp_rect.width
        self.bandeau_tetes_rect.y = 10

        self.base = Base (screen)
        self.rect_vie = pygame.rect.Rect(600, 250, 500, 50)

        self.ennemi = Ennemi (screen, self.background_rect)
        self.rect_ennemi = pygame.rect.Rect(5300, 250, 500, 50)

        # Variables
        self.timer = Timer()
        self.new_game(screen)
        self.xp_max = 100000000

    def new_game (self, screen) :
        self.timer.restart()
        self.monnaie = 200
        self.revenus_passifs = 1
        self.ressources = 1
        self.temps = 0
        self.xp = 0
        self.xp_suiv = 1000
        self.population = 0
        self.population_max = 50
        self.vitesse = 1
        self.deplacement = 0
        self.emplacements = [Emplacement(screen, "vide") for i in range (9)]
        self.soldats = pygame.sprite.Group()
        self.pieces = pygame.sprite.Group()
        self.base.new()
        self.ennemi.new(screen)

    def evoluer (self, c_xp, c_or) :
        self.xp -= c_xp
        self.monnaie -= c_or
        self.base.epoque_nbr += 1
        self.xp_suiv = self.xp_suiv * 10
        self.base.health_base = 100 * (self.base.epoque_nbr + 1) ** 5
        self.base.image = pygame.transform.scale(pygame.image.load("../assets/base/"+str(self.base.epoque_nbr)+".png"), (750, 557))
        self.base.recolte = pygame.transform.scale(pygame.image.load("../assets/base/"+str(self.base.epoque_nbr)+"_recolte.png"), (100, 100))

    def transforme_bg (self, screen) :
        h = screen.get_height()
        L = self.background_rect.width * h // self.background_rect.height
        self.background = pygame.transform.scale(self.background, (L, h))

    def transforme_nbr (self, n) :
        if (n >= 1000000) :
            a = n // 1000000
            b = (n - 1000000 * a) // 100000
            if (a < 100 and b != 0) :
                txt = str(a) + "," + str(b) + ".m"
            else :
                txt = str(a) + ".m"
        elif (n >= 1000) :
            a = n // 1000
            b = (n - 1000 * a) // 100
            if (a < 100 and b != 0) :
                txt = str(a) + "," + str(b) + ".K"
            else :
                txt = str(a) + ".K"
        else :
            txt = str(n)
        return txt

    def txt_xp (self) :
        t1 = self.transforme_nbr (self.xp)
        t2 = self.transforme_nbr (self.xp_suiv)
        return (t1 + " / " + t2)

    def damage_soldat (self, soldat, attaque) :
        soldat.health -= attaque
        if (soldat.health) <= 0 :
            self.soldats.remove(soldat)
            self.population -= 1

    def actualise (self, main) :
        # Spawn des soldats
        for emplacement in self.emplacements :
            if (emplacement.nom == "monnaie") :
                a = 0
            elif (emplacement.nom == "recolte") :
                a = 0
            elif (emplacement.nom != "vide" and self.population < self.population_max and self.monnaie > emplacement.epoque) :
                emplacement.new_spawn (main.screen, self)

        # Actions des soldats
        for soldat in self.soldats :
            a = soldat.agir (main)
            if (a != True) :
                if (type(a) == tuple and len(a) == 3) :
                    self.pieces.add(Piece(a[0], a[1], a[2]))

        # Divers actions
        self.base.calcul_health()
        if (self.temps < self.timer.temps) :
            self.temps = self.timer.temps
            self.monnaie += self.revenus_passifs

    def afficher (self, screen) :
        # Réglage des extremums
        x = self.deplacement
        if (x > 0) :
            x = 0
        elif (x < screen.get_width() - self.background_rect.width + 1000) :
            x = screen.get_width() - self.background_rect.width + 1000
        self.deplacement = x
        screen.blit(self.background, (self.background_rect.x + self.deplacement, self.background_rect.y))

        self.afficher_bandeau (screen)

        # Player
        self.base.rect.x = self.base.rectx + self.deplacement
        screen.blit(self.base.image, self.base.rect)
        self.base.recolte_rect.x = self.base.recoltex + self.deplacement
        screen.blit(self.base.recolte, self.base.recolte_rect)
        self.rect_vie.x = 600 + self.deplacement
        pygame.draw.rect(screen, (150, 150, 150), self.rect_vie)
        pygame.draw.rect(screen, (0, 255, 0), [600 + self.deplacement, 250, 500 * self.base.health // self.base.max_health, 50])
        for i in range (9) :
            self.emplacements[i].afficher(screen, self.deplacement, i % 3, i // 3)
        for soldat in self.soldats :
            soldat.afficher (screen)


        # Monster
        self.ennemi.rect.x = self.ennemi.rectx + self.deplacement
        screen.blit(self.ennemi.image, self.ennemi.rect)
        self.rect_ennemi.x = 5300 + self.deplacement
        pygame.draw.rect(screen, (150, 150, 150), self.rect_ennemi)
        pygame.draw.rect(screen, (0, 255, 0), [self.rect_ennemi.x, self.rect_ennemi.y, 500 * self.ennemi.health // self.ennemi.max_health, 50])
        for monstre in self.ennemi.soldats :
            monstre.afficher (screen)
        for defense in self.ennemi.defenses :
            defense.afficher (screen)



    def afficher_bandeau (self, screen) :
        pygame.draw.rect(screen, (150, 150, 150), [5, 5, 900, 110])

        screen.blit(self.bandeau_monnaie, self.bandeau_monnaie_rect)
        txt = (pygame.font.SysFont("arial" , 45, bold=True)).render(self.transforme_nbr(self.monnaie), 1, (0,0,0))
        screen.blit(txt, (25, 40))

        screen.blit(self.bandeau_xp, self.bandeau_xp_rect)
        pygame.draw.rect(screen, (0, 255, 255), [40 + self.bandeau_monnaie_rect.width, 35, 200, 50])
        pygame.draw.rect(screen, (0, 0, 255), [40 + self.bandeau_monnaie_rect.width, 35, min(200, (200 * self.xp // self.xp_suiv)), 50])
        txt = (pygame.font.SysFont("arial" , 45, bold=True)).render(self.txt_xp(), 1, (0,0,0))
        screen.blit(txt, (60 + self.bandeau_monnaie_rect.width, 35))

        screen.blit(self.bandeau_tetes, self.bandeau_tetes_rect)
        txt = (pygame.font.SysFont("arial" , 45, bold=True)).render(str(self.population) + " / " + str(self.population_max), 1, (0,0,0))
        screen.blit(txt, (30 + self.bandeau_tetes_rect.x, 40))


# _______________________________________________________________________________________________________#

def jeu (main) :
    while (True) :
        # Déplacement de la map
        (a, b) = pygame.mouse.get_pos()
        if (type(main.pressed_button[1]) == tuple) :
            x = main.game.deplacement + a - main.pressed_button[1][0]
            main.game.deplacement = x
            main.pressed_button[1] = (a, main.pressed_button[1][1])
        elif (a < 100) :
            main.game.deplacement += (100 - a) // 5
        elif (a > main.screen.get_width() - 50) :
            main.game.deplacement -= (100 + a - main.screen.get_width()) // 5

        # Mises à jour
        main.game.timer.actualise(main.game.vitesse)
        main.game.actualise (main)
        main.game.ennemi.actualise(main)

        if (main.game.base.health <= 0) :
            main.etape = 4
            return True
        elif (main.game.ennemi.health <= 0) :
            main.etape = 5
            return True

        # Affichage de la map
        main.game.afficher (main.screen)

        for piece in main.game.ennemi.pieces :
            piece.afficher (main.screen, main.game.deplacement)
            if (piece.nbr > main.fps) :
                main.game.ennemi.pieces.remove(piece)
        for piece in main.game.pieces :
            piece.afficher (main.screen, main.game.deplacement)
            if (piece.nbr > main.fps) :
                main.game.ennemi.pieces.remove(piece)

        # Détails du bandeau
        if (main.game.bandeau_monnaie_rect.collidepoint((a, b))) :
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Monnaie : " + str(main.game.monnaie), 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_monnaie_rect.x, main.game.bandeau_monnaie_rect.y + 100))
        elif (main.game.bandeau_xp_rect.collidepoint((a, b))):
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("XP : " + str(main.game.xp), 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_xp_rect.x, main.game.bandeau_xp_rect.y + 100))
        elif (main.game.bandeau_tetes_rect.collidepoint((a, b))):
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Soldats : 1 - Outils : 2", 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_tetes_rect.x, main.game.bandeau_tetes_rect.y + 100))
        elif (main.game.rect_vie.collidepoint((a, b))):
            txt = "Vie : " + str(main.game.base.health) + " / " + str(main.game.base.max_health)
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render(txt, 1, (0,0,0))
            main.screen.blit(txt, (600 + main.game.deplacement, 200))
        elif (main.game.rect_ennemi.collidepoint((a, b))):
            txt = "Vie : " + str(main.game.ennemi.health) + " / " + str(main.game.ennemi.max_health)
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render(txt, 1, (0,0,0))
            main.screen.blit(txt, (5300 + main.game.deplacement, 200))

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
                    main.game.timer.pause (main.game.vitesse)
                    return (main.menu.menu(main))
            elif (event.type == pygame.KEYUP) :
                main.pressed_button[event.key] = False

            # Souris bouton gauche
                # Appuyé
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) :
                if (test_emplacements(main, event.pos, 0)) :
                    a = 0
                elif (main.game.base.rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "base"
                elif (main.pressed_button[event.button] == "") :
                    main.pressed_button[event.button] = event.pos
                # Laché
            elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1) :
                if (test_emplacements(main, event.pos, 1)) :
                    a = 0
                elif (main.game.base.rect.collidepoint(event.pos) and main.pressed_button[event.button] == "base") :
                    main.pressed_button[event.button] = ""
                    main.game.timer.pause (main.game.vitesse)
                    a = game_base (main)
                else :
                    main.pressed_button[event.button] = ""

##

def test_emplacements (main, pos, k) :
    if (k == 0) :
        for i in range (9) :
            if (main.game.emplacements[i].rect.collidepoint(pos)) :
                main.pressed_button[1] = str(i)
                return True
    else :
        for i in range (9) :
            if (main.game.emplacements[i].rect.collidepoint(pos) and main.pressed_button[1] == str(i)) :
                main.pressed_button[1] = ""
                main.game.timer.pause (main.game.vitesse)
                game_emplacement(main, main.game.emplacements[i])
                return True