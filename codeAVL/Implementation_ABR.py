# -*- coding: utf-8 -*-


import random
import time
import sys


class Arbre:
    
    """les fonctions modifient l'abre sur lesquels elles sont appelées:
        il faut faite T.insertion(x) pour insérer T, pas besoin de faire T = T.insertion(x)"""
    def __init__(self,clef,gauche = None,droit = None,hauteur = None):
        self.clef=clef
        self.gauche=gauche
        self.droit=droit
        self.hauteur
        
    def getClef(self):
        return self.clef
    
    def filsGauche(self):
        return self.gauche
    
    def filsDroit(self):
        return self.droit
    
    def setClef(self,x):
        self.clef = x
    
        
    def estVide(self):
        if self.clef == None:
            return True
        return False

    def insertion(self,x):
        if self.clef is not None:
            if x<self.clef:
                if self.gauche is not None:
                    self.gauche.insertion(x)
                #cas où le sous arbre gauche est vide
                else :
                    self.gauche = Arbre(x)
                
            elif x > self.clef:
                if self.droit is not None:
                     self.droit.insertion(x)
                #cas où le sous arbre droit est vide
                else :
                    self.droit = Arbre(x)
            #s'il y a égalité il n'y a rien à faire
            
        #cas ou l'arbre est vide
        else:
            self.clef = x
    

    #fonction utilisé dans suppression
    def Max(self):
        if self.clef == None:
            return None
        while (self.droit is not None):
            self=self.droit
        return self.clef
    
    def Min(self):
        if self.clef == None:
            return None
        while(self.gauche is not None):
            self = self.gauche
        return self.clef
    
    def recherche(self,x):
        if self.clef == None:
            return False
        
        if x<self.clef:
            if self.gauche is not None:
                return self.gauche.recherche(x)
            else :
                return False
        elif x > self.clef:
            if self.droit is not None:
                return self.droit.recherche(x)
            else: 
                return False
        else: #cas où x == clef
            return self
    
    def estFeuille(self):
        if self.clef == None:
            return False
        return (self.gauche == None and self.droit == None)
    
    
    
    #suppression : on distingue les 3 possibilités en fonction
    #du nombre d'enfant. On sépare les fonction pour la lisibilité
    def suppression(self,x):
        """on fait l'hypothèse que x est forcément dans l'arbre"""
        #cas 1 : arbre vide
        if(self.clef is None):
            return None
        #appels récursifs:
        if x < self.clef:
            #self.gauche n'est pas vide puisque x est dans l'arbre
            self.gauche = self.gauche.suppression(x)
        elif x > self.clef:
            self.droit = self.droit.suppression(x)
        #on a trouvé le noeud qui a x pour clef
        else:
            #si x n'a qu'un fils (ou aucun):
            if self.gauche is None:
                #si le gauche est vide on retourne le fils droit directement
                #qui est éventuellement vide
                temp = self.droit
                self = None
                return temp
            elif self.droit is None:
                #même idée, sauf que self.gauche est forcément non vide ici
                temp = self.gauche
                self = None
                return temp
            else: #c'est le cas où les deux fils sont non vide
                #le successeur de x est le plus petit élément de son sous arbre droit:
                succ = self.droit.Min()
                self.clef = succ
                #il reste à supprimer succ de l'arbre droit :
                self.droit = self.droit.suppression(succ)
                
        return self
                
            
            
    
    
    def hauteur(self):
        """convention : arbre vide de hauteur 0
        arbre réduit à un noeud : hauteur 1"""
        if self.clef == None:
            return 0
        if self.gauche is None and self.droit is None:
            return 1
        if self.gauche is None:#l'arbre droit est forcément non vide
            return self.droit.hauteur()+1
        if self.droit is None:#l'arbre gauche est forcément non vide
            return self.gauche.hauteur()+1
        #les deux fils sont non vide:
        return max(self.gauche.hauteur(),self.droit.hauteur())+1
        
    
    def parcoursInfixe(self):
        """affichage gauche puis racine puis droit"""
        if self.clef is None:
            return
        if self.gauche is not None:
            self.gauche.parcoursInfixe()
        print(self.clef,end=' ')
        if self.droit is not None:
            self.droit.parcoursInfixe()
            
    def parcoursPostfixe(self):
        """postfixe = suffixe... affichage gauche puis droit puis racine"""
        if self.clef is None:
            return
        if self.gauche is not None:
            self.gauche.parcoursInfixe()
        if self.droit is not None:
            self.droit.parcoursInfixe()
        print(self.clef,end=' ')
        
    def parcoursPrefixe(self):
        """affichage racine puis gauche puis droit"""
        if self.clef is None:
            return
        print(self.clef,end=' ')
        if self.gauche is not None:
            self.gauche.parcoursInfixe()
        if self.droit is not None:
            self.droit.parcoursInfixe()
            

    def hauteurMin(self):
        """On renvoit la hauteur miniamal.
        convention : arbre vide de hauteur 0
        arbre réduit à un noeud : hauteur 1"""
        if self.clef == None:
            return 0
        if self.gauche is None and self.droit is None:
            return 1
        if self.gauche is None:#l'arbre droit est forcément non vide
            return self.droit.hauteur()+1
        if self.droit is None:#l'arbre gauche est forcément non vide
            return self.gauche.hauteur()+1
        #les deux fils sont non vide:
        return min(self.gauche.hauteur(),self.droit.hauteur())+1
            
    def coeffEquilibreBis(self):
        """renvoit un indicateur de l'équilibrage de l'arbre :
            différence entre la hauteur min et la hauteur max.
        """
        if self.clef is None:
            return 0
        else:
            return abs(self.hauteur-self.hauteurMin)
        
        
    def coeffEquilibre(self):
        """coefficient plus classique, retourne la difference entre
        la hauteur du sous arbre droit et celle du sous arbre gauche"""
        
        if self is None:
            return 0
        if self.gauche is None and self.droit is None:
            return 0
        if self.gauche is None:
            return self.droit.hauteur
        if self.droit is None:
            return self.gauche.hauteur
        return self.gauche.hauteur - self.droit.hauteur
    
    def rotationGauche(self):
        """on fait une rotation gauche à l'arbre.
        Vu qu'on ne peut pas modifier sur place on renvoit un nouvel arbre
        utilisation recommandée : 
        abr = abr.rotationGauche pour éviter les copies inutiles"""
       
        if self is None: #arbre vide : rien à faire
            return self
        if self.droit is None: #arbre droite vide : rien à faire
            return self
        racine = self.droit.clef
        clef_gauche = self.clef
        arbre_droit = self.droit.droit
        sous_arbre_gauche = self.gauche
        sous_arbre_droit = self.droit.gauche
        return Arbre(racine,Arbre(clef_gauche,sous_arbre_gauche,sous_arbre_droit),arbre_droit)
    
    def rotationDroit(self):
        """rotation droite..."""
        racine = self.gauche.clef
        clef_droite = self.clef
        arbre_gauche = self.gauche.gauche
        sous_arbre_gauche = self.gauche.droit
        sous_arbre_droit = self.droit
        return Arbre(racine,arbre_gauche,Arbre(clef_droite,sous_arbre_gauche,sous_arbre_droit))
        
    def reequilibrage(self):
        """rééquilibrage de l'arbre.
        dijsonction de cas puis rotations """
        if abs(self.coeffEquilibre()) <= 1: #arbre déjà équilibré
            return self
        if self.coeffEquilibre() < -1 #cas où le plus grand sous arbre est à droite
            
        
        
        
    def copy(self):
        """renvoie une copie de l'arbre
        utilise un parcours en largeur itératif"""
        res = Arbre(None)
        if self.clef == None:
            return res
        else:
            #file : on utilise une liste et le pop et le append
            f = []
            f.append(self)
            while(len(f)!=0):
                racine = f.pop()
                res.insertion(racine.clef)
                if racine.gauche is not None:
                    f.append(racine.gauche)
                if racine.droit is not None:
                    f.append(racine.droit)
        return res
        
    def taille(self):
        """renvoie la taille de l'arbre
        utilise un parcours en largeur itératif"""
        cpt = 0
        if self.clef == None:
            return cpt
        else:
            f = []
            f.append(self)
            while(len(f)!=0):
                racine = f.pop()
                cpt += 1
                if racine.gauche is not None:
                    f.append(racine.gauche)
                if racine.droit is not None:
                    f.append(racine.droit)
        return cpt
    
    
                
def arbreAleatoire(n,m):
    """renvoie un BSR de taille n initialisé par des valeurs entre 0 et m"""
    res = Arbre(None,None,None)
    for i in range(n):
        x = random.randrange(0,m)
        res.insertion(x)
    return res


#le test
def main_loop():
    """T=Arbre(1,None,None)
    T.parcoursInfixe()
    print("\n")
    T.insertion(4)
    T.parcoursInfixe()
    print("\n")
    T.insertion(2)
    T.parcoursInfixe()
    print("\n")
    T.insertion(7)
    T.parcoursInfixe()
    print("\n")
    T.suppression(2)
    T.parcoursInfixe()
if __name__=='__main__':
    main_loop()"""
    


    