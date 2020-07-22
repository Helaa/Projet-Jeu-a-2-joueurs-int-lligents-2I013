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
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        if(game.getScore(copie,joueur%2+1)>score_max):
            score_max=game.getScore(copie,joueur%2+1)
            best_cp=cp
    return cp


def diff_scores(jeu):
    joueur=game.getJoueur(jeu)
    adv=joueur%2+1
    return game.getScore(jeu,joueur)-game.getScore(jeu,adv)

def diff_graines(jeu):
    joueur=game.getJoueur(jeu)
    adv=joueur%2+1
    campJou=0
    campAdv=0
    for i in range(6):
        campJou+=game.getCaseVal(jeu, joueur-1,i)
        campAdv+=game.getCaseVal(jeu,adv-1,i)
    return campJou-campAdv

def evaluation(jeu):
    """ jeu-->int
        retourne une évaluation de la situation actuelle"""
    poids1=5
    poids2=3
    return poids1*diff_scores(jeu)+poids2*diff_graines(jeu)









    
