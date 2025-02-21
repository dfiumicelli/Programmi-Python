import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np


class Sistema2:
    def __init__(self, a):
        self.a = a
        A = np.array([[-1., 0., -1.], [0., -a, 1.], [1., -1., 0.]])
        B = np.array([[1.], [0.], [0.]])
        C = np.array([0., 1., 0.])
        D = [0.]
        self.__sys = signal.StateSpace(A, B, C, D)

    def step_response(self):
        t_step, y_step = signal.step(self.__sys)
        fig, ax = plt.subplots()
        ax.plot(t_step, y_step)
        ax.set(xlabel='Time', ylabel='y', title='Step Response')
        ax.grid(True, which='both')
        plt.show()

    def bode_diagram(self):
        w, mag, phase = signal.bode(self.__sys)
        fig, ax = plt.subplots(2)
        ax[0].semilogx(w, mag)
        ax[1].semilogx(w, phase)
        ax[0].grid(True, which='both')
        ax[1].grid(True, which='both')
        plt.show()

    def generic_response(self, u, t):
        tout, yout, xout = signal.lsim(self.__sys, u, t)
        # yout = signal.lsim(self.__sys, u, t)[1]
        fig, ax = plt.subplots()
        ax.plot(t, yout)
        ax.set(title="Generic Response", xlabel="Time", ylabel="Response")
        ax.grid(True, which='both')
        plt.show()

    def stamp(self):
        print(self.__sys.A)
        print(self.__sys.B)
        print(self.__sys.C)
        print(self.__sys.D)

    def is_stable(self):
        poles = self.__sys.poles
        stable = True
        for pole in poles:
            if pole >= 0.:
                stable = False
        print(stable)

    def get_A(self):
        return self.__sys.A


sys = Sistema2(a=1.0)
sys.step_response()
sys.bode_diagram()
t = np.linspace(0, 4, 2000)
u = 2 * np.cos(2 * np.pi * 4 * t)
sys.generic_response(u, t)
A = sys.get_A()



def custom_func(A, custom_array):
    if A.shape[1] != custom_array.shape[0]:
        return "Non è possibile fare il prodotto matriciale"
    custom_array[custom_array < 2.0] = 0.0
    B = A @ custom_array
    means = B.mean(axis=1)
    return means.sum()


custom_array = np.random.normal(size=(3, 4), scale=2.0, loc=5.0)
print(custom_func(A, custom_array))