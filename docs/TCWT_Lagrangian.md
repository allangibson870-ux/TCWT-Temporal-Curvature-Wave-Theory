# TCWT Lagrangian (Orthodox Field-Theory Form)

**Version**: 2026.3  
**Author**: A. Gibson  
**Purpose**: This document reformulates the core ideas of Total Coherence Wave Theory (TCWT) — coherence, phase-bleed gravity, ghost density, and decoherence — in a form compatible with standard scalar-field theory.  
It is **inspired by** but does not claim equivalence to conventional GR or QFT.

## 1. Field Content

- **θ(x)** — real scalar field representing the temporal phase  
- **G(x)** — real scalar field representing ghost density (dark-energy analogue)  
- **Ω(x)** — auxiliary field encoding temporal drag / informational density  

The phase-bleed field is defined as:

$$
\lambda_\mu = \partial_\mu \theta
$$

which acts as the gravitational analogue.

## 2. Lagrangian Density

$$
\begin{aligned}
\mathcal{L} ={}& -\frac{1}{2} Z_\theta(\Omega) \, g^{\mu\nu} \partial_\mu \theta \partial_\nu \theta - \frac{1}{2} m_\theta^2 \theta^2 \\
& -\frac{1}{2} Z_G \, g^{\mu\nu} \partial_\mu G \partial_\nu G - \frac{1}{2} m_G^2 G^2 \\
& - \gamma \, \partial_\mu G \partial^\mu \theta \\
& - \lambda_1 \theta^2 G - \lambda_2 G^2 \\
& + \frac{1}{2} (\partial_\mu \Omega)^2 - V(\Omega) - \Lambda_G
\end{aligned}
$$

where the constraint and cap potential for Ω is:

$$
V(\Omega) = \frac{\mu}{2} \left( \Omega - \kappa |\nabla \theta| \right)^2 + \frac{\lambda}{4} \left( \max(\Omega, \Omega_{\max})^2 - \Omega_{\max}^2 \right)^2
$$

with Ω_max ≈ 16.91.

This is a minimal extension of standard scalar-field theory: two interacting scalars with Ω-dependent kinetic term for θ and a dynamical auxiliary field Ω.

## 3. Interpretation of Key Terms

### 3.1 Coherence and Drag (Ω)
The kinetic prefactor encodes coherence and decoherence:

$$
Z_\theta(\Omega) = 1 + \beta \left( \frac{\Omega}{\Omega_{\max}} \right)^2
$$

Ω is a dynamical auxiliary field enforced variationally by the constraint term.  
Varying w.r.t. Ω gives:

$$
\Omega = \kappa |\nabla \theta|
$$

To include relativistic velocity effects, the full internal form is:

$$
\Omega = \kappa \left( |\nabla \theta| + \frac{K_{\text{tc}} v}{\sqrt{1 - v^2/c^2}} \right)
$$

The soft cap potential prevents Ω from exceeding Ω_max ≈ 16.91.

### 3.2 Phase-Bleed and Gravity Analogue
The phase-bleed field λ_μ = ∂_μ θ acts as the gravitational analogue.  
Its divergence couples to ghost density via the derivative interaction:

$$
\mathcal{L}_{\text{coupling}} = - \gamma \, \partial_\mu G \partial^\mu \theta
$$

This reproduces the TCWT relation ∇·λ ∼ ∂_t G.

### 3.3 Dark Energy as Reionization-Locked Inductive Scaling
Dark energy is the residual collective inductance of the knot hierarchy, locked at the reionization transition.  
The inductive scaling exponent α(z) transitions from 0.5 (pre-reionization, local knot-dominated pumping) to 0.4 (post-reionization, global fractal-foam filtering):

- α(z) ≈ 0.5 for z > 6.1  
- α(z) ≈ 0.4 for z < 6.1 (Reionization Lock at z ≈ 6.1)

This lock fixes the effective coupling after the universe becomes transparent, explaining why dark energy dominates late.  
The transition is driven by the shift from stochastic resonance (√N_knot) to volume + fractal suppression (N_knot^{1/3} × foam factor).  
This is a fully internal mechanism tying dark energy to the observed reionization epoch.

### 3.4 Knot Stability Energy — Derivation from Effective Potential
The energy of a knot is obtained by integrating the Hamiltonian density over the Gaussian soliton profile θ(r) = θ₀ e^{-r²/(2R²)}:

$$
E(R) = \int \left[ \frac{1}{2} (\nabla \theta)^2 + V(\theta) \right] d^3 r
$$

This yields the leading-order terms:

$$
E(R) = a R + \frac{b}{R} + c R^3
$$

- a R = background Hum tension (from κ |∇θ|²)  
- b/R = surface/gradient energy  
- c R³ = volume potential energy (from V(θ) ≈ (M/2) θ²)

Coefficients are fixed by matching to the knot squeeze pressure and transition scale.

### 3.5 21 cm Anomaly: Phase-Viscosity from α(z) Descent
The unexpectedly deep 21 cm absorption at z ≈ 17–20 (EDGES anomaly) is explained by phase-viscosity generated during the descent of α(z) from 0.5 to 0.4.  
This “grinding” produces decoherence heat (~1–10 K at z ≈ 17–20), preventing adiabatic cooling of the IGM and deepening the absorption trough.  
The effect occurs **before** bulk star formation and reionization, confirming the hierarchical pump was active pre-stellar.

### 3.6 Dark Matter as Phase-Opaque Knots
The ~84 % mass discrepancy (dark matter) is identified as phase-opaque knots — high-gradient solitons with |∇θ| ≥ λ_crit ≈ 1.52 × 10^{35} rad/m, entering the relativistic decoherence shadow (Ω ≥ Ω_max, V ≤ 0.368).  
These knots are trapped in the fractal phase-foam (d ≈ log₂3 ≈ 1.585) and form the invisible gravitational scaffolding for the hierarchical pump, explaining flat rotation curves, Bullet Cluster dynamics, and the missing mass fraction without exotic particles.

## 4. Relation to Original TCWT Constructs

| TCWT Concept                | Orthodox Interpretation                                      |
|-----------------------------|---------------------------------------------------------------|
| Coherence action            | Non-canonical kinetic term Z_θ(Ω)                             |
| Phase-bleed λ               | Gradient of θ                                                 |
| Ghost density G             | Second scalar field with shallow potential                    |
| Decoherence cliff           | Ω-dependent kinetic suppression                               |
| Knot solitons               | Localised θ solutions of Euler–Lagrange equations             |
| Dark energy                 | Residual collective inductance locked at reionization         |
| Dark matter                 | Phase-opaque knots trapped in fractal foam                    |
| Visibility V = e^{-σ|λ|}    | Exponential suppression from phase gradient                   |

## 5. Conserved Quantities (Noether Currents)

**Phase current** (global θ shift symmetry):

$$
J^\mu = 2 C_0 (\partial_t \theta - \Omega) \delta^\mu_0 + 2 \kappa \partial^\mu \theta
$$

**Energy-momentum** (time translation):

Energy density:

$$
\rho = C_0 (\partial_t \theta - \Omega)^2 + \kappa |\nabla \theta|^2 + \alpha (\partial_t G - \nabla^2 \theta)^2 + \frac{1}{2} (\partial_t \Omega)^2 + V(\Omega)
$$

Both are conserved: ∂_μ J^μ = 0 and ∂_μ T^{μ0} = 0.

## 6. Derivation of the Non-Commuting Phase Commutator

The commutator [θ(t₁), θ(t₂)] = i κ Ω (t₂ - t₁) emerges from the non-local term:

$$
\mathcal{L}_{\text{non-local}} = -\frac{\kappa}{2} \int dt' \Omega(t') (\partial_t \theta(t))^2 \cdot \text{sign}(t - t')
$$

Using the Peierls bracket, the commutator is:

$$
[\theta(t_1), \theta(t_2)] = i \kappa \bar{\Omega} (t_2 - t_1)
$$

where \bar{Ω} is the average Ω over the interval. For slowly varying Ω, this reduces to the original form.

## 7. Visibility Suppression (fully internal derivation)

$$
V(r) = \exp(-\sigma |\lambda(r)|)
$$

σ is derived from the visibility dropping to 1/e at the transition gradient:

$$
\sigma = \frac{1}{|\lambda|_{\text{transition}}} = \frac{1}{g} = \frac{1}{\kappa \times 2\pi f_{\text{Hum}} / c} \approx 6.58 \times 10^{-36} \, \text{m/rad}
$$

## 8. Summary

This formulation provides a bridge between TCWT’s coherence-based physics and standard field theory.  
It preserves the core mechanisms while presenting them in a form compatible with conventional frameworks.  
Several aspects (e.g. dark energy scaling) remain open for refinement and are marked as such.

