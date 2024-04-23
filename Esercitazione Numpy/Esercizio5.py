import numpy as np

a = np.array([1, 4, 1, 0, 4, 0])
print(np.nonzero(a))
print(a[np.nonzero(a)])
