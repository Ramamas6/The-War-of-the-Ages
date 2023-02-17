import pygame
import random as rd

class Soldat (pygame.sprite.Sprite) :

    def __init__ (self, emp, screen) :
        super().__init__()
        self.nom = emp.nom
        self.image = pygame.transform.scale(pygame.image.load("../assets/armee/"+emp.nom+"/"+str(emp.epoque)+"_cours.png"), (100, 100))
        self.rect = self.image.get_rect()
        self.rectx = 850
        self.rect.x = 0
        self.rect.y = screen.get_height() - 150 + rd.randint(-25, 25)
        self.temps = 0
        self.vitesse = 2 + emp.vitesse
        self.health = emp.calcul_vie ()
        self.max_health = emp.calcul_vie ()
        self.attaque = emp.calcul_attaque ()
        self.attaque_speed = 1
        self.epoque = emp.epoque
        self.range = emp.range

    def afficher (self, screen) :
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen, (150, 150, 150), [self.rect.x, self.rect.y - 40, 100, 5])
        pygame.draw.rect(screen, (0, 255, 0), [self.rect.x, self.rect.y - 40, 100 * self.health // self.max_health, 5])

    """ Action function """
    def agir (self, main) :
        # Collision avec une troupe :
        for enemi in main.game.ennemi.soldats :
            if (enemi.rectx < self.rectx + self.range and self.vitesse > 0) :
                self.rect.x = self.rectx + main.game.deplacement
                if (main.game.timer.temps0 - self.temps >= self.attaque_speed) :
                    self.temps = main.game.timer.temps0
                    v = main.game.ennemi.damage_soldat (enemi, self.attaque)
                    main.game.monnaie += v
                    main.game.xp = min (main.game.xp_max, main.game.xp + v)
                return True
        # Collision avec une défense :
        for defense in main.game.ennemi.defenses :
            if (defense.rectx < self.rectx + self.range and self.vitesse > 0) :
                self.rect.x = self.rectx + main.game.deplacement
                if (main.game.timer.temps0 - self.temps >= self.attaque_speed) :
                    self.temps = main.game.timer.temps0
                    main.game.ennemi.damage_defense (defense, self.attaque)
                return True
        # Collision avec la base :
        if (self.rectx >= main.game.ennemi.rectx - 100 - self.range) :
            self.rect.x = self.rectx + main.game.deplacement
            if (main.game.timer.temps0 - self.temps >= self.attaque_speed) :
                self.temps = main.game.timer.temps0
                main.game.ennemi.damage (self.attaque)
            return True
        # Cas des récolteurs
        elif (self.nom == "recolteur") :
            # Contact avec le point
            if (self.vitesse > 0 and self.rectx >= main.game.base.recoltex) :
                if (main.game.timer.temps0 - self.temps > 2) :
                    self.temps = main.game.timer.temps0
                elif (main.game.timer.temps0 - self.temps > 1) :
                    self.vitesse *= -1
                self.rect.x = self.rectx + main.game.deplacement
                return True
            # Contact avec la base
            elif (self.vitesse < 0 and self.rectx <= main.game.base.rectx + main.game.base.rect.width + 50) :
                main.game.monnaie += (1 + main.game.ressources) * (1 + self.epoque)
                a = (self.rect.x, self.rect.y, (1 + main.game.ressources) * (1 + self.epoque))
                main.game.soldats.remove (self)
                return a
            # Déplacement
            else :
                self.rectx += self.vitesse
                self.rect.x = self.rectx + main.game.deplacement
                return True
        # Déplacement
        else :
            self.rectx += self.vitesse
            self.rect.x = self.rectx + main.game.deplacement
            return True