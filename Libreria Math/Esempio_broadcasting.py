import numpy as np

a11 = np.array([1, 2, 3])
print(a11.shape)
b11 = np.array([[1, 2, 3], [4, 5, 6]])
print(a11 + b11)

d = np.zeros(shape=(2, 1, 1))  # tensore forzatamente a tre dimensioni
d11 = np.zeros(shape=(2,))  # stesso tensore ma ai fini del broadcasting genera errori
e = np.ones(shape=(2, 3, 4))
print(d+e)
print(d11+e)
