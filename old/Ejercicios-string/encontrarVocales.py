# -*- coding: cp1252 -*-
'''
PROGRAMA QUE REVISA QUÉ VOCALES EXISTEN EN
UN TEXTO, INDICA LAS VOCALES QUE APARECEN
EN UN TEXTO Y LAS QUE NO

Python v3
'''

# Se solicita el texto de entrada
texto = input("Ingrese un texto: ")

# Se crea una lista con 5 ceros, que se
# usará para marcar la existencia de las
# vocales A, E, I, O y U
vocales = [0,0,0,0,0]

# Para cada caracter en el texto
for caracter in texto :
    # Si el caracter a revisar es una A o una a
    if caracter == "A" or caracter == "a" :
        # Se marca la primera posición de la lista
        # con el valor 1, y se usa para
        # indicar que se encontró la A
        vocales[0] = 1
    # Si el caracter a revisar es una E o una e
    if caracter == "E" or caracter == "e" :
        # Se marca la segunda posición de la lista
        # indicando que se encontró la E
        vocales[1] = 1
    # Si el caracter a revisar es una I o una i
    if caracter == "I" or caracter == "i" :
        # Se marca la tercera posición de la lista
        # indicando que se encontró la I
        vocales[2] = 1
    # Si el caracter a revisar es una O o una o
    if caracter == "O" or caracter == "o" :
        # Se marca la cuarta posición de la lista
        # indicando que se encontró la O
        vocales[3] = 1
    # Si el caracter a revisar es una U o una u
    if caracter == "U" or caracter == "u" :
        # Se marca la quinta posición de la lista
        # indicando que se encontró la U
        vocales[4] = 1

# Se cuenta el total de vocales sumando los valores
# de las cinco posiciones de la lista
totalVocales = vocales[0] + vocales[1] + vocales[2]+\
               vocales[3] + vocales[4]

# Se indican cuántas vocales se encontraron
print ("Se encontraron ", totalVocales, "vocales:" )
# Se revisa con cinco ifs cuáles vocales se encontraron
# Si está marcada la A
if vocales[0] == 1 :
    # Se imprime la A
    print ("A", end=" ")
# Si está marcada la E
if vocales[1] == 1 :
    print ("E", end=" ")
# Si está marcada la I
if vocales[2] == 1 :
    print ("I", end=" ")
# Si está marcada la O
if vocales[3] == 1 :
    print ("O", end=" ")
# Si está marcada la U
if vocales[4] == 1 :
    print ("U", end=" ")
# SE imprime un espacio en blanco
print("")
# Si no se encontraron las 5 vocales
if totalVocales != 5 :
    # Se calculan e imprimen las vocales que faltan
    print ("Faltan:", 5 - totalVocales, ":")
# Si no se marcó la primera posición con un 1
# es decir, la A no se encontró, y si la A no se encontró
if vocales[0] == 0 :
    # Se imprime en las letras faltantes
    print ("A", end=" ")
# Si no se marcó la segunda posición
if vocales[1] == 0 :
    # Se imprime la E como letra faltante
    print ("E", end=" ")
# Si no se marcó la tercera posición
if vocales[2] == 0 :
    # Se imprime la I como letra faltante
    print ("I", end=" ")
# Si no se marcó la cuarta posición
if vocales[3] == 0 :
    # Se imprime la O como letra faltante
    print ("O", end=" ")
# Si no se marcó la quinta posición
if vocales[4] == 0 :
    # Se imprime la U como letra faltante
    print ("U", end=" ")
