import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 30)
ax = plt.axes()
ax.plot(x, np.sin(x), marker='o', linestyle='None')
plt.show()