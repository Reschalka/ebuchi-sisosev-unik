import numpy as np
import matplotlib.pyplot as plt

t = np.arange(-1, 1.01, 0.01)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown']

for i in range(1, 7):
    omega = (i+1) * np.pi
    y = np.sin(omega * t)
    plt.plot(t, y, color=colors[i-1], label=f'ω={(i+1)}π')


plt.legend()
plt.grid(True)
plt.show()