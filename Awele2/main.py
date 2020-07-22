#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awele
import sys
sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_Minimax
import joueur_AlphaBeta
game.joueur1=joueur_AlphaBeta
game.joueur2=joueur_Minimax



it=0
jeu=game.initialiseJeu()
game.affiche(jeu)
for el in tab_poids:
    print (el, "\t")
for j in range (len(tab_poids)):
    for i in range (100):
        while (it<100) and (not game.finJeu(jeu)):
            s1=game.getScore(jeu)
            coup=game.saisieCoup(jeu)
            game.joueCoup(jeu,coup)
            s2=game.getScore(jeu)
            print("Scores: ",game.getScore(jeu,game.getJoueur(jeu)), game.getScore(jeu,game.getJoueur(jeu)%2+1))
            it+=1
            game.affiche(jeu)
        print ("gagnant: ", game.getGagnant(jeu))
            if (s2[moi-1]>s1[moi-1])
                tab_poids[j]+=esilon 
            else:
                tab_poids[j]-=esilon 

for el in tab_poids:
    print (el, "\t")



