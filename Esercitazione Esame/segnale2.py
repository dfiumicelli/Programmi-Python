import numpy as np
import scipy.signal as sgn
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


class segnale2:
    def __init__(self, num_waves, frequency, amplitude, duration, sampling_rate, phase):
        self.num_waves = num_waves
        self.frequency = frequency
        self.amplitude = amplitude
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.phase = phase
        self.time_index = np.linspace(0, self.duration, int(self.duration * self.sampling_rate))
        self.signal = None

    def generate_signal(self):
        signal = self.amplitude * np.sin(2 * np.pi * self.frequency * self.time_index + self.phase)
        multi = 10
        for i in range(1, self.num_waves):
            if i % 2 == 0:
                signal += self.amplitude * np.cos(2 * np.pi * self.frequency * multi * self.time_index + self.phase)
            else:
                signal += self.amplitude * np.sin(2 * np.pi * self.frequency * multi * self.time_index + self.phase)
            multi *= 10
        self.signal = signal

    def show_signal(self):
        if self.signal is None:
            self.generate_signal()
        signal_fft = fft(self.signal)
        xf = fftfreq(int(self.duration * self.sampling_rate), 1.0 / self.sampling_rate)
        fig, ax = plt.subplots(2)
        ax[0].plot(self.time_index, self.signal)
        ax[0].set(title='Signal')
        ax[0].grid(True, which='both')
        ax[1].plot(xf, np.abs(signal_fft))
        ax[1].set(title='Signal FFT')
        ax[1].grid(True, which='both')
        plt.show()

    def filtered_signal(self, num, cut_off):
        if self.signal is None:
            self.generate_signal()
        h = sgn.firwin(numtaps=num, cutoff=cut_off, fs=self.sampling_rate)
        signal_filtered = sgn.convolve(self.signal, h, mode='same')
        w, hf = sgn.freqz(h)
        fig, ax = plt.subplots(2)
        ax[0].plot(w, 20 * np.log10(abs(hf)))
        ax[0].set(title='Risposta in frequenza Filtro')
        ax[0].grid(True, which='both')
        ax[1].plot(self.time_index, signal_filtered)
        ax[1].set(title='Signale filtrato')
        ax[1].grid(True, which='both')
        plt.show()

    def custom_func(self):
        if self.signal is None:
            self.generate_signal()
        custom_array = self.signal.reshape(200, 30)
        a = custom_array[:14, :5]
        b = a[::3, :]
        c = np.random.normal(size=b.shape, scale=2.0, loc=3.0)
        return b @ c


sig = segnale2(3, 5, 1.0, 3.0, 2000, 0.0)
sig.filtered_signal(num=80, cut_off=5)
print(sig.custom_func())
