# Задание 23 - вычисление определителя матрицы

import numpy as np

M = np.loadtxt('Matrix.txt')
det = np.linalg.det(M)

print("Матрица:")
print(M)
