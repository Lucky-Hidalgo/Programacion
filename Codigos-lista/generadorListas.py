# Generador de números enteros
from random import randint

# ENTRADA
# Solicito la cantidad de valores para la lista
cantidad = int(input("Ingrese la cantidad de valores que desea: "))

# Solicito el mínimo del rango
minimo = int(input("Ingrese el valor más bajo del rango: "))

# Solicito el máximo del rango
maximo = int(input("Ingrese el valor más alto del rango: "))

# PROCESO
# Declaro la lista vacia
lista = []

# Mientras la lista no tenga la cantidad de elementos
while len(lista) < cantidad :
    #  Se genera un número aleatorio
    numero = randint(minimo, maximo)
    # Se agrega el numero a la lista
    lista.append(numero)
# SALIDA
# Se imprime la lista
print(lista)
