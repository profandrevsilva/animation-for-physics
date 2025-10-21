import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ======================
# Dados do problema
# ======================
t = np.linspace(0, 5, 100)
sA = 15 + 75 * t
sB = 495 - 75 * t

t_encontro = 3.2
s_encontro = 15 + 75 * t_encontro

# ======================
# Configuração do gráfico
# ======================
fig, ax = plt.subplots(figsize=(8, 6))
lineA, = ax.plot([], [], 'b-', label='Veículo A', linewidth=0.5)
lineB, = ax.plot([], [], 'g-', label='Veículo B', linewidth=0.5)
pointA, = ax.plot([], [], 'bo', markersize=8)
pointB, = ax.plot([], [], 'go', markersize=8)
meeting_point, = ax.plot([], [], 'ro', label='Ponto de encontro', markersize=8)
annotation = ax.text(0, 0, '', fontsize=10, color='red')  # anotação para o ponto de encontro

ax.set_xlim(0, 5)
ax.set_ylim(0, 500)
ax.set_xlabel('Tempo (h)')
ax.set_ylabel('Posição (km)')
ax.set_title('Movimento dos Veículos A e B em Sentidos Opostos', fontsize=14)
ax.legend()
ax.grid(True)

# ======================
# Função de animação
# ======================
def animate(i):
    # Atualiza trajetórias
    lineA.set_data(t[:i+1], sA[:i+1])
    lineB.set_data(t[:i+1], sB[:i+1])
    # Atualiza posição atual dos veículos
    pointA.set_data([t[i]], [sA[i]])
    pointB.set_data([t[i]], [sB[i]])
    
    # Exibe o ponto de encontro e a anotação somente depois do encontro
    if t[i] >= t_encontro:
        meeting_point.set_data([t_encontro], [s_encontro])
        ax.axvline(t_encontro, color='red', linestyle='--', linewidth=0.5)
        ax.axhline(s_encontro, color='red', linestyle='--', linewidth=0.5)
        annotation.set_text(f'Encontro: ({t_encontro:.1f} h, {s_encontro:.0f} km)')
        annotation.set_position((t_encontro-2, s_encontro-20))
    else:
        meeting_point.set_data([], [])
        annotation.set_text('')
    
    return lineA, lineB, pointA, pointB, meeting_point, annotation

# ======================
# Criar animação e salvar como GIF
# ======================
anim = FuncAnimation(fig, animate, frames=len(t), interval=100, blit=True)
anim.save('animacao_veiculos.gif', writer=PillowWriter(fps=8))

print("GIF salvo como 'animacao_veiculos.gif'")
