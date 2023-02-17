from state_home import *
from state_menu import *
from state_continuer import *
from state_game import *

import pygame


pygame.init()
"""
Clock not working
clock = pygame.time.Clock()
"""

# JEU
class Main :

    def __init__ (self, screen) :
        self.screen = screen
        self.fps = 60
        self.pressed = {}
        self.pressed_button = {}
        self.etape = "Home"
        self.accueil = Accueil (self.screen)
        self.menu = Menu (self.screen)
        self.game = Game (self.screen)

        # Confirmer
        self.confirmer = pygame.transform.scale(pygame.image.load("../assets/confirmer.png"), (400, 400))
        self.confirmer_rect = self.confirmer.get_rect()
        self.confirmer_rect.x = self.screen.get_width() // 2 - 400
        self.confirmer_rect.y = self.screen.get_height() // 2 - 100

        self.annuler = pygame.transform.scale(pygame.image.load("../assets/annuler.png"), (400, 400))
        self.annuler_rect = self.annuler.get_rect()
        self.annuler_rect.x = self.confirmer_rect.x + 400
        self.annuler_rect.y = self.confirmer_rect.y

    """ Print a confirm message on the screen """
    def game_confirmer (self, message) :
        pygame.draw.rect(main.screen, (255, 255, 255), [self.confirmer_rect.x, self.confirmer_rect.y - 100, 810, 600])
        txt = (pygame.font.SysFont("arial" , 100, bold=True)).render("Confirmer ?", 1, (0,0,0))
        screen.blit(txt, (self.confirmer_rect.x + 190, self.confirmer_rect.y - 100))
        self.screen.blit(self.confirmer, self.confirmer_rect)
        self.screen.blit(self.annuler, self.annuler_rect)
        txt = (pygame.font.SysFont("arial" , 80, bold=True)).render(message, 1, (0,0,0))
        screen.blit(txt, (self.confirmer_rect.x + 10, self.confirmer_rect.y + 400))
        pygame.display.flip()
        while (True) :
            for event in pygame.event.get() :
                # Fenêtre fermée
                if (event.type == pygame.QUIT) :
                    pygame.quit()
                    return False
                # Bouton
                elif (event.type == pygame.KEYDOWN) :
                    self.pressed_button[event.key] = True
                    if (event.key == pygame.K_ESCAPE) :
                        return False
                elif (event.type == pygame.KEYUP) :
                    self.pressed_button[event.key] = False

                # Souris bouton gauche
                    # Appuyé
                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1) :
                    if (self.confirmer_rect.collidepoint(event.pos)) :
                        self.pressed_button[event.button] = "confirmer"
                    elif (self.annuler_rect.collidepoint(event.pos)) :
                        self.pressed_button[event.button] = "annuler"
                    # Laché
                elif (event.type == pygame.MOUSEBUTTONUP and event.button == 1) :
                    if (self.confirmer_rect.collidepoint(event.pos) and self.pressed_button[event.button] == "confirmer") :
                        self.pressed_button[event.button] = ""
                        return True
                    elif (self.annuler_rect.collidepoint(event.pos) and self.pressed_button[event.button] == "annuler") :
                        self.pressed_button[event.button] = ""
                        return False
                    else :
                        self.pressed_button[event.button] = ""


# Création de l'affichage
pygame.display.set_caption("TownAge")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

image = pygame.image.load("../assets/icon.png")
pygame.display.set_icon(image)


""" Launch of the game """
main = Main (screen)
running = True

while (running) :
    if (main.etape == "Home") :
        running = accueil (main)
    elif (main.etape == "Continue") :
        running = jeu (main)
    elif (main.etape == "NewGame") :
        main.game.new_game (main.screen)
        running = jeu (main)
    else :
        running = accueil (main)

pygame.quit()
