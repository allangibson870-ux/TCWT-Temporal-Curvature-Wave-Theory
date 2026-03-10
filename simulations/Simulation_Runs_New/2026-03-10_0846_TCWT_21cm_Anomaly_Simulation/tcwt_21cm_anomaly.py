import numpy as np
import matplotlib.pyplot as plt

# TCWT internal parameters
kappa = 1.455
Omega_max = 16.91
N_knot = 6.17e35
reion_lock_z = 6.1
sigma = 6.58e-36  # m/rad
L_coh = 6.0e-35   # m
f_Hum = 5.0e42    # Hz
P_leak = 5.6847e-24  # Pa ≈ J/m³

# Redshift range (high to low z)
z = np.linspace(25, 0, 1000)

# Inductive scaling exponent α(z): sigmoid transition 0.5 → 0.4
delta_alpha = 0.1
alpha = 0.5 - delta_alpha / (1 + np.exp((z - reion_lock_z) / 2.0))
alpha = np.clip(alpha, 0.4, 0.5)

# Phase-viscosity heating rate proxy: |dα/dz| * scale factors
dalpha_dz = np.gradient(alpha, z)
viscosity_heating = np.abs(dalpha_dz) * kappa * f_Hum  # illustrative scaling

# IGM temperature components
T_CMB = 2.725 * (1 + z)                    # CMB temperature
T_ad = T_CMB / (1 + z)                     # Adiabatic approximation proxy (simplified)
cum_heat = np.cumsum(viscosity_heating[::-1])[::-1] * (z[1] - z[0])  # rough cumulative
T_heat = 2.0 * cum_heat / (1 + z)          # damped by expansion, normalized ~few K
T_IGM = T_ad + T_heat                      # TCWT IGM with decoherence heat

# 21 cm absorption depth proxy (deeper trough = more negative)
delta_T_21 = - (T_CMB - T_IGM) * 0.1       # rough scaling to match EDGES depth ~0.5 K

# Plot setup
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
fig.patch.set_facecolor('#0a0a0a')

ax1.plot(z, alpha, color='#00CCFF', lw=3, label='Inductive Exponent α(z)')
ax1.axvline(reion_lock_z, color='red', ls='--', lw=2, label=f'Reionization Lock (z={reion_lock_z})')
ax1.set_ylabel('α(z)', color='#00CCFF', fontsize=13)
ax1.tick_params(axis='y', labelcolor='#00CCFF')
ax1.set_title('TCWT 21 cm Anomaly: Phase-Viscosity & IGM Heating', color='white', fontsize=15)
ax1.grid(alpha=0.2)
ax1.legend(facecolor='#111111', labelcolor='white')

ax2.plot(z, T_ad, color='white', lw=2, ls='--', label='Adiabatic T_IGM')
ax2.plot(z, T_IGM, color='#FF8800', lw=3, label='TCWT T_IGM (with decoherence heat)')
ax2.set_ylabel('IGM Temperature (K)', color='white', fontsize=13)
ax2.tick_params(axis='y', labelcolor='white')
ax2.set_yscale('log')
ax2.grid(alpha=0.2)
ax2.legend(facecolor='#111111', labelcolor='white')

ax3.plot(z, delta_T_21, color='#00FF88', lw=3, label='21 cm Absorption Depth Proxy')
ax3.axvspan(17, 20, color='gray', alpha=0.15, label='EDGES anomaly window')
ax3.set_xlabel('Redshift z', color='white', fontsize=13)
ax3.set_ylabel('ΔT_21 Proxy (arb. units)', color='#00FF88', fontsize=13)
ax3.tick_params(axis='y', labelcolor='#00FF88')
ax3.grid(alpha=0.2)
ax3.legend(facecolor='#111111', labelcolor='white')

for ax in [ax1, ax2, ax3]:
    ax.set_facecolor('#0a0a0a')
    ax.tick_params(colors='white')
    for spine in ax.spines.values():
        spine.set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')

plt.xlim(25, 0)
plt.tight_layout()
plt.savefig("$PNG_NAME", dpi=200, facecolor=fig.get_facecolor())
plt.close()
print("Plot saved as $PNG_NAME")
