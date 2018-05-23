# Función que solicita una palabra
# Entrada: Ninguna
# Salida: Palabra
def pedirPalabra():
	# Se solicita la palabra usando input
	palabra = input("Ingrese una palabra: ")
	# Si se ingresan solo letras
	if palabra.isalpha() :
		# Se retorna la palabra en minusculas
		return palabra.lower()
	# En caso contrario
	else :
		# Se informa que el ingreso es incorrecto
		print ("INGRESO INCORRECTO!!")
		# Se vuelve a llamar la función
		return pedirPalabra()


# Función que solicita una letra
# Entrada: Ninguna
# Salida: Letra
def pedirLetra():
	# Se solicita el ingreso de una letra
	letra = input("Ingrese una letra: ")
	# Si lo que se ingresa son sólo letras
	# y tiene largo 1 (Es decir, es una sola letra)
	if letra.isalpha() and len(letra) == 1:
		# Se retorna la letra en minuscula
		return letra.lower()
	# En caso contrario
	else :
		# Se informa que el ingreso es incorrecto
		print ("INGRESO INCORRECTO!!")
		# Se vuelve a llamar la función
		return pedirLetra()

# Función que imprime "numero" lineas en blanco
# Entrada: Un número entero positivo
# Salida: Booleano True cuando el proceso termina
def imprimirLineas(numero):
	# Mientras número no llegue a cero
	while numero > 0 :
		# Se imprime una línea en blanco
		print ("")
		# Se reduce la cuenta en uno
		numero = numero - 1
	# Se retorna un valor True
	return True

# Función que revisa si una letra está en una palabra
# Entrada: Letra (string), palabra (string)
# Salida: Booleano (True o False) 
def existeEnPalabra(letra, palabra):
	# Si la letra está en la palabra
	if letra in palabra :
		# Se retorna un valor True
		return True
	# En caso contrario
	else :
		# Se retorna un valor False
		return False

# Función que marca los aciertos en la lista de aciertos
# Entrada: letra (string), objetivo (lista de strings), 
#		   aciertos (lista de strings)
# Salida: aciertos (lista de strings)
def marcarAciertos(letra, objetivo, aciertos):
	# Se añade un contador 
	i = 0
	# Mientras i no llegue a la última posicion
	while i < len(objetivo):
		# Si la letra se encuentra en la posición i de 
		# la lista objetivo
		if objetivo[i] == letra :
			# Se reemplaza la letra en la lista aciertos
			aciertos[i] = letra 
		# Se incrementa el iterador
		i = i + 1
	# Se retorna la lista aciertos
	return aciertos 



# PREPARAR EL JUEGO
# Se pide la palabra secreta original
palabraSecreta = pedirPalabra()
# Se imprimen 300 líneas en blanco
imprimirLineas(300)

# COMENZAR EL JUEGO

# Se pasa la palabra secreta a una lista
listaPalabraSecreta = list(palabraSecreta)
# Se genera una lista de aciertos
listaAciertos = list("_" * len(palabraSecreta))
# Se crea un contador de intentos (MÁXIMO 7)
INTENTOS = 7
# Se crea una lista para ir guardando las letras que ya fueron usadas
letrasUsadas = []
# Se declara un booleano para mantener el While andando
sigue = True
# Mientras queden intentos y sigue esté marcado como True
while INTENTOS > 0 and sigue:
	# Se pide la letra usando la función pedirLetra()
	letra = pedirLetra()
	# Se revisa si la letra está en la palabra secreta usando la función
	# existeEnPalabra()
	acierto = existeEnPalabra(letra, palabraSecreta)
	# Se agrega la letra a la lista de letras usadas
	letrasUsadas.append(letra)
	# Si la letra está en la palabra
	if acierto :
		# Se informa al usuario que acertó
		print ("CORRECTO!")
		# Se agrega la letra a la lista aciertos usando la función marcarAciertos
		listaAciertos = marcarAciertos(letra, listaPalabraSecreta, listaAciertos)
		# Se imprime como va el juego hasta el momento
		print (" ".join(listaAciertos))
		# En caso de que la listaAciertos sea igual a la listaPalabraSecreta
		# es decir, ya no existan letras por adivinar
		if listaAciertos == listaPalabraSecreta :
			# Se cambia el booleano sigue a False para salir del While
			sigue = False
			# Se imprime "Has ganado"
			print ("HAS GANADO")
	# En caso de que el usuario no acierte
	else :
		# Se reducen los intentos
		INTENTOS = INTENTOS - 1
		# Se imprime como va el juego hasta el momento
		print (" ".join(listaAciertos))
		# Se informa al usuario de que ha fallado y cuántos intentos le quedan
		print ("INCORRECTO!, LE QUEDAN", INTENTOS, "INTENTOS")
		# Se indica las letras que ha usado
		print ("HA USADO: ")
		# Se imprimen las letras usadas
		print (" ".join(letrasUsadas))

# Si el While termina porque se acabaron los intentos
if INTENTOS == 0 :
	# Se informa al usuario que ha perdido el juego
	print("HAS PERDIDO")
