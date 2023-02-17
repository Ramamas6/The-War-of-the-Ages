"""
Manage enemi base
"""

import pygame
from class_ennemi_soldier import *

class Ennemi () :

    def __init__ (self, screen, bg) :
        # Durée de respawn ; Décalage ; Respawn
        self.army = [[(6, 0), False], [(7, 3), False], [(7, 0), False]]
        self.new(screen)
        self.pieces = pygame.sprite.Group()
        # Graphiques
        self.image = pygame.transform.scale(pygame.image.load("../assets/ennemi/0.png"), (750, 557))
        self.rect = self.image.get_rect()
        self.rectx = bg.width - self.rect.width - 1000
        self.rect.x = bg.width - self.rect.width - 1000
        self.rect.y = screen.get_height() - self.rect.height

    def new (self, screen) :
        self.max_health = 1000
        self.health = 1000
        self.damages = 0
        self.stade = 1
        self.soldats = pygame.sprite.Group()
        self.defenses = pygame.sprite.Group()
        self.defenses.add (Defense (screen, 0, 0, 3400))
        self.defenses.add (Defense (screen, 0, 1, 4500))

    def actualise (self, main) :
        t = main.game.timer.temps

        # Nouveaux monstres
        self.stade = min(len(self.army), 1 + t // 100)
        self.max_health = 1000 * self.stade

        # Spawn des monstres
        for i in range (self.stade) :
            soldat = self.army[i]
            if (t % soldat[0][0] == soldat[0][1] and not soldat[1]) :
                soldat[1] = True
                self.soldats.add(Troupe(main.screen, main.game.background_rect, (t) // (soldat[0][0] * 10), i))
            elif (soldat[1] and t % soldat[0][0] != soldat[0][1]) :
                soldat[1] = False

        # Action des défenses
        for defense in self.defenses :
            defense.agir (main)

        # Action des monstres
        for monster in self.soldats :
            monster.agir (main)

        # Divers actions
        self.health = self.max_health - self.damages

    def damage (self, attaque) :
        self.damages += attaque

    def damage_soldat (self, soldat, attaque) :
        soldat.health -= attaque
        if (soldat.health <= 0) :
            v = soldat.valeur
            self.pieces.add (Piece(soldat.rectx, soldat.rect.y, v))
            self.soldats.remove(soldat)
            return v
        else :
            return 0

    def damage_defense (self, defense, attaque) :
        defense.health -= attaque
        if (defense.health <= 0) :
            self.defenses.remove(defense)
            return 0