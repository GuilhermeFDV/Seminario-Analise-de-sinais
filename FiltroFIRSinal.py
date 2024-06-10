import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, firwin

# Definindo os parâmetros do filtro FIR
numtaps = 51  # Número de coeficientes do filtro (ordem + 1)
cutoff = 0.3  # Frequência de corte normalizada (0.3 corresponde a 0.3*Nyquist)

# Gerando os coeficientes do filtro usando uma janela Hamming
b = firwin(numtaps, cutoff)

# Gerando um sinal de entrada (sinal com ruído)
n = np.arange(0, 100)
x = np.sin(0.2 * np.pi * n) + 0.5 * np.random.randn(len(n))

# Aplicando o filtro ao sinal de entrada
y = lfilter(b, 1, x)

# Plotando o sinal de entrada e o sinal filtrado
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(n, x, label='Sinal de Entrada')
plt.title('Sinal de Entrada com Ruído')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(n, y, label='Sinal Filtrado', color='red')
plt.title('Sinal Filtrado')
plt.grid()
plt.tight_layout()
plt.show()