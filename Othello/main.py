#!/usr/bin/env python
# -*- coding: utf-8 -*-
import othello
import sys
import random 

sys.path.append("..")
import game
game.game=othello

sys.path.append("./Joueurs")
import joueur_Minimax
import joueur_aleatoire

game.joueur1=joueur_aleatoire
game.joueur2=joueur_Minimax
vict1=0
vict2=0
it=0
jeu=game.initialiseJeu()
#for i in range(100):
    while (it<100) and (not game.finJeu(jeu)):
        game.affiche(jeu)
        coup=game.saisieCoup(jeu)
        game.joueCoup(jeu,coup)
        it+=1
        game.affiche(jeu)
    print ("gagnant: ", game.getGagnant(jeu))
    if game.getGagnant(jeu)==1:
    	vict1+=1
    else:
    	vict2+=1
print ("joueur1", vict1)
print ("joueur2",vict2)

"""def apprentissage(jeu):
    e=5
    #v = pourcentage du joueur actuel 
    while True:
        p=random.choice(tab_poids)
        alea=rand()
        if alea<0.5:
            dep=-e
        else:
            dep=e
        v=joueNparties
        eleve=addParametre(e)
        v1=joueNparties
        if v>v1:
        	eleve.parametre(j,-e)
        else:
        	print (eleveParametre)"""

