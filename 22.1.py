# Задание 22 - первая программа (генерация распределений)

import numpy as np
import os

# Создаём папку, если её нет
if not os.path.exists('Распределения'):
    os.mkdir('Распределения')

os.chdir('Распределения')

# Равномерное распределение
x_uniform = np.random.uniform(-5, 5, 1000)
f = open('равномерное.txt', 'w')
for v in x_uniform:
    f.write(str(v) + '\n')
f.close()

# Нормальное распределение
x_normal = np.random.normal(0, 1, 1000)
f = open('нормальное.txt', 'w')
for v in x_normal:
    f.write(str(v) + '\n')
f.close()

# Распределение χ² с 5 степенями свободы
x_chi2 = np.random.chisquare(5, 1000)
f = open('хи-квадрат.txt', 'w')
for v in x_chi2:
    f.write(str(v) + '\n')
f.close()

print("Файлы с распределениями созданы в папке 'Распределения'")