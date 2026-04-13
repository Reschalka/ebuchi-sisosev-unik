import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Функция 7: z = x² + y² + x
Z = X**2 + Y**2 + X

# 1. Контурная диаграмма
plt.figure()
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar()
plt.title('z = x² + y² + x (контур)')
plt.savefig('contour.png')

# 2. 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title('z = x² + y² + x (3D)')
plt.savefig('3d.png')

plt.show()