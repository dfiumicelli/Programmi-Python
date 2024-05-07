from matplotlib import pyplot as plt
from scipy import signal
import numpy as np


class SineWave:
    def __init__(self, frequency, amplitude, duration, sampling_rate, phase=0.0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.time_index = np.linspace(0, self.duration, int(self.sampling_rate * self.duration))
        print(int(self.sampling_rate * self.duration))

    def sine_wave(self):
        signal = self.amplitude * np.sin(2 * np.pi * self.frequency * self.time_index + self.phase)
        return signal

    def cosine_wave(self):
        signal = self.amplitude * np.cos(2 * np.pi * self.frequency * self.time_index + self.phase)
        return signal

    def get_time_index(self):
        return self.time_index


sampling_rate = 1000
sine_wave_10 = SineWave(amplitude=2.0, frequency=10.0, sampling_rate=sampling_rate, duration=1)
sine_wave_100 = SineWave(amplitude=2.0, frequency=100.0, sampling_rate=sampling_rate, duration=1)
signal1 = sine_wave_10.sine_wave() + sine_wave_100.sine_wave()
b1 = signal.firwin(40, 20, fs=sampling_rate)
filtered = signal.convolve(signal1, b1, mode='same')
fig, ax = plt.subplots(3)
ax[0].plot(sine_wave_10.get_time_index(), signal1)
ax[1].plot(sine_wave_10.get_time_index(), filtered)
w1, h1 = signal.freqz(b1)
ax[2].plot(w1, 20*np.log10(abs(h1)), 'b')
plt.grid()
plt.show()