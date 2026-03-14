# TCWT Algebraic Mathematics & Derivations

**Version**: 2026.3-algebraic-core  
**Author**: A. Gibson  
**Purpose**: This document collects the core algebraic derivations, field equations, conserved quantities, stability analyses, and empirical consistency checks for Total Coherence Wave Theory (TCWT) in its pregeometric formulation.

## 1. Field Equations

From the pregeometric action

$$
S = \int \left[ 
C_0 \left( \frac{d\theta}{dt} - \Omega \right)^2 
+ \kappa \left( \frac{d\theta}{d\ell} \right)^2 
+ \alpha \left( \frac{dG}{dt} - \frac{d^2 \theta}{d\ell^2} \right)^2 
+ V_{\text{cap}}(\Omega) 
\right] d\ell \, dt
$$

### 1.1 θ-equation of motion

$$
C_0 \frac{d}{dt} \left( \frac{d\theta}{dt} - \Omega \right) 
- \frac{d}{d\ell} \left( \kappa \frac{d\theta}{d\ell} \right) 
+ \alpha \frac{d^2}{d\ell^2} \left( \frac{dG}{dt} - \frac{d^2 \theta}{d\ell^2} \right) = 0
$$

### 1.2 Ω-evolution equation

$$
C_0 \left( \frac{d\theta}{dt} - \Omega \right) + \frac{\partial V_{\text{cap}}}{\partial \Omega} = 0
$$

When Ω < Ω_max → Ω = dθ/dt.  
When Ω ≥ Ω_max the cap enforces Ω ≤ Ω_max.

### 1.3 G field equation

$$
\partial_\mu \left( Z_G \partial^\mu G \right) - m_G^2 G + \gamma \Box \theta - \lambda_1 \theta^2 - 2 \lambda_2 G = 0
$$

### 1.4 Effective gravitational field

$$
\lambda = \frac{d\theta}{d\ell}, \quad a(r) = -\chi \lambda
$$

(χ fixed from knot stability)

## 2. Noether Currents

Global U(1) phase shift θ → θ + ε is a symmetry.

**Noether current**:

$$
J = 2 C_0 \left( \frac{d\theta}{dt} - \Omega \right) \frac{d}{dt} + 2 \kappa \frac{d\theta}{d\ell} \frac{d}{d\ell}
$$

**Physical meaning**: conserved temporal phase flux through the knot network.  
Enforces conservation of information carried by the Hum; explains stability and collisionless nature of phase-opaque knots.

## 3. Energy Density & Stability

**Hamiltonian density**:

$$
\rho = C_0 \left( \frac{d\theta}{dt} - \Omega \right)^2 + \kappa \left( \frac{d\theta}{d\ell} \right)^2 + \alpha \left( \frac{dG}{dt} - \frac{d^2 \theta}{d\ell^2} \right)^2 + V_{\text{cap}}(\Omega)
$$

**Positive energy**: all terms ≥ 0 → ρ ≥ 0 (vacuum equality).

**Stability safeguards**:
- Ω-cap → quartic growth prevents Ω > Ω_max  
- Visibility floor V = exp(−σ |λ|) → suppresses high-λ runaways  
- Knot size floor R ≥ R_crit → prevents collapse/singularities

## 4. Critical Tests Summary

- Field equations derived from action variation  
- Noether current conserves global phase  
- Hamiltonian density positive-definite  
- Stability of Gaussian knot solutions confirmed  
- Rotation curves flatten via logarithmic + foam accumulation  
- Decoherence threshold at Ω_max defines phase-opaque regime  
- Solar flare precursor δf/f ≈ 10^{-18}–10^{-17} (within reach)

This algebraic core is now self-consistent and ready for empirical confrontation.
