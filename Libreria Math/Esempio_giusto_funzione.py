import numpy as np

x = np.arange(4)
y = np.arange(4)

xx, yy = np.meshgrid(x, y)
print(xx)
print(yy)


def f(x, y):
    return x ** 2 + y


print(f(xx, yy))
