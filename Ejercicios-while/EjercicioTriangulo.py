# -*- coding: cp1252 -*- 

'''
# Entrada
numero = input("Ingrese la cantidad de líneas: ")

# Proceso y salida

# Se inicia un contador para las filas de la figura
i = 0

# Mientras no se escriba el número de filas de la figura
while i < numero :
	# Se inicia un contador para las columnas de la figura
	j = 0
	# Mientras no se escriba el número adecuado de caracteres
	while j < numero - i :
		# Si el caracter va en una columna par
		if j % 2 == 0 :
			# Se escribe un #
			print "#",
		# Si el caracter se escribe en una columna impar
		else : 
			# Se escribe una O
			print "O",
			# Los print llevan coma para que el siguiente caracter
			# se escriba en la misma línea
		# Se incrementa el contador de j, para escribir la línea completa
		j = j + 1
	# Se imprime un salto de línea, una vez escrita una línea
	print "\n",
	# Se incrementa el contador de i, para escribir cada una de las filas
	i = i + 1

'''

####################################################################################
#
# SOLUCIÓN USANDO SÓLAMENTE UN PRINT
#
####################################################################################

# Entrada
numero = input("Ingrese la cantidad de líneas: ")

# Proceso 

# Se inicia un contador para las filas de la figura
i = 0

# Se inicializa un string vacío para almacenar la figura
figura = ""

# Mientras no se escriba el número de filas de la figura
while i < numero :
	# Se inicia un contador para las columnas de la figura
	j = 0
	# Mientras no se escriba el número adecuado de caracteres
	while j < numero - i :
		# Si el caracter va en una columna par
		if j % 2 == 0 :
			# Se añade un # al string
			figura = figura + "#"
		# Si el caracter se escribe en una columna impar
		else : 
			# Se añade una O al string
			figura = figura + "O"
			# Los print llevan coma para que el siguiente caracter
			# se escriba en la misma línea
		# Se incrementa el contador de j, para escribir la línea completa
		j = j + 1
	# Se añade un salto de línea a la figura
	figura = figura + "\n"
	# Se incrementa el contador de i, para escribir cada una de las filas
	i = i + 1

# Salida
print figura