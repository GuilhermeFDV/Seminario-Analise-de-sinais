import numpy as np
import matplotlib.pyplot as plt

# Definindo os sinais de entrada
x = np.array([1, 2, 3, 4, 5])
h = np.array([1, -1, 1])

# Calculando a convolução
y = np.convolve(x, h)

# Plotando os sinais
n_x = np.arange(0, len(x))
n_h = np.arange(0, len(h))
n_y = np.arange(0, len(y))

plt.figure(figsize=(12, 6))

plt.subplot(3, 1, 1)
plt.stem(n_x, x)
plt.title('Sinal de Entrada x[n]')
plt.grid()

plt.subplot(3, 1, 2)
plt.stem(n_h, h)
plt.title('Resposta ao Impulso h[n]')
plt.grid()

plt.subplot(3, 1, 3)
plt.stem(n_y, y)
plt.title('Sinal de Saída y[n] = x[n] * h[n]')
plt.grid()

plt.tight_layout()
plt.show()
