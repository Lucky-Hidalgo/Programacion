# -*- coding: cp1252 -*- 
# ENTRADA
frase = raw_input("Ingrese frase:")

# PROCESAMIENTO

# Defino un string vacío para poner la frase procesada
nuevaFrase = ""
# Inicializo un contador en 0 para recorrer toda la frase
i = 0
# Mientras no haya recorrido toda la frase
while i < len(frase) :
	# Si el caracter a revisar no es un espacio
    if frase[i] != " ":
    	# Lo agrego a un string con la frase procesada
        nuevaFrase = nuevaFrase +frase[i].lower()
    # Incremento el iterador
    i = i + 1

# Reinicio el contador, para recorrer ahora la frase procesada
i = 0
# Defino un booleano para verificar si la frase es un palíndromo
esPalindromo = True
# Mientras no haya recorrido toda la frase procesada
while i < len(nuevaFrase) :
	# Si encuentro dos caracteres que no coincidan
	if nuevaFrase[i] != nuevaFrase[len(nuevaFrase) -i - 1] :
		# La frase no es palíndromo
		esPalindromo = False

	# Incremento el iterador para seguir revisando
	i = i + 1

# SALIDA

# Si la frase es palíndromo, se lo informo al usuario
if esPalindromo :
	print "La frase"
	print "\t" + frase
	print "es un palíndromo"

# En caso contrario, informo que no es un palíndromo
else :
	print "La frase"
	print "\t" + frase
	print "no es un palíndromo"
