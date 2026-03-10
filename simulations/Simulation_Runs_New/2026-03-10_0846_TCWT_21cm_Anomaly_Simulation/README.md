# TCWT 21 cm Anomaly Simulation

**Run Date**: 2026-03-10 0846

**Description**  
This script visualizes the TCWT explanation of the 21 cm anomaly (EDGES deep absorption at z ≈ 17–20):  
- Inductive scaling exponent α(z) descending from 0.5 to 0.4 around reionization lock (z ≈ 6.1)  
- Phase-viscosity heating preventing adiabatic IGM cooling  
- Resulting deeper 21 cm absorption trough

**Key Parameters** (internal TCWT v2026.3):
- κ = 1.455
- Ω_max ≈ 16.91
- N_knot = 6.17e35
- Reionization lock at z ≈ 6.1
- σ ≈ 6.58e-36 m/rad
- L_coh ≈ 6.0e-35 m

**Files**:
- tcwt_21cm_anomaly.py
- 21cm_anomaly_simulation.png
- README.md

**Interpretation**  
The sharp drop in α(z) generates phase-viscosity heat, raising T_IGM above adiabatic levels in the z ≈ 17–20 window → deeper absorption signal.  
This occurs pre-stellar, from hierarchical pump activity.

Open refinement: quantitative heating rate calibration.
