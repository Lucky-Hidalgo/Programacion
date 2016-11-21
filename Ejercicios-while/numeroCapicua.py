'''
 EJERCICIO : Obtenga por teclado un número entero y determine si el 
 número es capicúa o no.
 
 Un número es capicúa, si puede leerse de derecha a izquierda y de izquieda a derecha del
 mismo modo.
 
 Por ejemplo: 12321 es capicúa y 12000 no lo es.
'''
# BLOQUE PRINCIPAL

# ENTRADA
# Se solicita el ingreso del número 
numero = input("Ingrese el número: ")

# PROCESAMIENTO
# Se determina una variable para ir reduciendo el número 
nuevoNumero = numero
# Se determina una variable, para almacenar el número invertido 
invertido = 0
# Mientras la variable nuevoNumero no sea reducida a cero 
while nuevoNumero > 0 :
	# Para obtener el número invertido, se tendrá el número invertido almacenado
	# anteriormente multiplicado por 10 y el resto de nuevoNumero dividido por 10
	# El objeto de multiplicar por 10 es para dar espacio a la nueva cifra
	# y con el resto de la división por 10 obtengo la última cifra del número 
    invertido = invertido * 10 + nuevoNumero % 10
	# Divido el nuevoNumero por 10 y lo reasigno a nuevoNumero para 
	# poder obtener la siguiente cifra en la próxima iteración
    nuevoNumero = nuevoNumero/10
# Una vez terminado el while

# SALIDA
# reviso si el número original es igual al invertido
if numero == invertido :
	# En caso de serlo, informo que es capicua 
    print "El numero", numero,"es capicua"
# De lo contrario
else:
	# Informo que el número no es capicua
    print "El número",numero,"no es capicua"

	
