# CIFRADOR CÉSAR

# DEFINICIÓN DE CONSTANTES
# Se construye un string con todas las letras del abecedario
ABECEDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Se entrega el nombre del archivo de entrada
ARCHIVO_ENTRADA = "entrada.txt"
# Se entrega el nombre del archivo de salida 
ARCHIVO_SALIDA = "salida.txt"

# Función que lee un archivo de texto
# ENTRADA: Nombre del archivo (string)
# SALIDA: Contenido del archivo (lista de listas)
def leerArchivo(nombreArchivo):
	# Se abre el archivo en modo de lectura
	archivo = open(nombreArchivo, 'r')
	# Se obtiene el contenido utilizando readlines 
	lista = archivo.readlines()
	# Se cierra el archivo 
	archivo.close()
	# se entrega el contenido 
	return lista
	
# Función que escribe en un archivo de texto 
# ENTRADA: Contenido a escribir (string), nombre del archivo (string)
# SALIDA: Booleano para indicar que se escribió con exito
def escribirArchivo(contenido, nombreArchivo):
	# Se abre el archivo en modo de escritura
	archivo = open(nombreArchivo, 'w')
	# Se escribe el contenido en el archivo 
	archivo.write(contenido)
	# Se cierra el archivo 
	archivo.close()
	# Se retorna True para indicar que el proceso finalizó
	return True
	
# Función que cifra una letra 
# ENTRADA: Letra a cifrar (string), Corrimiento (string)
# SALIDA: Letra cifrada (string)
def cifrarLetra(letra, corrimiento):
	# Se divide el corrimiento por el largo del abecedario
	# pues el resto mantiene el corrimiento entre 0 y 26 
	corrimiento = corrimiento % len(ABECEDARIO)
	# Se declara un iterador para encontrar la letra en el abecedario 
	i = 0 
	# Se genera un while para encontrar la letra a cifrar en el abecedario 
	while letra.upper() != ABECEDARIO[i] :
		# Se incrementa la posición para seguir con la busqueda
		i =  i + 1
	# Una vez que tengo la posición de la letra en el alfabeto, realizo el corrimiento
	# Si la posición más el corrimiento es mayor que el largo del abecedario
	if i + corrimiento >= len(ABECEDARIO) :
		# Se corrige el desplazamiento para evitar un error de index out of range 
		desplazamiento = i + corrimiento - len(ABECEDARIO)
		# La letra nueva es igual a la posición nueva en el abecedario 
		letraNueva = ABECEDARIO[desplazamiento]
	# En caso de que el corrimiento + la posición de la letra no supere el largo del abecedario
	# simplemente se realiza el corrimiento 
	else :
		# Se calcula el desplazamiento 
		desplazamiento = i + corrimiento
		# Se asigna la nueva letra a la letra nueva 
		letraNueva = ABECEDARIO[desplazamiento]
	
	# Para entregar la letra nueva se genera un if/else para entregar mayúscula o minúscula
	# Si la letra está en ABECEDARIO (entonces la letra es mayúscula)
	if letra in ABECEDARIO :
		# Por lo tanto se entrega la letra en mayúscula originalmente
		return letraNueva
	# En cambio si la letra no está en ABECEDARIO 
	else :
		# Se entrega la letra nueva en mayúscula
		return letraNueva.lower()
		

		
# Función que cifra una línea de texto
# ENTRADA: Linea de texto (string) 
# SALIDA: Linea de texto cifrado (string)
def cifrarLinea(linea, corrimiento):
	# Se determina un string vacío para guardar la linea cifrada 
	lineaCifrada = ""
	# Para cada caracter en la línea a cifrar 
	for caracter in linea:
		# Si el caracter en mayúsculas está en el ABECEDARIO 
		# (Es decir, si lo que queremos cifrar es una letra)
		if caracter.upper() in ABECEDARIO :
			# Se invoca a la función cifrar letra 
			caracterCifrado = cifrarLetra(caracter, corrimiento)
			# Se agrega la letra cifrada a la línea 
			lineaCifrada = lineaCifrada + caracterCifrado
		# Sino, es decir, si el caracter no es alfabético 
		else :
			# Se mantiene directamente em la línea cifrada sin alteraciones
			lineaCifrada = lineaCifrada + caracter
	# Una vez completado el ciclo se entrega la línea cifrada
	return lineaCifrada
	
# Función que cifra una lista de strings
# ENTRADA: lista de strings 
# SALIDA: string 
def cifrarTexto(texto, corrimiento):
	# Se declara un string vacío para almacenar el texto cifrado 
	textoCifrado = ""
	# Para cada línea en el texto 
	for linea in texto :
		# Se invoca la función cifrar línea y se agrega a la variable textoCifrado 
		textoCifrado = textoCifrado + cifrarLinea(linea, corrimiento)
	# una vez completado el ciclo se entrega la línea cifrada 
	return textoCifrado

	
# BLOQUE PRINCIPAL

# ENTRADA
# Se solicita el factor de corrimiento (Positivo para cifrar, negativo para descifrar)
factorDeCorrimiento = input("Ingrese factor de corrimiento: ")
# Se lee el archivo de entrada 
contenido = leerArchivo(ARCHIVO_ENTRADA)

# PROCESAMIENTO
# Se realiza el proceso de cifrado 
cifrado = cifrarTexto(contenido, factorDeCorrimiento)

# SALIDA
# Se escribe el archivo 
exito = escribirArchivo(cifrado, ARCHIVO_SALIDA)
# Si el archivo se escribió 
if exito :
	# Se informa de ello al usuario
	print "El archivo", ARCHIVO_SALIDA, "ha sido escrito exitosamente"
