##Ejercicio 3 Crea una función modificar() que a partir de una lista de números realice las siguientes tareas sin modificar la original:

# Borrar los elementos duplicados. Ordenar la lista de mayor a menor. 
# Eliminar todos los números impares. Realizar una suma de todos los números que quedan. 
# Añadir como primer elemento de la lista la suma realizada. Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, 
# concuerda con el primer número de la lista, 
# tal que así: nueva_lista = modificar(lista)

#print( nueva_lista[0] == sum(nueva_lista[1:]) )

#True
#Recordatorio
#La función sum(lista) devuelve una suma de los elementos de una lista.

Lista = [10, 2, 2, 4, 7, 1, 4]
#eliminar_dobles=set(Lista)
#print(eliminar_dobles)

x =[]
def modificar(lista, x):
    for i in lista:
        if i not in x:
            x.append(i)
            x.sort()
    for i in x:
        if i%2 != 0:
            del x[i]
    return print(x)

solucion = modificar(Lista, x)

