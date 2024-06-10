import numpy as np
import matplotlib.pyplot as plt

# Definindo parâmetros do sinal
fs = 1000  # Frequência de amostragem (Hz)
T = 1  # Duração do sinal (s)
N = fs * T  # Número de amostras
t = np.linspace(0, T, N, endpoint=False)  # Vetor de tempo

# Criando um sinal com duas frequências
f1 = 50  # Frequência do primeiro seno (Hz)
f2 = 150  # Frequência do segundo seno (Hz)
x = 0.6 * np.sin(2 * np.pi * f1 * t) + 0.4 * np.sin(2 * np.pi * f2 * t)

# Computando a FFT
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(N, 1/fs)

# Calculando o espectro de magnitude
magnitude_spectrum = np.abs(X)

# Plotando o sinal original e seu espectro de magnitude
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Sinal Original')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(frequencies[:N // 2], magnitude_spectrum[:N // 2])
plt.title('Espectro de Magnitude')
plt.xlabel('Frequência [Hz]')
plt.ylabel('Magnitude')
plt.grid()

plt.tight_layout()
plt.show()
