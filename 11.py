import numpy as np

# Одномерные массивы
mass_10 = np.ones(10)
print("1. Одномерный массив из единиц длины 10:")
print(mass_10)

mass_55 = np.ones(55)
print("2. Одномерный массив из единиц длины 55:")
print(mass_55)

# Матрица 3x4
matr_3x4 = np.ones((3, 4))
print("3. Матрица 3x4 из единиц:")
print(matr_3x4)

# Трехмерный массив 2x4x5
matr_2x4x5 = np.ones((2, 4, 5))
print("4. Трехмерный массив 2x4x5 из единиц:")
print(matr_2x4x5[0])

# Сохранение в файлы
np.savetxt('10.txt', mass_10, fmt='%g')
np.savetxt('55.txt', mass_55, fmt='%g')
np.savetxt('3x4.txt', matr_3x4, fmt='%g')
np.savetxt('3d.txt', matr_2x4x5[0], fmt='%g')