#!/usr/bin/python3.5
# -*-coding:utf-8 -


import pygame
from pygame.locals import *

pygame.init()

continuer = True

nb_case = 15
sprit_size = 30
screen_size = (nb_case*sprit_size, nb_case*sprit_size)



fenetre = pygame.display.set_mode(screen_size)
titre_fenetre = "Jeu Pygame/DK"


accueil = pygame.image.load("accueil.png").convert()

fond = pygame.image.load("fond.jpg").convert()


#Elements
mur = pygame.image.load("mur.png")

dk_gauche = pygame.image.load("dk_gauche.png").convert()
dk_droite = pygame.image.load("dk_droite.png").convert()
dk_bas = pygame.image.load("dk_bas.png").convert()
dk_haut = pygame.image.load("dk_haut.png").convert()

arrivee = pygame.image.load("arrivee.png").convert()
depart = pygame.image.load("depart.png").convert()

#Icone du jeu
icone = pygame.image.load("arrivee.png")
