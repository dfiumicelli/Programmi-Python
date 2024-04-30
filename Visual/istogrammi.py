import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

# definisco una variabile keyword argument
kwargs = dict(histtype='stepfilled', alpha=0.3, bins=40, normed=True)
fig, ax = plt.subplots()
ax.hist(x1, color="blue", histtype='stepfilled', alpha=0.3, bins=40, density=True)
ax.hist(x2, color="red", histtype='stepfilled', alpha=0.3, bins=40, density=True)
ax.hist(x3, color="green", histtype='stepfilled', alpha=0.3, bins=40, density=True)

plt.show()
