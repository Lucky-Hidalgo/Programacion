#BLOQUE DE DEFINICIONES

# Función que retorna el elemento de mayor valor de una lista
# Entrada: Lista de números
# Salida: Valor entero
def encontrarMaximo(lista):
	maximo = lista[0]
	for elemento in lista :
		if maximo < elemento :
			maximo = elemento
	return maximo

# Función que entrega una lista ordenada de manera descendente
# Entrada: Lista de números
# Salida: Lista de números ordenada
def ordenarLista(lista):
	listaOrdenada = []
	while len(lista) > 0 :
		listaOrdenada.append(encontrarMaximo(lista))
	return listaOrdenada

	
# BLOQUE PRINCIPAL

# ENTRADA
lista = input("Ingrese una lista: ")

# PROCESAMIENTO
lista = ordenarLista(lista)

# SALIDA
print lista
		