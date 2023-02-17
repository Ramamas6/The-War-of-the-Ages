import pygame
from p_soldats import *
from p_troupes_ennemi import *


class Emplacement () :

    def __init__ (self, screen, nom) :
        # Variables
        self.nom = nom
        self.epoque = 0
        self.cout_total = 100

        self.attaque = 0
        self.attaque_plus = 0
        self.attaque_fois = 0

        self.health = 0
        self.health_plus = 0
        self.health_fois = 0

        self.vitesse = 0
        self.respawn = 0
        self.spawn = True

        # Achats

        self.rect_usine = pygame.rect.Rect(50, 200, 450, 188)
        self.txt_rect_usine = (pygame.font.SysFont("arial" , 50, bold=True)).render("Production d'or (100)", 1, (0,0,0))
        self.rect_recolteur = pygame.rect.Rect(540, 200, 450, 188)
        self.txt_rect_recolteur = (pygame.font.SysFont("arial" , 50, bold=True)).render("Récolteurs (50)", 1, (0,0,0))
        self.rect_combattant = pygame.rect.Rect(1030, 200, 450, 188)
        self.txt_rect_combattant = (pygame.font.SysFont("arial" , 50, bold=True)).render("combattants (50)", 1, (0,0,0))
        self.rect_assassin = pygame.rect.Rect(50, 420, 450, 188)
        self.txt_rect_assassin = (pygame.font.SysFont("arial" , 50, bold=True)).render("Assassins (100)", 1, (0,0,0))
        self.rect_tireur = pygame.rect.Rect(540, 420, 450, 188)
        self.txt_rect_tireur = (pygame.font.SysFont("arial" , 50, bold=True)).render("Tireur (100)", 1, (0,0,0))
        self.rect_snipeur = pygame.rect.Rect(1030, 420, 450, 188)
        self.txt_rect_snipeur = (pygame.font.SysFont("arial" , 50, bold=True)).render("Snipeur (150)", 1, (0,0,0))
        self.rect_tank = pygame.rect.Rect(50, 640, 450, 188)
        self.txt_rect_tank = (pygame.font.SysFont("arial" , 50, bold=True)).render("Tank (250)", 1, (0,0,0))
        self.rect_lanceur = pygame.rect.Rect(540, 640, 450, 188)
        self.txt_rect_lanceur = (pygame.font.SysFont("arial" , 50, bold=True)).render("Lanceur (250)", 1, (0,0,0))
        self.rect_rapide = pygame.rect.Rect(1030, 640, 450, 188)
        self.txt_rect_rapide = (pygame.font.SysFont("arial" , 50, bold=True)).render("Véhicule rapide (250)", 1, (0,0,0))

        # Graphiques

        self.image = pygame.transform.scale(pygame.image.load("../assets/armee/vide/0_base.png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rect0 = self.image.get_rect()
        self.rect0.x = 50
        self.rect0.y = screen.get_height() - self.rect.height - 50

        self.pose = pygame.transform.scale(pygame.image.load("../assets/armee/vide/0_pose.png"), (200, 200))
        self.pose_rect = self.pose.get_rect()
        self.pose_rect.x = screen.get_width() - 210
        self.pose_rect.y = 420

        self.fermer = pygame.transform.scale(pygame.image.load("../assets/fermer.png"), (100, 100))
        self.fermer_rect = self.fermer.get_rect()
        self.fermer_rect.x = screen.get_width() - 160
        self.fermer_rect.y = 30

        self.vendre = pygame.transform.scale(pygame.image.load("../assets/armee/vendre.png"), (450, 188))
        self.vendre_rect = self.vendre.get_rect()
        self.vendre_rect.x = screen.get_width() - 460
        self.vendre_rect.y = screen.get_height() - 200

        self.ameliorer_oui = pygame.transform.scale(pygame.image.load("../assets/ameliorer_oui.png"), (450, 188))
        self.ameliorer_non = pygame.transform.scale(pygame.image.load("../assets/ameliorer_non.png"), (450, 188))
        self.ameliorer_rect = self.ameliorer_oui.get_rect()
        self.ameliorer_rect.x = 10
        self.ameliorer_rect.y = self.vendre_rect.y

        self.icon_vie = pygame.transform.scale(pygame.image.load("../assets/armee/coeur.png"), (100, 100))
        self.icon_piece = pygame.transform.scale(pygame.image.load("../assets/piece.png"), (100, 100))
        self.icon_vie_rect = self.icon_vie.get_rect()
        self.icon_vie_rect.x = 50
        self.icon_vie_rect.y = 150
        self.vie_plus_rect = pygame.rect.Rect(50, 260, 100, 100)
        self.vie_fois_rect = pygame.rect.Rect(180, 260, 100, 100)

        self.icon_attaque = pygame.transform.scale(pygame.image.load("../assets/armee/attaque.png"), (100, 100))
        self.icon_attaque_rect = self.icon_attaque.get_rect()
        self.icon_attaque_rect.x = screen.get_width() // 2 - 30
        self.icon_attaque_rect.y = 150
        self.attaque_plus_rect = pygame.rect.Rect(screen.get_width() // 2 - 30, 260, 100, 100)
        self.attaque_fois_rect = pygame.rect.Rect(screen.get_width() // 2 + 100, 260, 100, 100)

        self.icon_respawn = pygame.transform.scale(pygame.image.load("../assets/armee/respawn.png"), (100, 100))
        self.icon_respawn_rect = self.icon_respawn.get_rect()
        self.icon_respawn_rect.x = 50
        self.icon_respawn_rect.y = 430
        self.respawn_rect = pygame.rect.Rect(50, 550, 100, 100)

        self.icon_vitesse = pygame.transform.scale(pygame.image.load("../assets/armee/vitesse.png"), (100, 100))
        self.icon_vitesse_rect = self.icon_vitesse.get_rect()
        self.icon_vitesse_rect.x = screen.get_width() // 2 - 30
        self.icon_vitesse_rect.y = 430
        self.vitesse_rect = pygame.rect.Rect(screen.get_width() // 2 - 30, 550, 100, 100)

        self.icon_fois_oui = pygame.transform.scale(pygame.image.load("../assets/armee/fois_oui.png"), (100, 100))
        self.icon_fois_non = pygame.transform.scale(pygame.image.load("../assets/armee/fois_non.png"), (100, 100))
        self.icon_fois_rect = self.icon_fois_oui.get_rect()
        self.icon_fois_rect.x = 50
        self.icon_fois_rect.y = 150

        self.icon_plus_oui = pygame.transform.scale(pygame.image.load("../assets/armee/plus_oui.png"), (100, 100))
        self.icon_plus_non = pygame.transform.scale(pygame.image.load("../assets/armee/plus_non.png"), (100, 100))
        self.icon_plus_rect = self.icon_plus_oui.get_rect()
        self.icon_plus_rect.x = 100
        self.icon_plus_rect.y = 150



    def new_spawn (self, screen, game) :
        if (self.nom == "usine") :
            if (self.spawn and game.timer.temps0 - self.temps >= self.respawn) :
                self.temps = game.timer.temps0
                game.monnaie += self.quantitee
                game.pieces.add (Piece(self.rect.x + 10, self.rect.y, self.quantitee))
        else :
            if (self.spawn and game.timer.temps0 - self.temps >= self.respawn) :
                game.soldats.add(Soldat(self, screen))
                self.temps = game.timer.temps0
                game.population += 1
                game.monnaie -= (self.epoque + 1)

    def achat (self, nom, timer) :
        self.nom = nom
        self.temps = timer.temps0
        self.actualise()
        if (nom == "usine") :
            self.quantitee = 1
            self.quantitee_max = 10
            self.respawn = 10
            self.respawn_min = 8
        elif (nom == "recolteur") :
            self.attaque = 5
            self.health = 50
            self.vitesse = 1
            self.vitesse_max = 15
            self.respawn = 5
            self.respawn_min = 1
        elif (nom == "combattant") :
            self.attaque = 10
            self.health = 100
            self.vitesse = 2
            self.vitesse_max = 15
            self.respawn = 5
            self.respawn_min = 2
        elif (nom == "assassin") :
            self.attaque = 15
            self.health = 50
            self.vitesse = 4
            self.vitesse_max = 25
            self.respawn = 7
            self.respawn_min = 3
        elif (nom == "tireur") :
            self.attaque = 10
            self.health = 100
            self.vitesse = 1
            self.vitesse_max = 20
            self.respawn = 7
            self.respawn_min = 3
        elif (nom == "snipeur") :
            self.attaque = 10
            self.health = 100
            self.vitesse = 1
            self.vitesse_max = 15
            self.respawn = 8
            self.respawn_min = 4
        elif (nom == "tank") :
            self.attaque = 5
            self.health = 400
            self.vitesse = 1
            self.vitesse_max = 5
            self.respawn = 15
            self.respawn_min = 10
        elif (nom == "tireur") :
            self.attaque = 10
            self.health = 100
            self.vitesse = 1
            self.vitesse_max = 10
            self.respawn = 15
            self.respawn_min = 10
        elif (nom == "rapide") :
            self.attaque = 10
            self.health = 200
            self.vitesse = 6
            self.vitesse_max = 30
            self.respawn = 13
            self.respawn_min = 8



    def actualise (self) :
        self.image = pygame.transform.scale(pygame.image.load("../assets/armee/"+self.nom+"/"+str(self.epoque)+"_base.png"), (100, 100))
        self.pose = pygame.transform.scale(pygame.image.load("../assets/armee/"+self.nom+"/"+str(self.epoque)+"_pose.png"), (200, 200))

    def reset (self) :
        self.nom = "vide"
        self.attaque = 0
        self.attaque_fois = 0
        self.attaque_plus = 0
        self.health = 0
        self.health_fois = 0
        self.health_plus = 0
        self.vitesse = 0
        self.respawn = 0
        self.cout_total = 0
        self.epoque = 0
        self.actualise()

    def upgrade (self) :
        self.epoque += 1
        if (self.nom == "vide") :
            return False
        elif (self.nom == "usine") :
            self.quantitee_max += 10
            self.respawn_min -= 1
        else :
            self.attaque = int (self.attaque * (self.epoque + 1) / self.epoque)
            self.health = int (self.health * (self.epoque + 1) / self.epoque)
        self.actualise()

    def afficher (self, screen, d, a, b) :
        self.rect.x = self.rect0.x + d + 150 * a + 50 * b
        self.rect.y = self.rect0.y - 150 * b
        screen.blit(self.image, self.rect)

    def calcul_vie (self) :
        return (int ((self.health + self.health_plus) * (1 + 0.1 * self.health_fois)))

    def calcul_attaque (self) :
        return (int ((self.attaque + self.attaque_plus) * (1 + 0.1 * self.attaque_fois)))

    def afficher_menu (self, main) :
        # Général
        pygame.draw.rect(main.screen, (150, 150, 150), [5, 5, main.screen.get_width() - 10, main.screen.get_height() - 10])
        main.screen.blit(self.fermer, self.fermer_rect)

        # Vide
        if (self.nom == "vide"):
            main.screen.blit(self.ameliorer_oui, self.rect_usine)
            main.screen.blit(self.txt_rect_usine, (self.rect_usine.x + 20, self.rect_usine.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_recolteur)
            main.screen.blit(self.txt_rect_recolteur, (self.rect_recolteur.x + 70, self.rect_recolteur.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_combattant)
            main.screen.blit(self.txt_rect_combattant, (self.rect_combattant.x + 65, self.rect_combattant.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_assassin)
            main.screen.blit(self.txt_rect_assassin, (self.rect_assassin.x + 70, self.rect_assassin.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_tireur)
            main.screen.blit(self.txt_rect_tireur, (self.rect_tireur.x + 105, self.rect_tireur.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_snipeur)
            main.screen.blit(self.txt_rect_snipeur, (self.rect_snipeur.x + 95, self.rect_snipeur.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_tank)
            main.screen.blit(self.txt_rect_tank, (self.rect_tank.x + 110, self.rect_tank.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_lanceur)
            main.screen.blit(self.txt_rect_lanceur, (self.rect_lanceur.x + 90, self.rect_lanceur.y + 65))

            main.screen.blit(self.ameliorer_oui, self.rect_rapide)
            main.screen.blit(self.txt_rect_rapide, (self.rect_rapide.x + 20, self.rect_rapide.y + 65))
        # Non vide
        else :
            img = pygame.transform.scale(self.image, (200, 200))
            main.screen.blit(img, (main.screen.get_width() - 230, 180))
            main.screen.blit(self.pose, self.pose_rect)
            main.screen.blit(self.vendre, self.vendre_rect)
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Vendre : " + str(int(self.cout_total * 0.8)), 1, (0,0,0))
            main.screen.blit(txt, (self.vendre_rect.x + 20, self.vendre_rect.y + 60))
            if (main.game.base.epoque_nbr > self.epoque and main.game.monnaie >= 99 + (self.epoque + 1) ** 7) :
                main.screen.blit(self.ameliorer_oui, self.ameliorer_rect)
            else :
                main.screen.blit(self.ameliorer_non, self.ameliorer_rect)
            txt = (pygame.font.SysFont("arial" , 50, bold=True)).render("Améliorer : " + str(99 + (self.epoque + 1) ** 7), 1, (0,0,0))
            main.screen.blit(txt, (self.ameliorer_rect.x + 20, self.ameliorer_rect.y + 60))

            if (self.respawn > self.respawn_min and main.game.monnaie >= int ((- 100 / (self.respawn_min - self.respawn)) ** 2)) :
                main.screen.blit(self.icon_plus_oui, self.respawn_rect)
            else :
                main.screen.blit(self.icon_plus_non, self.respawn_rect)

            main.screen.blit(self.icon_respawn, self.icon_respawn_rect)
            txt = (pygame.font.SysFont("arial" , 100, bold=True)).render(str(self.respawn), 1, (0,0,0))
            main.screen.blit(txt, (self.icon_respawn_rect.x + 150, self.icon_respawn_rect.y))

            if (self.nom == "usine") :
                main.screen.blit(self.icon_piece, self.icon_vie_rect)
                txt = (pygame.font.SysFont("arial" , 100, bold=True)).render(str(self.quantitee), 1, (0,0,0))
                main.screen.blit(txt, (self.icon_vie_rect.x + 150, self.icon_vie_rect.y))

                if (self.quantitee < self.quantitee_max and main.game.monnaie >= (1 + self.quantitee) ** 4) :
                    main.screen.blit(self.icon_plus_oui, self.vie_plus_rect)
                else :
                    main.screen.blit(self.icon_plus_non, self.vie_plus_rect)
            else :
                main.screen.blit(self.icon_vie, self.icon_vie_rect)
                txt = (pygame.font.SysFont("arial" , 100, bold=True)).render(str(self.calcul_vie()), 1, (0,0,0))
                main.screen.blit(txt, (self.icon_vie_rect.x + 150, self.icon_vie_rect.y))

                main.screen.blit(self.icon_attaque, self.icon_attaque_rect)
                txt = (pygame.font.SysFont("arial" , 100, bold=True)).render(str(self.calcul_attaque()), 1, (0,0,0))
                main.screen.blit(txt, (self.icon_attaque_rect.x + 150, self.icon_attaque_rect.y))

                main.screen.blit(self.icon_vitesse, self.icon_vitesse_rect)
                txt = (pygame.font.SysFont("arial" , 100, bold=True)).render(str(self.vitesse), 1, (0,0,0))
                main.screen.blit(txt, (self.icon_vitesse_rect.x + 150, self.icon_vitesse_rect.y))

                if (self.health_plus < self.health and main.game.monnaie >= (1 + self.health_plus) ** 2) :
                    main.screen.blit(self.icon_plus_oui, self.vie_plus_rect)
                else :
                    main.screen.blit(self.icon_plus_non, self.vie_plus_rect)
                if (self.health_fois < (10 * self.epoque + 10) / 2 and main.game.monnaie >= 1 + self.health_fois ** 4) :
                    main.screen.blit(self.icon_fois_oui, self.vie_fois_rect)
                else :
                    main.screen.blit(self.icon_fois_non, self.vie_fois_rect)

                if (self.attaque_plus < self.attaque and main.game.monnaie >= (1 + self.attaque_plus) ** 2) :
                    main.screen.blit(self.icon_plus_oui, self.attaque_plus_rect)
                else :
                    main.screen.blit(self.icon_plus_non, self.attaque_plus_rect)
                if (self.attaque_fois < ((10 * self.epoque + 10) / 2) and main.game.monnaie >= 1 + self.attaque_fois ** 4) :
                    main.screen.blit(self.icon_fois_oui, self.attaque_fois_rect)
                else :
                    main.screen.blit(self.icon_fois_non, self.attaque_fois_rect)

                if (self.vitesse < self.vitesse_max and main.game.monnaie >= int((self.vitesse_max - self.vitesse) ** 2)):
                    main.screen.blit(self.icon_plus_oui, self.vitesse_rect)
                else :
                    main.screen.blit(self.icon_plus_non, self.vitesse_rect)

##

def game_emplacement (main, emplacement) :

    while (True) :
        emplacement.afficher_menu (main)
        main.game.afficher_bandeau(main.screen)

        # Détails du bandeau
        a = pygame.mouse.get_pos()
        style = (pygame.font.SysFont("arial" , 50, bold=True))
        if (main.game.bandeau_monnaie_rect.collidepoint(a)):
            txt = style.render("Monnaie : " + str(main.game.monnaie), 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_monnaie_rect.x, main.game.bandeau_monnaie_rect.y + 100))
        elif (main.game.bandeau_xp_rect.collidepoint(a)):
            txt = style.render("XP : " + str(main.game.xp), 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_xp_rect.x, main.game.bandeau_xp_rect.y + 100))
        elif (main.game.bandeau_tetes_rect.collidepoint(a)):
            txt = style.render("Soldats : 1 - Outils : 2", 1, (0,0,0))
            main.screen.blit(txt, (main.game.bandeau_tetes_rect.x, main.game.bandeau_tetes_rect.y + 100))
        elif (emplacement.nom == "vide") :
            if (emplacement.rect_usine.collidepoint(a)) :
                txt = style.render("Usine de production d'or automatique", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_usine.x, emplacement.rect_usine.y - 50))
            elif (emplacement.rect_recolteur.collidepoint(a)) :
                txt = style.render("Envoie des personnages récolter automatiquement de l'or", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_recolteur.x - 300, emplacement.rect_recolteur.y - 50))
            elif (emplacement.rect_combattant.collidepoint(a)) :
                txt = style.render("Des combattants classiques (attaque et vie standard)", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_combattant.x - 550, emplacement.rect_combattant.y - 50))
            elif (emplacement.rect_assassin.collidepoint(a)) :
                txt = style.render("Des combattants forts et rapides mais peu résistants", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_assassin.x, emplacement.rect_assassin.y - 47))
            elif (emplacement.rect_tireur.collidepoint(a)) :
                txt = style.render("Des soldats qui tirent de loin", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_tireur.x - 50, emplacement.rect_tireur.y - 47))
            elif (emplacement.rect_snipeur.collidepoint(a)) :
                txt = style.render("Des soldats qui tirent de très loin, mais faibles au corps à corps", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_snipeur.x - 750, emplacement.rect_snipeur.y - 47))
            elif (emplacement.rect_tank.collidepoint(a)) :
                txt = style.render("Des machines de guerre lentes mais très résistantes", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_tank.x, emplacement.rect_tank.y - 47))
            elif (emplacement.rect_lanceur.collidepoint(a)) :
                txt = style.render("Des machines tirant de très loin, mais inefficaces au corps à corps", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_lanceur.x - 400, emplacement.rect_lanceur.y - 47))
            elif (emplacement.rect_rapide.collidepoint(a)) :
                txt = style.render("Des machines de guerres rapides", 1, (0,0,0))
                main.screen.blit(txt, (emplacement.rect_rapide.x - 200, emplacement.rect_rapide.y - 47))
        elif (emplacement.respawn_rect.collidepoint(a)):
            if (emplacement.respawn > emplacement.respawn_min) :
                txt = style.render(str(int ((- 100 / (emplacement.respawn_min - emplacement.respawn)) ** 2)), 1, (0,0,0))
            else :
                txt = style.render("Non achetable", 1, (0,0,0))
            main.screen.blit(txt, emplacement.respawn_rect)
        elif (emplacement.nom == "usine") :
            if (emplacement.vie_plus_rect.collidepoint(a)):
                if (emplacement.quantitee < emplacement.quantitee_max) :
                    txt = style.render(str((1 + emplacement.quantitee) ** 4), 1, (0,0,0))
                else :
                    txt = style.render("Non achetable", 1, (0,0,0))
                main.screen.blit(txt, emplacement.vie_plus_rect)
        else :
            if (emplacement.vie_plus_rect.collidepoint(a)):
                if (emplacement.health_plus < emplacement.health) :
                    txt = style.render(str((1 + emplacement.health_plus) ** 2), 1, (0,0,0))
                else :
                    txt = style.render("Non achetable", 1, (0,0,0))
                main.screen.blit(txt, emplacement.vie_plus_rect)
            elif (emplacement.vie_fois_rect.collidepoint(a)):
                if (emplacement.health_fois < (10 * emplacement.epoque + 10) / 2) :
                    txt = style.render(str(1 + emplacement.health_fois ** 4), 1, (0,0,0))
                else :
                    txt = style.render("Non achetable", 1, (0,0,0))
                main.screen.blit(txt, emplacement.vie_fois_rect)
            elif (emplacement.attaque_plus_rect.collidepoint(a)):
                if (emplacement.attaque_plus < emplacement.attaque) :
                    txt = style.render(str((1 + emplacement.attaque_plus) ** 2), 1, (0,0,0))
                else :
                    txt = style.render("Non achetable", 1, (0,0,0))
                main.screen.blit(txt, emplacement.attaque_plus_rect)
            elif (emplacement.attaque_fois_rect.collidepoint(a)):
                if (emplacement.attaque_fois < ((10 * emplacement.epoque + 10) / 2)) :
                    txt = style.render(str(1 + emplacement.attaque_fois ** 4), 1, (0,0,0))
                else :
                    txt = style.render("Non achetable", 1, (0,0,0))
                main.screen.blit(txt, emplacement.attaque_fois_rect)
            elif (emplacement.vitesse_rect.collidepoint(a)):
                if (emplacement.vitesse < emplacement.vitesse_max) :
                    txt = style.render(str(int((emplacement.vitesse_max - emplacement.vitesse) ** 2)), 1, (0,0,0))
                else :
                    txt = style.render("Non achetable", 1, (0,0,0))
                main.screen.blit(txt, emplacement.vitesse_rect)

        pygame.display.flip() # Met à jour la fenêtre

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
                if (emplacement.fermer_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "fermer"
                elif (emplacement.nom == "vide") :
                    if (emplacement.rect_usine.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "usine"
                    elif (emplacement.rect_recolteur.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "recolteur"
                    elif (emplacement.rect_combattant.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "combattant"
                    elif (emplacement.rect_assassin.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "assassin"
                    elif (emplacement.rect_tireur.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "tireur"
                    elif (emplacement.rect_snipeur.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "snipeur"
                    elif (emplacement.rect_tank.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "tank"
                    elif (emplacement.rect_lanceur.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "lanceur"
                    elif (emplacement.rect_rapide.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "rapide"
                elif (emplacement.ameliorer_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "ameliorer"
                elif (emplacement.vendre_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "vendre"
                elif (emplacement.vie_plus_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "vie_plus"
                elif (emplacement.respawn_rect.collidepoint(event.pos)) :
                    main.pressed_button[event.button] = "respawn"
                elif (emplacement.nom != "usine") :
                    if (emplacement.vie_fois_rect.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "vie_fois"
                    elif (emplacement.attaque_plus_rect.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "attaque_plus"
                    elif (emplacement.attaque_fois_rect.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "attaque_fois"
                    elif (emplacement.vitesse_rect.collidepoint(event.pos)) :
                        main.pressed_button[event.button] = "vitesse"
                # Laché
            elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1) :
                if (emplacement.fermer_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "fermer") :
                    main.pressed_button[event.button] = ""
                    return True
                elif (emplacement.nom == "vide") :
                    if (emplacement.rect_usine.collidepoint(event.pos) and main.pressed_button[event.button] == "usine") :
                        main.pressed_button[event.button] = ""
                        b = 100
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (100)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("usine", main.game.timer)
                                return True
                    elif (emplacement.rect_recolteur.collidepoint(event.pos) and main.pressed_button[event.button] == "recolteur") :
                        main.pressed_button[event.button] = ""
                        b = 50
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (50)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("recolteur", main.game.timer)
                                return True
                    elif (emplacement.rect_combattant.collidepoint(event.pos) and main.pressed_button[event.button] == "combattant") :
                        main.pressed_button[event.button] = ""
                        b = 50
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (50)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("combattant", main.game.timer)
                                return True
                    elif (emplacement.rect_assassin.collidepoint(event.pos) and main.pressed_button[event.button] == "assassin") :
                        main.pressed_button[event.button] = ""
                        b = 100
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (100)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("assassin", main.game.timer)
                                return True
                    elif (emplacement.rect_tireur.collidepoint(event.pos) and main.pressed_button[event.button] == "tireur") :
                        main.pressed_button[event.button] = ""
                        b = 100
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (100)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("tireur", main.game.timer)
                                return True
                    elif (emplacement.rect_snipeur.collidepoint(event.pos) and main.pressed_button[event.button] == "snipeur") :
                        main.pressed_button[event.button] = ""
                        b = 150
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (100)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("snipeur", main.game.timer)
                                return True
                    elif (emplacement.rect_tank.collidepoint(event.pos) and main.pressed_button[event.button] == "tank") :
                        main.pressed_button[event.button] = ""
                        b = 250
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (100)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("tank", main.game.timer)
                                return True
                    elif (emplacement.rect_lanceur.collidepoint(event.pos) and main.pressed_button[event.button] == "lanceur") :
                        main.pressed_button[event.button] = ""
                        b = 250
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (100)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("lanceur", main.game.timer)
                                return True
                    elif (emplacement.rect_rapide.collidepoint(event.pos) and main.pressed_button[event.button] == "rapide") :
                        main.pressed_button[event.button] = ""
                        b = 250
                        if (main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût (100)")
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.cout_total = b
                                emplacement.achat ("rapide", main.game.timer)
                                return True
                else :
                    if (emplacement.ameliorer_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "ameliorer") :
                        main.pressed_button[event.button] = ""
                        b = 99 + (emplacement.epoque + 1) ** 7
                        if (main.game.base.epoque_nbr > emplacement.epoque and main.game.monnaie >= b) :
                            a = main.game_confirmer ("Coût : " + str(b))
                            if (a) :
                                main.game.monnaie -= b
                                emplacement.upgrade ()
                                return True
                    elif (emplacement.vendre_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "vendre") :
                        main.pressed_button[event.button] = ""
                        if (emplacement.cout_total > 0) :
                            a = main.game_confirmer ("Vente à " + str(int(emplacement.cout_total * 0.8)) + " (80%)")
                            if (a) :
                                main.game.monnaie += int(emplacement.cout_total * 0.8)
                                emplacement.reset()
                    elif (emplacement.vie_plus_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "vie_plus") :
                        main.pressed_button[event.button] = ""
                        if (emplacement.nom != "usine") :
                            if (emplacement.health_plus < emplacement.health) :
                                b = (1 + emplacement.health_plus) ** 2
                                if (main.game.monnaie >= b) :
                                    a = main.game_confirmer ("Coût : " + str(b))
                                    if (a) :
                                        main.game.monnaie -= b
                                        emplacement.cout_total += b
                                        emplacement.health_plus += 1
                        else :
                            if (emplacement.quantitee < emplacement.quantitee_max) :
                                b = (1 + emplacement.quantitee) ** 4
                                if (main.game.monnaie >= b) :
                                    a = main.game_confirmer ("Coût : " + str(b))
                                    if (a) :
                                        main.game.monnaie -= b
                                        emplacement.cout_total += b
                                        emplacement.quantitee += 1
                    elif (emplacement.respawn_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "respawn") :
                        main.pressed_button[event.button] = ""
                        if (emplacement.respawn > emplacement.respawn_min) :
                            b = int ((- 100 / (emplacement.respawn_min - emplacement.respawn)) ** 2)
                            if (main.game.monnaie >= b) :
                                a = main.game_confirmer ("Coût : " + str(b))
                                if (a) :
                                    main.game.monnaie -= b
                                    emplacement.cout_total += b
                                    emplacement.respawn -= 0.1
                    elif (emplacement.nom != "usine") :
                        if (emplacement.vie_fois_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "vie_fois") :
                            main.pressed_button[event.button] = ""
                            if (emplacement.health_fois < (10 * emplacement.epoque + 10) / 2) :
                                b = 1 + emplacement.health_fois ** 4
                                if (main.game.monnaie >= b) :
                                    a = main.game_confirmer ("Coût : " + str(b))
                                    if (a) :
                                        main.game.monnaie -= b
                                        emplacement.cout_total += b
                                        emplacement.health_fois += 1
                        elif (emplacement.attaque_plus_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "attaque_plus") :
                            main.pressed_button[event.button] = ""
                            if (emplacement.attaque_plus < emplacement.attaque) :
                                b = (1 + emplacement.attaque_plus) ** 2
                                if (main.game.monnaie >= b) :
                                    a = main.game_confirmer ("Coût : " + str(b))
                                    if (a) :
                                        main.game.monnaie -= b
                                        emplacement.cout_total += b
                                        emplacement.attaque_plus += 1
                        elif (emplacement.attaque_fois_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "attaque_fois") :
                            main.pressed_button[event.button] = ""
                            if (emplacement.attaque_fois < (10 * emplacement.epoque + 10) / 2) :
                                b = 1 + emplacement.attaque_fois ** 4
                                if (main.game.monnaie >= b) :
                                    a = main.game_confirmer ("Coût : " + str(b))
                                    if (a) :
                                        main.game.monnaie -= b
                                        emplacement.cout_total += b
                                        emplacement.attaque_fois += 1
                        elif (emplacement.vitesse_rect.collidepoint(event.pos) and main.pressed_button[event.button] == "vitesse") :
                            main.pressed_button[event.button] = ""
                            if (emplacement.vitesse < emplacement.vitesse_max) :
                                b = int((emplacement.vitesse_max - emplacement.vitesse) ** 2)
                                if (main.game.monnaie >= b) :
                                    a = main.game_confirmer ("Coût : " + str(b))
                                    if (a) :
                                        main.game.monnaie -= b
                                        emplacement.cout_total += b
                                        emplacement.vitesse += 1
                main.pressed_button[event.button] = ""