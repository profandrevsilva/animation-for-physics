import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

v = 5
t_final = 10
frames = 100  # normal frames
pause_duration = 20  # number of extra frames to pause

fig, ax = plt.subplots(figsize=(8,5))
ax.set_xlim(0, t_final)
ax.set_ylim(0, v + 2)
ax.set_xlabel("Tempo (s)")
ax.set_ylabel("Velocidade (m/s)")
ax.set_title("Área sob v x t = deslocamento")

linha_v, = ax.plot([0, t_final], [v, v], color='green', lw=2)
texto = ax.text(0.7*t_final, v+0.5, "", fontsize=12, color='blue')

# -----------------------------
# Create frames list with pause
# -----------------------------
frame_list = list(range(frames // 2)) + [frames // 2] * pause_duration + list(range(frames // 2, frames))

def animate(i):
    t_atual = t_final * i / frames

    # Remove previous PolyCollections
    for coll in ax.collections[:]:
        coll.remove()
    
    # Draw area
    ax.fill_between([0, t_atual], 0, v, color='orange', alpha=0.5)
    
    # Update text
    delta_s = v * t_atual
    texto.set_text(f"ΔS = {delta_s:.1f} m")
    
    return ax.collections + [texto]

ani = FuncAnimation(fig, animate, frames=frame_list, interval=100, blit=False)
writer = PillowWriter(fps=5)
ani.save("area_velocidade_mru_pause.gif", writer=writer)
plt.show()
