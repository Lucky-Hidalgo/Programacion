'''
# ENTRADA

# Solicito lista de valores
lista = input("Ingrese una lista de valores: ")

# PROCESAMIENTO
# Declaro iterador
i = 0
# Declaro acumulador para ir guardando la suma de los elementos
acumulador = 0

# Declaro una variable para buscar el menor elemento de la lista
menor = lista[0]

# Declaro una variable para buscar el mayor elemento de la lista
mayor = lista[0]

# Mientras no haya recorrido toda la lista
while i < len(lista) :
    # Si el elemento que estoy revisando es menor que el menor
    if lista[i] < menor :
        # El elemento se vuelve el menor
        menor = lista[i]
    # Si el elemento que estoy revisando es mayor que el mayor
    if lista[i] > mayor :
        # El elemento se vuelve el mayor
        mayor = lista[i]
    # Acumulo cada elemento de la lista para almacenar
    # la suma de todos los elementos
    acumulador = lista[i] + acumulador
    # Incremento el iterador para revisar el siguiente elemento de la lista
    i = i + 1

# Una vez terminado el while, calculo el promedio dividiendo por la
# cantidad de elementos en la lista
promedio = acumulador/ float(len(lista))

# SALIDA
# Entrego las salidas solicitadas
print "Para la lista", lista
print "Su menor elemento es:", menor
print "Su mayor elemento es:", mayor
print "El promedio de sus elementos es:", promedio

'''

# ENTRADA

# Solicito lista de valores
lista = input("Ingrese una lista de valores: ")

# PROCESAMIENTO

# Declaro acumulador para ir guardando la suma de los elementos
acumulador = 0

# Declaro una variable para buscar el menor elemento de la lista
menor = lista[0]

# Declaro una variable para buscar el mayor elemento de la lista
mayor = lista[0]

# Para cada elemento en la lista
for elemento in lista :
    # Si el elemento que estoy revisando es menor que el menor
    if elemento < menor :
        # El elemento se vuelve el menor
        menor = elemento
    # Si el elemento que estoy revisando es mayor que el mayor
    if elemento > mayor :
        # El elemento se vuelve el mayor
        mayor = elemento
    # Acumulo cada elemento de la lista para almacenar
    # la suma de todos los elementos
    acumulador = elemento + acumulador


# Una vez terminado el for, calculo el promedio dividiendo por la
# cantidad de elementos en la lista
promedio = acumulador/ float(len(lista))

# SALIDA
# Entrego las salidas solicitadas
print "Para la lista", lista
print "Su menor elemento es:", menor
print "Su mayor elemento es:", mayor
print "El promedio de sus elementos es:", promedio

