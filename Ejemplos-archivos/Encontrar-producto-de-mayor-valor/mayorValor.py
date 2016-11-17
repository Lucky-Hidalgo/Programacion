# -*- coding: cp1252 -*-
# Función que lee un archivo
# ENTRADA: Nombre del archivo a leer (string)
# SALIDA: Contenido del archivo (lista de strings)
def leerArchivo(nombreArchivo):
    # Abro el archivo
    archivo = open(nombreArchivo , "r")
    # Obtengo el contenido del archivo
    contenido = archivo.readlines()
    # Cierro el archivo
    archivo.close()
    # Entrego el contenido
    return contenido

# Función que procesa el contenido de la lista de Strings y lo transforma a lista de listas
# ENTRADA: Contenido (lista de strings)
# SALIDA: Contenido procesado (lista de listas)
def convertirAListaDeListas(listaDeStrings):
    # Creo una lista vacía
    listaDeListas = []
    # Elimino el encabezado del archivo.csv
    listaDeStrings.pop(0)
    # Para cada línea en la lista de strings
    for linea in listaDeStrings :
        # Utilizo split para transformar la línea de texto en una lista (utilizando como separador la ,)
        lista = linea.split(",")
        # Transformo el precio, que originalmente venía en string a entero
        precio = lista[2]
        lista[2] = int(precio)
        # Agrego la lista que representa todos los atributos del producto a la lista completa
        listaDeListas.append(lista)
    # Retorno la lista completa
    return listaDeListas

# Función que encuentra el máximo elemento en una lista
def encontrarMaximo(listaDeListas):
    # Determino que el máximo valor será el primer elemento de la lista
    maximo = lista[0][2]
    # Almaceno el producto al que corresponde ese maximo
    productoDeMayorValor = lista[0]
    # Para cada elemento en la lista
    for elemento in listaDeListas :
        # Si el precio del elemento a revisar es menor que el máximo
        if maximo < elemento[2] :
            # Modifico el valor del máximo, con el valor del precio más alto
            maximo = elemento[2]
            # Actualizo cuál es el producto al que corresponde el máximo precio
            productoDeMayorValor = elemento
    # Retorno el producto de mayor valor
    return productoDeMayorValor

def buscarMayorValor(listaDeProductos, precioMaximo):

    listaMaximos = []
    for producto in listaDeProductos :
        precioDeProducto = producto[2]
        if precioDeProducto == precioMaximo :
            listaMaximos.append(producto)
    return listaMaximos
    
   
# BLOQUE PRINCIPAL
# ENTRADA
contenido = leerArchivo("productos2.csv")
# PROCESAMIENTO
lista = convertirAListaDeListas(contenido)

producto =  encontrarMaximo(lista)

# SALIDA
print "El producto de mayor valor es:", producto[0], "con un precio de", producto[2]
