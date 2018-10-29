'''
Ejercicio:

Construir una baraja de cartas del naipe inglés y obtener
una mano a partir de ellas

'''

# Programa que crea una baraja de cartas y reparte una mano de cartas 


# Desde random importo la función shuffle 
from random import shuffle

'''
Alternativa:
from random import shuffle
'''

# CONSTANTES
# Se indica la cantidad de cartas que se requieren para una mano 
CARTAS_MANO = 6

# Se indican la cantidad de barajas de 52 cartas, que se necesitan para la baraja completa 
BARAJAS = 2

# ENTRADA

# NO HAY ENTRADAS

# PROCESAMIENTO
# Se crea una lista para almacenar los valores de las cartas 
monos = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

# Se crea una lista para almacenar las pintas de las cartas 
pintas = ['Diamante', 'Corazón', 'Pica', 'Trébol']

# Se crea una lista con los dos jokers 
jokers = ['Joker rojo', 'Joker negro']

# Se crea una lista vacía para almacenar la baraja completa 
baraja = []

# For para crear la cantidad de barajas 
for e in range(BARAJAS) :
	# Agrego los jokers respectivos de la baraja 

    baraja = baraja + jokers
	# Realizo la combinatoria de valores de cartas y pintas de cartas 
    for numero in monos:
            for pinta in pintas :
		    # Agrego cada carta de la combinatoria en la baraja 
                    baraja.append(numero + " de " + pinta)

# Se mezcla la baraja
shuffle(baraja)

# Se declara una lista para almacenar la mano 
mano = []
# Mientras la cantidad de cartas en la mano, no alcance el número de la constante CARTAS_MANO 
while len(mano) < CARTAS_MANO :
	
	mano.append(baraja.pop())
	
	'''
	# Se selecciona una carta utilizando choice 
	carta = choice(baraja)
	# Se elimina la carta de la baraja 
	baraja.remove(carta)
	# Se agrega la carta a la mano 
	mano.append(carta)
        '''
# SALIDA

# Para cada carta en la mano 
for carta in mano :
	# Se imprime la carta 
	print carta






