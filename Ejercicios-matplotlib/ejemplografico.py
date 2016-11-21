import matplotlib.pyplot as grafico
import numpy

# PRO
vectorX = numpy.arange(-50, 50.01, 0.01)

vectorX2 = numpy.arange(-500, 500.01, 0.01)
vectorY = vectorX ** 3 - 5 * vectorX **2 - 50 * vectorX - 25

vectorY2 = - vectorX2 ** 3 + 25 * vectorX2 - 20

# SALIDA

recta1 = grafico.plot(vectorX, vectorY)

recta2 = grafico.plot(vectorX2, vectorY2)

grafico.setp(recta1, 'linestyle', '-', 'color', \
             'c', 'linewidth', 1.5)

grafico.setp(recta2, 'linestyle', '--', 'color', \
             'r', 'linewidth', 1.5)

grafico.title("TITULO")

grafico.xlabel("eje X")

grafico.ylabel("eje Y")

grafico.show()

grafico.show()
