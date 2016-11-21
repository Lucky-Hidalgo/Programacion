# -*- coding: cp1252 -*- 

# ENTRADA

# Solicito la cantidad de números primos
numero = input("Ingrese el valor: ")

# Declaro una lista vacía para almacenar números primos
listaPrimos = []

# Inicializo el contador en 2 (El primer número primo)
# La idea es usar j para determinar qué números son primos y cuáles no
j = 2

# Mientras la lista de números primos no tenga la cantidad de números deseada
# EL WHILE EXTERNO BUSCA ALCANZAR UNA LISTA CON LA CANTIDAD DE NÚMEROS PRIMOS DESEADA
while len(listaPrimos) < numero :
	# Inicializo el contador i en 2
	# para revisar si un número (j) es primo
    i = 2
    # Declaro una bandera para revisar si el número es primo
    esPrimo = True

    # EL WHILE INTERIOR REVISA SI J ES UN NÚMERO PRIMO
    # Mientras no haya revisado todos los números entre 2 y j
    while i < j :
    	# Si el resto de j divido en i es 0
        if j % i == 0 :
        	# Entonces el número no es primo
            esPrimo = False
        # Incremento el valor de i para seguir revisando si j 
        # cumple las condiciones para ser un número primo
        i = i + 1
    
    # Si j es primo (Es decir no se encontraron divisores exactos entre i = 2 e i = j - 1)
    if esPrimo :
    	# Agrego j a listaPrimos
        listaPrimos.append(j)
    # Incremento el valor de j para seguir buscando números primos
    j = j + 1

# SALIDA
# Imprimo la cantidad de números primos solicitada
print listaPrimos
