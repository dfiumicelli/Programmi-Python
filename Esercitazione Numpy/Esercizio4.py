import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = a[::-1]  # Con lo slice posso specificare tre parametri, inizio, fine e step. Step -1 è come dire scorri al
# contrario
print(b)
