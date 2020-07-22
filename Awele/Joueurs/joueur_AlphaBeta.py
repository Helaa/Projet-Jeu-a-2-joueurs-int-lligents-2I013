  #!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.path.append("../..")
import game

tab_poids=[20,10,-10,15,20]
pmax=4
moi=0
compteur=0
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
        global compteur
        compteur+=1
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
            if (game.getScore(jeu,moi)==game.getScore(jeu,moi%2+1)):
                return -100
            else: 
                return -1000
    if (p==pmax):
        return evaluation(jeu)
    coups=game.getCoupsValides(jeu)

    if (p%2==1):   #on est dans un noeud min 
        v= 10000
        for cp in coups:
            copie=game.getCopieJeu(jeu)
            game.joueCoup(copie,cp)
            v=min(v, estimation(copie,p+1, alpha, beta))
            if(alpha>v):
                return v
            beta= min(beta, v)
    else:           #on est dans un noeud max      
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
    """jeu -> int
    retourne la différence de scores entre les deux joueurs 
    """
    joueur=moi
    adv=joueur%2+1
    return game.getScore(jeu,joueur)-game.getScore(jeu,adv)

def diff_graines(jeu):
    """jeu -> int
    retourne la différence de graines sur le plateau entre les deux joueurs 
    """
    joueur=moi 
    adv=joueur%2+1
    campJou=0
    campAdv=0
    for i in range(6):
        campJou+=game.getCaseVal(jeu, joueur-1,i)
        campAdv+=game.getCaseVal(jeu,adv-1,i)
    return campJou-campAdv

def moinsCasesVides(jeu):
# remarque plus importante => poids accordé élevé négatif car situation désaventageuse
    """jeu -> int 
    retourne le nombre de cases vides dans son camp 
    """
    plateau=jeu[0]
    ligne= game.getJoueur(jeu)-1
    nb=0
    for i in range(6):
        if ( plateau[ligne][i]==1 or plateau[ligne][i]==2):
            nb= nb + 1 
    return nb 

def tourSurPlateau(jeu):
    """jeu -> int 
    retourne le nombre de case contenant plus de 12 graines (possibilité de faire 
    2 tours complets et manger dans le camp adverse)
    """
    plateau=jeu[0]
    ligne= game.getJoueur(jeu)-1
    nb=0
    for i in range(6):
        if ( plateau[ligne][i]>=12):
            nb= nb + 1 
    return nb 

def nextCase(l,c,horaire=False):
    """int * int * boolean -> (int, int)
    retourne la case qui suit la  case passée en paramètre (l,c)
    """
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
    """jeu -> int 
    retourne le nombre de cases qui contiennent assez de graines 
    pour ne pas etre mangé par l'adversaire 
    """
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
    return nb 

def dott(t1,t2):
    produit=1
    for i in range(len(t1)):
        produit+=t1[i]*t2[i]
    return produit

def evaluation(jeu):
    """ jeu-->int
    retourne une évaluation de la situation actuelle
    """
    tab_fonctions=[diff_scores(jeu),diff_graines(jeu),moinsCasesVides(jeu),tourSurPlateau(jeu),stratAdv(jeu)]
    return dott(tab_poids,tab_fonctions)
    

















