# PROGRAMA QUE CALCULA EL FACTORIAL DE UN NÚMERO ENTERO
# AUTOR: Luciano Hidalgo S.
# FECHA: 26-10-2018

####################################################################
# SOLUCIÓN 1
####################################################################
# ENTRADA
# Se solicita la entrada
numero = int(input('Ingrese el valor para calcular el factorial: '))

# PROCESAMIENTO
# Se declara una variable para almacenar el factorial del número
factorial = 1
# Mientras el número sea mayor que 1
while numero > 1 :
	# Se agrega cada número al producto total del factorial
	factorial = factorial * numero
	# Se reduce el número en 1
	numero = numero - 1

# SALIDA
# Se imprime el resultado del factorial
print('El factorial es:', factorial)


####################################################################
# SOLUCIÓN 2
####################################################################
# ENTRADA
# Se solicita la entrada
numero = int(input('Ingrese el valor para calcular el factorial: '))

# PROCESAMIENTO
# Se declara una variable para almacenar el factorial del número
factorial = 1
# Se declara un contador para asegurar la iteración entre i y el número
i = 1
# Mientras el número sea mayor que 1
while i <= numero  :
	# Se agrega cada número al producto total del factorial
	factorial = factorial * i
	# Se aumenta el contador en 1
	i = i + 1

# SALIDA
# Se imprime el resultado del factorial
print('El factorial de', numero, 'es', factorial)