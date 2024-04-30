import numpy as np

a = np.ones(3) + 1
b = np.ones(3) + 2
np.add(a, b, out=b)
np.divide(a, b, out=a)
np.negative(a, out=a)
np.multiply(a, b, out=a)
print(a)
