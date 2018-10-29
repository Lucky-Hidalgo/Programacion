'''
PREGUNTA:

Una caja TATA es una secuencia de ADN encontrada en varios organismos vivos.

Comienza siempre con “TATAAA”. Siempre sigue con tres o más A’s en múltiplos de tres, es decir, TATAAAAAA es una caja TATA, pues contiene 6 letras A, pero TATAAAAA no lo es, pues sólo contiene 5.

Construya una función en Python que reciba como entrada una secuencia de ADN como string y entregue la mayor secuencia de la caja TATA. Su solución debe funcionar para cualquier secuencia de ADN. Los datos del ejemplo son solo referenciales

Por ejemplo: 
•	Para el string “ATTTGATGATAATTTATAAAAAAAAAATGATAAATA”
•	La caja TATA está ubicada en:
 ATTTGATGATAATTTATAAAAAAAAAATGATAAATA 
•	y por lo tanto, la función debería entregar: TATAAAAAAAAA

Considere que se debe entregar siempre la secuencia TATA de mayor tamaño en el texto. 

'''
# SOLUCIÓN

# Función que entrega la mayor caja TATAAA encontrada en 
# una secuencia de ADN
# ENTRADA: Secuencia de ADN (string)
# SALIDA: Caja TATAAA de mayor tamaño (string)
def encontrarCajaTata(secuencia):
	# Determino el patrón a buscar
	cajaTata = "TATAAA"
	# Si no encuentro el patrón en la secuencia
	if not (cajaTata in secuencia):
		# Se entrega un string vacío
		return ""
	# Mientras la caja TATAAA se encuentre en la secuencia de ADN 
	while cajaTata in secuencia :
		# Se agregan 3 A a la caja a buscar 
		cajaTataNueva = cajaTata + "AAA"
		# Si el patrÃ³n con las 3 AAA no se encuentra
		if not (cajaTataNueva in secuencia) :
			# Se retorna el patrón anterior
			return cajaTata
		# En caso contrario
		else :
			# Se continúa la búsqueda con el nuevo patrón
			cajaTata = cajaTataNueva
	
	











from random import random, randint









TEMPERATURAS_MAXIMAS = []

while len(TEMPERATURAS_MAXIMAS) < 365 :
	temp = randint(-3,36) + round(random(),1)
	TEMPERATURAS_MAXIMAS.append(temp)

# FunciÃ³n que ordena una lista
# ENTRADA: Lista de elementos
# SALIDA: Lista de elementos ordenados
def ordenarLista(lista):
	# Se declara una lista vacÃ­a para agregar los elementos ordenados 
	listaOrdenada = []
	# Mientras queden elementos en la lista
	while len(lista) > 0 :
		# Se determina un valor mÃ­nimo como el elemento inicial de la lista
		minimo = lista[0]
		# Se declara un iterador para encontrar el mÃ­nimo 
		i = 0
		# Mientras i no alcance el largo de la lista 
		while i < len(lista) :
			# Si el minimo es mayor que el elemento a revisar
			if minimo > lista[i]:
				# Se cambia el valor del mÃ­nimo 
				minimo = lista[i]
			# Se incrementa el valor de i 
			i = i + 1
		# Se agrega el mÃ­nimo a la lista ordenada 
		listaOrdenada.append(minimo)
		# Se elimina el elemento de la lista original 
		lista.remove(minimo)
	# Se retorna la lista ordenada 
	return listaOrdenada
	
#
# BLOQUE PRINCIPAL
#

# ENTRADA
# Se solicita la cantidad de elementos a buscar  
entrada = input("Ingrese la cantidad de elementos:")

# PROCESO
# Se declara una lista vacÃ­a para las n temperaturas 
temperaturas = []
# Se ordena la lista de temperaturas mÃ¡ximas 
temperaturasOrdenadas = ordenarLista(TEMPERATURAS_MAXIMAS)
# Se declara un iterador para ir agregando los n elementos del final 
i = 1
# Mientras i no alcance el valor de la entrada 
while i <= entrada :
	# Se agrega el valor a la lista de temperaturas 
	temperaturas.append(temperaturasOrdenadas[-i])
	# Se incrementa el valor de i 
	i = i + 1

# Se imprimen las n temperaturas mÃ¡s altas
print "Las", entrada, "temperaturas mÃ¡s altas del aÃ±o son: ", temperaturas


