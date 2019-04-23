def main():
    class Point():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def is_equal(self, point):
            return (self.x == point.x and self.y == point.y)

        def get_x(self):
            return self.x

        def get_y(self):
            return self.y

        def is_NW(self, point):  # le point est au nord-ouest du self

            return (self.x >= point.x and self.y < point.y)

        def is_SW(self, point):
            return (self.x > point.x and self.y >= point.y)
            
        def is_SE(self, point):
            return (self.x <= point.x and self.y > point.y)

        def is_NE(self, point):
            return (self.x < point.x and self.y <= point.y)

        def distance(self, point):
            return ((self.x - point.x)**2 + (self.y - point.y)**2)**(1/2)

    class Arbre():
        def __init__(self, point, ID, NW, SW, SE, NE):
            self.point = point
            self.ID = ID
            self.NW = NW
            self.SW = SW
            self.SE = SE
            self.NE = NE


main()
