# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:26:11 2019

@author: Serge
"""

class ArbreBinaire():
    def __init__(self,clef,gauche = None ,droite = None):
        """ Anything x ArbreBinaire x ArbreBinaire -> ArbreBinaire
        Constructeur d'arbre"""
        self.clef = clef
        self.gauche = gauche
        self.droite = droite
        
    
        
    def filsGauche(self):
        """renvoie le sous arbre gauche"""
        if self == None :
            return None
        return self.gauche
    
    def filsDroit(self):
        """renvoie le sous arbre droit"""
        if self == None :
            return None
        return self.droite
    
    
        
    
    