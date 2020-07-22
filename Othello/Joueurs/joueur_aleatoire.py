#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game
import random 

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    return random.choice(game.getCoupsValides(jeu))

        


