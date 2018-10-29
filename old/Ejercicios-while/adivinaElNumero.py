'''
Programa que genera un numero aleatorio y le entrega al usuario
10 intentos para adivinar, el programa no entrega pistas, solo
indica cuándo el número es correcto
'''
# Desde el módulo random importo
# la función randint
from random import randint
# Genero un número secreto entre 0 y 100
# y lo almaceno en la variable numero secreto
numeroSecreto = randint(0,100)

# Se definen los intentos para adivinar en 1
intentos = 1
# Mientras el número de intentos no alcance 10
while intentos <= 10 :
        # Se pregunta al usuario el número
	numeroEscogido = int(input("Adivina el número: "))
	# Si el número escogido es igual al número secreto
	if numeroEscogido == numeroSecreto :
                # Se imprime que el usuario ha adivinado y el número
                # de intentos que tomó
		print ("Has adivinado y solo te tomó", intentos, "intentos")
		# Se aumentan los intentos a 10 para forzar la salida del
		# ciclo
		intentos = 10
	# En caso contrario, es decir, no se ha adivinado el número
	else :
                # Se imprime que el número es incorrecto
		print ("Incorrecto")
	# En ambos casos se incrementa el número de intentos en 1
	intentos = intentos + 1
# Si se termina el juego sin adivinar el número
if numeroEscogido != numeroSecreto :
        # Se imprime que el juego ha terminado y el
        # usuario ha perdido
        print ("Has perdido, el número era:", numeroSecreto)
        print("Game over")
