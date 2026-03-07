TCWT — Total Coherence Wave Theory (v2026.2)
A coherence‑based scalar framework where time is a physical wave, knots are stable solitons, and gravity emerges from phase‑bleed.
1. Overview
TCWT proposes that time is a physical oscillation — the TimeWave — with tension, stiffness, and coherence.
All physical structure (matter), long‑range interaction (gravity), and quantum behaviour emerge from distortions of this wave.
The theory is built from four primitives:
- θ — unwinding phase
- Ω — temporal drag
- λ = ∇θ — phase‑bleed (gravity analogue)
- G — ghost density (dark‑energy analogue)

2. The Eternal Hum
θ_Hum(t) = A_Hum sin(2π f_Hum t + ψ)



3. Knots (Matter)
θ_Knot(r,t) = Θ0(t) e^{-r²/R²}


Knots have finite binding energy, finite radius, and stability enforced by the coherence action.

4. Phase‑Bleed (Gravity)
λ = ∇θ
∇·λ = ∂t G


Poisson‑like law:
∇·λ = 4π γ ρ_knot


Newton‑like acceleration:
a(r) = -χ λ(r)



5. Ghost Density (Dark Energy)
∂t G = ∇²θ



6. The Coherence Action
S_TCWT[θ, Ω, G] = ∫ dt ∫ d³r  L_TCWT


L_TCWT =
  - C0 (∂tθ - Ω)²
  - κ |∇θ|²
  - α (∂tG - ∇²θ)²
  - U(Ω)



7. Knot Stability
E(R) = aR + b/R + cR³



8. Relativistic Decoherence
Ω(v) = 1 / sqrt(1 - (v/v_Hum)²)
Ω_max = 24.6
v_crit = 0.9992 v_Hum
C(v) = max(0, 1 - (Ω(v)/24.6)²)
S(v) = 2√2 · C(v)



9. Visibility & Dark Matter
V(r) = exp(-σ |λ(r)|)



10. Cosmology
ΔT/T = A κ λ + B κ ∫ ∂tλ dr
ρ_DE ∝ κ P_leak (c / (R_slab H0))



11. Quantum Behaviour
[θ(t1), θ(t2)] = i κ (t2 - t1)
V = exp(-σ λ)
S = 2√2 C(v)



12. Status & Roadmap
- Coherence action defined
- Knot stability proven
- Gravity = λ‑field
- Dark matter = low‑visibility knots
- Dark energy = ghost accumulation
- Relativistic decoherence curve derived
- Bell‑test prediction curve defined
- CMB anisotropy mechanism established


LICENSE: Apache-2.0
cff-version: 1.2.0
message: "If you use this theory or code, please cite it as below."
authors:
  - family-names: "Gibson"
    given-names: "Allan"
title: "TCWT: Total Coherence Wave Theory"
version: "1.0.0"
date-released: "2024-05-22"
url: "https://github.com"
license: "Apache-2.0"
abstract: "A framework for interpreting quantum decoherence as a function of informational density (Omega) and temporal curvature."

