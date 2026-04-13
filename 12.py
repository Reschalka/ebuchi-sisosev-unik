import numpy as np

m = np.loadtxt('5x5.txt')

v = np.array([1, 2, 3, 4, 5])

r = m + v

print("Max:", np.max(r))
print("Min:", np.min(r))

s = np.sum(r, axis=1)
print("Суммы по строкам:", s)

np.savetxt('mat.txt', r, fmt='%d')
np.savetxt('sums.txt', s, fmt='%d')