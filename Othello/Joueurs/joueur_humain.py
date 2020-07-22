#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")
import game


def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    while True:
        print("Lecture des coordonnées de votre case: ")
        l= input("ligne:")
        c= input("colonne:")
        liste= game.getCoupsValides(jeu)
        if ((int(l), int(c)) in liste):
            return (int(l), int(c))
        print("Coup invalide, saisissez un autre coup")

