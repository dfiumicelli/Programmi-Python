import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

A = np.array([[0., 1.],
              [1., 0.]])
B = np.array([[0.],
              [1.]])
C = np.array([1., 0.])
D = [0.]
sys = signal.StateSpace(A, B, C, D)
print("Formulazione State Space: ", sys)
print("Formulazione Funzione di Trasferimento: ", sys.to_tf())
print("Formulazione Zeri, Poli, Guadagno: ", sys.to_zpk())
t, y = signal.impulse(sys)
fig1, ax1 = plt.subplots(1)
ax1.plot(t, y)
ax1.set(title="Risposta all'impulso - Sistema Instabile",
        xlabel="Tempo (secondi)",
        ylabel="y(t)")
plt.show()


sys2 = signal.ZerosPolesGain([], [-1, -10], [1])
t, y = signal.impulse(sys2)
t_step, y_step = signal.step(sys2)
fig2, ax2 = plt.subplots(2)
ax2[0].plot(t, y)
ax2[0].set(title="Risposta all'impulso - Sistema Stabile",
        xlabel="Tempo (secondi)",
        ylabel="y(t)")
ax2[1].plot(t_step, y_step)
ax2[1].set(title="Risposta al gradino - Sistema Stabile",
        xlabel="Tempo (secondi)",
        ylabel="y(t)")
plt.show()
fig3, ax3 = plt.subplots(2)
w, mag, phase = signal.bode(sys2)
ax3[0].semilogx(w, mag)
ax3[0].grid(True, which='both')
ax3[0].set(title="Diagramma di Bode del Modulo",
          ylabel='dB')
ax3[1].semilogx(w, phase)
ax3[1].grid(True, which='both')
ax3[1].set(title="Diagramma di Bode della Fase",
          xlabel='rad/s',
          ylabel='gradi°')
plt.show()

fig4, ax4 = plt.subplots(2)
time_index = np.linspace(0, 3, 500, endpoint=False)
u = np.cos(2*np.pi*4*time_index)
tout, yout, xout = signal.lsim(sys2, u, time_index)
ax4[0].plot(time_index, u)
ax4[0].set(title="Segnale in ingresso",
        xlabel="Tempo (secondi)",
        ylabel="u(t)")
ax4[1].plot(time_index, yout)
ax4[1].set(title="Risposta alla sinusoide a 4 Hz",
        xlabel="Tempo (secondi)",
        ylabel="y(t)")
plt.show()

# Circuito RLC
A = np.array([[-1., -1., 0.],
              [1., -1., 1.],
              [0., 1., -1.]])
B = np.array([[1.],
              [0.],
              [0.]])
C = np.array([0., 1., -1.])
D = [0.]
sys3 = signal.StateSpace(A, B, C, D)
print(sys3.to_tf())
print(sys3.to_zpk())

fig5, ax5 = plt.subplots(2)
w, mag, phase = signal.bode(sys3)
ax5[0].semilogx(w, mag)
ax5[0].grid(True, which='both')
ax5[0].set(title="Diagramma di Bode del Modulo - Circuito RLC",
          ylabel='dB')
ax5[1].semilogx(w, phase)
ax5[1].grid(True, which='both')
ax5[1].set(title="Diagramma di Bode della Fase - Circuito RLC",
          xlabel='rad/s',
          ylabel='gradi°')
plt.show()

t, y = signal.impulse(sys3)
t_step, y_step = signal.step(sys3)
fig6, ax6 = plt.subplots(2)
ax6[0].plot(t, y)
ax6[0].set(title="Risposta all'impulso - Circuito RLC",
        xlabel="Tempo (secondi)",
        ylabel="y(t)")
ax6[1].plot(t_step, y_step)
ax6[1].set(title="Risposta al gradino - Circuito RLC",
        xlabel="Tempo (secondi)",
        ylabel="y(t)")
plt.show()

#
# t = np.linspace(0, 20, 2000)
# u = np.sin(100*t)
# tout, yout, xout = signal.lsim(sys, u, t)
# fig, ax = plt.subplots(1)
# ax.plot(tout, yout)
# ax.set(title="Risposta alla sinusoide",
#        xlabel="Secondi",
#        ylabel="y(t)")
# plt.show()
#
#
#
#
#
# tout, yout, xout = signal.lsim(sys, u, t)
# fig, ax = plt.subplots(1)
# ax.plot(t, yout)
# ax.set(title="Risposta all'ingresso sinusoidale",
#        xlabel="Secondi",
#        ylabel="y(t)")
#
# fig, ax = plt.subplots(2)
# w, mag, phase = signal.bode(sys)
# ax[0].semilogx(w, mag)
# ax[0].grid(True, which='both')
# ax[0].set(title="Diagramma di Bode del Modulo",
#           ylabel='dB')
# ax[1].semilogx(w, phase)
# ax[1].grid(True, which='both')
# ax[1].set(title="Diagramma di Bode della Fase",
#           xlabel='rad/s',
#           ylabel='gradi°')

# fig, ax = plt.subplots(2)
# w, mag, phase = signal.bode(sys)
# ax[0].semilogx(w, mag)
# ax[0].grid(True, which='both')
# ax[0].set(title="Diagramma di Bode del Modulo",
#           ylabel='dB')
# ax[1].semilogx(w, phase)
# ax[1].grid(True, which='both')
# ax[1].set(title="Diagramma di Bode della Fase",
#           xlabel='rad/s',
#           ylabel='gradi°')


# A = np.zeros(shape=(3, 3))
# A[0, 0] = -1.0
# A[2, 0] = -1.0
# A[1, 1] = -1.0
# A[1, 2] = 1.0
# A[2, 0] = 1.0
# A[2, 1] = -1.0
# B = np.zeros(shape=(3, 1))
# B[0, 0] = 1.0
# C = np.zeros(shape=(1, 3))
# C[0, 1] = 1.0
# system = signal.StateSpace(A, B, C, 0.0)
# print(system)
# fig0, ax0 = plt.subplots(2)
# t0 = np.linspace(0, 10, 100)
# ax0[0].plot(t0, np.cos(t0))
# ax0[1].plot(t0, np.sin(t0))
# cursor = mplcursors.cursor(ax0, hover=True)
# @cursor.connect("add")
# def on_add(sel):
#     x, y = sel.target
#     sel.annotation.set_text(f'f({x:.2f}) = {y:.2f}')
# w, mag, phase = signal.bode(system)
# fig, ax = plt.subplots(2)
# ax[0].semilogx(w, mag)    # Bode magnitude plot
# ax[0].grid(True, which='both')
# ax[1].semilogx(w, phase)  # Bode phase plot
# ax[1].grid(True, which='both')
# # Enable the cursor
# cursor = mplcursors.cursor(ax, hover=True)
# @cursor.connect("add")
# def on_add(sel):
#     x, y = sel.target
#     sel.annotation.set_text(f'f({x:.2f}) = {y:.2f}')
#
# t = np.linspace(0, 60, 10000, endpoint=False)
# u = np.cos(0.7*t)
# tout, yout, xout = signal.lsim(system, U=u, T=t)
# plt.figure()
# plt.plot(t, u, 'r', alpha=0.5, linewidth=1, label='input')
# plt.plot(tout, yout, 'k', linewidth=1.5, label='output')
# plt.legend(loc='best', shadow=True, framealpha=1)
# plt.grid(alpha=0.3)
# plt.xlabel('t')
# plt.show()
