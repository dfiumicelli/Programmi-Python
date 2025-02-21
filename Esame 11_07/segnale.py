import numpy as np
import scipy.signal as sgn
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

class Segnale:
    def __init__(self, A, f, L, duration, sampling_rate):
        self.__A = A
        self.__f = f
        self.__L = L
        self.__duration = duration
        self.__sampling_rate = sampling_rate
        self.__time_index = np.linspace(0, self.__duration, int(self.__sampling_rate*self.__duration))
        self.signal = self.__A*np.sin(2*np.pi*self.__f*self.__time_index)
        for l in range(2, self.__L+1):
                self.signal += (l % 2)*self.__A*np.sin(2*np.pi*(l**3)*self.__f*self.__time_index)
                self.signal += ((l+1) % 2)*self.__A*np.cos(2*np.pi*(l**3)*self.__f*self.__time_index)

    def signal_and_fft(self):
        signal__fft = fft(self.signal)
        xf = fftfreq(int(self.__duration*self.__sampling_rate), 1.0/self.__sampling_rate)
        fig, ax = plt.subplots(2)
        ax[0].plot(self.__time_index, self.signal)
        ax[0].set_title('Signal')
        ax[1].stem(xf, abs(signal__fft))
        ax[1].set_title('FFT')
        ax[0].grid()
        ax[1].grid()
        plt.show()

    def filt(self, M, fcut):
        filter = sgn.firwin(M, fcut, fs=self.__sampling_rate)
        signal_filtered = sgn.convolve(self.signal, filter, mode="same")
        fig, ax = plt.subplots(2)
        ax[0].plot(self.__time_index, self.signal)
        ax[0].set_title('Signal')
        ax[1].plot(self.__time_index, signal_filtered)
        ax[1].set_title('Filtered')
        plt.show()
        return signal_filtered

    def somma_gradino(self, s):
        step_signal = np.zeros(len(self.__time_index))
        step_signal[int((self.__duration*self.__sampling_rate)//2):] = 10.0
        s += step_signal
        fig, ax = plt.subplots(2)
        ax[0].plot(self.__time_index, step_signal)
        ax[0].set_title('Gradino')
        ax[1].plot(self.__time_index, s)
        ax[1].set_title('Somma')
        plt.show()

    def bonus(self):
        a = np.random.normal(size=len(self.__time_index), loc=1.0, scale=3.0)
        b = self.signal*a
        print(b<2.0)

        c = b<2.0
        print(np.mean(c))

s = Segnale(2.0,6.0,4,3.0,2000)
s.signal_and_fft()
signal_filtered = s.filt(80,8)
s.somma_gradino(signal_filtered)
s.bonus()
