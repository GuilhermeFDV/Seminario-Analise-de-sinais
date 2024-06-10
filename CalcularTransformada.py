import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz

# Definindo a sequência discreta x[n]
a = 0.5
n = np.arange(0,10)
x = a**n

# Calculando a Transformada Z usando a função freqz
b = [1]  # Numerador do sistema
a = [1, -0.5]  # Denominador do sistema
w, h = freqz(b, a)

# Plotando a magnitude e fase da resposta em frequência
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

ax1.plot(w, 20 * np.log10(abs(h)))
ax1.set_title('Resposta em Frequência')
ax1.set_ylabel('Magnitude [dB]')
ax1.set_xlabel('Frequência [rad/sample]')
ax1.grid()

ax2.plot(w, np.angle(h))
ax2.set_ylabel('Fase [radianos]')
ax2.set_xlabel('Frequência [rad/sample]')
ax2.grid()

plt.tight_layout()
plt.show()