import numpy as np

z = np.random.random((100,2))
x, y = np.atleast_2d(z[:, 0], z[:, 1])
d = np.sqrt((x-x.T)**2 + (y-y.T)**2)
print(d)
