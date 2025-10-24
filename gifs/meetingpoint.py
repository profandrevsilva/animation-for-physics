import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# ======================================================
# DADOS DO PROBLEMA
# ======================================================
v_marta = 80 / 60   # km/min
v_pedro = 100 / 60  # km/min

tempo_marta_antes = (10 / 80) * 60  # 7,5 min
tempo_extra = 30  # minutos até o encontro após Pedro sair
tempo_total = tempo_marta_antes + tempo_extra  # 37,5 min

# Vetor de tempo
t = np.linspace(0, tempo_total, 300)

# ======================================================
# CÁLCULO DAS POSIÇÕES (vetorizado)
# ======================================================
S_marta = np.where(t <= tempo_marta_antes,
                   v_marta * t,
                   10 + v_marta * (t - tempo_marta_antes))

S_pedro = np.where(t <= tempo_marta_antes,
                   0,
                   v_pedro * (t - tempo_marta_antes))

# ======================================================
# CONFIGURAÇÃO DOS GRÁFICOS
# ======================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# -------- Gráfico 1: Estrada --------
ax1.set_xlim(0, 60)
ax1.set_ylim(-2, 2)
ax1.set_xlabel("Posição (km)")
ax1.set_yticks([])
ax1.set_title("Estrada – Encontro de Marta e Pedro")

marta_point, = ax1.plot([], [], 'ro', label="Marta (80 km/h)")
pedro_point, = ax1.plot([], [], 'bo', label="Pedro (100 km/h)")
linha_encontro = ax1.axvline(50, color='green', linestyle='--', label="Encontro (50 km)")
ax1.legend(loc="upper left")

# -------- Gráfico 2: Posição × Tempo --------
ax2.set_xlim(0, tempo_total)
ax2.set_ylim(0, 60)
ax2.set_xlabel("Tempo (min)")
ax2.set_ylabel("Posição (km)")
ax2.set_title("Gráfico S × t (MRU)")

linha_marta, = ax2.plot([], [], 'r-', label="Marta")
linha_pedro, = ax2.plot([], [], 'b-', label="Pedro")
ax2.legend(loc="upper left")

# ======================================================
# FUNÇÃO DE ATUALIZAÇÃO
# ======================================================
def update(frame):
    # Atualiza pontos na estrada (passando listas)
    marta_point.set_data([S_marta[frame]], [0.5])
    pedro_point.set_data([S_pedro[frame]], [-0.5])

    # Atualiza gráfico posição × tempo
    linha_marta.set_data(t[:frame], S_marta[:frame])
    linha_pedro.set_data(t[:frame], S_pedro[:frame])

    return marta_point, pedro_point, linha_marta, linha_pedro

# ======================================================
# CRIA E SALVA ANIMAÇÃO
# ======================================================
ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=False)

writer = PillowWriter(fps=20)
ani.save("encontro_marta_pedro_duplo.gif", writer=writer)

print("✅ Animação salva como 'encontro_marta_pedro_duplo.gif'")
