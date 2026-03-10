import numpy as np
import matplotlib.pyplot as plt

# TCWT parameters (internal)
kappa = 1.455
Omega_max = 16.91
N_knot = 6.17e35
reion_lock_z = 6.1

# Redshift range
z = np.linspace(0, 25, 1000)

# Inductive scaling exponent α(z) - sigmoid-like transition
alpha = 0.5 - 0.1 / (1 + np.exp((z - reion_lock_z) / 1.0))
alpha = np.clip(alpha, 0.4, 0.5)

# Qualitative ρ_DE scaling (increases as α decreases, illustrative)
rho_DE = 1e-26 * (0.5 / alpha)**3   # arbitrary normalization to ~observed scale

fig, ax1 = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#0a0a0a')
ax1.set_facecolor('#0a0a0a')

ax1.plot(z, alpha, color='#00CCFF', lw=3, label='Inductive Exponent α(z)')
ax1.axvline(reion_lock_z, color='red', linestyle='--', lw=2, label=f'Reionization Lock (z ≈ {reion_lock_z})')

ax1.set_xlabel('Redshift z', color='white', fontsize=14)
ax1.set_ylabel('α(z)', color='#00CCFF', fontsize=14)
ax1.tick_params(axis='y', labelcolor='#00CCFF')
ax1.set_xlim(25, 0)
ax1.grid(alpha=0.2)
ax1.legend(loc='upper left', facecolor='#111111', edgecolor='#444444', labelcolor='white')

ax2 = ax1.twinx()
ax2.plot(z, rho_DE, color='#FF8800', lw=2.5, linestyle='-', label='ρ_DE (qualitative scaling)')
ax2.set_ylabel('Dark Energy Density (arb. units)', color='#FF8800', fontsize=14)
ax2.tick_params(axis='y', labelcolor='#FF8800')
ax2.set_yscale('log')
ax2.legend(loc='upper right', facecolor='#111111', edgecolor='#444444', labelcolor='white')

plt.title('TCWT: Inductive Scaling α(z) & Dark Energy Density Evolution', color='white', fontsize=16)
fig.tight_layout()
plt.savefig("$PNG_NAME", dpi=200, bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
