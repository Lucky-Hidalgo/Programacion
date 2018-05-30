# -*- coding: cp1252 -*-
'''
Programa que descompone un número entero en sus
factores primos

Lenguaje: Python v2.7
'''
# Se solicita el ingreso del número utilizando input 
numero = input("Ingrese un número:")
# Declaro un contador inicializado en 2 (el primer número primo)
i = 2
# Mientras el número no alcance el valor 1
while numero > 1 :
	# Si el número es divisible por el contador 
    if numero % i == 0 :
		# Se imprime el número 
        print i,
		# Se descompone el número al dividirlo por el
		# valor actual del contador
        numero = numero / i
    # En caso contrario, ya se descompuso el número
	# todo lo posible por ese valor de contador
	# por lo que se incrementa el contador
	else :
		# Incremento el contador
        i = i + 1
        
