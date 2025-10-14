import matplotlib
matplotlib.use("Agg")  # evita o erro _resize_id em backends interativos

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# === Dados do movimento uniforme ===
t = np.linspace(0, 10, 100)  # tempo (s)
v = 2                        # velocidade constante (m/s)
s0 = 1                       # posição inicial (m)
s = s0 + v * t               # posição ao longo do tempo

# === Criação da figura ===
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Gráfico posição x tempo ---
ax1.set_xlim(0, 10)
ax1.set_ylim(0, max(s) + 2)
ax1.set_title('Posição x Tempo (Movimento Uniforme)')
ax1.set_xlabel('Tempo (s)')
ax1.set_ylabel('Posição (m)')
ax1.grid(True)

# --- Gráfico velocidade x tempo ---
ax2.set_xlim(0, 10)
ax2.set_ylim(0, 3)
ax2.set_title('Velocidade x Tempo (Movimento Uniforme)')
ax2.set_xlabel('Tempo (s)')
ax2.set_ylabel('Velocidade (m/s)')
ax2.grid(True)

# --- Linhas pontilhadas e pontos móveis ---
linha_s, = ax1.plot(t, s, '--', color='blue', label=r'$s = s_0 + v t$')
ponto_s, = ax1.plot([], [], 'ro', markersize=8)

linha_v, = ax2.plot(t, [v]*len(t), '--', color='green', label='v = constante')
ponto_v, = ax2.plot([], [], 'ro', markersize=8)

# --- Texto dinâmico da equação ---
equacao_texto = ax1.text(
    0.2, 0.9,
    '',
    transform=ax1.transAxes,
    fontsize=12,
    bbox=dict(facecolor='white', alpha=0.7, edgecolor='gray')
)

ax1.legend()
ax2.legend()

# === Função de atualização ===
def update(frame):
    # valores atuais
    t_atual = t[frame]
    s_atual = s[frame]

    # atualizar posição dos pontos
    ponto_s.set_data([t_atual], [s_atual])
    ponto_v.set_data([t_atual], [v])

    # atualizar o texto da equação com valores numéricos
    equacao_texto.set_text(
        fr"$s = s_0 + v \cdot t = {s0:.1f} + {v:.1f} \cdot {t_atual:.1f} = {s_atual:.1f}\,\text{{ m}}$"
    )

    return ponto_s, ponto_v, equacao_texto

# === Criar animação ===
ani = animation.FuncAnimation(
    fig, update, frames=len(t), interval=80, blit=True
)

# === Salvar como GIF ===
ani.save("movimento_uniforme.gif", writer=animation.PillowWriter(fps=15))
plt.close(fig)

print("✅ GIF gerado com sucesso: movimento_uniforme.gif")
