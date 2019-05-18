from PIL import Image
import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Pixel(object):
    def __init__(self, color = [0, 0, 0], 
            topLeft = Point(0, 0), 
            bottomRight = Point(0, 0)):
        self.R = color[0]
        self.G = color[1]
        self.B = color[2]
        self.topLeft = topLeft
        self.bottomRight = bottomRight
 
class quadtree():
    def __init__(self, image):
        
        self.tailletab = 0 #nb de noeuds
        #chargement de l'image
        self.image = image.load()
        
        self.tree = [] #liste de noeuds
        self.x = image.size[0]
        #print("self x:",self.x)
        self.y = image.size[1]
        #print("self y:",self.y)
        nbpixels = image.size[0] * image.size[1] #nombre total de feuilles (pixels)
        print(self.x)
        print(self.y)
        print(nbpixels)
        
        
        nbtemp=nbpixels
        nbq=0 #nombre de quadrants
        while(nbtemp>=1):
            nbtemp=int(nbtemp/4)
            nbq+=nbtemp
            #print("nbtemp: ",nbtemp)
        self.tailletab=nbq+nbpixels #taille du tableau: nombre de pixels+nombre de quadrants

        for i in range(self.tailletab):
            self.tree.append(Pixel())
        #print(tree)
        cpt=0
        for i in range(self.x-1,0,-2): #Insertion des feuilles à la fin du tableau
            for j in range(self.y-1,0,-2): #Remplissage ligne par ligne de droite à gauche, de bas en haut
                self.tree[self.tailletab-1-4*cpt]=Pixel(self.image[i, j], Point(i, j), Point(i, j))
                self.tree[self.tailletab-1-4*cpt-1]=Pixel(self.image[i, j-1], Point(i, j-1), Point(i, j-1))
                self.tree[self.tailletab-1-4*cpt-2]=Pixel(self.image[i-1, j], Point(i-1, j), Point(i-1, j))
                self.tree[self.tailletab-1-4*cpt-3]=Pixel(self.image[i-1, j-1], Point(i-1, j-1), Point(i-1, j-1))
                cpt+=1
        
        #insertion des quadrants
        print("tailletab-cpt= ",self.tailletab-4*cpt-1)
        for i in range(self.tailletab-4*cpt-1,-1,-1):
            #print("i= ",i)
            #print("4i+1= ",4*i+1)
            if (4*i+4<self.tailletab):
                self.tree[i] = Pixel( #Coordonnées des 4 fils de tree[i]: 4*i+1,4*i+2,4*i+3,4*i+4
                    [(self.tree[4 * i + 1].R + self.tree[4 * i + 2].R + self.tree[4 * i + 3].R + self.tree[4 * i + 4].R) / 4,
                    (self.tree[4 * i + 1].G + self.tree[4 * i + 2].G + self.tree[4 * i + 3].G + self.tree[4 * i + 4].G) / 4,
                    (self.tree[4 * i + 1].B + self.tree[4 * i + 2].B + self.tree[4 * i + 3].B + self.tree[4 * i + 4].B) / 4], #La couleur du nouveau pixel i est la moyenne arithmétique des couleurs de ses 4 pixels fils
                    self.tree[4 * i + 1].topLeft,
                    self.tree[4 * i + 4].bottomRight)
    def compression(self,qual): #prend le niveau de compression en paramètre
        start = 1
        for i in range(0, qual):
            start = 4 * start
        """while (start<self.size):
            start=4*start+1
        start=int((start-1)/4)
        print(start)"""
        if (start > self.tailletab):
            print('Qualité trop grande')
            return
        img = Image.new("RGB", (self.x, self.y), "black")
        pixels = img.load()

        for i in self.tree[0 : 4 * start]: #parcours du quadtree, plus qual est grand, plus la qualité de l'image sera meilleure
            x1 = i.topLeft.x
            y1 = i.topLeft.y
            x2 = i.bottomRight.x
            y2 = i.bottomRight.y
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                     pixels[x, y] = (int(i.R), int(i.G), int(i.B)) #Construction de la nouvelle image
        img.show();
        img.save('compression2.jpg')



def main():
    I=Image.open("galaxie.jpg")
    Tree=quadtree(I)        
    Tree.compression(8)
    #Faire des tests avec le paramètre de la fonction compression. Trop bas: trop basse qualité, trop haut: comportement bizarre
