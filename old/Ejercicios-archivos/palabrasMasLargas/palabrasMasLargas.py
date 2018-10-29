# Función que lee un archivo
# Entrada: nombre del archivo (string)
# Salida: contenido del archivo (string)
def leerArchivo(nombreArchivo):
	# Se abre el archivo en modo de lectura
	archivo = open(nombreArchivo, 'r')
	# Se declara un texto vacio para almacenar el contenido
	texto = ""
	# Para cada linea en el archivo
	for linea in archivo :
		# Se agrega el texto de la línea en el texto
		# se usa strip para agregarlo sin salto de línea 
		texto += linea.strip("\n") + " "
	# Se cierra el archivo
	archivo.close()
	# Se retorna el texto, se utiliza un strip para sacar espacios 
	# adicionales que pudieron haberse agregado
	return texto.strip(" ")

# Función que transforma el string en una lista de palabras
# Entrada: Texto (string) (separará usando el caracter espacio)
# Salida: Lista de strings
def obtenerListaPalabras(texto):
	return texto.split(" ")

# Función que obtiene la cantidad de caracteres que tiene la palabra 
# más larga
# Entrada: Lista de palabras (lista de strings)
# Salida: Número máximo de caracteres (entero)
def obtenerMaximo(listaPalabras):
	# Se declara un maximo para almacenar 
	# el número de caracteres de la primera palabra
	# de la lista
	maximo = len(listaPalabras[0])
	# Para cada palabra en la lista
	for palabra in listaPalabras :
		# Reviso si la cantidad de caracteres de 
		# esa palabra es mayor al que tengo en maximo
		if len(palabra) > maximo :
			# En caso de que así sea, reemplazo el valor
			maximo = len(palabra)
	# Entrego el maximo
	return maximo

# Función que obtiene todas las palabras que tengan una 
# cantidad determinada de caracteres
# Entrada: Lista de palabras (lista), 
#		   cantidad de caracteres (int)
# Salida: Lista de palabras (string)
def obtenerPalabras(listaPalabras,maximo):
	# Se declara una lista vacía
	lista = []
	# Para cada palabra en la lista
	for palabra in listaPalabras :
		# Si el largo de la palabra coincide 
		# con el maximo
		if len(palabra) == maximo :
			# Se agrega a lista la palabra
			lista.append(palabra)
	# Entrego la lista
	return lista


# Función que escribe un string en el contenido
# Entrada: Contenido a escribir (string)
# 			Nombre de archivo (string)
# Salida: Booleano en caso de que todo sea 
# 			escrito correctamente
def escribirArchivo(contenido, nombreArchivo):
	# Se abre el archivo en modo de escritura
	archivo = open(nombreArchivo, 'w')
	# Se escribe el archivo
	archivo.write(contenido)
	# Se cierra el archivo
	archivo.close()
	# Se retorna el True en caso de escribir
	return True



# Se solicita el archivo de entrada
entrada = leerArchivo("entrada.txt")

# Se convierte en una lista de palabras
lista = obtenerListaPalabras(entrada)
# Se obtiene el máximo de caracteres que tiene una palabra
maximo = obtenerMaximo(lista)

# Se obtienen las palabras más grandes
palabrasMasGrandes = obtenerPalabras(lista, maximo)

# Se prepara el texto que se imprimirá en la salida
salida = "La(s) palabra(s) más larga(s) tiene(n): "
salida += str(maximo) + 'caracteres y es(son):\n'
salida += " ".join(palabrasMasGrandes)

# Se escribe la salida
if escribirArchivo(salida,"salida.txt"):
	print("Se ha escrito exitosamente la salida")
