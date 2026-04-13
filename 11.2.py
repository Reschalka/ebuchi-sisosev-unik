import numpy as np

start = -15 * np.pi
stop = 15 * np.pi
step = np.pi / 12

massiv = np.arange(start, stop, step)

print(f"Начало: {start:.4f}")
print(f"Конец: {stop:.4f}")
print(f"Шаг: {step:.4f}")

np.savetxt('mass_7.txt', massiv, fmt='%.6f')
