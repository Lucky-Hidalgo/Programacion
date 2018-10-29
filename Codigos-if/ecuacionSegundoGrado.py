# PROGRAMA QUE CALCULA LAS SOLUCIONES REALES DE UNA ECUACIÓN DE SEGUNDO GRADO
# AUTOR: Luciano Hidalgo S.
# FECHA: 16-10-2018

# ENTRADAS
# Solicito el valor de las entradas 
# y las transformo a número de punto flotante
valorA = float(input('Ingrese el valor de A: '))
valorB = float(input('Ingrese el valor de B: '))
valorC = float(input('Ingrese el valor de C: '))

# PROCESAMIENTO
# Se calcula el valor del discriminante
discriminante = valorB ** 2 - 4 * valorA * valorC

# Si el discriminante es menor que cero
if discriminante < 0 :
	# SALIDA 
	# Se informa que la ecuación no tiene solución
	print('La ecuación con valores:')
	print('\tA:', valorA)
	print('\tB:', valorB)
	print('\tC:', valorC)
	print('No tiene solución en los reales')

# Si el discriminante es igual a cero
if discriminante == 0 :
	# Se calcula el valor de la solución
	solucion = - valorB / (2 * valorA)
	#SALIDA
	# Se informa que la ecuación tiene solución única
	print('La ecuación con valores:')
	print('\tA:', valorA)
	print('\tB:', valorB)
	print('\tC:', valorC)
	print('Tiene solución única:', solucion)

if discriminante > 0 :
	# Se calcula el valor de ambas soluciones
	solucion1 = (- valorB + (discriminante) ** (1/2) )/ (2 * valorA)
	solucion2 = (- valorB - (discriminante) ** (1/2) )/ (2 * valorA)
	#SALIDA
	# Se informa que la ecuación tiene dos soluciones
	print('La ecuación con valores:')
	print('\tA:', valorA)
	print('\tB:', valorB)
	print('\tC:', valorC)
	print('Tiene dos soluciones:')
	print('\tSolución 1:', solucion1)
	print('\tSolución 2:', solucion2)