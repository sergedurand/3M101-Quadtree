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
import Implementation_AVL as AVL
import Implementation_ABR as ABR
import statistics

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

def median(data):
    """renvoie la médiane d'un dictionnaire)
    """
    l_triee = []
    for key,value in data.items():
        for i in range(value):
            l_triee.append(key)
    l_triee = sorted(l_triee)
    taille = len(l_triee)
    if(taille%2 == 0):
        return l_triee[taille//2]
    else:
        return (l_triee[taille//2]+l_triee[taille//2+1])/2.0
    

def moyenne(data):
    """renvoie la moyenne d'un dictionnaire"""
    q = 0
    v = 0
    for key,value in data.items():
        v = v+key*value
        q = q + value
    return v/q

def graphe_distribution_hauteur(taille,nom_fichier = None):
    """renvoie le graphe avec les hauteurs en abscisses et le nombre d'arbres en ordonnées,
    pour 1000 arbres étiquetés de 1 à taille aléatoirement """
    l_arbres = batch_tree_BST(taille,1000)
    freq_haut = distribution_hauteur_BST(l_arbres)
    listes = sorted(freq_haut.items())
    x,y = zip(*listes)
    print("hauteur médiane = ",median(freq_haut))
    print("hauteur moyenne = ",moyenne(freq_haut))
    K = moyenne(freq_haut)/math.log(taille)
    print("K = Hn/Log(n) = ",K)
    print("max : ",listes[len(listes)-1][0])
    fig = plt.figure()
    plt.plot(x,y)
    stringK = "{:.2f}".format(K)
    fig.suptitle('distribution des arbres en fonction de leur hauteur')
    plt.xlabel('hauteur')
    plt.ylabel('arbres')
    plt.axvline(K*math.log(taille),color="black",label=stringK+"log(n)")
    if(nom_fichier is not None):
        fig.savefig(nom_fichier)
    plt.legend()
    plt.show()
    

