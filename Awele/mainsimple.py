#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import numpy 
import numpy
import matplotlib.pyplot as plt

import awele
import sys

sys.path.append("..")
import game
game.game=awele

sys.path.append("./Joueurs")
import joueur_Minimax 
import joueur_1_coup_valide

game.joueur1=joueur_Minimax 
game.joueur2=joueur_1_coup_valide #ensuite joueur_1_coup_valide 

profondeur=[1,2,3,4]
diff_scores=[]
#vict1=0
#vict2=0
it=0
jeu=game.initialiseJeu()
game.affiche(jeu)
#for j in range (4):
#   joueur_AlphaBeta.pmax= j
while (it<100) and (not game.finJeu(jeu)):
    #rajouter une boucle while pour le joueur humain 
    print(game.getJoueur(jeu))
    coup=game.saisieCoup(jeu)
    game.joueCoup(jeu,coup)
    it+=1
    game.affiche(jeu)
print ("gagnant: ", game.getGagnant(jeu))
# diff_scores.append(game.getScores(jeu)[0]-game.getScores(jeu)[1])
#print ("joueur1", vict1)
#print ("joueur2",vict2)
