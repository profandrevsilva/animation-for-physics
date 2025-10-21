import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =====================
# Dados
# =====================
x = np.array([0, 2, 4, 6, 10, 12])
y = np.array([3, 7, 9.5, 10.5, 15, 16])

# Ajuste linear
coef = np.polyfit(x, y, 1)
slope, intercept = coef
print(f"Equação da reta: y = {slope:.2f}x + {intercept:.2f}")

# =====================
# Configuração da figura
# =====================
fig, ax = plt.subplots()
ax.set_xlim(0, 16)
ax.set_ylim(0, 22)
ax.set_xlabel('tempo (s)')
ax.set_ylabel('deslocamento (m)')
ax.set_title('Animação do ajuste linear com triângulo para estimar a velocidade')
ax.grid(True)

# Objetos da animação
point, = ax.plot([], [], 'o', color='orange', markersize=8, label='Pontos')
line, = ax.plot([], [], 'b--', label='Linha Ajustada')
triangle, = ax.plot([], [], 'r-', lw=2, label='Δy / Δx (velocidade)')
delta_x_text = ax.text(0, 0, '', color='red', fontsize=12)
delta_y_text = ax.text(0, 0, '', color='red', fontsize=12)
v_text = ax.text(0, 0, '', color='green', fontsize=12, fontweight='bold')

# Linha completa do ajuste
x_line = np.linspace(0, 12, 100)
y_line = slope * x_line + intercept

# =====================
# Funções de animação
# =====================
def init():
    point.set_data([], [])
    line.set_data([], [])
    triangle.set_data([], [])
    delta_x_text.set_text('')
    delta_y_text.set_text('')
    v_text.set_text('')
    return point, line, triangle, delta_x_text, delta_y_text, v_text

def update(frame):
    # Animação dos pontos
    if frame < len(x):
        point.set_data(x[:frame+1], y[:frame+1])
        line.set_data([], [])
        triangle.set_data([], [])
        delta_x_text.set_text('')
        delta_y_text.set_text('')
        v_text.set_text('')
    else:
        point.set_data(x, y)
        
        # Desenho progressivo da linha ajustada
        t = frame - len(x)
        n_line = int((t / (total_frames - len(x))) * len(x_line))
        line.set_data(x_line[:n_line], y_line[:n_line])
        
        # Triângulo para estimar a velocidade, só depois que a linha estiver completa
        if n_line == len(x_line):
            # Intervalo do triângulo
            x0, x1 = 2, 6
            y0 = slope * x0 + intercept
            y1 = slope * x1 + intercept
            
            # Linhas do triângulo
            tri_x = [x0, x1, x1]
            tri_y = [y0, y0, y1]
            triangle.set_data(tri_x, tri_y)
            
            # Catetos Δx e Δy
            delta_x = x1 - x0
            delta_y = y1 - y0
            delta_x_text.set_position(((x0+x1)/2, y0-1))
            delta_x_text.set_text(f'Δx = {delta_x:.1f}')
            delta_y_text.set_position((x1+0.2, (y0+y1)/2))
            delta_y_text.set_text(f'Δy = {delta_y:.1f}')
            
            # Velocidade média v = Δy/Δx
            v = delta_y / delta_x
            v_text.set_position((x0+1, y1+1))
            v_text.set_text(f'v ≈ {v:.2f} m/s')
            
    return point, line, triangle, delta_x_text, delta_y_text, v_text

# =====================
# Configuração dos frames
# =====================
total_frames = len(x) + 40
ani = FuncAnimation(fig, update, frames=total_frames, init_func=init, blit=True, interval=300, repeat=True)

plt.legend()
plt.show()
