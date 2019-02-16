class Arbre:
	def __init__(self,clef,gauche,droit):
		self.clef=clef
		self.gauche=gauche
		self.droit=droit
#c'est plus simple de ne pas mettre les fonction dans la classe car je me retrouve toujours à acceder à un objet null
def estVide(T):
	if T is None or T.clef is None and T.gauche is None and T.droit is None :
		return True
	return False

def insertion(x,T):
	if estVide(T):
		return Arbre(x,None,None)
	if x==T.clef:
		return T
	if x<T.clef:
		return Arbre(T.clef,insertion(x,T.gauche),T.droit)
	return Arbre(T.clef,T.gauche,insertion(x,T.droit))

#fonction utilisé dans suppression
def Max(T):
	if estVide(T):
		return None
	while not estVide(T.droit):
		T=T.droit
	return T.clef

def recherche(x,T):
	if estVide(T):
		return False
	if x==T.clef:
		return T
	if x<T.clef:
		return recherche(x,T.gauche);
	return recherche(x,T.droit)

def suppression(x,T):
	if estVide(T):
		return T
	if x==T.clef:
		if estVide(T.gauche) and estVide(T.droit):
			return Arbre(None,None,None)
		if estVide(T.gauche):
			return T.droit
		if estVide(T.droit):
			return T.gauche
		else:
			y=Max(T.gauche)
			return Arbre(y,suppression(y,T.gauche),T.droit)
	if x<T.clef:
		return Arbre(T.clef,suppression(x,T.gauche),T.droit)
	return Arbre(T.clef,T.gauche,suppression(x,T.droit))

def parcoursInfixe(T):
	if estVide(T):
		return
	parcoursInfixe(T.gauche);
	print(T.clef,end=' ')#pour avour un affichage sur la meme ligne 
	parcoursInfixe(T.droit)
#le test
def main_loop():
	arbre=Arbre(1,None,None)
	parcoursInfixe(arbre)
	print("\n")
	T=insertion(4,arbre)
	parcoursInfixe(T)
	print("\n")
	T=insertion(2,T)
	T=insertion(7,T)
	parcoursInfixe(T)
	print("\n")
	T=suppression(2,T)
	parcoursInfixe(T)
if __name__=='__main__':
	main_loop()
	