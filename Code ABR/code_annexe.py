# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 15:36:53 2019

@author: Serge

fonctions qui n'ont pas été retenues...
"""

"""l'approche ci-dessous de la suppression, basée sur le cours 2i003 (cours 8) ne fonctionne pas
	en l'état. Je la laisse en annexe, on a implémenté une autre approche
	qui fonctionne, et qui est celle décrite dans le rapport"""
	
	def suppressionMax(self):
		"""supprime le max d'un arbre"""
		if(self.clef is None):
			return self
		else:
			return self.suppressionMaxNoeud(self)
	
	def suppressionMaxNoeud(self,n):
		"""supprimer le max à partir d'un noeud"""
		if(n.droit is not None):
			n.droit = self.suppressionMaxNoeud(n.droit)
			return n
		else:
			return self.gauche
		
	def suppressionMin(self):
		if(self.clef is None):
			return self
		else: 
			self = self.suppressionMinNoeud(self)
	def suppressionMinNoeud(self,n):
		if(n.gauche is not None):
			n.gauche = self.suppressionMinNoeud(n.gauche)
			return n
		else:
			return self.droit
		
		
	def suppressionRacine(self):
		"""supprime la racine. On choisit de la remplacer par le max
		du sous arbre gauche par défaut, sinon par le min du sous arbre droit"""
		
		if self.clef is not None:
			if self.gauche is not None:
				self.clef = self.gauche.Max()
				self.gauche.suppressionMax()
			elif self.droit is not None:
				self.clef=self.droit.Min()
				self.droit.suppressionMin()
			
			
				
	
	def suppression(self,x):
		"""on suppose que l'élément est forcément dans l'arbre"""
		if self.clef == None:
			return self
		if x==self.clef:
				self.suppressionRacine()
				return self
		if x<self.clef:
			return Arbre(self.clef,self.gauche.suppression(x),self.droit)
		return Arbre(self.clef,self.gauche,self.droit.suppression(x))