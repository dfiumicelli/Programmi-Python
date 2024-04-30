import numpy as np

z = np.arange(100)
v = np.random.uniform(0, 100)
index = (np.abs(z - v)).argmin()
print(z[index])
