import numpy as np

z = np.random.random(10)
z[z.argmax()] = 0
print(z)