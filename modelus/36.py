import math
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
from Z35 import bisection, newton

# Отрезок
a, b = 0.0, math.pi

# Точности
powers = list(range(2, 23))
epsilons = [2.0 ** -p for p in powers]


# Уравнения
def eq1(x): return math.sin(x - math.pi / 6) - 0.5

def eq2(x): return math.cos(x) - 0.5

def eq3(x): return math.tan(x) - 1.0

def eq4(x): return math.atan(x) - math.pi / 3

def eq5(x): return (x + 4) * (x - 1) * (x - 20) * (x + 33)

equations = [
    (eq1, math.pi / 3, "sin(x-π/6)-0.5=0"),
    (eq2, math.pi / 3, "cos(x)-0.5=0"),
    (eq3, math.pi / 4, "tg(x)=1"),
    (eq4, math.sqrt(3), "arctan(x)=π/3"),
    (eq5, 1.0, "(x+4)(x-1)(x-20)(x+33)=0")
]

for f, xtrue, title in equations:
    n_b, n_n = [], []

    for eps in epsilons:
        root, nb = bisection(a, b, eps, f)
        n_b.append(nb)

        root, nn = newton(a, b, eps, f)
        n_n.append(nn)

    plt.plot(powers, n_b, 'o-', color='black', label='Бисекция')
    plt.plot(powers, n_n, 's-', color='gray', label='Ньютон')
    plt.xlabel('log₂(ε)')
    plt.ylabel('Итерации n')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()