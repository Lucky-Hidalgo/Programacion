# PROGRAMA QUE INVIERTE UN NÚMERO ENTERO POSITIVO
# AUTOR: Luciano Hidalgo S.
# FECHA: 26-10-2018

# ENTRADA
numero = int(input('Ingrese un número entero positivo: '))

# PROCESAMIENTO
# Se declara una variable para almacenar el número invertido
invertido = 0 

# Mientras el número sea mayor que cero
while numero > 0 :
	# Se obtiene la cifra, utilizando el resto de 10
	cifra = numero % 10
	# Se elimina la última cifra, utilizando la 
	# división entera de 10
	numero = numero // 10
	# Se multiplica el valor almacenado en invertido por 10 
	# para agregar el espacio de la próxima cifra y se agrega
	# esta al número invertido
	invertido = invertido * 10 + cifra

# SALIDA
# Se imprime la salida
print('El número invertido es:', invertido)