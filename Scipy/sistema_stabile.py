from matplotlib import pyplot as plt
from scipy import signal
import numpy as np

sys = signal.ZerosPolesGain([], [-1, -10], 1)
fig, ax = plt.subplots(4)
t, y = signal.impulse(sys)
t1, y1 = signal.step(sys)
w, mag, phase = signal.bode(sys)
ax[0].plot(t, y)
ax[0].set_title('Risposta Impulsiva')
ax[1].plot(t1, y1)
ax[1].set_title('Risposta al Gradino')
ax[2].semilogx(w, mag)
ax[3].semilogx(w, phase)

fig1, ax1 = plt.subplots(1)
time = np.linspace(0, 3, 500, endpoint=False)
u = np.cos(2*np.pi*time)
tout, yout, xout = signal.lsim(sys, u, time)
ax1.plot(time, yout)
ax1.set_title('Risposta Custom al coseno')
plt.show()