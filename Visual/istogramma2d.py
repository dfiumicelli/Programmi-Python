import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

mean = [0, 0]
cov = [[1, 1], [1, 2]]
x, y = np.random.multivariate_normal(mean, cov, 1000).T
fig, ax = plt.subplots()
hist2d, xedges, yedges, hist_image = ax.hist2d(x, y, cmap='Blues', alpha=1.0, bins=40, density=True)
fig.colorbar(hist_image, ax=ax)
plt.show()

