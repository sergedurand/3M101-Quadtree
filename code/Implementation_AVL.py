# -*- coding: utf-8 -*-


import random
import time
import sys


class ArbreAVL:
    
    def __init__(self,clef,gauche = None,droit = None,hauteur = None):
        self.clef=clef
        self.gauche=gauche
        self.droit=droit
        if self.clef is None:
            h=0
        h = 1
        #distinction de cas pour la gestion de la hauteur
        if gauche is not None :
            if droit is None :
                h=h+gauche.hauteur
            else:
                h=h+max(droit.hauteur,gauche.hauteur)
        else:
            if droit is not None:
                h=h+droit.hauteur
        self.hauteur = h
        
        
    def getClef(self):
        return self.clef
    
    def filsGauche(self):
        return self.gauche
    
    def filsDroit(self):
        return self.droit
    
    def setClef(self,x):
        self.clef = x
    
        
    def estVide(self):
        return self.clef == None


    def insertion(self,x):
        """insertion de l'élément x à sa position attendue.
        on maintient l'arbre équilibré. Si x est déjà dedans on
        ne fait aucune modification. Ce n'est pas un algorithme en place,
        il faut l'appeler par :
        T = T.insertion(x)"""
        T_x = ArbreAVL(x)
        if self.clef is None:
            self.clef = x
            return self
        
        else:
            temp = self
            parents = []
            while(temp is not None):
                parents.append(temp)
                pere_insertion = temp
                if T_x.clef == temp.clef:
                    return self
                if T_x.clef > temp.clef:
                    temp = temp.droit
                else:
                    temp = temp.gauche
            #on fait l'insertion, en mettant à jour la hauteur :
            if T_x.clef > pere_insertion.clef :
                pere_insertion.droit = T_x
                if pere_insertion.gauche is None:
                    pere_insertion.hauteur = 1
            else:
                pere_insertion.gauche = T_x
                if pere_insertion.droit is None:
                    pere_insertion.hauteur = 1
            
            #on repasse sur tout les parents pour rééquilibrer:
            while(len(parents)>0):
                y = parents.pop()
                y.hauteur = y.updateHauteur()
                y = y.reequilibrageFils()
                
            y = self.reequilibrageFils()
            return y
        
        

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
    
    
    def updateHauteur(self):
        """met la hauteur de l'arbre à jour. à utiliser
        après mise à jour des hauteurs des sous arbres"""
        if self.droit is None:
            if self.gauche is None:
                return 1
            else:
                return 1+self.gauche.hauteur
        else:
            if self.gauche is None:
                return 1+self.droit.hauteur
            else:
                return 1+max(self.gauche.hauteur,self.droit.hauteur)
            
            

    def suppression(self,x):
        """on fait l'hypothèse que x est forcément dans l'arbre
        appel : T = T.suppression(x)"""
        #cas 1 : arbre vide
        if(self.clef is None):
            return self
        else:
            temp = self
            parents = []
            parent_cour = None
            #identification de la position du noeud à supprimer
            while(temp.clef!=x):
                parent_cour = temp
                parents.append(parent_cour)
                if x < temp.clef:
                    temp = temp.gauche
                else:
                    temp = temp.droit

            #gestion suppression, distinction de cas comme pour ABR
            if temp.gauche is None:
                if temp.droit is not None:
                    if temp.droit.droit is None:
                        t_droit = None
                    else:
                        t_droit = temp.droit.droit
                    if temp.droit.gauche is None:
                        t_gauche = None
                    else:
                        t_gauche = temp.droit.gauche
                    temp.clef = temp.droit.clef
                    temp.droit = t_droit
                    temp.gauche = t_gauche
                else:
                    if parent_cour is not None:
                        if x < parent_cour.clef:
                            parent_cour.gauche = None
                        else:
                            parent_cour.droit = None
                            
            elif temp.droit is None:
                if temp.gauche.droit is None:
                    t_droit = None
                else:
                    t_droit = temp.gauche.droit
                
                if temp.gauche.gauche is None:
                    t_gauche = None
                else:
                    t_gauche = temp.gauche.gauche
                    
                temp.clef = temp.gauche.clef
                temp.gauche = t_gauche
                temp.droit = t_droit
            else: #cas ou les deux fils sont non vides
                succ = temp.droit.Min()
                temp.clef = succ
                temp.droit = temp.droit.suppression(succ)
                
            while(len(parents)>0):
                y = parents.pop()
                y.hauteur = y.updateHauteur()
                y = y.reequilibrageFils()
            
            y = self.reequilibrageFils()
            return y
            

    def suppression_affichage(self,x):
        """suppression avec affichage des rééquilibrages"""
        #cas 1 : arbre vide
        if(self.clef is None):
            return self
        else:
            temp = self
            parents = []
            parent_cour = None
            #identification de la position du noeud à supprimer
            while(temp.clef!=x):
                parent_cour = temp
                parents.append(parent_cour)
                if x < temp.clef:
                    temp = temp.gauche
                else:
                    temp = temp.droit
    
            #gestion suppression, distinction de cas comme pour ABR
            if temp.gauche is None:
                if temp.droit is not None:
                    if temp.droit.droit is None:
                        t_droit = None
                    else:
                        t_droit = temp.droit.droit
                    if temp.droit.gauche is None:
                        t_gauche = None
                    else:
                        t_gauche = temp.droit.gauche
                    temp.clef = temp.droit.clef
                    temp.droit = t_droit
                    temp.gauche = t_gauche
                else:
                    if parent_cour is not None:
                        if x < parent_cour.clef:
                            parent_cour.gauche = None
                        else:
                            parent_cour.droit = None
                            
            elif temp.droit is None:
                if temp.gauche.droit is None:
                    t_droit = None
                else:
                    t_droit = temp.gauche.droit
                
                if temp.gauche.gauche is None:
                    t_gauche = None
                else:
                    t_gauche = temp.gauche.gauche
                    
                temp.clef = temp.gauche.clef
                temp.gauche = t_gauche
                temp.droit = t_droit
            else: #cas ou les deux fils sont non vides
                succ = temp.droit.Min()
                temp.clef = succ
                temp.droit = temp.droit.suppression(succ)
                
            while(len(parents)>0):
                y = parents.pop()
                y.hauteur = y.updateHauteur()
                print("sous arbre à rééquilibrer : ")
                time.sleep(1)
                y.display()
                print("")
                time.sleep(1.5)
                y = y.reequilibrageFils()
                time.sleep(1)
                print("après rééquilibrage : ")
                time.sleep(1)
                y.display()
                time.sleep(1.5)
                
                
            y = self.reequilibrageFils()
            return y  
    
    def hauteur(self):
        """convention : arbre vide de hauteur 0
        arbre réduit à un noeud : hauteur 1"""
        if self.clef == None:
            return 0
        return self.hauteur
        
    
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
        """postfixe = suffixe
        affichage gauche puis droit puis racine"""
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
        """On renvoit la hauteur minimale.
        convention : arbre vide de hauteur 0
        arbre réduit à un noeud : hauteur 1"""
        if self.clef == None:
            return 0
        if self.gauche is None and self.droit is None:
            return 1
        if self.gauche is None:#l'arbre droit est forcément non vide
            return self.droit.hauteurMin()+1
        if self.droit is None:#l'arbre gauche est forcément non vide
            return self.gauche.hauteurMin()+1
        #les deux fils sont non vide:
        return min(self.gauche.hauteurMin(),self.droit.hauteurMin())+1

    def hauteurMax(self):
        """convention : arbre vide de hauteur 0
        arbre réduit à un noeud : hauteur 1"""
        if self.clef == None:
            return 0
        if self.gauche is None and self.droit is None:
            return 1
        if self.gauche is None:#l'arbre droit est forcément non vide
            return self.droit.hauteurMax()+1
        if self.droit is None:#l'arbre gauche est forcément non vide
            return self.gauche.hauteurMax()+1
        #les deux fils sont non vide:
        return max(self.gauche.hauteurMax(),self.droit.hauteurMax())+1
        
    def coeffEquilibre(self):
        """retourne la difference entre
        la hauteur du sous arbre droit et celle du sous arbre gauche
        un résultat négatif indique un désequilibre du côté gauche
        (ie le côté gauche est plus gros)"""
        
        if self is None:
            return 0
        if self.gauche is not None :
            if self.droit is None :
                return -self.gauche.hauteur
            else:
                return self.droit.hauteur-self.gauche.hauteur
        else:
            if self.droit is not None:
                return self.droit.hauteur
        return 0
    
    def rotationGauche(self):
        """on fait une rotation gauche à l'arbre.
        Vu qu'on ne peut pas modifier sur place on renvoit un nouvel arbre
        utilisation recommandée : 
        abr = abr.rotationGauche() pour éviter les copies inutiles"""
       
        if self is None: #arbre vide : rien à faire
            return self
        if self.droit is None: #arbre droite vide : rien à faire
            return self
        racine = self.droit.clef
        clef_gauche = self.clef
        arbre_droit = self.droit.droit
        sous_arbre_gauche = self.gauche
        sous_arbre_droit = self.droit.gauche
        arbre_gauche = ArbreAVL(clef_gauche,sous_arbre_gauche,sous_arbre_droit)
        
        return ArbreAVL(racine,arbre_gauche,arbre_droit)
    
    def rotationDroite(self):
        """Renvoie l'arbre
        obtenu après rotation droite, pas de modification en place
        doit être appelé par abr = abr.rotationDroite() """
        racine = self.gauche.clef
        clef_droite = self.clef
        arbre_gauche = self.gauche.gauche
        sous_arbre_gauche = self.gauche.droit
        sous_arbre_droit = self.droit
        arbre_droit = ArbreAVL(clef_droite,sous_arbre_gauche,sous_arbre_droit)
        return ArbreAVL(racine,arbre_gauche,arbre_droit)
        
    def reequilibrageNoeud(self):
        """rééquilibrage de l'arbre à partir d'un noeud dont on sait qu'il a besoin
        d'un rééquilibrage
        dijsonction de cas puis rotations """
        diff_h = self.coeffEquilibre()
        if abs(diff_h) <= 1: #arbre déjà équilibré
            return self
        if diff_h > 1: #cas où le plus grand sous arbre est à droite
            if self.droit.coeffEquilibre() >= 0 :
                return self.rotationGauche()
            else: #le coeff vaut -1 : il faut faire deux rotations successives
                self.droit = self.droit.rotationDroite()
                return self.rotationGauche()
                
        else:#cas symétrique
            if self.gauche.coeffEquilibre() <=0:
                return self.rotationDroite()
            else:
                self.gauche = self.gauche.rotationGauche()
                return self.rotationDroite()


    def reequilibrageFils(self):
        """rééquilibre les deux fils de l'arbre sur lequel 
        la fonction est appelée"""
        if self.gauche is not None:
            self.gauche = self.gauche.reequilibrageNoeud()
        if self.droit is not None:
            self.droit = self.droit.reequilibrageNoeud()
        self.hauteur = self.updateHauteur()
        return self.reequilibrageNoeud()
            
    def copy(self):
        """renvoie une copie de l'arbre
        utilise un parcours en profondeur itératif"""
        res = ArbreAVL(None)
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
        utilise un parcours en profondeur itératif"""
        if self.clef is None:
           return 0
        if self.droit is None:
           if self.gauche is None:
               return 1
           else:
               return 1 + self.gauche.taille()
           
        else:
            if self.gauche is None:
                return 1+self.droit.taille()
            else:
                return 1+self.droit.taille() + self.gauche.taille()
            
    def display(self):
        """renvoie une représentation du graphe dessiné par l'arbre"""
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

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

def AVL_from_list(L):
    res = ArbreAVL(None,None,None)
    for x in L:
        res = res.insertion(x)
    return res
                
def arbreAleatoire(n,m):
    """renvoie un arbre AVL de taille n 
    initialisé par des valeurs entre 0 et m"""
    L = random.sample(range(m),n)
    return AVL_from_list(L)


#le test
def main_loop():
    print("creation d'un arbre aleatoire de 12 éléments")
    arbre = arbreAleatoire(12,12)
    time.sleep(1.5)
    arbre.display()
    time.sleep(1.5)
    print("ajout de 5 éléments")
    for x in range(20,25):
        arbre = arbre.insertion(x)
    time.sleep(1.5)
    arbre.display()
    time.sleep(1.5)
    print("suppression de 5 éléments : ")
    for x in range(2,7):
        arbre = arbre.suppression(x)
    time.sleep(1.5)
    arbre.display()
    print("exemple de suppression étape par étape")
    time.sleep(1)
    print("arbre initial : ")
    arbre = AVL_from_list([x for x in range(20)])
    time.sleep(1)
    arbre.display()
    time.sleep(1.5)
    print("suppression de 16 : ")
    time.sleep(1)
    arbre = arbre.suppression_affichage(16)
    
    
    
    
if __name__=='__main__':
    main_loop()
    
    


    