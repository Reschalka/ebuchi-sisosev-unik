import numpy as np

M = np.loadtxt ("Matrix.txt")
V = np.loadtxt ("Vector.txt")

x = np.linalg.solve(M, V)
np.savetxt('roots.txt', x)

print(np.linalg.det(M))
