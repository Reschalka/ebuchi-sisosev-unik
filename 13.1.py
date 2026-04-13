import numpy as np

# ЗАДАНИЕ 2: x^3
print("x^3 от -2 до 2:")
for step in [0.01, 0.1, 0.25]:
    x = np.arange(-2, 2 + step/2, step)
    y = x**3
    print(f"Шаг {step}: {len(x)} значений")
    print(f"  x от {x[0]} до {x[-1]:.3f}")
    print(f"  y от {y[0]:.3f} до {y[-1]:.3f}")

# ЗАДАНИЕ 7: 4 sin(πt + π/8) - 1
for step in [1, 0.25]:
    t = np.arange(-10, 10 + step/2, step)
    y = 4*np.sin(np.pi*t + np.pi/8) - 1
    print(f"Шаг {step}: {len(t)} значений")
    print(f"  t от {t[0]} до {t[-1]:3.f}")
    print(f"  y от {y.min():.3f} до {y.max():.3f}")

# ЗАДАНИЕ 12: e^x
for step in [0.01, 0.1, 0.25]:
    x = np.arange(-2, 2 + step/2, step)
    y = np.exp(x)
    print(f"Шаг {step}: {len(x)} значений")
    print(f"  x от {x[0]} до {x[-1]:.3f}")
    print(f"  y от {y[0]:.3f} до {y[-1]:.3f}")