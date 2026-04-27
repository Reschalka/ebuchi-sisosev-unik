# Задание 29
import numpy as np
from math import pi
import matplotlib.pyplot as plt

t = np.arange(-10, 10, 0.05)
x = 4 * np.sin(pi * t + pi / 8) - 1
Px = np.abs(np.fft.rfft(x) / (0.5 * len(t)))**2
fn = 1 / (2 * 0.05)
freq = np.linspace(0, fn, len(Px))
plt.grid(True)
plt.plot(freq, Px, color='red')
plt.show()