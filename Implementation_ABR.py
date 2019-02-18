import random


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
			if not self or not (self.clef or self.gauche or self.droit):
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
				#cas où le sous arbre droite est vide
				else :
					self.droit = Arbre(x)
			#s'il y a égalité il n'y a rien à faire
			else:
				return
			
		#cas ou l'arbre est vide
		else:
			self.clef = x
	

	#fonction utilisé dans suppression
	def Max(self):
		if not self:
			return None
		while (self.droit is not None):
			self=self.droit
		return self.clef

	def recherche(self,x):
		if self.clef == None:
			return False
		if x==self.clef:
			return self
		if x<self.clef:
			if self.gauche is not None:
				return self.gauche.recherche(x)
			else :
				return False
		else:
			if self.droit is not None:
				return self.droit.recherche(x)
			else: 
				return False
	
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
	
	def parcoursInfixe(self):
		if self.clef == None:
			return
		if self.gauche is not None:
			self.gauche.parcoursInfixe()
		print(self.clef,end=' ')
		if self.droit is not None:
			self.droit.parcoursInfixe()
			
	def copy(self):
		"""renvoie une copie de l'arbre
		utilise un parcours en largeur itératif"""
		res = Arbre(None)
		#file
		if self.clef == None:
			return res
		else:
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
		
		
	
	
				
def arbreAleatoire(n,m):
	"""renvoie un BSR de taille n initialisé par des valeurs entre 0 et m"""
	res = Arbre(None,None,None)
	for i in range(n):
		x = random.randrange(0,m)
		print("x = ",x)
		res.insertion(x)
	return res

		
#le test
def main_loop():
	T=Arbre(1,None,None)
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
	main_loop()
	