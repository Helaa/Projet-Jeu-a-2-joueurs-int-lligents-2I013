  #!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.path.append("../..")
import game

tab_poids=[20,10,30,10]
pmax=4
moi=0

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
    """jeu->int
    retourne la difference de scores entre le joueur et son adversaire"""
    #le but du jeu est d’avoir plus de pions que l’autre à la fin de la partie
    #et non pendant la partie
    adv=moi%2+1
    if game.getScore(jeu,moi)-game.getScore(jeu,adv)>45 :
        return game.getScore(jeu,moi)-game.getScore(jeu,adv)
    else:
        return -(game.getScore(jeu,moi)-game.getScore(jeu,adv))

def coins(jeu):
    """ jeu->int 
    retourne le nombre de cases bonus que le joueur a """
    plateau=game.getPlateau(jeu)
    bonus=0
    if (plateau[0][0]==moi):
        bonus+=1
    if (plateau[0][7]==moi):
        bonus+=1
    if (plateau[7][0]==moi):
        bonus+=1
    if (plateau[7][7]==moi):
        bonus+=1
    return bonus 

#pensez à découper le jeu en 3 parties début milieu et fin grace au 
#comptage des pions sur le platau et disposer
#les fcts d'évaluation selon le stade de la partie 
#le nombre de pions définitifs non attaquables


def parite(jeu):
    """jeu->int 
    retourne 1 si c'est le joueur qui joue en dernier 0 sinon """
    scores=game.getScores(jeu)
    pions_sur_plat=scores[0]+scores[1]
    if (pions_sur_plat==63 and game.getJoueur(jeu)==moi):
        return 1
    return 0

def pions_definitifs(jeu):
    """jeu->int 
    retourne le nombre de pions définitifs (non attaquables par l'adv jusqu'à la fin de la partie)"""
    pions=0
    plateau=game.getPlateau(jeu)        #  .  .  .  .
    k=4                                 #  .  .  .
    for i in range(4):                  #  .  .
        for j in range (k):             #  .
            if (plateau[i][j]==jeu[1]):    
                pions+=1                #                        . 
        k-=1                            #                     .  . 
    k=4                                 #                  .  .  .      
    for i in range(7,3,-1):             #               .  .  .  .
        for j in range (k,8):
            if (plateau[i][j]==jeu[1]):
                pions+=1
        k+=1
    return pions 

def diff_pions(jeu): #plus efficace à la fin de la partie/ au début de la partie 
#vaut mieux avoir moins de pions que l'adversaire
    plateau=game.getPlateau(jeu)  
    mon_camp=0
    camp_adv=0
    for i in range(8):
        for j in range (8):
            if (plateau[i][j]==moi):
                mon_camp+=1
            if (plateau[i][j]==moi%2+1):
                camp_adv+=1

    return mon_camp - camp_adv



def dott(t1,t2):
    produit=1
    for i in range(len(t1)):
        produit+=t1[i]*t2[i]
    return produit
    

def evaluation(jeu):
    """ jeu-->int
        retourne une évaluation de la situation actuelle"""
    tab_fcts=[diff_scores(jeu), coins(jeu), pions_definitifs(jeu),parite(jeu)]
    return dott(tab_poids,tab_fcts)











