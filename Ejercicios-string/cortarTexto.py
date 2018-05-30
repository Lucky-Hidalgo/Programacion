# -*- coding: cp1252 -*-
'''
Función que divide un string por un único 
caracter de corte

Lenguaje: Python
'''
# Función que corta un string por un caracter de corte
# ENTRADA: texto (string), car (caracter de corte)
# SALIDA: (lista de string)
def cortar(texto, car):
	# Se declara una lista auxiliar para almacenar el resultado
    resultado = []
	# Se declara un contador para recorrer el texto 
    i  = 0
	# Se declara un aux para almacenar los strings 
	# antes de llegar al caracter de corte 
    aux = ""
	# Mientras i no alcance el final del texto 
    while i < len(texto):
		# Si el caracter de corte es igual al
		# texto en la posición i
        if car == texto[i]:
			# Se agrega lo que llevo en el texto
			# a la lista 
            resultado.append(aux)
			# Se vacía el texto para comenzar de nuevo
            aux = ""
			# Se incrementa el contador 
            i = i  + 1
		# En caso contrario
        else :
			# Se agrega el caracter  en la posición i 
			# del texto a aux 
            aux = aux + texto[i]
			# Se incrementa el contador 
            i = i + 1
	# Se agrega el resultado de lo quedaba en aux
	# a la lista 
    resultado.append(aux)
	# Se retorna la lista resultado
    return resultado
