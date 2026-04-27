# Задание 30

import numpy as np
import matplotlib.pyplot as plt

n = 10000
x = np.random.uniform(0, 1, n)

# Построение гистограммы
plt.hist(x, bins=50, density=True, color='green', edgecolor='black', alpha=0.7)
plt.title('Гистограмма равномерного распределения [0; 1]')
plt.xlabel('Значение')
plt.ylabel('Плотность вероятности')
plt.grid(True, alpha=0.3)
plt.show()
