import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import scipy.signal as sgn
class Sistema:
    def __init__(self, alpha):
        self.__alpha = alpha
        self.__A = np.array([[-8.,-alpha,-8.],[1., 0., 0.],[0., 1., 0.]])
        self.__B = np.array([[1.], [0.], [0.]])
        self.__C = np.array([0., 4., -3.])
        self.__D = 0.
        self.__sys = sgn.StateSpace(self.__A, self.__B, self.__C, self.__D)

    def descrivi(self):
        print("A: ", self.__A)
        print("B: ", self.__B)
        print("C: ", self.__C)
        print("D: ", self.__D)
        print("Funzione di trasferimento:\n ", self.__sys.to_tf())
        print("Poli:\n ", self.__sys.poles)

    def bode_diagram(self):
        w, mag, phase = sgn.bode(self.__sys)
        fig, ax = plt.subplots(2)
        ax[0].semilogx(w, mag)
        ax[0].set_title('Magnitude')
        ax[1].semilogx(w, phase)
        ax[1].set_title('Phase')
        ax[0].grid(True, which='both')
        ax[1].grid(True, which='both')
        plt.show()

    def step_response(self):
        t, y=sgn.step(self.__sys)
        fig, ax = plt.subplots()
        ax.plot(t, y)
        ax.set_title('Step Response')
        ax.grid(True, which='both')
        plt.show()

    def func(self):
        T = np.random.uniform(size=self.__B.shape, low=5.0, high=10.0)
        K = self.__B*T
        K[K>6.0]=-1
        print(K)
        print(np.sum(K))

    def is_stable(self):
        poles = self.__sys.poles
        is_stable = True
        for p in poles:
            if p >=0.:
                is_stable = False
                break

def alpha_instabili():
    alphas = np.linspace(-10,10)
    alpha_instab = []
    for alpha in alphas:
        sys=Sistema(alpha)
        if not sys.is_stable():
            alpha_instab.append(alpha)
            if len(alpha_instab) == 3:
                print("I 3 valori di alpha sono: ", alpha_instab)
                break

s = Sistema(13.)
s.descrivi()
s.bode_diagram()
s.step_response()
s.func()
alpha_instabili()