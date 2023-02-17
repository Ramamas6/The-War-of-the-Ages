import pygame

def afficher_sauvegardes () :
    fichier = open("../assets/liste_saves.txt","r")
    a = fichier.read()
    fichier.close()
    a = a.split("\n")
    del a[len(a)-1]
    return a
