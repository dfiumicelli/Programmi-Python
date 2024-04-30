import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(0)
x = rng.randn(100)  # campionamento su gaussiana
y = rng.randn(100)
colors = rng.rand(100)  # campionamento su uniforme
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3, cmap='viridis')  # alpha è l'opacità
plt.colorbar()
plt.show()
