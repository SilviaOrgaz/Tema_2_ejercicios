
#Ejercicio

#Crea una clase llamada Punto con sus dos coordenadas X e Y.
#Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
#Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
#Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, 
# teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
#Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.

import math

class Punto:

    def __init__(self, x, y):
        self.x=x
        self.y=y
        #print("Coordenadas creadas con éxito")

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def cuadrante(self):
        if self.x == 0 and self.y != 0:
            print("{} se encuentra sobre el eje Y".format(self))
        elif self.x > 0 and self.y > 0:
            print("{} se encuentra en el primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} se encuentra en el segundo cuadrante".format(self))
        elif self.y < 0 and self.x <0:
            print("{} se encuentra en el tercer cuadrante".format(self))
        elif self.y <0 and self.x >0:
            print("{} se encuentra en el cuarto cuadrante".format(self))
        elif self.x == 0 and self.y == 0:
            print("{} se ecnceuntra sobre el origen".format(self))
        else:
            print("{} se encuentra sobre el eje X".format(self))

    def vector(self,punto):
        print("El vector resultante entre {} y {} es ({},{})".format(self, punto, punto.x - self.x, punto.y - self.y))

    def distancia(self, punto):
        distancia = math.sqrt((punto.x - self.x)**2+(punto.y - self.y)**2)
        print("La distancia resultante entre {} y {} es: {}".format(self, punto, distancia))

class Rectangulo:

    def __init__(self, pi, pf):
        self.pi = pi
        self.pf = pf
        
    def base(self):
        self.base=abs(self.pf.x - self.pi.x)
        print("La base del rectángulo entre {}  y {} es: {} ".format(self.pi, self.pf, self.base))

    def altura(self):
        self.altura = abs(self.pf.y - self.pi.y)
        print("La altura del rectángulo entre {} y {} es {}". format(self.pi, self.pf, self.altura))

    def area(self):
        self.area = self.base * self.altura
        print("El area del rectángulo de los puntos {} y {} es: {}".format(self.pi, self.pf, self.area))

#experimentación
A=Punto(2, 3)
B=Punto(5, 5) 
C=Punto(-3, -1)
D=Punto(0, 0)
E=Rectangulo(A,B)


print("/n Mostrando información: ")
print(A)
print(B)
print(C)
print(D)

#Comprobamos
A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)
A.distancia(D)
B.distancia(D)
C.distancia(D)

E=Rectangulo(A,B)
E.base()
E.altura()
E.area()