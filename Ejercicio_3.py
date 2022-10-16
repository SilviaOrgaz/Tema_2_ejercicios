##Ejercicio 3 Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

# Borrar los elementos duplicados.
#  Ordenar la lista de mayor a menor. 
# Eliminar todos los números impares. 
# Realizar una suma de todos los números que quedan. 
# Añadir como primer elemento de la lista la suma realizada.
# Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, 
# concuerda con el primer número de la lista, 
# tal que así: nueva_lista = modificar(lista)

#print( nueva_lista[0] == sum(nueva_lista[1:]) )

#True
#Recordatorio
#La función sum(lista) devuelve una suma de los elementos de una lista.

class Lista_numeros:
    def __init__(self, x):
        self.x= x

    def modificar(self, lista):
        for i in lista:
            if i not in self.x:
                self.x.append(i)
        print(self.x)
        
    
    def ordenar(self):
        self.x.sort()
        print(self.x)

    
    def eliminar_impares(self):
        for i in self.x:
            if i%2 != 0:
                self.x.remove(i)
        print(self.x)
                
    def sumar(self):
        self.suma = sum(self.x)
        print(self.suma)
            
        
    def añadir(self):
        self.x.append(self.suma)
        self.x= self.x[-1:]+ self.x[:-1]
        print(self.x)

Lista = [10, 2, 2, 4, 7, 1, 4]
#x=[]
Lista_final = Lista_numeros([])
Lista_final.modificar(Lista)
Lista_final.ordenar()
Lista_final.eliminar_impares()
Lista_final.sumar()
Lista_final.añadir()

print(Lista_final.x[0]==sum(Lista_final.x[1:]))