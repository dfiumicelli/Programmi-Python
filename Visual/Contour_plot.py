import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    return np.sin(x) ** 5 + np.cos(3 + y * x) * np.cos(x)


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)
x, y = np.meshgrid(x, y)
z = f(x, y)
fig, ax = plt.subplots(1)
contour = ax.contourf(x, y, z, cmap="RdGy")
fig.colorbar(contour, ax=ax)
plt.show()
