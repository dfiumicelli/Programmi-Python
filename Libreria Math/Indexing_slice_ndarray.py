import numpy as np

a = np.random.normal(size=(2, 2, 3))
print(a)
print("a[1, 1, 2]", a[1, 1, 2])
print("a[1, :, :]", a[1, :, :])  # visuallizzo la prima delle due matrici 2x3

print("a[1]", a[1])  # analoga alla precedente
print("a[:, 1, 0:2]", a[:, 1, 0:2])  # visualizziamo uno slice

# possiamo anche modificare un singolo elemento accedendovi

a[1, 1, 2] = 0.0
print("nuova a", a)
