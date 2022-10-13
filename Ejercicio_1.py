
#Ejercicio

#Crea una clase llamada Punto con sus dos coordenadas X e Y.
#Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
#Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
#Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, 
# teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
#Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.

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


#experimentación
A=Punto(2, 3)
B=Punto(5, 5) 
C=Punto(-3, -1)
D=Punto(0, 0)


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
