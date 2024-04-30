import numpy as np

a = np.random.randint(0, 2, 5)
b = np.random.randint(0, 2, 5)

equal = np.allclose(a, b, atol=0.00001, rtol=0.00001)
print(equal)