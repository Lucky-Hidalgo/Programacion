# Programa que realiza operaciones sobre imágenes

# CONSTANTES

# NO SE REQUIEREN CONSTANTES


############################################################################
#
#   FUNCIONES
#
############################################################################

############################################################################
#
#   IMPORTACIÓN DE FUNCIONES
#
############################################################################

# Desde el módulo PIL importo las operaciones sobre imágenes
from PIL import Image

# Importo el módulo numpy completo con sus operaciones numéricas
import numpy

############################################################################
#
# DEFINICIÓN DE FUNCIONES PROPIAS
#
############################################################################


def convertir_imagen_a_archivo(nombre_imagen, nombre_destino):
    '''

    Función que lee una imagen, la codifica a una matriz de componentes RGB
    y la escribe en un archivo de salida .txt
    ENTRADA: String que representa el nombre y la extensión de la imagen,
            por ejemplo "imagen.bmp"
            String que representa el nombre y la extensión del archivo de
            destino, por ejemplo "salida.txt"
    SALIDA:  Entrega true si el archivo fue escrito correctamente
    '''
    # Se abre la imagen y se le almacena en una variable llamada imagen
    imagen = Image.open(nombre_imagen)
    # Se codifica la imagen a codificación RGB para mantener el formato solicitado
    imagen = imagen.convert('RGB')
    # Se convierte la imagen a una matriz del módulo numpy
    # (No se puede operar con ella)
    matriz_numpy = numpy.array(imagen)
    # Se abre el archivo con el nombre entregado en los parámetros formales
    # en modo de escritura
    archivo = open(nombre_destino, 'w')
    # Para cada fila de la matriz_numpy
    for fila in matriz_numpy:
        # Para cada lista de 3 componentes (RGB) en la fila
        # es decir, para cada pixel en la fila
        for pixel in fila :
            # Para cada componente en el pixel
            for componente in pixel :
                # Se escribe en el archivo un espacio el valor del componente
                # se transforma el valor del componente a string para permitir
                # que python lo escriba
                archivo.write( ' ' + str(componente))
            # Se separan los pixeles de cada fila escribiendo una coma cada vez que
            # se escriben los 3 componentes del pixel
            archivo.write(',')
        # Se escribe un salto de línea cada vez que se ha recorrido una fila de la
        # matriz
        archivo.write('\n')
    # Se cierra el archivo
    archivo.close()
    # Se retorna el valor booleano True, indicando que la operación se realizó
    return True


def leer_archivo(nombre_entrada):
    '''
    Función que lee un archivo .txt que representa una imagen y devuelve una matriz
    de listas.
    ENTRADA: String que representa el nombre y la extensión del archivo de
            a leer, por ejemplo "entrada.txt"
    SALIDA:  Entrega una matriz de listas, representando una imagen
    '''
    # Se abre el archivo con el nombre entregado como parámetro formal
    # en modo de escritura
    archivo = open(nombre_entrada,'r')
    # Se crea una matriz vacia para almacenar la salida
    matriz = []
    # Para cada linea del archivo
    for i in archivo :
        # Se genera una lista vacía que servirá para operar
        lista = []
        # Se genera una lista vacía que almacenará la fila completa de
        # la imagen
        fila = []
        # Se elimina la última coma (,) y el \n de la fila utilizando strip
        # luego se divide por las comas restantes utilizando split
        lista = i.strip(",\n").split(',')
        # Para cada pixel en la lista
        for pixel in lista :
            # Se divide el pixel por los espacios para obtener una lista con
            # las tres componentes
            aux  = pixel.split()
            # Para cada uno de los 3 elementos de aux
            # se usa un range para recorrer por índice y no por elemento
            for e in range(3) :
                # Se transforma el valor a entero
                
                aux[e] = int(aux[e])
            # Se añade aux, que es una lista de 3 elementos representando el
            # valor de rojo, verde y azul, a la fila de la matriz
            fila.append(aux)
        # Una vez que se ha recorrido la fila completa, ésta se añade a la matriz
        matriz.append(fila)
    # Se retorna la matriz
    return matriz


# Función que recibe una matriz de listas y entrega una copia exacta de la entrada
#
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos
# REQUIERE: Que la matriz exista y tenga el formato indicado

def copiar_matriz(matriz):
    '''
    Función que recibe una matriz de listas y entrega una copia exacta de la entrada
    ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
    SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos
    REQUIERE: Que la matriz exista y tenga el formato indicado
    '''
    # Se genera una matriz vacía para almacenar la copia de la matriz
    matriz_resultado = []
    # Se almacena la cantidad de filas en una variable filas
    filas = len(matriz)
    # Se almacena la cantidad de  elementos por fila en una variable columnas
    columnas = len(matriz[0])
    # Para cada elemento entre 0 y la cantidad de filas
    for i in range(filas):
        # Se genera una fila vacía
        nueva_fila = []
        # Para cada elemento (Pixel) entre 0 y la cantidad de elementos por fila
        for  j in range(columnas):
            # Se obtiene la componente roja (R) de cada pixel
            rojo = matriz[i][j][0]
            # Se obtiene la componente verde (G) de cada pixel
            verde = matriz [i][j][1]
            # Se obtiene la componente azul (B) de cada pixel
            azul = matriz[i][j][2]
            # Se crea una nueva lista con las componentes rojo, verde y azul de cada pixel
            pixel = [rojo, verde, azul]
            # Se agrega el pixel a la fila de la nueva matriz
            nueva_fila.append(pixel)
        # Una vez agregados todos los pixeles de la fila original a la fila nueva,
        # se agrega la nueva fila a la matriz
        matriz_resultado.append(nueva_fila)
    # Una vez agregadas todas las filas a la matriz nueva, esta se retorna
    return matriz_resultado

# Función que recibe una matriz de listas y transforma a 0 todos los componentes
# de la lista que no estén representando el verde
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
# SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos,
#          donde cada lista será de la forma [0, valor, 0]
# REQUIERE: Que la matriz exista y tenga el formato indicado
#
# IMPORTANTE: NO SE REQUIERE MODIFICAR ESTA FUNCIÓN
def aislar_verde(m):
    '''
    Función que recibe una matriz de listas y transforma a 0 todos los componentes
    de la lista que no estén representando el verde
    ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos  
    SALIDA:  Matriz, donde cada celda de la matriz es una lista de 3 elementos,
             donde cada lista será de la forma [0, valor, 0]
    REQUIERE: Que la matriz exista y tenga el formato indicado
    '''
    # Se llama dentro de la función aislar verde a la función
    # copia_matriz, asegurando de este modo que siempre las operaciones de esta función
    # se realizarán sobre una matriz distinta a la original
    matriz = copiar_matriz(m)
    # Para cada fila en la matriz
    for fila in matriz :
        # Para cada pixel en la fila
        for pixel in fila :
            # Se modifica el valor de la componente roja (La primera de la lista pixel)
            # igualándola a 0
            pixel[0] = 0
            # Se modifica el valor de la componente azul (La tercera de la lista pixel)
            # igualándola a 2
            pixel[2] = 0
            # Se puede observar que la componente verde no se ha alterado, por lo que
            # pixel[1] = pixel[1], operación que no impactaría en el resultado
            
    # Se retorna la matriz con todos los valores rojos y azules modificados
    return matriz

# Función que recibe una matriz de listas y crea el archivo de imagen que está representando
# ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
#          String representando el nombre y la extensión del archivo de salida
# SALIDA:  Entrega True si el archivo fue escrito correctamente
# REQUIERE: Que la matriz exista y tenga el formato indicado

def convertir_matriz_a_imagen(matriz, nombre_salida):
    '''
    Función que recibe una matriz de listas y crea el archivo de imagen que está representando
    ENTRADA: Matriz, donde cada celda de la matriz es una lista de 3 elementos
             String representando el nombre y la extensión del archivo de salida
    SALIDA:  Entrega True si el archivo fue escrito correctamente

    '''
    # Se convierte la matriz a un tipo de dato del módulo numpy para poder
    # realizar la conversión a imagen
    arr = numpy.array(matriz)
    # Se transforma el arr de numpy a la matriz, indicando la codificación que
    # el dato representa, el rango de los números y el formato de los números
    im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
    # Se guarda la imagen en el archivo de salida que se indicó en los parámetros formales
    im.save(nombre_salida)
    return True

##############################################################################################
#
#
#       BLOQUE PRINCIPAL
#
#
##############################################################################################


#
# ENTRADA
#
print("Ingrese la imagen a procesar")
nombre_entrada = input("por ejemplo, imagen.bmp: ")
print("Ingrese el nombre del archivo de destino,")
nombre_salida = input("por ejemplo, salida.txt ")

archivo_exitoso=convertir_imagen_a_archivo(nombre_entrada, nombre_salida)
if archivo_exitoso:
    print("El archivo ", nombre_salida, " se ha creado exitosamente")
    matriz = leer_archivo(nombre_salida)

#
# PROCESAMIENTO
#
    copia_original = copiar_matriz(matriz)
    copia_solo_verde = aislar_verde(matriz)

#
# SALIDA
#
    copia_exitosa = convertir_matriz_a_imagen(copia_original, "copia.bmp")

    copia_verde_exitosa = convertir_matriz_a_imagen(copia_solo_verde, "verde.bmp")

    if copia_exitosa and copia_verde_exitosa :
        print("Los archivos copia.bmp y verde.bmp se han creado correctamente")
    
else :
    print("Error al leer ", nombre_entrada, "compruebe que la ruta y el nombre del archivo son correctos")
