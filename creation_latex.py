# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 18:50:13 2019

@author: Serge

Fonctions permettant de générer le code latex d'un arbre en txt. Il suffit de
les coller dans un fichiter TeX pour les afficher ensuite.
Le fichier TeX devra avoir en import :

"""


from Implementation_ABR import *

def creationNoeud(clef):
	return "\\node [vertex] {$"+str(clef)+"$}"

def ajoutNoeudGauche(clef,s,i):
	if(s is None):
		print("probleme arbre vide, il faut créer une racine d'abord) \n")
		return
	indent =""
	for j in range(i):
		indent += " "
	s += "\n"
	s += indent+"child{\n"
	s += indent +"   "
	s += "\\node [vertex, left] {$"+str(clef)+"$}"
	s += "\n"
	return s

def ajoutNoeudDroite(clef,s,i):
	if(s is None):
		print("probleme arbre vide, il faut créer une racine d'abord) \n")
		return
	
	indent =""
	for j in range(i):
		indent += " "
	s += "\n"
	s += indent+"child{\n"
	s += indent +"   "
	s += "\\node [vertex, right] {$"+str(clef)+"$}"
	s += "\n"
	return s

def ajoutNoeud(clef,s,i):
	if(clef is None):
		print("probleme arbre vide, il faut créer une racine d'abord) \n")
		return
	
	indent =""
	for j in range(i):
		indent += " "
	s += "\n"
	s += indent+"child{\n"
	s += indent +"   "
	s += "\\node [vertex] {$"+str(clef)+"$}"
	s += "\n"
	return s
	
def fermerNoeud(s,i):
	indent = ""
	for j in range(i):
		indent += " "
	s+= "} \n"
	return s

def indente(n):
	s =" "
	for i in range(n):
		s+=" "
	return s

def arbreToTex(arbre,racine,s,i):
	"""il faut appeler cet fonction avec racine à True
	et indendation à 0"""
	#premier appel : on créer la racine
	if racine:
		s = creationNoeud(arbre.clef)
		#si l'arbre est réduit à une racine on renvoit le code de la racine
		if arbre.estFeuille():
			return s
		else:
			s = arbreToTex(arbre.gauche,False,s,i+4)
			s = arbreToTex(arbre.droit,False,s,i+4)
		
	#cas de base : feuille atteinte
	if arbre is None:
		return s

	#on est dans les appels récursifs
	s += ajoutNoeud(arbre.clef,s,i+4)
	s += arbreToTex(arbre.gauche,False,s,i+4)
	s += arbreToTex(arbre.droit,False,s,i+4)
	s += fermerNoeud(s,i+4)
	
	
			
