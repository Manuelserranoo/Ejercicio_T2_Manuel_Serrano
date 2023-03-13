import math
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #si no se recibe una x y una y se le asigna 0
    def __str__(self):
        return f'({self.x}, {self.y})'
    def cuandrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y == 0:
            return "Origen"
        elif self.x == 0 and self.y != 0:
            return "Sobre el eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre el eje X"
    def vector(self, pto2):
        return f'({self.x - pto2.x}, {self.y - pto2.y})'
    def dist(self, pto2):
        return f'{math.sqrt(((self.x - pto2.x)**2 + (self.y - pto2.y)**2))}'


def main():
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)
    print(A)
    print(A.cuandrante())
    print(B)
    print(C)
    print(C.cuandrante())
    print(D)
    print(D.cuandrante())
    print(A.vector(B))
    print(B.vector(A))
    print(A.dist(B))
    print(B.dist(A))
    if A.dist(D) < B.dist(D) and A.dist(D) < C.dist(D):
        print("A esta mas cerca del origen que B y C")
    elif B.dist(D) < A.dist(D) and B.dist(D) < C.dist(D):
        print("B esta mas cerca del origen que A y C")
    elif C.dist(D) < A.dist(D) and C.dist(D) < B.dist(D):
        print("C esta mas cerca del origen que A y B")
    
if __name__ == '__main__':
    main()


