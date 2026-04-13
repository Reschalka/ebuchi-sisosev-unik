import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-10, 10.1, 0.5)
y = 4*np.sin(np.pi*t + np.pi/8) - 1

plt.plot(t, y, 'ro--')
plt.grid(True)

plt.savefig('grap.png')
plt.savefig('grap.jpg')
plt.savefig('grap.pdf')

plt.show()