# Función que lee un archivo
# Entrada: nombre del archivo (string)
# Salida: contenido del archivo (string)
def leerArchivo(nombreArchivo):
	# Se abre el archivo en modo de lectura
	archivo = open(nombreArchivo, 'r')
	# Se lee el contenido del archivo y se vuelca en una lista
	contenido = archivo.readlines()
	# Se cierra el archivo
	archivo.close()
	# Se retorna el contenido del archivo
	return contenido

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


# Función que determina si una patente es válida o no
# Entrada: Patente (string)
# Salida: Booleano (True si la patente es válida, False si no)
def esValida(patente):
	# Declaro una lista de los dígitos válidos
	digitos = "0123456789"
	# Declaro una lista con las letras permitidas en las patentes
	# antiguas
	letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	# Declaro una lista con las letras permitidas en las patentes
	# nuevas
	letrasNueva = "BCDFGHJKLMNPQRSTVWXYZ"
	# Si el largo de la patente (Sin el salto de línea)
	# es distinto de 6
	if len(patente.strip()) != 6 :
		# La patente no es válida
		return False
	# Reviso primero si en las últimas dos posiciones hay números
	if patente[4] in digitos and patente[5] in digitos :
		# Si en las posiciones del medio existen digitos
		if patente[2] in digitos and patente[3] in digitos :
			# La patente es antigua, por lo que debería revisar 
			# si los caracteres en la primera posición son letras del 
			# string "letras"
			if patente[0] in letras and patente[1] in letras :
				# Si cumple todas las condiciones, se retorna un True
				return True
			# Sino, se retorna un False
			else :
				return False
		# Si no tiene dígitos en las posiciones del medio
		# Reviso que las letras en dichas posiciones sean letras
		# permitidas en las patentes nuevas
		elif patente[2] in letrasNueva and patente[3] in letrasNueva :
			# Realizo la misma revisión para los primeros dos caracteres
			if patente[0] in letrasNueva and patente[1] in letrasNueva :
				# Si en ambos casos la condición se cumple, se retorna True
				return True
			# Sino
			else :
				# Se retorna un False
				return False
		# En caso contrario
		else :
			# Se retorna False
			return False
	# Si no se cumplen las condiciones ni para patentes antiguas, ni nuevas
	# retorno False
	return False


# Función que revisa si las patentes son válidas o no
# La función prepara inmediatamente el texto para
# escribirlo en un archivo, por lo que la salida de esta
# es un string, donde cada línea corresponde a la patente
# con el resultado de la validación
# Entrada: Lista de patentes (lista de strings)
# Salida: texto (string)
def aplicarRevision(lista):
	# Se declara un texto vacío para almacenar el resultado
	texto = ""
	# Para cada patente en la lista
	for patente in lista :
		# Invoco a la función esValida() para saber si la patente
		# es valida o no
		resultado = esValida(patente)
		# Si fuese válida
		if resultado :
			# Escribo el resultado en el texto
			texto += patente.strip() + ": " + "VALIDA\n"
		# Sino
		else :
			# Escribo el resultado en el texto
			texto += patente.strip() + ": " + "NO VALIDA\n"
	# Se retorna el texto
	return texto


# Leo el archivo de texto
contenido = leerArchivo("patentes.txt")

# Aplico la revisión
resultado = aplicarRevision(contenido)

# Si el proceso se completa, informo al usuario que se ha escrito con éxito la salida
if escribirArchivo(resultado, "patentesValidas.txt") :
	print ("El archivo se ha escrito exitosamente")
