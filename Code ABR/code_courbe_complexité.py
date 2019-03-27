#pip install xlwt -> Commande à taper dans la console avant d'exécuter le programme
import random
import time
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import csv
import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)
            
    def delete(self,val):
        if(self.root != None):
            return self._delete(val, self.root)
        else:
            return None
            
    def _delete(self, val, node):
        if(val == node.v):
            node.v=None
        elif(val < node.v and node.l != None):
            self._delete(val, node.l)
        elif(val > node.v and node.r != None):
            self._delete(val, node.r)        
            

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print (str(node.v) + ' ')
            self._printTree(node.r)
    
    def vide(self):
        if self.root==None:
            return True
        return False
    
    def height(self):
        return trueheight(self.root)
            
def trueheight(node):
    if node==None:
        return 0
    else:
        return 1 + max(trueheight(node.l), trueheight(node.r))

def nodevide(node):
    if node==None:
        return True
    return False
            
    
        
    
        

    
            
def arbreRd(deb,n,m):
	res = Tree()
	res.add(deb)
	for i in range(n):
		x = random.randrange(0,m)
		res.add(x)
	return res         

def testMasseRecherche(t): #Le paramètre t correspond au nombre de mesures effectuées pour chaque arbre d'une taille donnée
    val=1000000000000
    Ln = []
    Lres = []
    listetaille=[10,100,500]
    for i in range(1,21): #Grand nombre de mesures sur les faibles valeurs de n pour éviter le bruit informatique
        listetaille.append(i*1000)
    for i in range(2,5): #Faible nombre de mesures pour les grandes valeurs de n pour éviter un  long temps d'exécution et des crash
        listetaille.append(i*15000)
    """for i in range(7,14):
        listetaille.append(i*30000)"""
    for j in (listetaille):
        #on ne créé qu'un arbre, mais on fait t recherches
        liste=listeparfaite(j)
        arbre=perfectTree(liste)
        Lt=[]
        for i in range(t):
            #e = random.randrange(0,j)
            tdeb = time.perf_counter()
            T = arbre.find(val) #La fonction de recherche est à remplacer par la fonction testée. La valeur val est choisie très grande pour que la fonction aille toujours jusqu'à une feuille
            tfin = time.perf_counter()-tdeb
            Lt.append(tfin)
        Lres.append(np.median(Lt))
        Ln.append(arbre.height())
        list1, list2 = (list(t) for t in zip(*sorted(zip(Ln, Lres))))
    return (list1,list2)
            

def perfect_tree_partition(n):
    """find the point to partition n keys for a perfect binary tree"""
    x = 1

    # find a power of 2 <= n//2
    # while x <= n//2:  # this loop could probably be written more elegantly :)
    #     x *= 2
    x = 1 << (n.bit_length() - 1)   # indeed you can

    if x//2 - 1 <= (n-x):
        return x - 1      # case 1
    else:
        return n - x//2 
    
def arbreparfait(n):
    i=perfect_tree_partition(n)
    arbre=Tree()
    arbre.add(i)
    print(i)
    arbre.add(n-i)
    print(n-i)
    while (i>0):
        i=perfect_tree_partition(i)
        arbre.add(i)
        arbre.add(n-i)
        print(i)
        print(n-i)
    return arbre

def listeparfaite(n):
    l=[int(n/2)]
    for i in range(math.floor(n)):
        if (int(l[math.floor((i-1)/2)]/2) not in l):
            l.append(int(l[math.floor((i-1)/2)]/2))
        if (int(3*l[math.floor((i-1)/2)]/2)+1 not in l):
            l.append(int(3*l[math.floor((i-1)/2)]/2)+1)
    return l
    

def perfectTree(liste):
    arbre=Tree()
    for elt in liste:
        arbre.add(elt)
    return arbre

            #     3
# 0     4
#   2      8
            
"""tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print (tree.find(3).v)
print (tree.find(10))
tree.deleteTree()
tree.printTree()"""


def graphe(L1,L2): #graphe obtenu par les mesures
    x = np.array(L1)
    y = np.array(L2)
    fig = plt.figure()
    plt.xlim(L1[0],L1[len(L1)-1])
    plt.plot(x,y)
    fig.savefig('CalculRecherche.png')
    plt.show()

(L1,L2) = testMasseRecherche(100)
graphe(L1,L2)
for i,e in enumerate(L1):
    sheet1.write(i,1,e)
for i,e in enumerate(L2):
    sheet1.write(i,2,e)
name = "finalrecherche.xls"
book.save(name)
book.save(TemporaryFile())
