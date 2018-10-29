import numpy as np
import matplotlib.pyplot as plt

NOMBRE_ARCHIVO = "marcas.csv"

def leerArchivo(nombreArchivo):
	archivo = open(nombreArchivo, "r")
	contenido = archivo.readlines()
	archivo.close()
	return contenido


def procesarContenido(contenido):
	listaFechas = []
	listaCorredor1 = []
	listaCorredor2 = []
	listaCorredor3 = []
	listaCorredor4 = []
	i = 1
	while i < len(contenido) :
		lista = contenido[i].split(",")
		listaFechas.append(lista[0])
		listaCorredor1.append(float(lista[1]))
		listaCorredor2.append(float(lista[2]))
		listaCorredor3.append(float(lista[3]))
		listaCorredor4.append(float(lista[4]))
		i = i + 1
		
	matrizValores = [listaFechas, listaCorredor1, listaCorredor2, listaCorredor3, listaCorredor4]
	return matrizValores
	
def convertirAArray(valores):
	valores[1] = np.array(valores[1])
	valores[2] = np.array(valores[2])
	valores[3] = np.array(valores[3])
	valores[4] = np.array(valores[4])
	return valores
	

def seleccionarRango(contenido, fechaInicio, fechaFin):
	rangoFechas = []
	rangoCorredor1 = []
	rangoCorredor2 = []
	rangoCorredor3 = []
	rangoCorredor4 = []
	
	
	i = 0
	while contenido[0][i] != fechaInicio :
		i = i + 1
	while contenido[0][i] != fechaTermino :
		rangoFechas.append(contenido[0][i])
		rangoCorredor1.append(contenido[1][i])
		rangoCorredor2.append(contenido[2][i])
		rangoCorredor3.append(contenido[3][i])
		rangoCorredor4.append(contenido[4][i])
		i = i + 1
	rango = [rangoFechas, rangoCorredor1, rangoCorredor2, rangoCorredor3, rangoCorredor4]
	return rango
# BLOQUE PRINCIPAL
#ENTRADA
contenidoArchivo = leerArchivo(NOMBRE_ARCHIVO)
fechaInicio = raw_input("Ingrese el día de inicio a graficar (formato DD/MM/AAAA): ")
fechaTermino = raw_input("Ingrese el día de término a graficar (formato DD/MM/AAAA): ")

# PROCESAMIENTO
valores = contenidoArchivo[0].strip().split(",")
contenidoProcesado = procesarContenido(contenidoArchivo)

rangoAGraficar = seleccionarRango(contenidoProcesado,fechaInicio, fechaTermino)

rangoAGraficar = convertirAArray(rangoAGraficar)
# SALIDA
rectaCorredor1 = plt.plot(rangoAGraficar[1], label=valores[1])
rectaCorredor2 = plt.plot(rangoAGraficar[2], label=valores[2])
rectaCorredor3 = plt.plot(rangoAGraficar[3], label=valores[3])
rectaCorredor4 = plt.plot(rangoAGraficar[4], label=valores[4])
plt.title("Marcas de corredores entre " + fechaInicio + " y " + fechaTermino)
plt.xlabel("fechas")
plt.ylabel("tiempo [s]")
plt.legend()
plt.show()
