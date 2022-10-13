
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
        print("Coordenadas creadas con éxito")

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def cuadrante(self):
        if self.x == 0 and self.y != 0:
            return self.y
        elif self.x != 0 and self.y == 0:
            return self.x
        else:
            return 0



