# -*- coding: utf-8 -*-

import random
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import csv




class Arbre:
	
	"""les fonctions modifient l'abre sur lesquels elles sont appelées:
		il faut faite T.insertion(x) pour insérer T, pas besoin de faire T = T.insertion(x)"""
	def __init__(self,clef,gauche = None,droit = None):
		self.clef=clef
		self.gauche=gauche
		self.droit=droit
		
	def getClef(self):
		return self.clef
	
	def filGauche(self):
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
	
	def suppressionMax(self):
		#on cherche le noeud le plus à droite
		while(self.droit is not None):
			self = self.droit
		#on le remplace par son sous arbre gauche
		self = self.gauche
	
	def suppressionRacine(self):
		if self.clef is not None:
			if self.gauche is not None:
				self.clef = self.gauche.Max()
				self.gauche.suppressionMax()
				
	
	def suppression(self,x):
		if self.clef == None:
			return self
		if x==self.clef:
			if self.estFeuille():
				return None
			if Arbre.estVide(self.gauche):
				return self.droit
			if Arbre.estVide(self.droit):
				return self.gauche
			else:
				y=self.gauche.Max()
				return Arbre(y,self.gauche.suppression(y),self.droit)
		if x<self.clef:
			return Arbre(self.clef,self.gauche.suppression(x),self.droit)
		return Arbre(self.clef,self.gauche,self.droit.suppression(x))
	
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
		if self.clef == None:
			return
		if self.gauche is not None:
			self.gauche.parcoursInfixe()
		print(self.clef,end=' ')
		if self.droit is not None:
			self.droit.parcoursInfixe()
			
	def parcoursPostfixe(self):
		"""postfixe = suffixe... affichage gauche puis droit puis racine"""
		if self.clef == None:
			return
		if self.gauche is not None:
			self.gauche.parcoursInfixe()
		if self.droit is not None:
			self.droit.parcoursInfixe()
		print(self.clef,end=' ')
		
	def parcoursPrefixe(self):
		"""affichage racine puis gauche puis droit"""
		if self.clef == None:
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
	


	
"""tests experimentaux"""

def testMasseRecherche(t,h):
	"""t = nombre de test à chaque taille d'arbre
	h = hauteur d'arbre"""
	Ln = []
	Lres = []
	j=10
	while(j<=2**h-1):
		#on ne créé qu'un arbre, mais on fait t recherches
		arbre = arbreAleatoire(j,1500)
		Lt = []
		e = random.randrange(0,1500)
		for i in range(t):
			
			tdeb = time.perf_counter()
			T = arbre.recherche(e)
			tfin = time.perf_counter()-tdeb
			Lt.append(tfin)
		Lres.append(np.median(Lt))
		Ln.append(j)
		j = j*2
	return (Ln,Lres)
	
def graphe(L1,L2): #graphe obtenu par les mesures
    x = np.array(L1)
    y = np.array(L2)
    fig = plt.figure()
    plt.xlim(L1[0],L1[len(L1)-1])
    plt.plot(x,y)
    fig.savefig('CalculRecherche.png')
    #plt.show()

(L1,L2) = testMasseRecherche(50,30)
graphe(L1,L2)
    
    

		
			
