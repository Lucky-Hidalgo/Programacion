'''
EJERCICIO:

Construya un programa que solicite una lista de elementos (elemento a elemento) y calcule el promedio, la desviación estándar, la moda 
y la mediana de dicha lista.

'''

# PROGRAMA QUE CALCULA EL PROMEDIO, DESVIACIÓN ESTÁNDAR,
# MODA Y MEDIANA DE UNA LISTA DE ELEMENTOS
# AUTOR:
# VERSIÓN: 1.0

# BLOQUE DE DEFINICIONES

# IMPORTACIÓN DE FUNCIONES
from math import sqrt

# DEFINICIÓN DE FUNCIONES

# Función que calcula el promedio de una lista
# ENTRADA: Lista
# SALIDA: Promedio de una lista
def calcularPromedio(lista):
    # Defino un acumulador en 0.0 para asegurar
    # que el resultado sea flotante
    acumulador = 0.0
    # Para cada elemento en la lista
    for elemento in lista:
        # Lo sumo al acumulador
        acumulador = acumulador + elemento
    # Calculo el promedio de la lista
    # como el resultado guardado en acumulador
    # dividido por la cantidad de elementos de la lista
    promedio = acumulador/len(lista)
    # Se entrega como resultado el promedio de la lista
    return promedio

# Función que calcula el promedio de una lista
# ENTRADA: Lista
# SALIDA: Promedio de una lista
def calcularPromedio2(lista):
    # Se utiliza la función nativa sum y se divide por el largo de la
    # lista transformado a flotante
    return sum(lista)/float(len(lista))

# Función que calcula el promedio de una lista
# ENTRADA: Lista
# SALIDA: Promedio de una lista
def calcularPromedio3(lista):
    # Defino un acumulador 
    sumatoria = 0
    # Defino un iterador
    i = 0
    # Mientras i sea menor que el largo de la lista
    while i < len(lista):
        # Sumo el elemento en la posición i
        # a la sumatoria
        acumulador = acumulador + lista[i]
        # Incremento el iterador en 1
        i += 1
    # Calculo el promedio de la lista
    # como el resultado guardado en acumulador
    # dividido por la cantidad de elementos de la lista
    promedio = float(sumatoria)/len(lista)
    # Se entrega como resultado el promedio de la lista
    return promedio


# Función que calcula la desviación estandar de una lista
# Entrada: lista
# Salida: Desviación estándar de la lista
def calcularDevStd(lista):
    # Calculo el promedio usando la función anterior :)
    promedio = calcularPromedio(lista)
    # Defino un iterador
    i = 0
    # Defino un acumulador para almacenar los resultados
    # parciales de la sumatoria
    acumulador = 0
    # Mientras el valor de i no alcance el largo de la lista
    while i < len(lista) :
        # Calculo el valor del término
        valorParcial = (lista[i] - promedio) ** 2
        # Lo agrego al acumulador
        acumulador = acumulador + valorParcial
        # Incremento el iterador en 1
        i = i + 1
    # Calculo la desviación estándar
    # utilizando la función sqrt desde el módulo math
    # (equivalente a elevar a 0.5)
    desviacionEstandar = sqrt(acumulador / (len(lista) - 1))
    # Entrego el valor de la desviación estándar
    return desviacionEstandar

# Función que cuenta cuantas veces se repite un elemento en una lista 
# ENTRADA: Lista de elementos, elemento a buscar
# SALIDA: Cantidad de veces que se repite un elemento
def contarApariciones(lista, elemento):
	# Declaro un contador, para contar las veces que se encuentra el elemento 
	veces = 0
	# Declaro un iterador para ir recorriendo los elementos de la lista 
	i = 0
	# Mientras i no alcance el largo de la lista 
	while i < len(lista):
		# Si el elemento es igual al elemento en la posición i de la lista 
		if elemento == lista[i]:
			# Incremento el contador en 1
			veces = veces + 1
		# Incremento el iterador para seguir avanzando
		i = i + 1
	# Retorno la cantidad de veces que aparece el elemento 
	return veces 
	
# Función que encuentra el máximo valor en una lista 
# ENTRADA: lista de elementos  
# SALIDA: Máximo valor 
def encontrarMaximo(lista):
	# Declaro que el maximo elemento será el primer elemento de la lista
	# esto sirve para efectos de comparación
	maximo = lista[0]
	# Para cada elemento en la lista 
	for valor in lista :
		# Si el valor a revisar es mayor que el máximo 
		if valor > maximo :
			# Actualizo el valor del máximo 
			maximo = valor
	# Al final del ciclo se retorna el maximo valor 
	return maximo

	
# Función que crea una tabla (lista de listas) indicando las veces que se repite 
# cada elemento 
# ENTRADA: Lista de enteros
# SALIDA: Tabla de frecuencias (lista de listas de enteros)
def crearTablaDeFrecuencias(lista):
	# Creo una lista de listas
	# En tablaDeFrecuencias[0] se almacenarán los valores
	# En tablaDeFrecuencias[1] se almacenarán las veces que se repite cada valor 
	tablaDeFrecuencias = [[],[]]
	# Se recorre la lista original para buscar las veces en que se repite cada elemento 
	for valor in lista :
		# Si el valor no se había agregado previamente a la tabla de frecuencias
		if not (valor in tablaDeFrecuencias[0]):
			# Se cuenta la cantidad de veces que este aparece 
			vecesQueSeRepite = contarApariciones(lista, valor)
			# Se agrega el valor a la lista [0]
			tablaDeFrecuencias[0].append(valor)
			# Se agrega las veces que se repite a la lista [1]
			tablaDeFrecuencias[1].append(vecesQueSeRepite)
	# Una vez completado el ciclo, se entrega la tabla de frecuencias completa 
	return tablaDeFrecuencias

# Función que calcula la moda de una lista
# ENTRADA: Lista de elementos
# SALIDA: Elemento(s) que más se repite(n) (lista de elementos)
def calcularModa(lista):
    # Se crea la tabla de frecuencias 
    tablaDeFrecuencias = crearTablaDeFrecuencias(lista)
    # Se encuentra la frecuencia máxima
    maximo = encontrarMaximo(tablaDeFrecuencias[1])
    # Se declara un iterador para recorrer la tabla de frecuencias 
    i = 0 
    # se crea una lista vacía para almacenar los valores de los elementos que más se repiten 
    modas = []
    # Mientras el iterador no alcance el largo de la tabla de frecuencias 
    while i < len(tablaDeFrecuencias[1]) :
        # Si el maximo coincide con la frecuencia del elemento 
        if maximo == tablaDeFrecuencias[1][i] :
            # Se agrega el valor del elemento a la lista 
            modas.append(tablaDeFrecuencias[0][i])
        # Se incrementa el iterador para avanzar en el ciclo while
        i = i + 1
    # Se retorna la lista de elementos que tienen la mayor frecuencia de la lista 
    return modas
		
# Función que ordena una lista utilizando el método de BubbleSort
# ENTRADA: lista de números  
# SALIDA: lista de números ordenada 
def ordenarLista(lista):
    # Declaro un iterador i para recorrer la lista 
    i = 0
    # Mientras el valor de  i no alcance el largo de la lista 
    while i < len(lista):
        # Declaro un iterador j para recorrer la lista 
        j = 0
        # Mientras el valor de j no alcance el largo de la lista 
        while j < len(lista):
            # Si el valor en la posición i es mayor al valor en la posición j 
            if lista[i] < lista[j] :
                # Se intercambian los valores 
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            # Se incrementa el valor de j 
            j = j + 1
        # Se incrementa el valor de i 
        
        i = i + 1
    # Se entrega la lista (original) ahora ordenada 
    return lista 
	
	
# Función que ordena una lista utilizando el método de ordenamiento por selección
# ENTRADA: lista de números  
# SALIDA: lista de números ordenada
def ordenarLista1(lista):
    # Se declara una lista vacía para almacenar la lista ordenada 
    listaOrdenada = []
    # Mientras a la lista original le queden elementos 
    while len(lista) > 0 :
        # Encuentro el mayor valor 
        mayor = encontrarMaximo(lista)
        # Lo elimino de la lista original 
        lista.remove(mayor)
        # Lo agrego al inicio de la lista nueva
        listaOrdenada = [mayor] + listaOrdenada
    # Entrego la lista ordenada 
    return listaOrdenada


# Función que calcula la mediana de una lista
# ENTRADA: Lista de elementos
# SALIDA: Elemento del medio de la muestra ordenada (mediana)
def calcularMediana(lista):
	# Ordeno la lista original 
    listaOrdenada = ordenarLista(lista)
	# Si el número de elementos de la lista es par
    if len(listaOrdenada) % 2 == 0 :
		# La mediana es el promedio de los dos valores 
        mediana = (listaOrdenada[len(listaOrdenada)/2] + listaOrdenada[len(listaOrdenada)/2 + 1])/2.0
		# Se entrega la mediana 
        return mediana
	# En caso contrario 
    else : 
		# La mediana es el elemento del medio 
        mediana = listaOrdenada[len(listaOrdenada)/2]
		# Se retorna el valor de la mediana 
        return mediana
#
# BLOQUE PRINCIPAL

# ENTRADA

# Solicito la cantidad de elementos a agregar
cantidad = input("Ingrese la cantidad de elementos que desea ingresar:")
if cantidad < 2 and not isinstance(cantidad,int): 
	print "Cantidad incorrecta, favor de volver a ingresarla"
	# Solicito la cantidad de elementos a agregar
	cantidad = input("Ingrese la cantidad de elementos que desea ingresar:")
# Creo una lista vacía para almacenarlos
elementos = []
# Mientras el largo de la lista no alcance la cantidad
while len(elementos) < cantidad :
    # solicito un elemento a agregar
    elemento = input("Ingrese el elemento a agregar: ")

    # Se utiliza la función isinstance para revisar que el elemento es una instancia
	# de los números flotantes, enteros o enteros largos 
    if isinstance(elemento, (float, int,long) ):
        # Agrego el elemento en la lista
        elementos.append(elemento)
	# Si el elemento no es ni entero, ni flotante, ni entero largo 
    else:
		# se indica que el elemento no se agregó 
        print "El elemento no se agregó por ser de tipo incorrecto"

    
# PROCESAMIENTO
# Invoco a la función calcularPromedio y almaceno el valor en una variable
promedio = calcularPromedio(elementos)
# Invoco a la función calcularDevStd y almaceno el valor en una variable
devStd = calcularDevStd(elementos)
# Invoco a la función calcularModa y almaceno el valor en una variable
modas = calcularModa(elementos)

# Invoco a la función para calcular las veces en que se repite los elementos de la moda 
vecesQueSeRepite = contarApariciones(elementos, modas[0])

# Invoco a la función calculaMediana y almaceno el valor en una variable
mediana = calcularMediana(elementos)

# SALIDA

# Se imprimen los mensajes de salida
print "Para la lista", elementos
print "El promedio es:", promedio
print "La desviacion estandar es:", devStd
print "La moda es:", modas, "con ", vecesQueSeRepite, "apariciones"
print "La mediana es:", mediana
