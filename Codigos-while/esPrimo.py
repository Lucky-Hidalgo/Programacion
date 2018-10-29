# PROGRAMA QUE DETERMINA SI UN NÚMERO ENTERO POSITIVO ES 1
# AUTOR: Luciano Hidalgo S.
# FECHA: 27-10-2018

############################################################
# SOLUCIÓN 1
############################################################
# ENTRADA
# Solicito el número a revisar
numero = int(input('Ingrese un número:'))

# PROCESAMIENTO
# Declaro un contador para ir iterando
# Se inicializa este en 2 para revisar los números
# entre 2 y número
i = 2
# Defino una bandera, la cuál marca que el número
# originalmente es primo, en caso de encontrar una 
# condición que contradiga las reglas de los números 
# primos, se modificará la bandera
esPrimo = True
# Mientras i no alcance el número
while i < numero :
	# Si el número al ser dividido por el iterador entrega
	# resto igual a cero
    if numero % i == 0 :
    	# Cambio la bandera a False, indicando que 
    	# el número no es primo
        esPrimo = False
        # Cómo no vale la pena seguir revisando, cambio el
        # valor del contador por el del número
        # a fin de salir del while
        i = numero
    # Incremento el valor de i para seguir revisando
    i = i + 1 

# SALIDA
# Si el número es igual a 1
if numero == 1 :
	# Se imprime que el número es 1
    print('El número es 1')
# Si la bandera es True, es decir
# el número SI es primo
elif esPrimo :
	# Se imprime el resultado
    print('El número es primo')
# Sino
else :
	# El número no es primo
    print('El número no es primo')

############################################################
# SOLUCIÓN 2
############################################################
# ENTRADA
# Solicito un número como entrada
numero = int(input('Ingrese un número:'))

# PROCESAMIENTO
# Declaro un iterador para recorrer los números entre 1 y número
i = 1
# Declaro un contador de divisores exactos, para aumentar
# la cuenta cuándo aparezca uno
divisores = 0
# Mientra i no alcance el número
while i <= numero :
	# Si i es un divisor exacto de número
	if numero % i == 0 :
		# Incremento el número de divisores
		divisores = divisores + 1
		# Incremento el valor de i
		i = i + 1
	# Sino
	else :
		# Solo incremento el valor de i
		i = i + 1
		# IMPORTANTE: Si la línea anterior no existiera
		# el ciclo sería infinito

# SALIDA
# Si el número es igual a 1
if numero == 1 :
	# Se imprime que el número es 1
    print('El número es 1')
# Si encuentro sólo dos divisores
elif divisores == 2 :
	# Se imprime el resultado
    print('El número es primo')
# Sino
else :
	# El número no es primo
    print('El número no es primo')


############################################################
# SOLUCIÓN 3
############################################################
# ENTRADA
# Solicito un número de entrada
numero = int(input('Ingrese un número:'))

# PROCESAMIENTO
# Declaro un iterador para recorrer entre 2 y número - 1
i = 2
# Se declara un contador de divisores y se inicializa este en 0
divisores = 0
# Mientras i no alcance el número
while i < numero :
	# Si i es divisor exacto de número
	if numero % i == 0 :
		# Se incrementa el contador de divisores
		divisores = divisores + 1
	# Tanto si entro en el if como si no, incremento el contador
	i = i + 1
	
# SALIDA
# Si el número es igual a 1
if numero == 1 :
	# Se imprime que el número es 1
    print('El número es 1')
# Si no encuentro divisores exactos
elif divisores == 0 :
	# Se imprime el resultado
    print('El número es primo')
# Sino
else :
	# El número no es primo
    print('El número no es primo')