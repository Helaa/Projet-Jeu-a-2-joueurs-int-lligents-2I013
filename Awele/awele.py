#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
import game

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu awele
    """
    #plateau= jeu[0] 
    #joueur=jeu[1]
    #Lnull=[0,0,0,0,0,0] #Liste de 0 
    #diff=[item for item in plateau[joueur%2+1] if (item not in Lnull) ] # liste des différences entre le camp du joueur advrese et la liste nulle 
    return game.getCoupsValides(jeu)==[] #and diff==[] 


def initialiseJeu():
    """ void -> jeu
        Initialise le jeu(nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    jeu=[]
    plateau=[]
    for i in range(2):
        l=[]
        plateau.append(l)
        for j in range(6):
            l.append(4)
    jeu.append(plateau)
    jeu.append(1)
    jeu.append(None)
    jeu.append([])
    jeu.append([0,0])
    return jeu
    
def advAffame (jeu): 
    j=game.getJoueur(jeu)
    adv= (j%2)+1
    return (sum(jeu[0][adv-1])==0)

def nourrit (jeu,coup):
    j= game.getJoueur(jeu)
    if (j==1):
        return coup[1]<game.getCaseVal(jeu, coup[0], coup[1])
    return 5 - coup[1] < game.getCaseVal(jeu,coup[0], coup[1])   

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met � jour la liste des coups valides
        Un coup est valide si la case du coup n'est pas vide et que l'adversaire n'est pas affamé ou le coup nourrit l'adv
    """
    j=game.getJoueur(jeu)
    a= advAffame(jeu)
    return [ (j-1,i) for i in range(6) if (game.getCaseVal(jeu, j-1, i)>0 and ((not a) or nourrit(jeu,(j-1,i))))]

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

def distribue (jeu,case):
    nc=case
    v=game.getCaseVal(jeu, case[0], case[1])
    jeu[0][case[0]][case[1]]=0
    while v>0:
        nc=nextCase(nc[0], nc[1])
        if (not(nc==case)):
            jeu[0][nc[0]][nc[1]]+=1
            v-=1
    return nc


def joueCoup(jeu,coup):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
    """
    l,c=distribue(jeu,coup)
    save=game.getCopieJeu(jeu)
    v=game.getCaseVal(jeu,l,c)
    j=game.getJoueur(jeu)
    while (l==j%2 and ((v==2) or (v==3))):
        jeu[0][l][c]=0
        jeu[4][j-1]+=v
        l,c=nextCase(l,c,True)
        v=game.getCaseVal(jeu,l,c)
    if advAffame(jeu):
        jeu[0]=save[0]
        jeu[4]=save[4]
    jeu[1]=game.changeJoueur(jeu)
    jeu[2]=None
    jeu[3].append(coup)


def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    scores=jeu[4]
    scoreMax=max(scores[0],scores[1])
    return scores.index(scoreMax)+1

jeu=[[[0,0,0,0,3,0],[1,2,3,0,0,0]],2,[(3,4), (1,2), (3,5)],[],(30,1)]
assert getGagnant(jeu)==1

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
    if (jeu[3] ==[]):
        print ("C'est votre premier coup")
    else:
        print ("Coup joue= ", jeu[3][-1], "\n")
    print ("Scores= ", jeu[4][0], ", ", jeu[4][1], "\n")
    print("Plateau: \n")
    for i in range (3):
         for j in range(6):
             if (j==0 and i==0):
                 print ("\t \t \t |\t ",i, end='')
                 continue;
             if (j==0):
                 print (" \t |\t", i-1, end='')
             if (i==0):
                 print (" \t |\t", j, end='')
             else:
                 print ("\t | \t", jeu[0][i-1][j], end='')
         print ("\n \t ------------------------------------------------------------------------------------------------------------------")








