# MAGIA NEGRA QUE PIDE UNA LISTA, Y LA TRANSFORMA AUTOMÁTICAMENTE A UNA LISTA DE ENTEROS
lista = list(map(int,input("Ingrese una lista de números enteros, separados por espacio:").split(" ")))

# Se imprime la lista para verificar que tenga lo que queremos
print(lista)

##########################################################################################
# EXPLICACIÓN
##########################################################################################
# PASO 1: Se solicita una entrada usando input(), esta será un string
lista = input("Ingrese una lista de números enteros, separados por espacio:")

# PRINTS PARA MOSTRAR EL PASO
print('PASO 1:')
print('\t', lista)

# PASO 2: Se utiliza el método .split(" ") para cortar el string por el caracter espacio
# obteniendo así una lista de strings
lista = lista.split(" ")

# PRINTS PARA MOSTRAR EL PASO
print('PASO 2:')
print('\t', lista)

# PASO 3: Se utiliza la función map(), lo que map hace es:
# Aplica la función entregada en el primer parámetro (en este caso int)
# Al objeto del segundo parámetro (en este caso la lista de string)
# Devolviendo un objeto de tipo map, el cuál es útil para iterar pero no para
# almacenar o modificar valores
lista = map(int, lista)

# PRINTS PARA MOSTRAR EL PASO
print('PASO 3:')
print('\t', lista)
# Como vemos, map nos entrega un mensaje de que algo existe en memoria, pero no muestra los valores

# PASO 4: Se realiza la conversión de map a lista, lo que nos permite volver a aplicar
# todas las operaciones de listas sobre la entrada
lista = list(lista)

# PRINTS PARA MOSTRAR EL PASO
print('PASO 4:')
print('\t', lista)
