#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
# ! Cours 3 diapo 9 
# ! faire les modif nécessaires 
# !
# !
# !

def saisieCoup(jeu): #Decision 
    """ jeu -> coup
        Retourne un coup a jouer
    """
    return decision(jeu)

def decision(jeu):
    """jeu -> coup
    Retourne le meilleur coup à l'horizon 1 """

    joueur=game.getJoueur(jeu)
    liste=game.getCoupsValides(jeu)
    score_init=game.getScore(jeu,joueur) 
    score_max=0
    for cp in liste:
        copie=game.getcopie(jeu)
        game.joueCoup(copie,cp)
        if(game.getScore(copie,joueur%2+1)>score_max):
            score_max=game.getScore(copie,joueur%2+1)
            best_cp=cp
    return cp


def evaluation(jeu):
 """Les fonctions d'évaluation pour othello voir sur internet"""



