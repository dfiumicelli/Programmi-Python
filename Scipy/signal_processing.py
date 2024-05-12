import numpy as np
import matplotlib
import scipy.signal

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

class SineWave:
    def __init__(self, amplitude, frequency, sampling_rate, duration, phase=0.0):
        self.amplitude = amplitude
        self.frequency = frequency
        self.sampling_rate = sampling_rate
        self.duration = duration
        self.phase = phase
        self.time_index = np.linspace(0, self.duration,
                                 int(self.sampling_rate*self.duration))
        print(int(self.sampling_rate*self.duration))

    def sine_wave(self):
        signal = self.amplitude*np.sin(2*np.pi*self.frequency*self.time_index + self.phase)
        return signal

    def cosine_wave(self):
        signal = self.amplitude*np.cos(2*np.pi*self.frequency*self.time_index + self.phase)
        return signal

    def get_time_index(self):
        return self.time_index

duration = 2.0
sampling_rate = 200
sine_wave = SineWave(amplitude=2.0, frequency=10,sampling_rate=sampling_rate,
                     duration=duration)
sine_signal = sine_wave.sine_wave()
cosine_signal = sine_wave.cosine_wave()
time_index = sine_wave.get_time_index()

fig, ax = plt.subplots(2)
ax[0].plot(time_index, sine_signal)
ax[0].set(title="Funzione Seno",
          ylabel="sin[n]",
          xlabel="Timestep n")
ax[1].plot(time_index, cosine_signal)
ax[1].set(title="Funzione Coseno",
          ylabel="sin[n]",
          xlabel="Timestep n")
plt.show()

# Plot tramite funzione stem()
fig2, ax2 = plt.subplots(2)
ax2[0].stem(time_index, sine_signal)
ax2[0].set(title="Funzione Seno",
          ylabel="sin[n]",
          xlabel="Timestep n")
ax2[1].stem(time_index, cosine_signal)
ax2[1].set(title="Funzione Coseno",
          ylabel="sin[n]",
          xlabel="Timestep n")
plt.show()

# Funzione Sinc
from scipy import special as sp
sampling_rate_sinc = 300
duration_sinc = 0.5
sinc_timesteps = np.linspace(-10, 10, int(sampling_rate_sinc*duration_sinc))
sinc = sp.sinc(sinc_timesteps)
fig3, ax3 = plt.subplots(1)
ax3.plot(sinc_timesteps, sinc)
ax3.set(title="Funzione Sinc",
          ylabel="sin[n]",
          xlabel="Timestep n")
plt.show()

# FFT e IFFT
from scipy.fft import fft, fftfreq, ifft
fft_sine = fft(sine_signal)
xf = fftfreq(int(duration*sampling_rate), 1.0/sampling_rate)
fig4, ax4 = plt.subplots(3)
ax4[0].plot(time_index, sine_signal)
ax4[0].set(title="Funzione Seno",
          ylabel="sin[n]",
          xlabel="Timestep n")
ax4[1].stem(xf, np.abs(fft_sine))
ax4[1].set(title="FFT di sin[n]",
          ylabel="abs(FFT)",
          xlabel="freq")
sin_reconstructed = ifft(fft_sine)
ax4[2].plot(time_index, sin_reconstructed)
ax4[2].set(title="Funzione Seno Ricostruita",
          ylabel="sin[n]",
          xlabel="Timestep n")
plt.show()

# Convoluzione
input_signal = np.repeat([0., 1., 0.], 100)
win = scipy.signal.windows.hann(50)
convolved_signal = scipy.signal.convolve(input_signal, win, mode="same") / sum(win)
fig5, ax5 = plt.subplots(3)
ax5[0].plot(input_signal)
ax5[0].set(title="Segnale originale",
          xlabel="Timestep n")
ax5[1].plot(win)
ax5[1].set(title="Filtro",
          xlabel="Timestep n")
ax5[2].plot(convolved_signal)
ax5[2].set(title="Segnale filtrato",
          xlabel="Timestep n")
plt.show()

# Filtro FIR
duration = 2.0
sampling_rate = 1000
sine_wave_10 = SineWave(amplitude=2.0, frequency=10,
                        sampling_rate=sampling_rate,
                      duration=duration)
sine_wave_100 = SineWave(amplitude=2.0, frequency=100,
                         sampling_rate=sampling_rate,
                      duration=duration)
signal1 = sine_wave_10.sine_wave() + sine_wave_100.sine_wave()
time_index = sine_wave_10.get_time_index()

# Filtro Passa Basso
fig6, ax6 = plt.subplots(3)
ax6[0].plot(time_index, signal1)
ax6[0].set(title="Segnale Originale",
          xlabel="Timestep n")
filter = scipy.signal.firwin(40, [40],
                             fs=sampling_rate)
w1, h1 = scipy.signal.freqz(filter)
ax6[1].plot(w1, 20*np.log10(np.abs(h1)))
ax6[1].set(title="Abs filtro (dB)",
          xlabel="Freq")
signal_filtered = scipy.signal.convolve(signal1, filter, mode="same")
ax6[2].plot(time_index, signal_filtered)
ax6[2].set(title="Segnale filtrato",
          xlabel="Timestep n")
plt.show()

# Filtro Passa Banda
fig7, ax7 = plt.subplots(3)
ax7[0].plot(time_index, signal1)
ax7[0].set(title="Segnale Originale",
          xlabel="Timestep n")
filter_band_pass = scipy.signal.firwin(41, [90., 110.],
                             pass_zero=False,
                             fs=sampling_rate)
w2, h2 = scipy.signal.freqz(filter_band_pass)
ax7[1].plot(w2, 20*np.log10(np.abs(h2)))
ax7[1].set(title="Abs filtro (dB)",
          xlabel="Freq")
signal_filtered_2 = scipy.signal.convolve(signal1, filter_band_pass, mode="same")
ax7[2].plot(time_index, signal_filtered_2)
ax7[2].set(title="Segnale filtrato",
          xlabel="Timestep n")
plt.show()



