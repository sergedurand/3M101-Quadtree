class Point:
	def __init__(self,x,y,data):
		self.x=x
		self.y=y
		self.data=data
	def equals(self,p):
		if self.x==p.x and self.y==p.y and self.data==p.data:
			return True
		return False
		
	def affiche_point(self):
		if self is None:
			print("le point est vide")
		print("(",self.x,",",self.y,",",self.data,")")
		
class Rectangle:
	def __init__(self,x,y,l,h):
		self.x=x
		self.y=y
		self.l=l
		self.h=h
		
	def contains(self,point):
		x=point.x
		y=point.y
		if not self.x<= x <=self.x+self.l:
			return False
		if not self.y<=y<=self.y+self.h:
			return False
		return True
		
		
	def est_divisible(self):
		if (self.l<=1 or self.h<=1):
			return False
		return True
		
class Quadtree():
	""" __________
		| NW | NE |
		----------
		| SW | SE |
		----------  """
	def __init__(self,rect,point,NW=None,NE=None,SW=None,SE=None):
		self.rect=rect
		self.point=point
		self.NW, self.NE, self.SW, self.SE = NW, NE, SW, SE
	
	def est_feuille(self): 
		if self is None:
			print("arbre vide")
			return
		if self.NW is None and self.NE is None and self.SE is None and self.SW is None:
			return True
		return False
			
	
	def nb_fils(self):
		"""compte le nombre de fils non nuls d'un quadrant donné(pas de l'arbre en entier), ça retourn un entier entre 0 et 4, on l'utilise dans la suppression """
		cpt=0
		if self.NW.point is not None:
			cpt=cpt+1
		if self.NE.point is not None:
			cpt=cpt+1
		if self.SE.point is not None:
			cpt=cpt+1
		if self.SW.point is not None:
			cpt=cpt+1
		return cpt
			
	def subdiviser(self):
		"""fonction pour diviser un quadtree courant en 4, elle est utile pour l'insertion"""
		if self is None:
			return
		elif self.rect.est_divisible():
			self.NW=Quadtree(Rectangle(self.rect.x,self.rect.y,self.rect.l/2,self.rect.h/2),None)
			self.NE=Quadtree(Rectangle(self.rect.x+self.rect.l/2,self.rect.y,self.rect.l/2,self.rect.h/2),None)
			self.SW=Quadtree(Rectangle(self.rect.x,self.rect.y+self.rect.h/2,self.rect.l/2,self.rect.h/2),None)				
			self.SE=Quadtree(Rectangle(self.rect.x+self.rect.l/2,self.rect.y+self.rect.h/2,self.rect.l/2,self.rect.h/2),None)
		else:
			return
			
			
	def recherche(self,p):
		if self is None:
			print("l'arbre est vide")
			return
		# on test si le point est en dehors du quadtree
		if not self.rect.contains(p): 
			print("cet element n'existe pas dans l'arbre")
			return 
		if self.est_feuille():
			if self.point.equals(p):
				return self
			else:
				print("cet element n'existe pas dans l'arbre")
				return
		elif self.NW.rect.contains(p):
			return self.NW.recherche(p)
		elif self.NE.rect.contains(p):
			return self.NE.recherche(p)
		elif self.SW.rect.contains(p):
			return self.SW.recherche(p)
		else:
			return self.SE.recherche(p)
	def recherche_quadrant(self,p):
		"""cette fonction nous aide pour trouver le quadrant ou on doit inserer un point, c'est le meme code que la fonction recherceh saut q'un ne test pas si le point est prensent  """
		if self is None:
			print("l'arbre est vide")
			return
		# on test si le point est en dehors du quadtree
		if not self.rect.contains(p): 
			print("cet element n'existe pas dans l'arbre")
			return 
		if self.est_feuille():
			return self
		elif self.NW.rect.contains(p):
			return self.NW.recherche(p)
		elif self.NE.rect.contains(p):
			return self.NE.recherche(p)
		elif self.SW.rect.contains(p):
			return self.SW.recherche(p)
		else:
			return self.SE.recherche(p)
	
	def recherche_pere(self,noeud):
		if self.est_feuille():
			return None
		elif self.NW.est_feuille() and self.NE.est_feuille() and self.SE.est_feuille() and self.SW.est_feuille():
				return self
		elif self.NW.rect.contains(noeud.p):
			return self.NW.recherche_pere(noeud)
		elif self.NE.rect.contains(noeud.p):
			return self.NE.recherche_pere(noeud)
		elif self.SE.rect.contains(noeud.p):
			return self.SE.recherche_pere(noeud)
		else:
			return self.SW.recherche_pere(noeud)
		
	def insertion(self,p):
		# on test d'abord si le point à inserer n'est pas en dehors su quadtree
		if not self.rect.contains(p): 
			return
		#on test si on peu diviser encore le quadtree 
		if not self.rect.est_divisible():
			return
		#on cherche le quadrant ou p doit etre inseré 
		noeud=self.recherche_quadrant(p)
		if noeud.point is None:
			noeud.point=p
		else:
			q=noeud.point;#on recupère le point déjà présent
			noeud.point=None
			noeud.subdiviser()
			#on place le point déjà existant la où il faut
			if self.NW.rect.contains(q):
				noeud.NW.point=q
			if self.NE.rect.contains(q):
				noeud.NE.point=q
			if self.SE.rect.contains(q):
				noeud.SE.point=q
			else:
				noeud.SW.point=q
			#on fait des appels recursifs pour inserer p c'est possible aussi qu'il rencontre encore une fois ou plus le point q c'est pour qu'on fait une récursion
			if self.NW.rect.contains(p):
				noeud.NW.insertion(p)
			if self.NE.rect.contains(p):
				noeud.NE.insertion(p)
			if self.SE.rect.contains(p):
				noeud.SE.insertion(p)
			else:
				noeud.SW.insertion(p)
	def fusion(self,noeud):
		"""fonction qui sert dans la suppression si on suprime un point et puis dans le quadrant il ne reste plus qu'n seul noued on doit fusioner ce point avec son pere
			et c'est possible que meme ce pere est aussi le seul fils donc il faut une recursion"""
		pere=self.recherche_pere(noeud.point)
		pere.point=noeud.point
		pere.NW=None
		pere.NE=None
		pere.SE=None
		pere.SW=None
		g_pere=self.recherche_pere(pere.point)
		if g_pereis is None:
			if g_pere.nb_fils()==1:
				self.fusion(pere)
			else:
				return 

	def suppression(self,p):
		if self is None:
			print("arbre vide")
			return
		pere=self.recherche_pere(p)#on recupere le pere
		noeud=self.recherche(p)
		noeud.point=None# on supprime le point 
		nb_fils=pere.nb_fils()
		if nb_fils==1:# on regarde le nombre de fils restant s'il ne reste qu'un seul on doit remplacer le pere pr son fils, 
		#normalement en aucun cas on trouvera un nb_fils =0 apres la suppression, c'est c'est le cas ça voudrai dire quele fils etait seul ce qui n'est pas possible
			self.fusion(noeud)
				
def main_loop():
	print("bonjour")
	rec=Rectangle(0,0,20,20)
	Qd=Quadtree(rec,Point(1,2,0))
	Qd.insertion(Point(11,5,0))
	Qd.insertion(Point(6,7,0))
	#print(Qd.NE is None)
	print(Qd.NW.point.affiche_point())
	
if __name__=='__main__':
	main_loop()