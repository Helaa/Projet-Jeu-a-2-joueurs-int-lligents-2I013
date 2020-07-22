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
import joueur_AlphaBeta
import joueur_horizon1

game.joueur1=joueur_AlphaBeta
game.joueur2=joueur_horizon1 #ensuite joueur_1_coup_valide 

profondeur=[1,2,3,4]
noeudsEvalues=[]

#vict1=0
#vict2=0
it=0
jeu=game.initialiseJeu()
game.affiche(jeu)
for j in range (4):
    joueur_AlphaBeta.pmax= profondeur[j]
    while (it<100) and (not game.finJeu(jeu)):
        #rajouter une boucle while pour le joueur humain 
        print(game.getJoueur(jeu))
        coup=game.saisieCoup(jeu)
        game.joueCoup(jeu,coup)
        it+=1
        game.affiche(jeu)
    print ("gagnant: ", game.getGagnant(jeu))
    noeudsEvalues.append(joueur_AlphaBeta.compteur)
    #print ("joueur1", vict1)
    #print ("joueur2",vict2)

plt.plot(profondeur,noeudsEvalues)
plt.show()