import numpy as np


class SineWave:
    def __init__(self, frequency, amplitude, duration, sampling_rate, phase=0.0):
        self.frequency = frequency
        self.amplitude = amplitude
        self.phase = phase
        self.duration = duration
        self.sampling_rate = sampling_rate
        self.time_index = np.linspace(0, self.duration, int(self.sampling_rate*self.duration))
        print(int(self.sampling_rate*self.duration))

    def sine_wave(self):
        signal = self.amplitude*np.sin(2*np.pi*self.frequency*self.time_index + self.phase)
        return signal

    def cosine_wave(self):
        signal = self.amplitude*np.cos(2*np.pi*self.frequency*self.time_index + self.phase)
        return signal
    def get_time_index(self):
        return self.time_index

from scipy import signal
import matplotlib.pyplot as plt

sine_wave_generator = SineWave(amplitude=2.0, frequency=10.0, sampling_rate=200.0, duration=1)
sin_wave = sine_wave_generator.sine_wave()
cos_wave = sine_wave_generator.cosine_wave()
fig, ax = plt.subplots(2)
ax[0].plot(sine_wave_generator.get_time_index(), sin_wave)
ax[0].set(title="Funzione Seno", ylabel="Sin[n]")
ax[1].plot(sine_wave_generator.get_time_index(), cos_wave)
ax[1].set(title="Funzione Coseno", ylabel="Cos[n]")
plt.show()