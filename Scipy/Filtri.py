import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
sig = np.repeat([0., 1., 0.], 100)
win = signal.windows.hann(50)
convolution = signal.convolve(sig, win, mode='same')/sum(win)
fig, ax = plt.subplots(3, 1, sharex=True)
ax[0].plot(sig)
ax[0].set_title('Original pulse')
ax[0].margins(0, 0.1)
ax[1].plot(win)
ax[1].set_title('Filter impulse response')
ax[1].margins(0, 0.1)
ax[2].plot(convolution)
ax[2].set_title('Filtered signal')
ax[2].margins(0, 0.1)
plt.show()
