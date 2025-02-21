import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


class Sistema:
    def __init__(self, a):
        self.a = a
        A = np.array([[-1., 0., -1.], [0., -a, 1.], [1., -1., 0.]])
        B = np.array([[1.], [0.], [0.]])
        C = np.array([0., 1., 0.])
        D = [0.]
        self.sys = signal.StateSpace(A, B, C, D)

    def step_response(self):
        t_step, y_step = signal.step(self.sys)
        plt.plot(t_step, y_step)
        plt.show()

    def bode_diagram(self):
        w, mag, phase = signal.bode(self.sys)
        fig, ax = plt.subplots()
        ax.semilogx(w, mag)
        ax.set(title='Bode Diagram', xlabel='w', ylabel='Magnitude')
        ax.grid(True, which='both')
        plt.show()

    def generic_response(self, u):
        t = np.linspace(0, 4, 2000)
        tout, yout, xout = signal.lsim(self.sys, u, t)
        plt.plot(t, yout)
        plt.grid(True)
        plt.show()

    def stamp(self):
        print(self.sys.A)
        print(self.sys.B)
        print(self.sys.C)

    def is_stable(self):
        poles = self.sys.poles
        stable = True
        for pole in poles:
            if pole >= 0.:
                stable = False
        print(stable)

    def get_A(self):
        return self.sys.A


a = 1.
sys = Sistema(a)
sys.stamp()
t = np.linspace(0, 4, 2000)
u = 2*np.cos(2 * np.pi * 4 * t)
sys.generic_response(u)
sys.bode_diagram()
sys.is_stable()


def custom_func(A, custom_array):
    if A.shape[1] != custom_array.shape[0]:
        return "Non è possibile fare il prodotto matriciale"
    custom_array[custom_array < 2.0] = 0.0
    C = A @ custom_array
    means = C.mean(axis=1)
    return means.sum()


custom_array = np.random.normal(size=(3, 4), loc=5.0, scale=2.0)
custom_array2 = np.random.normal(size=(2, 4), loc=5.0, scale=2.0)
print(custom_func(sys.get_A(), custom_array=custom_array))
print(custom_func(sys.get_A(), custom_array=custom_array2))
