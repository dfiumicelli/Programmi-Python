import numpy as np
import time

a = np.ones(shape=(10000000, 1))
b = np.ones(shape=(10000000, 1))

start = time.time()
c = a+b
print("Tempo di esecuzione con elementwise ", time.time() - start)

start = time.time()
for i, j in zip(a, b):
    somma = i+j
print("Tempo esecuzione col for", time.time() - start)