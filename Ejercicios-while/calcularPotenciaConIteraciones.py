# -*- coding: cp1252 -*- 

# ENTRADA

# Solicito el valor de la base
base = input("Ingrese el valor de la base: ")
# Solicito el valor del exponente
exponente = input("Ingrese el valor del exponente: ")


# PROCESAMIENTO

# Declaro una variable para almacenar los resultados
acumulador = 1

# Declaro un iterador para que realice el proceso de la potencia
j = 1

# Mientras el proceso no se haya realizado tantas veces como el exponente solicita
while j <= exponente :
	# Declaro una variable auxiliar para almacenar resultados parciales
    auxiliar = 0
    # Declaro un iterador para que realice el proceso de la multiplicación
    i = 1
    # Mientras el proceso no se haya realizado tantas veces como la base lo requiere
    while i <= base :
    	# Le sumo el acumulador al auxiliar
        auxiliar = auxiliar + acumulador
        # Incremento el iterador de la multiplicación
        i = i + 1
    # Incremento el iterador de la potencia
    j = j + 1
    # El acumulador pasa a ser el valor almacenado en auxiliar
    acumulador = auxiliar

'''
# DESCOMENTAR PARA QUE EL PROGRAMA MUESTRE UNA TRAZA

# Declaro una variable para almacenar los resultados
acumulador = 1

# Declaro un iterador para que realice el proceso de la potencia
j = 1

# Mientras el proceso no se haya realizado tantas veces como el exponente solicita
while j <= exponente :
    print "================================"
    print "Iteración de j N°:", j
    # Declaro una variable auxiliar para almacenar resultados parciales
    auxiliar = 0
    # Declaro un iterador para que realice el proceso de la multiplicación
    i = 1
    # Mientras el proceso no se haya realizado tantas veces como la base lo requiere
    while i <= base :
        print "\tIteración de i N°:", i
    	# Le sumo el acumulador al auxiliar
        print "\t\tauxiliar:", auxiliar
        print "\t\tacumulador", acumulador
        auxiliar = auxiliar + acumulador
        print "\t\tnuevo auxiliar: ", auxiliar
        # Incremento el iterador de la multiplicación
        i = i + 1
    # Incremento el iterador de la potencia
    j = j + 1
    # El acumulador pasa a ser el valor almacenado en auxiliar
    acumulador = auxiliar
    print "================================\n"

'''

# SALIDA

# Entrego el resultado
print "la potencia de", base, "elevado a", exponente, "es: "
print acumulador
