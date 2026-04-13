import numpy as np
mat12 = np.ones((5, 5)) * np.arange(1, 6).reshape(5, 1)
np.savetxt('5x5.txt', mat12, fmt='%d')