# ENTRADA
# Paso N°1: Obtener la nota de prueba N°1 del estudiante
prueba1 = input("Ingrese la nota de la prueba N°1: ")
# Paso N°2: Obtener la nota de prueba N°2 del estudiante
prueba2 = input("Ingrese la nota de la prueba N°2: ")
# Paso N°3:Obtener la nota del trabajo del estudiante
trabajo = input("Ingrese la nota de la trabajo: ")

# PROCESOS
# Paso N°4: Calcular el promedio considerando
# - 35% prueba N°1
# - 35% prueba N°2
# - 30% trabajo
promedio = prueba1 * 0.35 + prueba2 * 0.35 + trabajo * 0.3

# SALIDAS
# Paso N°5: Si el promedio es mayor o igual a 4.0
if promedio >= 4.0 :
    print "El estudiante aprueba con promedio: ", promedio
    if promedio >= 6.0 :
        print "El estudiante se gana un premio"
# Sino
else :
    print "El estudiante reprueba con promedio:", promedio
    if promedio < 3.0 :
        print "Hasta el otro semestre :c"
    else :
        print "A estudiar en verano :c"
