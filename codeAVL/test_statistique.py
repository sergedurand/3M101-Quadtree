# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:25:01 2019

@author: Serge
"""

import time
import math
import numpy as np
import matplotlib.pyplot as plt
import random
import csv
import Implementation_AVL
import Implementation_ABR

def shuffled_ranges(n,m):
    """retourne m listes d'entiers entre 0 et n exclu, d'ordre
    aléatoire, avec d'éventuels doublons"""
    res = []
    L1 = list(range(n))
    for i in range(m):
        res.append(random.sample(L1,len(L1)))
    return res

def graphe(L1,L2,nom_fichier=None): #graphe obtenu par les mesures
    x = np.array(L1)
    y = np.array(L2)
    fig = plt.figure()
    plt.xlim(L1[0],L1[len(L1)-1])
    plt.plot(x,y)
    if(nom_fichier is not None):
        fig.savefig('CalculSigma2.png')
    plt.show()

def batch_tree_BST(n,m):
    listes = shuffled_ranges(n,m)
    res = []
    for l in listes:
        res.append(BST_from_list(l))
    return res
        
def batch_tree_AVL(n,m):
    listes = shuffled_ranges(n,m)
    res = []
    for l in listes:
        res.append(AVL_from_list(l))
    return res

def distribution_hauteur_AVL(L_arbres):
    """renvoie la fréquences des hauteur dans un dictionnaire 
    indexé par les hauteurs"""
    res = {}
    l_h = []
    for arbre in L_arbres:
        l_h.append(arbre.hauteur)
    for h in l_h:
        res[h] = l_h.count(h)
    
    return res

def distribution_hauteur_BST(L_arbres):
    """renvoie la fréquences des hauteur dans un dictionnaire 
    indexé par les hauteurs"""
    res = {}
    l_h = []
    for arbre in L_arbres:
        l_h.append(arbre.hauteur())
    for h in l_h:
        res[h] = l_h.count(h)
    
    return res