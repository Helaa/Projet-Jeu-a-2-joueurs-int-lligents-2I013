#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.path.append("../..")
import game


pmax=4
moi=0
tab_poids=[15,5,-10,15,20]
epsilon=5

def saisieCoup(jeu): #Decision 
    """ jeu -> coup
        Retourne un coup a jouer
    """    
    global moi
    moi=game.getJoueur(jeu)    
    return decision(jeu)

def decision(jeu, p=1):
    joueur=moi
    coups=game.getCoupsValides(jeu)
    best_cp=None
    v_max=None
    alpha=-10000
    beta= 10000
    for cp in coups:
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        v=estimation(copie,p,alpha,beta)
        if (v_max is None or v_max<v):
            v_max=v
            best_cp=cp
    return best_cp

     
def estimation(jeu,p, alpha, beta):
    if (game.finJeu(jeu)):
        g=game.getGagnant(jeu)
        if (g==moi):
            return 1000
        else: 
            if (game.getScore(jeu,moi)==24):
                return -100
            else: 
                return -1000
    if (p==pmax):
        return evaluation(jeu)
    coups=game.getCoupsValides(jeu)
    #if(jeu[1] == moi)
    if (p%2==1):
        v= 10000
        for cp in coups:
            copie=game.getCopieJeu(jeu)
            game.joueCoup(copie,cp)
            v=min(v, estimation(copie,p+1, alpha, beta))
            if(alpha>v):
                return v
            beta= min(beta, v)
    else:
        v = -10000
        for cp in coups:
            copie=game.getCopieJeu(jeu)
            game.joueCoup(copie,cp)
            v=max (v, estimation(copie,p+1, alpha, beta))
            if(beta<v):  
                return v
            alpha= max(alpha, v)
    return v
     
def diff_scores(jeu):
    joueur=moi
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

def moinsCasesVides(jeu): # remarque plus importante => poids accordé élevé négatif car situation désaventageuse
    plateau=jeu[0]
    ligne= game.getJoueur(jeu)-1
    nb=0
    for i in range(6):
        if ( plateau[ligne][i]==1 or plateau[ligne][i]==2):
            nb= nb + 1 
    return (nb *10)/6

def tourSurPlateau(jeu):
    plateau=jeu[0]
    ligne= game.getJoueur(jeu)-1
    nb=0
    for i in range(6):
        if ( plateau[ligne][i]>=12):
            nb= nb + 1 
    return (nb *10)/6




def nextCase(l,c,horaire=False):
    if horaire: 
        if (c==5 and l==0):
            return (1,c)
        if (c==0 and l==1):
            return (0,c)
        if (l==0):
            return (l,c+1)
        return (l,c-1)
    else: 
        if (c==0 and l==0):
            return (1,c)
        if (c==5 and l==1):
            return (0,c)
        if (l==0):
            return (l,c-1)
        return (l, c+1)

def caseMenacee(jeu,case):
    nc=case
    v=game.getCaseVal(jeu, case[0], case[1])
    while v>0:
        nc=nextCase(nc[0], nc[1])
        v-=1
    return nc

def stratAdv(jeu):
    plateau=jeu[0]
    nb=0
    if (game.getJoueur(jeu)==1):
        ligneJoueur=0
        ligneAdv=1
    else:
        ligneJoueur=1
        ligneAdv=0
    for i in range(6):
        case=ligneAdv, i
        nCase=caseMenacee(jeu, case)
        l, c = nCase
        if (game.getCaseVal(jeu, l, c)>2):
            nb = nb + 1
    return (nb *10)/6

def dott(t1,t2):
    produit=1
    for i in range(len(t1)):
        produit+=t1[i]*t2[i]
    return produit

def evaluation(jeu):
     """ jeu-->int
         retourne une évaluation de la situation actuelle"""
     tab_fonctions=[diff_scores(jeu),diff_graines(jeu),moinsCasesVides(jeu),tourSurPlateau(jeu),stratAdv(jeu)]
     return dott(tab_poids,tab_fonctions)
    

#what to write in th emain: 
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
            if (s1[moi-1]>s2[moi-1])
                tab_poids[j]+=esilon 
            else:
                tab_poids[j]-=esilon 

for el in tab_poids:
    print (el, "\t")















