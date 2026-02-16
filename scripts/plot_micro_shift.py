import matplotlib.pyplot as plt
import numpy as np
import os

# Paths updated for repository structure
std_f = 'output/tcwt_eternal_test_00_z1_pk.dat'
mic_f = 'output/micro_squeeze_00_pk.dat'

if not os.path.exists(std_f) or not os.path.exists(mic_f):
    print("Data missing. Run class with micro.ini first.")
    exit()

s_data, m_data = np.loadtxt(std_f), np.loadtxt(mic_f)
plt.figure(figsize=(12, 6))
plt.loglog(s_data[:, 0], s_data[:, 1]/s_data[0,1], 'r-', label='Standard (0.12)')
plt.loglog(m_data[:, 0], m_data[:, 1]/m_data[0,1], 'g--', label='Micro-Squeeze (0.135)')
plt.axvline(0.1, color='k', ls=':', label='Cluster Threshold')
plt.title('TCWT: Micro-Squeeze Resonance')
plt.legend()
plt.savefig('docs/plots/micro_shift_plot.png')
