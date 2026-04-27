# аппроксимация параболы с шумом

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-6, 6, 0.1)
y = x**2 - x - 6
r = np.random.normal(0, 2, len(x))
z = y + r

# Аппроксимация полиномом 2-й степени методом наименьших квадратов
a = np.ones((len(x), 3))
a[:, 1] = x
a[:, 2] = x**2
result = np.linalg.lstsq(a, z, rcond=None)
za = np.dot(a, result[0])

# Ошибка аппроксимации
error = result[1][0] / len(x)
print(f'Ошибка аппроксимации: {error:.4f}')

plt.plot(x, z, 'o', color='red', markersize=2, label='Данные с шумом')
plt.plot(x, za, color='blue', linewidth=2, label='Аппроксимация')
plt.plot(x, y, '--', color='green', linewidth=1, label='Истинная парабола')
plt.title('Аппроксимация параболы полиномом 2-й степени')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()