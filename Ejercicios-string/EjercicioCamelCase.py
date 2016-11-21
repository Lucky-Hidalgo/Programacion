# -*- coding: cp1252 -*- 

# ENTRADA
# Solicito el texto para aplicar camel case
texto = raw_input("Ingrese texto: ")

# PROCESAMIENTO

# Genero un string para guardar el texto en camel case
textoNuevo = ""
# Defino un contador para avanzar por los caracteres
i = 0
# Mientras no haya recorrido todo el texto
while i < len(texto):
	# Si es el primer caracter, lo pongo en mayúsculas
    if i == 0 :
        textoNuevo = textoNuevo + texto[i].upper()
    # Sino es el primer caracter y se encuentra un espacio
    elif texto[i] == " ":
    	# El siguiente caracter se agrega al nuevo texto en mayúsculas
        textoNuevo = textoNuevo + texto[i+1].upper()
        # incremento el iterador en 1 para saltarme el caracter y no escribirlo duplicado
        i = i + 1
    # Sino se cumplen las dos condiciones anteriores
    else :
    	# Se agrega la letra en minúsculas
        textoNuevo = textoNuevo + texto[i].lower()
    # Incremento el contador en uno
    i = i + 1

# SALIDA
# Imprimo el texto en CamelCase
print "El texto"
print "\t" + texto + "en CamelCase quedaría como: " 
print textoNuevo
        
