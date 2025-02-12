import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
m1, m2, m3 = 1.0, 1.0, 1.0  # Massas
k1, k2 = 10.0, 10.0  # Constantes das molas
x1, x2, x3 = -1.0, 0.0, 1.0  # Posições iniciais
v1, v2, v3 = 0.0, 0.0, 0.0  # Velocidades iniciais

dt = 0.01  # Passo de tempo
t_max = 10  # Tempo total da simulação
steps = int(t_max / dt)

# Listas para armazenar resultados
x1_list, x2_list, x3_list, cm_list, t_list = [], [], [], [], []

for t in np.arange(0, t_max, dt):
    # Forças das molas pela Lei de Hooke
    F1 = -k1 * (x1 - x2)
    F2 = k1 * (x1 - x2) - k2 * (x2 - x3)
    F3 = k2 * (x2 - x3)

    # Acelerações pela Segunda Lei de Newton
    a1 = F1 / m1
    a2 = F2 / m2
    a3 = F3 / m3

    # Atualização das velocidades (método de Euler)
    v1 += a1 * dt
    v2 += a2 * dt
    v3 += a3 * dt

    # Atualização das posições (método de Euler)
    x1 += v1 * dt
    x2 += v2 * dt
    x3 += v3 * dt

    # Cálculo do Centro de Massa
    cm = (m1 * x1 + m2 * x2 + m3 * x3) / (m1 + m2 + m3)

    # Armazenar valores para o gráfico
    x1_list.append(x1)
    x2_list.append(x2)
    x3_list.append(x3)
    cm_list.append(cm)
    t_list.append(t)

# Plotando os resultados
plt.plot(t_list, cm_list, label="Centro de Massa")
plt.xlabel("Tempo")
plt.ylabel("Posição do CM")
plt.legend()
plt.grid()
plt.show()
