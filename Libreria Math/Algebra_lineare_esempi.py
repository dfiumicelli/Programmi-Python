import numpy as np

a = np.array([0, 0, 1, 1,])
b = np.array([1, 1, 0, 0,])

print("a dot b", np.dot(a, b))
print("a dot a", np.dot(a, a))
print("b dot b", np.dot(b, b))

c = 2 * np.diag(np.ones(4))
print("c dot a", np.dot(c, a))
print("c dot b", np.dot(c, b))

d = np.ones(shape=(4, 4))
print("c dot d\n", np.dot(c, d))

A = np.random.normal(size=(4, 4))
eigvals, eigvecs = np.linalg.eig(A)  # autovalori e autovettori di una matrice
det = np.linalg.det(A)
inv = np.linalg.inv(A)
print("inv\n", inv)