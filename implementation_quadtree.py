class Point:
	def __init__(self,x,y,data):
		self.x=x
		self.y=y
		self.data=data
		
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
	
	def insertion(self,p):
		# on test d'abord si le point à inserer n'est pas en dehors su quadtree
		if not self.rect.contains(p): 
			return
		#on test si on peu diviser encore le quadtree 
		if not self.rect.est_divisible():
			return
		#on regarde sur quel coté on doit inserer le point en coparant les coordonnées 
		#apres avoir trouvé le bon coté si il est nul on le divise en quatre ie on cree un arbre a cet endroit si c'est pas nul on fait un appel recursif
		else:
			if(p.y<=self.rect.y+self.rect.h/2):
				if(p.x<=self.rect.x+self.rect.l/2):
					if(self.NW is None):
						self.NW=Quadtree(Rectangle(self.rect.x,self.rect.y,self.rect.l/2,self.rect.h/2),p)
					else:
						self.NW.insertion(p)
				else:
					if(self.NE is None):
						self.NE=Quadtree(Rectangle(self.rect.x+self.rect.l/2,self.rect.y,self.rect.l/2,self.rect.h/2),p)
					else:
						self.NE.insertion(p)
			else:
				if(p.x<=self.rect.x+self.rect.l/2):
					if(self.SW is None):
						self.SW=Quadtree(Rectangle(self.rect.x,self.rect.y+self.rect.h/2,self.rect.l/2,self.rect.h/2),p)
					else:
						self.SW.insertion(p)
				else:
					if(self.SE is None):
						self.SE=Quadtree(Rectangle(self.rect.x+self.rect.l/2,self.rect.y+self.rect.h/2,self.rect.l/2,self.rect.h/2),p)
					else:
						self.SE.insertion(p)
						
						
	def recherche(self,p):
		# on test d'abord si le point est en dehors du quadtree
		if not self.rect.contains(p): 
			return None
		#la on est sure que le point est present donc si on peu plus diviser encore le quadtree on le renvoie
		if not self.rect.est_divisible():
			return self
		#on cherche le coté ou se trouve le point s'il est null ca veut dire le point n'existe pas sinon on fait un appel recursif
		else:
			if(p.y<=self.rect.y+self.rect.h/2):
				if(p.x<=self.rect.x+self.rect.l/2):
					if(self.NW is None):
						return self
					else:
						return self.NW.recherche(p)
				else:
					if(self.NE is None):
						return self
					else:
						return self.NE.recherche(p)
			else:
				if(p.x<=self.rect.x+self.rect.l/2):
					if(self.SW is None):
						return self
					else:
						return self.SW.recherche(p)
				else:
					if(self.SE is None):
						return self 
					else:
						return self.SE.recherche(p)
