# -*- coding: cp1252 -*- 

# ENTRADA
# Solicito el valor del número de punto flotante para trabajar como string
numeroDecimal = raw_input("Ingrese el número deseado: ")
# Solicito la cantidad de decimales que deseo en el texto
decimales = input("Ingrese número de cifras decimales deseadas: ")

# PROCESAMIENTO
redondeado = ""
# Se divide el string por el punto decimal
listaNumeroDecimal = numeroDecimal.split(".")
parteEntera = listaNumeroDecimal[0]
parteDecimal = listaNumeroDecimal[1]

# Busco la cifra decimal siguiente a la cantidad de cifras 
# que deseo y la convierto a entero para 
# su revisión de acuerdo a las reglas de redondeo	
numeroARevisar = int(parteDecimal[decimales])


# Si se desea el número sin decimales
if decimales == 0 :
	# Reviso si su primera cifra decimal es igual o superior a 5
	if 	numeroARevisar >= 5 :
		# entrego sólo su parte entera aumentada en uno
		redondeado = parteEntera + 1
	# De lo contrario
	else :
		# entrego sólo su parte entera 
		redondeado = parteEntera + 1

# Si se desea un número distinto de cifras
else :

	# Si la cifra siguiente tiene un valor igual o superior a 5
	if  numeroARevisar >= 5:
		# La última cifra del redondeo se aumenta en 1 en su valor
		cifraRedondeada = int(parteDecimal[decimales - 1]) + 1
		# Se construye la parte decimal a partir de los dígitos 
		# que deseo de la parte decimal actual
		# y de la cifra redondeada
		parteDecimal = parteDecimal[0:decimales - 1] + str(cifraRedondeada)
		# Se construye el número redondeado combinando 
		# la parte entera, la parte decimal y el punto
		redondeado = parteEntera + "." + parteDecimal
	# En caso de que la cifra siguiente no sea igual o superior a 5
	else :
		# Se construye el número redondeado a partir 
		# de la parte entera y los caracteres 
		# deseados de la parte decimal
		redondeado = parteEntera + "." + parteDecimal[0:decimales]

# SALIDA

# Se entrega por pantalla la salida al usuario
print "El valor de", numeroDecimal, "redondeado con ", 
print decimales, "cifras decimales es: "
print "\t", redondeado