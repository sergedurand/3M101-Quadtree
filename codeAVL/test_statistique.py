# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 19:25:01 2019

@author: Serge
"""

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

def batch_tree_BST(n,m):
    """retourne m arbres aléatoirement générés,
    étiquetés sur {1,..,n}"""
    listes = shuffled_ranges(n,m)
    res = []
    for l in listes:
        res.append(ABR.BST_from_list(l))
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
    """
    renvoie la fréquences des hauteur dans un dictionnaire 
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
    fig.suptitle('répartition des hauteurs en fonction de leur fréquences')
    plt.xlabel('hauteur')
    plt.ylabel('arbres')
    plt.axvline(K*math.log(taille),color="black",label=stringK+"log(n)")
    plt.legend()
    if(nom_fichier is not None):
        fig.savefig(nom_fichier)
    plt.show()
    
    

    
def graphe_complexite(n,nb_tests,fonction,nom_fichier=None):
    """à chaque étape on créé un arbre binaire, on applique la fonction sur nb_éléments
    aléatoires, on divise par nb_éléments la durée obtenue. On itère sur la taille 
    de l'arbre jusqu'à atteindre un arbre de taille n. Le saut dans 
    l'itération dépend de la valeur de n, on espace les itérations pour 
    les grandes tailles"""
    import timeit
    if(n<100):
        print("insérer un nombre plus grand que 100 pour avoir des données significatives")
        return
    if fonction not in {"suppression","insertion","recherche"}:
        print("le nom de la fonction n'est pas bon. Il faut mettre 'insertion', 'suppression' ou 'recherche'")
        return
    i = 400
    l_taille = []
    l_temps = []
    def recherche_liste(arbre,l_elem):
        for x in l_elem:
            arbre.recherche(x)
    def insertion_liste(arbre,l_elem):
        for x in l_elem:
            arbre.insertion(x)
    def suppression_liste(arbre,l_elem):
        for x in l_elem:
            arbre.suppression(x)
    
    while(i<=n):
        arbre = ABR.arbreAleatoire(i,i)
        #génère une liste de nb_tests éléments disctincts de {0,...,i}
        l_elems = random.sample(range(i),nb_tests)
        if fonction is "recherche":
            t = timeit.timeit('recherche_liste(arbre,l_elems)',number=1,globals={'recherche_liste':recherche_liste,'arbre': arbre,'l_elems':l_elems})
        if fonction is "insertion":
            t = timeit.timeit('insertion_liste(arbre,l_elems)',number=1,globals={'insertion_liste':insertion_liste,'arbre': arbre,'l_elems':l_elems})
        if fonction is "suppression":
            t = timeit.timeit('suppression_liste(arbre,l_elems)',number=1,globals={'suppression_liste':suppression_liste,'arbre': arbre,'l_elems':l_elems})
        l_taille.append(i)
        l_temps.append(t/(nb_tests*1.0))
        if(i<5000):
            i=i+20
        else:
            i=i+100
    l_log = [math.log(x,2) for x in l_taille]
    taux = l_taille[len(l_taille)//2]/l_temps[len(l_temps)//2]
    l_temps_bis = [x*taux for x in l_temps]
    l_const = [l_temps[k]/l_log[k] for k in range(len(l_temps))]
    fig = plt.figure()
    strtaux = "{:.2f}".format(taux)
    plt.plot(l_taille,l_temps_bis,label="temps moyen mesuré, multiplié par "+strtaux+" pour comparer avec la courbe linéaire")
    plt.plot(l_taille,l_taille,label="y=x")
    plt.xlabel("taille")
    plt.ylabel("temps d'exécution")
    fig.suptitle("temps d'exécution en fonction de la taille pour la fonction "+fonction)
    plt.legend()  
    plt.show()
    if(nom_fichier is not None):
        fig.savefig(nom_fichier)
    
    
        
    
    
    
def hauteur_max(n):
    h = 0
    for i in range(5):
         l_arbres = batch_tree_BST(n,1000) 
         freq_haut = distribution_hauteur_BST(l_arbres)
         listes = sorted(freq_haut.items())
         x,y = zip(*listes)
         temp = x[len(x)-1]
         if temp>h:
             h=temp
    
    return h

