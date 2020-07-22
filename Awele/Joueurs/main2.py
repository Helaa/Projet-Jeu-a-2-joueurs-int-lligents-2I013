#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pylab import *

import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_AlphaBeta
import joueur_negamax
game.joueur1=joueur_AlphaBeta
game.joueur2=joueur_negamax

#joueur_AlphaBeta.pmax= pour changer la profondeur 

while True;
    jeu=game.InitialiseJeu()
    while (not game.FinJeu())
        coups=game.getCoupsValides(jeu)
        for cp in coups:
        	copie=game.getCopie(jeu)
        	oracle.estimation(copie,p=5,alpha=-1000,beta=1000)
        	