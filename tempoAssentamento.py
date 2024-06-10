import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import dlti, dstep

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

# Definindo a faixa de tolerância
valor_final = y[-1]
tolerancia = 0.02
faixa_superior = valor_final * (1 + tolerancia)
faixa_inferior = valor_final * (1 - tolerancia)

# Encontrando o tempo de assentamento
tempo_de_assentamento = np.where((y > faixa_inferior) & (y < faixa_superior))[0]
if len(tempo_de_assentamento) > 0:
    tempo_de_assentamento = tempo_de_assentamento[-1]
else:
    tempo_de_assentamento = None

# Plotando a resposta ao passo
plt.figure(figsize=(10, 6))
plt.stem(t, y, basefmt=" ")
plt.axhline(valor_final, color='green', linestyle='--', label='Valor Final')
plt.axhline(faixa_superior, color='red', linestyle='--', label='Faixa de Tolerância Superior')
plt.axhline(faixa_inferior, color='red', linestyle='--', label='Faixa de Tolerância Inferior')
if tempo_de_assentamento is not None:
    plt.axvline(tempo_de_assentamento, color='blue', linestyle='--', label='Tempo de Assentamento')
plt.title('Resposta ao Passo e Tempo de Assentamento de um Sistema Discreto')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

if tempo_de_assentamento is not None:
    print(f"Tempo de Assentamento: {tempo_de_assentamento} amostras")
else:
    print("O sistema não atinge a faixa de tolerância especificada.")
