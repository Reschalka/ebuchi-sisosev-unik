# Задание 26

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6, 6, 0.1)
y = x**2 - x - 6

# 5 рядов с разными реализациями шума
r = np.random.normal(0, 2, len(x))
y1 = y + r

r = np.random.normal(0, 2, len(x))
y2 = y + r

r = np.random.normal(0, 2, len(x))
y3 = y + r

r = np.random.normal(0, 2, len(x))
y4 = y + r

r = np.random.normal(0, 2, len(x))
y5 = y + r

# Объединяем в один двумерный массив
y_all = np.column_stack([y1, y2, y3, y4, y5])

plt.errorbar(x, y_all.mean(axis=1), yerr=y_all.std(axis=1),
             marker='.', color='green', ecolor='blue',
             linestyle='-', linewidth=1, capsize=3,
             label='Среднее ± стандартное отклонение (5 экспериментов)')


plt.title('График с планками погрешностей (5 экспериментов)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('errorbars_5.png')
plt.show()
