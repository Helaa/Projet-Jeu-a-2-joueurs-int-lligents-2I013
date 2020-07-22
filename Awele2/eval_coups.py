#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awelle
import sys
sys.path.append("..")
import game
game.game=awelle
sys.path.append("./Joueurs")
import joueur_humain


def score_max(jeu, coup):
    joueur=game.getJoueur(jeu)
    copie=game.getcopie(jeu)

    score_init=game.getScore(copie,joueur)
    game.joueCoup(copie,coup)
    score=game.getScore(copie,joueur)
    if (score>score_init):
        return 1

    return 0

def evite_coupAdv (jeu,coup):
    joueur=game.getJoueur(jeu)
    adv=joueur%2 +1
    liste=game.getCoupsValides(jeu)
    

    for cp in liste:
        copie=game.getcopie(jeu)
	game.joueCoup(copie,cp)
        score_init_adv=game.getScore(copie,joueur)
	game.joueCoup(copie,cp)
        score_apres_adv=game.getScore(copie,adv)

        if (score_apres_adv<score_init_adv):
            bestCp=cp

    return bestCp

def eval_coups(jeu):
    """jeu->coup
    renvoie le meilleur coup"""#les fonctions d'évaluation: f1=le coup qui fait augmenter le score *1 + f2= jouer le coup qui evite un coup adverse*1 +
    
    joueur=game.getJoueur(jeu)
    liste=game.getCoupsValides(jeu)
    copie=game.getcopie(jeu) 

    for cp in liste:
        


        



















