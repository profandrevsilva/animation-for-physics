import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =====================
# Dados do problema
# =====================
vA = 3.0      # m/s (corredor A)
vB = 3.5      # m/s (corredor B)
SA0 = -900    # posição inicial de A
SB0 = -1200   # posição inicial de B

# Tempo total da animação (um pouco depois da chegada de B)
t_total = 650  # segundos
dt = 1         # passo de tempo
t = np.arange(0, t_total+dt, dt)

# Posições
SA = SA0 + vA * t
SB = SB0 + vB * t

# =====================
# Configuração do gráfico
# =====================
fig, ax = plt.subplots(figsize=(8,4))
ax.set_xlim(0, t_total)
ax.set_ylim(min(SB0, SA0)-100, max(SA[-1], SB[-1])+400)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Posição (m)")
ax.set_title("Corrida: Corredor A vs Corredor B")

# Linha de chegada
ax.axhline(0, color='black', linestyle='--', label='Chegada (S=0)')

# Pontos dos corredores
pointA, = ax.plot([], [], 'bo', label='Corredor A')
pointB, = ax.plot([], [], 'go', label='Corredor B')

# Trajetória (opcional)
lineA, = ax.plot([], [], 'b--', alpha=0.9)
lineB, = ax.plot([], [], 'g--', alpha=0.9)

# Ponto de Chegada
plt.axvline(x=300, color='red', linestyle='--', linewidth=1, label='Chegada')

# Ponto de Encontro
plt.axvline(x=600, color='red', linestyle='--', linewidth=1, label='Encontro')

plt.axhline(y=-150, color='blue', linestyle='--', linewidth=1, label=f'y = {-150}')


ax.legend()

# =====================
# Função de animação
# =====================
def animate(i):
    # Garantir que i seja válido
    i = min(i, len(t)-1)
    
    # Atualiza os pontos
    pointA.set_data([t[i]], [SA[i]])
    pointB.set_data([t[i]], [SB[i]])
    
    # Atualiza as linhas
    lineA.set_data(t[:i+1], SA[:i+1])
    lineB.set_data(t[:i+1], SB[:i+1])
    
    return pointA, pointB, lineA, lineB

# Cria animação
ani = FuncAnimation(fig, animate, frames=len(t), interval=50)

plt.show()
