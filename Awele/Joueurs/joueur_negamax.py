#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game

    
pmax=4
moi=0
def saisieCoup(jeu): 
    """ jeu -> coup
        Retourne un coup a jouer
    """    
    global moi
    moi=game.getJoueur(jeu)
    return decision(jeu)

def decision(jeu, p=0):
    coups=game.getCoupsValides(jeu)
    v_max=None
    best_cp=None
    for cp in coups:
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        v=estimation(copie,p)
        if (v_max is None or v>v_max):
            v_max=v
            best_cp=cp
    return best_cp

#NEGAMAX

def estimation(jeu,p=1,signe=1):
    if (game.finJeu(jeu)):
        g=game.getGagnant(jeu)
        if (g==moi):
            return signe*1000
        else: 
            if (game.getScore(jeu,moi)==24):
                return signe*-100
            else: 
                return signe*-1000
    if (p==pmax):
        return signe*evaluation(jeu)

    coups=game.getCoupsValides(jeu)
    v=-10000
		
    for cp in coups:
        copie=game.getCopieJeu(jeu)
        game.joueCoup(copie,cp)
        v=max(v,-estimation(copie,p+1,-signe))
    return v

def moinsCasesVides(jeu): # remarque plus importante => poids accordé élevé négatif car situation désaventageuse
    plateau=jeu[0]
    ligne= moi-1
    nb=0
    for i in range(6):
        if ( plateau[ligne][i]==1 or plateau[ligne][i]==2):
            nb= nb + 1 
    return (nb *10)/6

def tourSurPlateau(jeu):
    plateau=jeu[0]
    ligne= moi-1
    nb=0
    for i in range(6):
        if ( plateau[ligne][i]>=12):
            nb= nb + 1 
    return (nb *10)/6

def nextCase(l,c,horaire=False):
    """int*int*boolean ->tuple
    retourne la case qui suit la case (l,c) dans le sens anti-horaire quand horaire=false horaire sinon"""
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
    if (moi==1):
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
                  
def diff_scores(jeu):
    return game.getScore(jeu,moi)-game.getScore(jeu,moi%2+1)

def diff_graines(jeu):
    adv=moi%2+1
    campJou=0
    campAdv=0
    for i in range(6):
        campJou+=game.getCaseVal(jeu, moi-1,i)
        campAdv+=game.getCaseVal(jeu,adv-1,i)
    return campJou-campAdv

def dott(t1,t2):
    produit=1
    for i in range(len(t1)):
        produit+=t1[i]*t2[i]
    return produit

def evaluation(jeu):
    """ jeu-->int
        retourne une évaluation de la situation actuelle"""
    tab_poids=[15,5,-20,15,20]
    tab_fonctions=[diff_scores(jeu),diff_graines(jeu),moinsCasesVides(jeu),tourSurPlateau(jeu),stratAdv(jeu)]
    return dott(tab_poids,tab_fonctions)




