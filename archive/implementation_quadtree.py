import random
import matplotlib.pyplot as plt
from matplotlib import collections  as mc


class Point():
    def __init__(self, ID, x, y):
        self.ID = ID
        self.x = x
        self.y = y

    def is_equal(self, point):
        return (self.ID == point.ID)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


    def is_NW(self, point):
        """ fonction qui renvoie si le point entré en paramètre se situe au nord-ouest du self
         a.is_NW(b) = True --> le point b est au nord-ouest du point a
        """
        return (self.x >= point.x and self.y < point.y)

    def is_SW(self, point):
        return (self.x > point.x and self.y >= point.y)

    def is_SE(self, point):
        return (self.x <= point.x and self.y > point.y)

    def is_NE(self, point):
        return (self.x < point.x and self.y <= point.y)

    def distance(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** (1 / 2)

class Quadtree():
    def __init__(self, point, NW=None, SW=None, SE=None, NE=None,pere=None): #points cardinaux dans le sens trigonométrique /!\
        self.point = point
        self.NW = NW
        self.SW = SW
        self.SE = SE
        self.NE = NE
        self.pere = pere

    def affiche_Quadtree(self):
        print(self.point.ID, ";")
        if self.NW is not None:
            self.NW.affiche_Quadtree()
        else:
            print('pas de quadrant NW')
        if self.SW is not None:
            self.SW.affiche_Quadtree()
        else:
            print('pas de quadrant SW')
        if self.SE is not None:
            self.SE.affiche_Quadtree()
        else:
            print('pas de quadrant SE')
        if self.NE is not None:
            self.NE.affiche_Quadtree()
        else:
            print('pas de quadrant NE')


    def recherche(self, x):
        """ recherche d'un point x dans le quadtree """
        if self.point.ID is None:
            return "le quadtree est vide"

        if self.point.is_equal(x):
            return self
        else:
            if self.point.is_NW(x):
                if self.NW is not None:
                    return self.NW.recherche(x)
                else:
                    return "le quadrant NW est vide"
            elif self.point.is_SW(x):
                if self.SW is not None:
                    return self.SW.recherche(x)
                else:
                    return "le quadrant SW est vide"
            elif self.point.is_SE(x):
                if self.SE is not None:
                    return self.SE.recherche(x)
                else:
                    return "le quadrant SE est vide"
            elif self.point.is_NE(x):
                if self.NE is not None:
                    return self.NE.recherche(x)
                else:
                    return "le quadrant NE est vide"


    def insertion(self,x):
        """ insertion d'un point x dans le quadtree """
        if self.point is not None:
            if self.point.is_NW(x):
                if self.NW is None:
                    self.NW = Quadtree(x,pere=self)
                else:
                    self.NW.insertion(x)
            elif self.point.is_SW(x):
                if self.SW is None:
                    self.SW = Quadtree(x,pere=self)
                else:
                    self.SW.insertion(x)
            elif self.point.is_SE(x):
                if self.SE is None:
                    self.SE = Quadtree(x,pere=self)
                else:
                    self.SE.insertion(x)
            elif self.point.is_NE(x):
                if self.NE is None:
                    self.NE = Quadtree(x,pere=self)
                else:
                    self.NE.insertion(x)
        else:
            self.point = x

    def is_leaf(self):
        if self.point is None:
            return None
        return (self.NW is None and self.NE is None and self.SW is None and self.SE is None)
    
    #we use a DFS in each direction for the nothernmost point/southernmost etc.
    def northernmost_point(self):
        """return the northernmost node of the tree"""
        if self.point.ID is None:
            print("quadtree is empty")
            return False
        best = self
        L = [self]
        while(len(L)>0):
            node = L.pop()
            if node.point.y > best.point.y :
                best = node
            if node.NE is not None:
                L.append(node.NE)
            if node.NW is not None:
                L.append(node.NW)
        return best
    
    def southernmost_point(self):
        """return the southernmost node of the tree"""
        if self.point.ID is None:
            print("quadtree is empty")
            return False
        best = self
        L = [self]
        while(len(L)>0):
            node = L.pop()
            if node.point.y < best.point.y :
                best = node
            if node.SE is not None:
                L.append(node.SE)
            if node.SW is not None:
                L.append(node.SW)
        return best
        
    
    def easternmost_point(self):
        """return the easternmost node of the tree"""
        if self.point.ID is None:
            print("quadtree is empty")
            return False
        best = self
        L = [self]
        while(len(L)>0):
            node = L.pop()
            if node.point.x > best.point.x :
                best = node
            if node.NE is not None:
                L.append(node.NE)
            if node.SE is not None:
                L.append(node.SE)
        return best
    
    def westernmost_point(self):
        """return the westernmost node of the tree"""
        if self.point.ID is None:
            print("quadtree is empty")
            return False
        best = self
        L = [self]
        while(len(L)>0):
            node = L.pop()
            if node.point.x < best.point.x :
                best = node
            if node.SW is not None:
                L.append(node.SW)
            if node.NW is not None:
                L.append(node.NW)
        return best
    
    def display(self,label=False):
        """return a 2D plot of the quadtree
        if label is True the IDs are displayed
        """
        Lx = []
        Ly = []
        Lid = []
        
        if self.point.ID is None:
            print("quadtree is empty")
            return False
        
        L = [self]
        while(len(L)>0):
            node = L.pop()
            Lx.append(node.point.x)
            Ly.append(node.point.y)
            Lid.append(node.point.ID)
            if node.SW is not None:
                L.append(node.SW)
            if node.NW is not None:
                L.append(node.NW)
            if node.SE is not None:
                L.append(node.SE)
            if node.NE is not None:
                L.append(node.NE)
                
        ymax = max(Ly)
        ymin = min(Ly)
        xmax = max(Lx)
        xmin = min(Lx)
        seg_vert = [(self.point.x,ymax),(self.point.x,ymin)]
        seg_hor = [(xmax,self.point.y),(xmin,self.point.y)]
        lines = [seg_vert,seg_hor]
        lc = mc.LineCollection(lines)
                
        fig = plt.figure()
        plt.scatter(Lx,Ly,s=2,c='red')
        plt(lc)
        plt.show()
        
            
        

    #à finir
    def suppression(self,x):
        """suppression de l'élément x de l'arbre
        renvoie l'arbre après la suppression
        """
        if self.point is None:
            return self
        
        temp = self
        #while(temp.point.ID!=x and (self.point.NW is not None or self.point.)
        

def Quadtree_from_list(L):
    """construit un quadtree à partir d'une liste de triplet (ID,x,y)"""
    T = Quadtree(None)
    for triplet in L:
        pt = Point(triplet[0],triplet[1],triplet[2])
        T.insertion(pt)
    return T

def creation_liste_triplet_aleatoire(n,p,q):
    Lx = random.sample(range(-p,p+1),n)
    Ly = random.sample(range(-q,q+1),n)
    res = []
    for i in range(n):
        triplet = (i,Lx[i],Ly[i])
        res.append(triplet)
    return res

def Quadtree_Aleatoire(n, p, q):
    """ renvoie un quadtree aléatoire de taille n dont les points ont leurs coordonnées (x,y) telles que
     x \in [-p,p] et y \in [-q,q]"""
    T = Quadtree(None)
    Lx = random.sample(range(-p,p+1),n)
    Ly = random.sample(range(-q,q+1),n)
    for i in range(n):
        x = random.randrange(-p, p+1)
        y = random.randrange(-q, q+1)
        pt = Point(i,x,y)
        T.insertion(pt)
    return T


pt1 = Point(1,1,1)
pt2 = Point(2,0,2)
print(pt1.is_equal(pt2))
print(pt1.is_NW(pt2))
print(pt1.is_SW(pt2))
print(pt1.is_NE(pt2))
print(pt1.is_SE(pt2))
print(pt1.distance(pt2))

pt3 = Point(3,0,0)
pt4 = Point(4,2,0)
pt5 = Point(5,2,2)

NW = Quadtree(pt2)
SW = Quadtree(pt3)
SE = Quadtree(pt4)
NE = Quadtree(pt5)
T = Quadtree(pt1,NW,SW,SE,NE)

pt6 = Point(6,0.5,3)

T.affiche_Quadtree()
T.recherche(pt3).affiche_Quadtree()

T.insertion(pt6)
T.affiche_Quadtree()
T.recherche(pt2).affiche_Quadtree()

A = Quadtree_Aleatoire(4, 10, 10)
A.affiche_Quadtree()
