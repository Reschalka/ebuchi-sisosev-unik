import math
import matplotlib.pyplot as plt

# Функция для табуляции и построения графика
def func1(x):
    return x**2 + 10*x + 1

dx = 0.01

# Создаём список значений
x_values = list(map(lambda i: -2 + i * dx, range(int(4 / dx) + 1)))

# Вычисляем значения функции
y_values = list(map(func1, x_values))

# Строим график
plt.plot(x_values, y_values, color='black')
plt.title(r'$f(x) = x^2 + 10x + 1$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

# 2)
# import math
# import matplotlib.pyplot as plt
#
# # Шаг по времени
# dt = 0.05
#
# # Создаём список значений t от -10 до 10 с шагом dt
# # Всего точек: (10 - (-10)) / dt = 20 / 0.05 = 400
# t_values = list(map(lambda i: -10 + i * dt, range(int(20 / dt) + 1)))
#
# # Вычисляем значения функции f(t) = cos(2πt)
# f_values = list(map(lambda t: math.cos(2 * math.pi * t), t_values))
#
# # Строим график
# plt.plot(t_values, f_values, color='black')
# plt.title(r'$f(t) = \cos(2\pi t)$')
# plt.xlabel('t')
# plt.ylabel('f(t)')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.show()

# 3)
# import math
# import matplotlib.pyplot as plt
#
# # Функция для вычисления 2^x
# def func2(x):
#     return 2 ** x  # или math.pow(2, x)
#
# # Шаг по x
# dx = 0.02
#
# # Создаём список значений x от -2 до 2 с шагом dx
# x_values = list(map(lambda i: -2 + i * dx, range(int(4 / dx) + 1)))
#
# # Вычисляем значения функции
# y_values = list(map(func2, x_values))
#
# # Строим график
# plt.plot(x_values, y_values, color='black')
# plt.title(r'$f(x) = 2^x$')
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.show()