import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter, dlti, dstep

# Coeficientes do sistema
b = [0.1, 0.2, 0.1]  # Numerador (coeficientes do filtro)
a = [1.0, -0.7, 0.2]  # Denominador (coeficientes do filtro)

# Criando o sistema discreto
system = dlti(b, a)

# Calculando a resposta ao passo
t, y = dstep(system)

# Convertendo a lista para um array e ajustando o vetor de tempo
y = np.squeeze(y)
t = np.arange(len(y))

# Plotando a resposta ao passo
plt.figure(figsize=(10, 6))
plt.stem(t, y, basefmt=" ")
plt.title('Resposta ao Passo de um Sistema Discreto')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
