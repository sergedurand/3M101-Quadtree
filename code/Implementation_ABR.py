# -*- coding: utf-8 -*-


import random
import time
import sys
import itertools as it


class Arbre:
    
    def __init__(self,clef,gauche = None,droit = None):
        self.clef=clef
        self.gauche=gauche
        self.droit=droit
        
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
        """modification en place : il faut faire l'appel via :
        T = T.insertion(x)"""
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
    
    def insertion_cpt(self,x,cpt=0):
        """ébauche non testée qui visait à compter
        le nombre d'opérations effectuées lors d'une insertion"""
        if self.clef is not None:
            if x<self.clef:
                cpt += 1
                if self.gauche is not None:
                    cpt = self.gauche.insertion_cpt(x,cpt)
                    return cpt
                #cas où le sous arbre gauche est vide
                else :
                    cpt += 1
                    self.gauche = Arbre(x)
                    return cpt
                
            elif x > self.clef:
                cpt += 1
                if self.droit is not None:
                     cpt = self.droit.insertion_cpt(x,cpt)
                     return cpt
                #cas où le sous arbre droit est vide
                else :
                    self.droit = Arbre(x)
                    return cpt
            #s'il y a égalité il n'y a rien à faire
            
        #cas ou l'arbre est vide
        else:
            self.clef = x
            return cpt
            
            
    def Max(self):
        """renvoie l'étiquette max présente dans l'arbre"""
        if self.clef == None:
            return None
        while (self.droit is not None):
            self=self.droit
        return self.clef
    
    def Min(self):
        """renvoie l'étiquette min présente dans l'arbre"""
        if self.clef == None:
            return None
        while(self.gauche is not None):
            self = self.gauche
        return self.clef
    
    def recherche(self,x):
        """renvoie le sous arbre dont x est la racine si
        x est dans l'arbre, False sinon"""
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
        """renvoie True si l'arbre est une feuille.
        On renvoit False si l'arbre est vide"""
        if self.clef == None:
            return False
        return (self.gauche == None and self.droit == None)
    

    def suppression(self,x):
        """on fait l'hypothèse que x est forcément dans l'arbre"""
        #cas 1 : arbre vide
        if(self.clef is None):
            return None
        #appels récursifs:
        if x < self.clef:
            if self.gauche is None:
                return self
            else:
                self.gauche = self.gauche.suppression(x)
        elif x > self.clef:
            if self.droit is None:
                return self
            else:
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
    
    def display(self):
        """renvoie un affichage sous forme d'arbre.
        le mieux est de tester la fonction"""
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)
        print("")

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.droit is None and self.gauche is None:
            line = '%s' % self.clef
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.droit is None:
            lines, n, p, x = self.gauche._display_aux()
            s = '%s' % self.clef
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.gauche is None:
            lines, n, p, x = self.droit._display_aux()
            s = '%s' % self.clef
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.gauche._display_aux()
        right, m, q, y = self.droit._display_aux()
        s = '%s' % self.clef
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2   
            
def BST_from_list(L):
    """construit un ABR par insertion successives
    des éléments de la liste L. L doit contenir des entiers"""
    res = Arbre(None,None,None)
    for x in L:
        res.insertion(x)
    return res    


def arbreAleatoire(n,m):
    """renvoie un BSR de taille n initialisé par des valeurs entre 0 et m"""
    L = random.sample(range(m),n)
    return BST_from_list(L)


def liste_complete_arbre(n):
    """renvoie tout les arbres étiquetés entre 1 et n, avec doublons éventuels
    lorsque deux permutations produisent le même arbre"""
    L = it.permutations([x for x in range(1,n+1)])
    res = []
    for l in L:
        res.append(BST_from_list(list(l)))
    return res

def analyse_hauteur_max(liste_arbre,n):
    """renvoie le nombre d'arbre atteignant la hauteur
    maximum possible = n.
    on suppose que les arbres sont tous de taille n"""
    cpt = 0
    for arbre in liste_arbre:
        if arbre.hauteur()==n:
            cpt += 1
    
    return cpt

def analyse_hauteur_max_n(n):
    liste_arbre = liste_complete_arbre(n)
    c = analyse_hauteur_max(liste_arbre,n)
    freq = float(c)/len(liste_arbre)
    print("nombre total d'arbre de taille et de hauteur " + str(n) + " = " + str(c))
    return(round(freq*100,1))

def analyse_hauteur_borne(liste_arbre,k):
    """renvoie le nombre d'arbre dont la hauteur dépasse k"""
    cpt = 0
    for arbre in liste_arbre:
        if arbre.hauteur()>=k:
            cpt += 1
    
    return cpt

def analyse_hauteur_borne_k(k,n):
    liste_arbre = liste_complete_arbre(n)
    c = analyse_hauteur_borne(liste_arbre,k)
    freq = float(c)/len(liste_arbre)
    print("nombre total d'arbre de taille " +str(n) + " dont la hauteur est superieure ou égale à " + str(k) + " = " + str(c))
    return(round(freq*100,1))

    

#le test
def main_loop():
    print("creation d'un arbre de 6 noeuds aléatoire et affichage des trois parcours : infixe, suffixe puis préfixe")
    arbre = arbreAleatoire(6,6)
    arbre.parcoursInfixe()
    print("")
    time.sleep(1.5)
    arbre.parcoursPostfixe()
    print("")
    time.sleep(1.5)
    arbre.parcoursPrefixe()
    print("")
    time.sleep(1.5)
    print("affichage comme arbre")
    time.sleep(1.5)
    arbre.display()
    time.sleep(1.5)
    print("recherche de 3, on affiche le sous arbre dont 3 est la racine")
    time.sleep(1.5)
    arbre1 = arbre.recherche(3)
    arbre1.display()
    time.sleep(1.5)
    print("suppression de 3")
    time.sleep(1.5)
    arbre2 = arbre.suppression(3)
    arbre2.display()
    time.sleep(1.5)
    print("insertion de 8")
    time.sleep(1.5)
    arbre2.insertion(8)
    arbre2.display()
    time.sleep(1.5)
    print("hauteur = " + str(arbre2.hauteur()) + " , taille = " + str(arbre2.taille()))
    
    
if __name__=='__main__':
    main_loop()
    


    