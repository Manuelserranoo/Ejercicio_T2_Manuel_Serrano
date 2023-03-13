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
        


def main():
    p1 = Punto(2, 3)
    p2 = Punto(-4, 5)
    print(p1)
    print(p1.cuandrante())
    print(p2)
    print(p2.cuandrante())

    
if __name__ == '__main__':
    main()


