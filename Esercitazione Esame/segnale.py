import numpy as np
import scipy.signal as sgn
import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq


class CustomSignal:

    def __init__(self, num_waves, f0, amplitude, duration, sampling_rate, phase):
        self.num_waves = num_waves
        self.f0 = f0
        self.amplitude = amplitude
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.phase = phase
        self.time_index = np.linspace(0, self.duration, int(self.sampling_rate * self.duration))
        self.signal = None

    def generate_signal(self):
        signal = self.amplitude * np.sin(2 * np.pi * self.f0 * self.time_index + self.phase)
        multi = 10
        for i in range(1, self.num_waves):
            if i % 2 == 0:
                signal += np.cos(2 * np.pi * self.f0 * multi * self.time_index + self.phase)
            else:
                signal += np.sin(2 * np.pi * self.f0 * multi * self.time_index + self.phase)
            multi *= 10
        self.signal = signal

    def visualizza_segnale_e_fft(self):
        if self.signal is None:
            self.generate_signal()
        signal_fft = fft(self.signal)
        xf = fftfreq(int(self.sampling_rate * self.duration), 1.0 / self.sampling_rate)
        fig, ax = plt.subplots(2)
        ax[0].plot(self.time_index, self.signal)
        ax[0].set(title="signal", xlabel="timestep n", ylabel="s[n]")
        ax[1].stem(xf, np.abs(signal_fft))
        ax[1].set(title="FFT", xlabel="freq", ylabel="abs(FFT)")
        plt.show()

    def filtro(self, n, cut_freq):
        if self.signal is None:
            self.generate_signal()
        hf = sgn.firwin(n, cut_freq, fs=self.sampling_rate)
        sig_filtered = sgn.convolve(self.signal, hf, mode='same')
        fig, ax = plt.subplots(2)
        ax[0].plot(self.time_index, self.signal)
        ax[0].set(title="signal", xlabel="timestep n", ylabel="s[n]")
        ax[1].plot(self.time_index, sig_filtered)
        ax[1].set(title="signal", xlabel="timestep n", ylabel="s[n]")
        plt.show()

    def custom_func(self):
        if self.signal is None:
            self.generate_signal()
        custom_array = self.signal.reshape(200, 30)
        custom_array = custom_array[:14, :5]
        custom_array = custom_array[::3, :]
        a = np.random.normal(loc=3.0, scale=2.0, size=custom_array.shape)
        return custom_array @ a


sig = CustomSignal(num_waves=3, f0=5, amplitude=1.0, duration=3.0, sampling_rate=2000, phase=0.0)
sig.visualizza_segnale_e_fft()
sig.filtro(n=80, cut_freq=5)
print(sig.custom_func())
