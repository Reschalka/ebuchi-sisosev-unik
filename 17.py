import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-1, 1, 0.01)

# Все графики сразу
fig = plt.figure(figsize=(15, 10))

# 1. Один столбец
for i in range(6):
    plt.subplot(6, 1, i+1)
    plt.plot(t, np.sin((i+2)*np.pi*t))
    plt.title(f'ω={(i+2)}π')
plt.savefig('1col.png')

# 2. Два столбца
fig = plt.figure(figsize=(15, 10))
for i in range(6):
    plt.subplot(3, 2, i+1)
    plt.plot(t, np.sin((i+2)*np.pi*t))
plt.savefig('2col.png')

# 3. Три столбца
fig = plt.figure(figsize=(15, 10))
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.plot(t, np.sin((i+2)*np.pi*t))
plt.savefig('3col.png')

# 4. Одна строка
fig = plt.figure(figsize=(15, 3))
for i in range(6):
    plt.subplot(1, 6, i+1)
    plt.plot(t, np.sin((i+2)*np.pi*t))
plt.savefig('1row.png')
plt.show()