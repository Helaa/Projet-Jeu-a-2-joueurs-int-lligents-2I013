#!/usr/bin/env python
# -*- coding: utf-8 -*-
import awele
import sys

sys.path.append("..")
import game
game.game=awele
sys.path.append("./Joueurs")
import joueur_humain
import joueur_AlphaBeta
import joueur_horizon1


game.joueur1=joueur_humain
game.joueur2=joueur_humain

oracle= joueur_AlphaBeta
joueurParametrique= joueur_horizon1
param=joueurParametrique.tab_poids 


o=[] #scores donnes par l'oracle aux différents coups 
s=[]


while (True):
    jeu=game.initialiseJeu()
    while (not (game.finJeu(jeu))):
        coups=game.getCoupsValides(jeu)
        for cp in coups:
            copie=game.getCopieJeu(jeu)
            o.append(oracle.estimation(copie, p=5, alpha=-1000, beta=1000))
            opt=oracle.decision(copie,p=1)  #coup joué par l'oracle 
            s.append(joueurParametrique.tab_fcts)
            optPos=s.index(max(s))

            for i in range(len(o)):
                if (o[i]<o[optPos]):
                    s.append(joueurParametrique.tab_fcts[i](copie))

                    for i in range (len(param)):

                        s[i]=dott(param,s[i])
                        s[optPos]=dott(param,s[opt])

                        if ((s[optPos]-s[i])<1):
                            for j in range(len(param)):
                                param[j]-=epsilon*(s[i][j]-s[optPos][j])
       
    
