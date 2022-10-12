#Ejercicio 2 Utilizando todo lo que sabes sobre cadenas, listas, sus métodos internos... Transforma este texto:

#un día que el viento soplaba con fuerzamira como se mueve aquella banderola 
# -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, 
# lo que se mueve son vuestras mentes -dijo el maestro

#En este otro:

#Un día que el viento soplaba con fuerza...
#Mira como se mueve aquella banderola -dijo un monje.
#Lo que se mueve es el viento -respondió otro monje.
#Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.
#Lo único prohibido es modificar directamente el texto.

cadena = "un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"

#Esta función convierte una cadena en una lista de elementos que en la cadena principal están separados por una almuadilla
def modificar_cadena(cadena):
    return cadena.split("#")

modificar= modificar_cadena(cadena)

modificar[0] += ".."
for i in range(len(modificar)):
    modificar[i] += "."
    modificar[i]= modificar[i][0].upper() + modificar[i][1:]
    
#Imprime los elementos de la lista
for i in modificar:
    print(i)


