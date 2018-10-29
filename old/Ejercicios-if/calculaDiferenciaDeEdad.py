# ENTRADA

# Solicito la edad de la primera persona
primeraEdad = input("Ingrese la edad de la primera persona: ")
# Solicito la edad de la segunda persona
segundaEdad = input("Ingrese la edad de la segunda persona: ")

# PROCESOS

# Calculo la diferencia de edad
diferencia = primeraEdad - segundaEdad

# SALIDA

# Si la diferencia es mayor a 0
if diferencia > 0 :
	print "La primera persona es ", diferencia, "años mayor que la segunda"
# Si la diferencia es igual a cero
elif diferencia == 0 :
        print "Ambas personas tienen la misma edad"

else : 
	print "La primera persona es ", - diferencia, "años menor que la segunda"
