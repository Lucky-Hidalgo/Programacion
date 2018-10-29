import numpy as np
import matplotlib.pyplot as plt

r1 = 0.8
r2 = 1.0
r3 = 3
angulo = np.arange(-np.pi,np.pi,0.0001)

vectorR1 = r3+ np.cos(angulo)
vectorX = vectorR1 * np.cos(angulo)
vectorY = vectorR1 * np.sin(angulo)

plt.plot(vectorX, vectorY)

ax = plt.gca()
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))
ax.spines['right'].set_position(('data', 0))
ax.spines['top'].set_position(('data', 0))


plt.show()
