import matplotlib

matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax = plt.axes(projection='3d')

zline = 2*np.linspace(0, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline,yline,zline,'gray')

# mostriamo anche uno scatter

zdata = 2*15*np.random.random(1000)
xdata = np.sin(zdata) + 0.1*np.random.randn(1000)
ydata = np.cos(zdata) + 0.1*np.random.randn(1000)
ax.scatter3D(xdata,ydata,zdata, c=zdata, cmap='Greens')
plt.show()