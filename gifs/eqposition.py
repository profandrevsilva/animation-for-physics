import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Dados do problema
S0 = 4       # posição inicial (km)
v = 15       # velocidade (km/h)
t = np.linspace(0, 3, 100)  # tempo de 0 a 3 horas

# Equação horária da posição
S = S0 + v * t

# Criação da figura
fig, ax = plt.subplots()
ax.set_xlim(0, 3.2)
ax.set_ylim(0, 50)
ax.set_xlabel("Tempo (h)")
ax.set_ylabel("Posição (km)")
ax.set_title("Movimento Uniforme: Gráfico S x t")

# Linha da posição e ponto animado
(line,) = ax.plot([], [], 'b-', lw=2)
(point,) = ax.plot([], [], 'ro')

# Linha pontilhada fixa em S0 = 4 km
ax.axhline(y=S0, color='black', linestyle='--', linewidth=1)
ax.text(-0.3, S0 + 0.5, '4 km', color='black', fontsize=11)

# Linhas pontilhadas móveis (vertical e horizontal)
(vertical_line,) = ax.plot([], [], 'k--', lw=1)
(horizontal_line,) = ax.plot([], [], 'k--', lw=1)

# Texto da equação
text_eq = ax.text(0.1, 45, '', fontsize=12, color='black')

# Função de inicialização
def init():
    line.set_data([], [])
    point.set_data([], [])
    vertical_line.set_data([], [])
    horizontal_line.set_data([], [])
    text_eq.set_text('')
    return line, point, vertical_line, horizontal_line, text_eq

# Função de atualização
def update(frame):
    # Atualiza linha principal
    line.set_data(t[:frame], S[:frame])
    
    # Atualiza ponto
    x = t[frame-1]
    y = S[frame-1]
    point.set_data([x], [y])
    
    # Linhas pontilhadas móveis
    vertical_line.set_data([x, x], [0, y])
    horizontal_line.set_data([0, x], [y, y])
    
    # Atualiza texto da equação
    text_eq.set_text(f"S = {S0} + {v}·t = {y:.1f} km")
    
    return line, point, vertical_line, horizontal_line, text_eq

# Criando a animação
ani = FuncAnimation(fig, update, frames=len(t), init_func=init, interval=150, blit=True)

plt.show()
