import pygame
import random as rd

# [ nom, vie, bonus_vie, attaque, bonus_attaque, vitesse, bonus_vitesse, vitesse d'attaque ]
T = [("alien1", 100, 8, 10, 2, 2, 0.1, 5), ("alien2", 100, 5, 15, 4, 3, 0.2, 8), ("alien3", 400, 20, 10, 1, 2, 0.1, 4), ("d_sorciere", 100, 1, 10, 3, 5, 0.5, 5),("z_momie", 100, 10, 5, 1, 2, 0.1, 4)]

class Troupe (pygame.sprite.Sprite) :

    def __init__ (self, screen, bg, boost, nbr) :
        super().__init__()
        self.nom = T[nbr][0]
        self.image = pygame.transform.scale(pygame.image.load("../assets/ennemi/"+self.nom+".png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rectx = bg.width - 1500
        self.rect.x = 0
        self.rect.y = screen.get_height() - 150 + rd.randint (-25, 25)
        self.temps = 0
        (self.health, self.max_health, self.attaque, self.vitesse, self.attaque_speed) = self.calcul (boost, nbr)
        self.valeur = 1 + nbr + boost

    def calcul (self, boost, nbr) :
        x = T[nbr]
        h = x[1] + x[2] * boost
        mh = x[1] + x[2] * boost
        a = x[3] + x[4] * boost
        v = x[5] + int (x[6] * boost)
        a_s = 10 / x[7]
        return (h, mh, a, v, a_s)

    def afficher (self, screen) :
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (150, 150, 150), [self.rect.x, self.rect.y - 40, 100, 5])
        pygame.draw.rect(screen, (255, 0, 0), [self.rect.x, self.rect.y - 40, 100 * self.health // self.max_health, 5])

    def agir (self, main) :
        # Tirs à distance
        if (self.nom[0] == 'd') :
            # Collision avec une troupe :
            a = pygame.sprite.spritecollide(self, main.game.soldats, False, pygame.sprite.collide_mask)
            if (a) :
                self.rect.x = self.rectx + main.game.deplacement
                if (main.game.timer.temps0 - self.temps >= self.attaque_speed) :
                    self.temps = main.game.timer.temps0
                    if (self.nom[1] == 'z') :
                        for i in range (len(a)) :
                            main.game.damage_soldat (a[i], self.attaque)
                    else :
                        main.game.damage_soldat (a[0], self.attaque)
                return True
            # Collision avec la base :
            elif (self.rectx <= main.game.base.rectx + main.game.base.rect.width + 50) :
                self.rect.x = self.rectx + main.game.deplacement
                if (main.game.timer.temps0 - self.temps >= self.attaque_speed) :
                    self.temps = main.game.timer.temps0
                    main.game.base.damage (self.attaque)
                return True
            else :
                self.rectx -= self.vitesse
                self.rect.x = self.rectx + main.game.deplacement
                return True
        # Contact
        else :
            # Collision avec une troupe :
            a = pygame.sprite.spritecollide(self, main.game.soldats, False, pygame.sprite.collide_mask)
            if (a) :
                self.rect.x = self.rectx + main.game.deplacement
                if (main.game.timer.temps0 - self.temps >= self.attaque_speed) :
                    self.temps = main.game.timer.temps0
                    if (self.nom[0] == 'z') :
                        for i in range (len(a)) :
                            main.game.damage_soldat (a[i], self.attaque)
                    else :
                        main.game.damage_soldat (a[0], self.attaque)
                return True
            # Collision avec la base :
            elif (self.rectx <= main.game.base.rectx + main.game.base.rect.width + 50) :
                self.rect.x = self.rectx + main.game.deplacement
                if (main.game.timer.temps0 - self.temps >= self.attaque_speed) :
                    self.temps = main.game.timer.temps0
                    main.game.base.damage (self.attaque)
                return True
            else :
                self.rectx -= self.vitesse
                self.rect.x = self.rectx + main.game.deplacement
                return True

##

# [ nom, vie, bonus_vie, attaque, bonus_attaque, vitesse d'attaque, range ]
D = [("d0", 1000, 100, 50, 1, 5, 400), ("d1", 500, 20, 200, 5, 10, 400)]

class Defense (pygame.sprite.Sprite) :

    def __init__ (self, screen, boost, nbr, y) :
        super().__init__()
        self.nom = D[nbr][0]
        self.image = pygame.transform.scale(pygame.image.load("../assets/ennemi/"+self.nom+".png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rectx = y
        self.rect.x = 0
        self.rect.y = screen.get_height() - 100
        self.temps = 0
        (self.health, self.max_health, self.attaque, self.attaque_speed, self.range) = self.calcul (boost, nbr)

    def calcul (self, boost, nbr) :
        x = D[nbr]
        h = x[1] + x[2] * boost
        mh = x[1] + x[2] * boost
        a = x[3] + x[4] * boost
        a_s = 10 / x[5]
        r = x[6]
        return (h, mh, a, a_s, r)

    def afficher (self, screen) :
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (150, 150, 150), [self.rect.x, self.rect.y - 10, 100, 5])
        pygame.draw.rect(screen, (215, 0, 0), [self.rect.x, self.rect.y - 10, 100 * self.health // self.max_health, 5])

    """ Action function """
    def agir (self, main) :
        self.rect.x = self.rectx + main.game.deplacement # Moove
        if (main.game.timer.temps0 - self.temps >= self.attaque_speed) : # Possibility to attack
            for soldat in main.game.soldats :
                if (soldat.rectx > self.rectx - self.range) :
                    self.temps = main.game.timer.temps0 # Initialize attack timer
                    if (self.nom[1] == 'z') : # For futur zone attack
                        main.game.damage_soldat (soldat, self.attaque)
                    else :
                        main.game.damage_soldat (soldat, self.attaque)
                    return True
        return True

##

class Piece (pygame.sprite.Sprite) :

    def __init__ (self, x, y, valeur) :
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("../assets/piece.png"), (50, 50))
        self.txt = (pygame.font.SysFont("arial" , 25)).render(str(valeur), 1, (0,0,0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.nbr = 0


    def afficher (self, screen, deplacement) :
        self.nbr += 1
        screen.blit (self.image, (self.x + deplacement, self.y - 50 - 1 * self.nbr))
        screen.blit (self.txt, (self.x + deplacement + 60, self.y - 50 - 1 * self.nbr))



