# Задание 22 - вторая программа (построение гистограмм)

import matplotlib.pyplot as plt
import os

os.chdir('Распределения')

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        # Читаем данные из файла
        f = open(filename, 'r')
        data = []
        for line in f:
            data.append(float(line.strip()))
        f.close()

        # Строим гистограмму
        plt.figure()
        plt.hist(data, bins=20, edgecolor='black', color='pink')
        plt.title(filename.replace('.txt', ''))
        plt.xlabel('Значения')
        plt.ylabel('Частота')

        # Сохраняем как PNG
        plt.savefig(filename.replace('.txt', '.png'))
        plt.close()

print("Гистограммы сохранены в папке 'Распределения'")