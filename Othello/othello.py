#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce
import sys
sys.path.append("..")
import game


def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu 
    """
    if (game.getCoupsValides(jeu)==[]):
        return True
    plateau= game.getPlateau(jeu)
    for i in range(8):
        for j in range(8):
            if (game.getCaseVal(jeu, i, j)==0):
                return False 
    return True 

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    jeu=[]
    plateau=[]
    for i in range(8):
        l=[]
        plateau.append(l)
        for j in range(8):
            if (i==3 and j==3):
                l.append(1)
            elif (i==4 and j==3):
                l.append(2)
            elif (i==3 and j==4):
                l.append(2)
            elif (i==4 and j==4):
                l.append(1)
            else:
                l.append(0)
   
    jeu.append(plateau)
    jeu.append(1)
    jeu.append(None)
    jeu.append([])
    jeu.append([2,2])
    return jeu


def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    scores=jeu[4]
    return scores.index(max(scores[0],scores[1]))+1


def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer
                    
         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    #print ("Coup joue= ", jeu[3][-1], "\n");
    print ("Scores= ", jeu[4][0], ", ", jeu[4][1], "\n");
    print("Plateau: \n")
    for i in range (9):
         for j in range(8):
             if (j==0 and i==0):
                 print ("\t \t \t |\t ",i, end='')
                 continue;
             if (j==0):
                 print (" \t |\t", i-1, end='')
             if (i==0):
                 print (" \t |\t", j, end='')
             else:
                 print ("\t | \t", jeu[0][i-1][j], end='')
         print ("\n \t -----------------------------------------------------------------------------------------------------------------------------------------------------")
   
def entourageVide(jeu,l,c):
    return {(l+i,c+j) for i in [-1,0,1] for j in [-1,0,1] if (c+j<=7 and c-j>=0 and l+i<=7 and l-i>=0 and jeu[0][l+i][c+j]==0) }

def coups (jeu):
    adv= jeu[1]%2+1
    s=[entourageVide(jeu,l,c) for l in range(8) for c in range (8) if (jeu[0][l][c]==adv)]
    return reduce(lambda a,b: a|b,s)
   

def checkEncadrementDirection(jeu,cp,i,j):
    ok=False
    l,c=cp
    while True:
        l+=i
        c+=j
        if (l>7 or l<0 or c>7 or c<0):
            return False
        if (jeu[0][l][c]==0):
            return False
        if (jeu[0][l][c]==jeu[1]):
            return ok
        ok=True

def getEncadrement(jeu,c,all=True):
    ret=[]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if (i==0 and j==0):
                continue
            if (checkEncadrementDirection(jeu,c,i,j)):
                ret.append((i,j))
                if (not all):
                    break
    return ret

def getCoupsValides(jeu):
    coup=coups(jeu)
    return [x for x in coup if (len(getEncadrement(jeu,x,False))>0)]

def retournePions(jeu,cp,cd):
    plateau= game.getPlateau(jeu)
    joueur=game.getJoueur(jeu)
    scores=game.getScores(jeu)
    adv= joueur%2 +1
    l,c= cp #couple de position actuelle
    i,j= cd #couple de direction 
   
    while True: 
        l+=i
        c+=j
        if (joueur==1):
            scores[0]+=1
            scores[1]-=1
            plateau[l][c]=1
        else:
            scores[1]+=1
            scores[0]-=1
            plateau[l][c]=2
        if (plateau[l][c]!=adv):
            break
        
     
def joueCoup(jeu,coup):
    plateau=game.getPlateau(jeu)
    j=game.getJoueur(jeu)
    plateau[coup[0]][coup[1]]=jeu[1]
    #jeu[4][j-1]+=1
    d=getEncadrement(jeu,coup)
    for x in d:
        retournePions(jeu,coup,x)
    jeu[3].append(coup)
    jeu[2]=None
    jeu[1]=j%2 +1














