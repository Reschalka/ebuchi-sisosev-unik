from numpy import random

n = int(input('Введите количество значений: '))
a = input('Введите диапазон равномерного распределения (min max): ').split()

x = random.uniform(float(a[0]), float(a[1]), n)
print(f'\nРавномерное распределение [{a[0]}; {a[1]}]:')
print(x)
