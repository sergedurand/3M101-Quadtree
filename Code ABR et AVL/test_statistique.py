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
        res.append(AVL.AVL_from_list(l))
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
    note = "hauteur médiane = " + str(median(freq_haut)) + "\n"
    note += "hauteur moyenne = " + str(moyenne(freq_haut)) + "\n"
    K = moyenne(freq_haut)/math.log(taille,2)
    stringK = "{:.2f}".format(K)
    note += "K = Hn/Log(n) = " + stringK + "\n"
    note += "hauteur max = " + str(listes[len(listes)-1][0]) + "\n"
    stringLog = "{:.2f}".format(math.log(taille,2))
    note += "log(n) = " + stringLog + "\n"
    note += "n = " + str(taille) + "\n"
    fig = plt.figure(1,figsize=(11,8))
    plt.plot(x,y)
    fig.suptitle("nombre d'arbres en fonction de la hauteur")
    plt.xlabel('hauteur')
    plt.ylabel("nombre d'arbres")
    plt.figtext(0.4, -0.1, note, horizontalalignment='left')
    plt.axvline(K*math.log(taille,2),color="black",label=stringK+"log(n)")
    plt.legend()
    if(nom_fichier is not None):
        fig.savefig(nom_fichier,bbox_inches = 'tight')
    plt.show()
    
    
def graphe_distribution_hauteur_AVL(taille,nom_fichier = None):
    """renvoie le graphe avec les hauteurs en abscisses et le nombre d'arbres en ordonnées,
    pour 1000 arbres étiquetés de 1 à taille aléatoirement """
    l_arbres = batch_tree_AVL(taille,1000)
    freq_haut = distribution_hauteur_AVL(l_arbres)
    listes = sorted(freq_haut.items())
    x,y = zip(*listes)
    print(freq_haut)
    note = "hauteur médiane = " + str(median(freq_haut)) + "\n"
    note += "hauteur moyenne = " + str(moyenne(freq_haut)) + "\n"
    K = moyenne(freq_haut)/math.log(taille,2)
    stringK = "{:.2f}".format(K)
    note += "K = Hn/Log(n) = " + stringK + "\n"
    note += "hauteur max = " + str(listes[len(listes)-1][0]) + "\n"
    stringLog = "{:.2f}".format(math.log(taille,2))
    note += "log(n) = " + stringLog + "\n"
    note += "n = " + str(taille) + "\n"
    note += "données : " + str(freq_haut)
    fig = plt.figure(1,figsize=(11,8))
    plt.plot(x,y)
    fig.suptitle("nombre d'arbres en fonction de la hauteur")
    plt.xlabel('hauteur')
    plt.ylabel("nombre d'arbres")
    plt.figtext(0.4, -0.1, note, horizontalalignment='left')
    plt.axvline(K*math.log(taille,2),color="black",label=stringK+"log(n)")
    plt.legend()
    if(nom_fichier is not None):
        fig.savefig(nom_fichier,bbox_inches = 'tight')
    plt.show()

    
def graphe_complexite_ABR(taille_max,nb_tests,fonction,nom_fichier=False):
    """à chaque étape on créé un arbre binaire, on applique la fonction sur nb_éléments
    aléatoires, on divise par nb_éléments la durée obtenue. On itère sur la taille 
    de l'arbre jusqu'à atteindre un arbre de taille taille_max. Le saut dans 
    l'itération dépend de la valeur de taille_max, on espace les itérations pour 
    les grandes tailles"""
    import timeit
    if(taille_max<100):
        print("insérer un nombre plus grand que 100 pour avoir des données significatives")
        return
    if fonction not in {"suppression","insertion","recherche"}:
        print("le nom de la fonction n'est pas bon. Il faut mettre 'insertion', 'suppression' ou 'recherche'")
        return
    i = 1000
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
    
    while(i<=taille_max):
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
        elif(i<50000):
            i=i+200
        else:
            i=i+500
    l_temps_bis = [x*1000000 for x in l_temps]
    coeff = regression_lineaire(l_taille,l_temps_bis)
    coeff_str  = ["{:.2f}".format(x) for x in coeff]
    if coeff[1] > 0 :
        coeff_str[1] = "+ "+coeff_str[1]
    l_theorique = [coeff[0]*math.log(x,2)+coeff[1] for x in l_taille]
    fig = plt.figure(1,figsize=(11,8))
    plt.plot(l_taille,l_temps_bis,label="temps moyen")
    plt.plot(l_taille,l_theorique,label="y = "+coeff_str[0]+"*log2(n) "+coeff_str[1])
    plt.xlabel("taille de l'arbre")
    plt.ylabel("temps d'exécution en μs")
    fig.suptitle("temps d'exécution de la méthode "+fonction+" en fonction de la taille")
    plt.legend()  
    plt.show()
    if(nom_fichier):
        fig.savefig("ABR_" + "_"+fonction+"_"+str(taille_max)+"_"+str(nb_tests))
    
    
        
def graphe_complexite_AVL(taille_max,nb_tests,fonction,nom_fichier=False):
    """à chaque étape on créé un arbre binaire, on applique la fonction sur nb_éléments
    aléatoires, on divise par nb_éléments la durée obtenue. On itère sur la taille 
    de l'arbre jusqu'à atteindre un arbre de taille taille_max. Le saut dans 
    l'itération dépend de la valeur de taille_max, on espace les itérations pour 
    les grandes tailles"""
    import timeit
    if(taille_max<100):
        print("insérer un nombre plus grand que 100 pour avoir des données significatives")
        return
    if fonction not in {"suppression","insertion","recherche"}:
        print("le nom de la fonction n'est pas bon. Il faut mettre 'insertion', 'suppression' ou 'recherche'")
        return
    i = 1000
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
    
    while(i<=taille_max):
        arbre = AVL.arbreAleatoire(i,i)
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
        elif(i<50000):
            i=i+200
        else:
            i=i+500
    l_temps_bis = [x*1000000 for x in l_temps]
    coeff = regression_lineaire(l_taille,l_temps_bis)
    coeff_str  = ["{:.2f}".format(x) for x in coeff]
    if coeff[1] > 0 :
        coeff_str[1] = "+ "+coeff_str[1]
    l_theorique = [coeff[0]*math.log(x,2)+coeff[1] for x in l_taille]
    fig = plt.figure(1,figsize=(11,8))
    plt.plot(l_taille,l_temps_bis,label="temps moyen")
    plt.plot(l_taille,l_theorique,label="y = "+coeff_str[0]+"*log2(n) "+coeff_str[1])
    plt.xlabel("taille de l'arbre")
    plt.ylabel("temps d'exécution en μs")
    fig.suptitle("temps d'exécution de la méthode "+fonction+" en fonction de la taille")
    plt.legend()  
    plt.show()
    if(nom_fichier):
        fig.savefig("AVL_" + "_"+fonction+"_"+str(taille_max)+"_"+str(nb_tests))
        
def graphe_complexite_comparaison(taille_max,nb_tests,fonction,nom_fichier=False):
    """à chaque étape on créé un arbre binaire, on applique la fonction sur nb_éléments
    aléatoires, on divise par nb_éléments la durée obtenue. On itère sur la taille 
    de l'arbre jusqu'à atteindre un arbre de taille taille_max. Le saut dans 
    l'itération dépend de la valeur de taille_max, on espace les itérations pour 
    les grandes tailles"""
    import timeit
    if(taille_max<100):
        print("insérer un nombre plus grand que 100 pour avoir des données significatives")
        return
    if fonction not in {"suppression","insertion","recherche"}:
        print("le nom de la fonction n'est pas bon. Il faut mettre 'insertion', 'suppression' ou 'recherche'")
        return
    i = 1000
    l_taille_AVL = []
    l_temps_AVL = []
    l_taille_ABR = []
    l_temps_ABR = []
    def recherche_liste(arbre,l_elem):
        for x in l_elem:
            arbre.recherche(x)
    def insertion_liste(arbre,l_elem):
        for x in l_elem:
            arbre.insertion(x)
    def suppression_liste(arbre,l_elem):
        for x in l_elem:
            arbre.suppression(x)
    
    while(i<=taille_max):
        arbre_AVL, arbre_ABR = arbreAleatoireAVLetABR(i,i)
        #génère une liste de nb_tests éléments disctincts de {0,...,i}
        l_elems = random.sample(range(i),nb_tests)
        
        #pour l'AVL
        if fonction is "recherche":
            t = timeit.timeit('recherche_liste(arbre_AVL,l_elems)',number=1,globals={'recherche_liste':recherche_liste,'arbre_AVL': arbre_AVL,'l_elems':l_elems})
        if fonction is "insertion":
            t = timeit.timeit('insertion_liste(arbre_AVL,l_elems)',number=1,globals={'insertion_liste':insertion_liste,'arbre_AVL': arbre_AVL,'l_elems':l_elems})
        if fonction is "suppression":
            t = timeit.timeit('suppression_liste(arbre_AVL,l_elems)',number=1,globals={'suppression_liste':suppression_liste,'arbre_AVL': arbre_AVL,'l_elems':l_elems})
        l_taille_AVL.append(i)
        l_temps_AVL.append(t/(nb_tests*1.0))
        
        #pour l'ABR
        if fonction is "recherche":
            t = timeit.timeit('recherche_liste(arbre_ABR,l_elems)',number=1,globals={'recherche_liste':recherche_liste,'arbre_ABR': arbre_ABR,'l_elems':l_elems})
        if fonction is "insertion":
            t = timeit.timeit('insertion_liste(arbre_ABR,l_elems)',number=1,globals={'insertion_liste':insertion_liste,'arbre_ABR': arbre_ABR,'l_elems':l_elems})
        if fonction is "suppression":
            t = timeit.timeit('suppression_liste(arbre_ABR,l_elems)',number=1,globals={'suppression_liste':suppression_liste,'arbre_ABR': arbre_ABR,'l_elems':l_elems})
        l_taille_ABR.append(i)
        l_temps_ABR.append(t/(nb_tests*1.0))
        

        if(i<5000):
            i=i+20
        elif(i<50000):
            i=i+200
        else:
            i=i+500
     
    #réalisation des courbes pour l'AVL
    l_temps_bis_AVL = [x*1000000 for x in l_temps_AVL]
    coeff_AVL = regression_lineaire(l_taille_AVL,l_temps_bis_AVL)
    coeff_str_AVL  = ["{:.2f}".format(x) for x in coeff_AVL]
    if coeff_AVL[1] > 0 :
        coeff_str_AVL[1] = "+ "+coeff_str_AVL[1]
    l_theorique_AVL = [coeff_AVL[0]*math.log(x,2)+coeff_AVL[1] for x in l_taille_AVL]
    fig = plt.figure(1,figsize=(11,8))
    plt.plot(l_taille_AVL,l_temps_bis_AVL,label="temps moyen AVL")
    plt.plot(l_taille_AVL,l_theorique_AVL,label="AVL : y = "+coeff_str_AVL[0]+"*log2(n) "+coeff_str_AVL[1])
   
    #idem ABR
    l_temps_bis_ABR = [x*1000000 for x in l_temps_ABR]
    coeff_ABR = regression_lineaire(l_taille_ABR,l_temps_bis_ABR)
    coeff_str_ABR  = ["{:.2f}".format(x) for x in coeff_ABR]
    if coeff_ABR[1] > 0 :
        coeff_str_ABR[1] = "+ "+coeff_str_ABR[1]
    l_theorique_ABR = [coeff_ABR[0]*math.log(x,2)+coeff_ABR[1] for x in l_taille_ABR]
    plt.plot(l_taille_ABR,l_temps_bis_ABR,label="temps moyen ABR")
    plt.plot(l_taille_ABR,l_theorique_ABR,label="ABR : y = "+coeff_str_ABR[0]+"*log2(n) "+coeff_str_ABR[1])
    
    plt.xlabel("taille de l'arbre")
    plt.ylabel("temps d'exécution en μs")
    fig.suptitle("temps d'exécution de la méthode "+fonction+" en fonction de la taille")
    plt.legend()  
    plt.show()
    if(nom_fichier):
        fig.savefig("comparaison_AVL_ABR_" + "_"+fonction+"_"+str(taille_max)+"_"+str(nb_tests))
    
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

def arbreAleatoireAVLetABR(n,m):
    """renvoie un arbre AVL et un arbre ABR de taille n 
    initialisé par des valeurs entre 0 et m.
    L'ordre d'insertion est le même pour les deux arbres"""
    L = random.sample(range(m),n)
    return (AVL.AVL_from_list(L),ABR.BST_from_list(L))

def regression_lineaire(L1,L2):
    """on suppose que L1 et L2 contiennent le meme nombre de données
    qui sont de la forme Y = Alog(X) + B, X dans L1 et Y dans L2
    la fonction renvoie [A,B]"""
    L1b = [math.log(x,2) for x in L1]
    coeff = np.polyfit(L1b,L2,1)
    return coeff

def creation_ABR(taille):
    """créé un ABR par insertion successive d'éléments en ordre croissant
    renvoie la durée nécessaire à la création, en micro secondes"""
    L = [x for x in range(taille)]
    BST_from_list = ABR.BST_from_list
    import timeit
    t = timeit.timeit("BST_from_list(L)",number=100,globals={'BST_from_list':BST_from_list,'L':L})
    return t

def creation_AVL(taille):
    """créé un AVL par insertion successive d'éléments en ordre croissant
    renvoie la durée nécessaire à la création, en micro secondes"""
    L = [x for x in range(taille)]
    AVL_from_list = AVL.AVL_from_list
    import timeit
    t = timeit.timeit("AVL_from_list(L)",number=100,globals={'AVL_from_list':AVL_from_list,'L':L})
    return t