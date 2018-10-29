'''
EJERCICIO

El reglamento complementario de la Facultad de Ingeniería de la Universidad de Santiago, 
indica que para obtener la situación final de un estudiante antes de la prueba acumulativa se utiliza la siguiente regla:

Si el estudiante tiene sus tres calificaciones parciales azules, el estudiante aprueba con el promedio simple de sus tres calificaciones.

Si el estudiante tiene una de sus calificaciones rojas, pero promedio igual o superior a 5.0 el estudiante aprueba con el promedio simple de
sus tres calificaciones.

En caso contrario, el estudiante debe rendir prueba acumulativa.

Construya un programa en Python que solicite al usuario el ingreso de sus tres calificaciones y le indique la situación final.


'''

# SOLUCIÓN

# BLOQUE PRINCIPAL

# ENTRADAS

# Obtener el promedio de notas parciales
notasParciales = input("Ingrese promedio de notas parciales: ")
# Obtener nota de PEP N°1
pep1 = input("Ingrese nota de PEP N°1: ")
# Obtener nota de PEP N°2
pep2 = input("Ingrese nota de PEP N°2: ")

# PROCESAMIENTO

# Calcular el promedio final
promedioFinal = (notasParciales + pep1 + pep2)/3.0

# SALIDA

# Si PEP N°1 o PEP N°2 o notas parciales son menores a 4.0 y promedio mayor o igual a 5.0
if (pep1 < 4.0 or pep2 < 4.0 or notasParciales < 4.0) and promedioFinal >= 5.0 :  
	# El estudiante aprueba
	print "El estudiante aprueba" 
# Si promedio menor que 5.0
if (pep1 < 4.0 or pep2 < 4.0 or notasParciales < 4.0) and promedioFinal < 5.0 :
	# El estudiante debe rendir PA 
	print "El estudiante debe rendir PA" 
# Si PEP N°1 y PEP N°2 y notas parciales son mayores o iguales a 4.0
if pep1 >= 4.0 and pep2 >= 4.0 and notasParciales >= 4.0 :
	# El estudiante aprueba
	print "El estudiante aprueba"
