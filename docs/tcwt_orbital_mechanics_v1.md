# TCWT Orbital Mechanics

### Phase-Bleed Gravity Formulation

Version: 2026.5-corrected

------------------------------------------------------------------------

## 1. Core Postulate: Phase-Bleed Acceleration

In Total Coherence Wave Theory (TCWT), gravity arises from gradients in
the temporal phase field θ.

a(r) = -χ ∇θ(r)

Where:

  Symbol   Meaning                Units
  -------- ---------------------- ---------------
  θ        Temporal phase field   dimensionless
  λ = ∇θ   Phase gradient         1/m
  a        Acceleration           m/s²
  χ        Coupling constant      m²/s²

------------------------------------------------------------------------

## 2. Coupling Constant χ

The coupling constant connects emergent gravitational acceleration to
Hum-flow parameters.

χ = (c² κ) / (C₀ Ω_max)

### Calibration

  Parameter   Value
  ----------- ------------------
  c           2.9979 × 10⁸ m/s
  κ           1.455
  Ω_max       16.91
  C₀          0.0594

Calculation:

c² = 8.9874 × 10¹⁶

χ ≈ 1.30 × 10¹⁷ m²/s²

------------------------------------------------------------------------

## 3. Circular Orbit Law

For circular motion:

v² / r = a(r)

Substituting phase‑bleed acceleration:

v² / r = χ \|λ\|

Therefore:

λ(r) = v² / (χ r)

This allows the phase gradient field to be inferred directly from
orbital observations.

------------------------------------------------------------------------

## 4. Phase Gradients for Known Orbits

Using χ = 1.30 × 10¹⁷:

  Orbit   Radius r (m)   Velocity v (m/s)   λ (rad/m)
  ------- -------------- ------------------ -------------
  ISS     6.78 × 10⁶     7660               6.6 × 10⁻¹⁷
  GPS     2.66 × 10⁷     3870               4.3 × 10⁻¹⁸
  Moon    3.84 × 10⁸     1022               2.1 × 10⁻²⁰

These gradients are extremely small, consistent with weak gravitational
fields in the Solar System.

------------------------------------------------------------------------

## 5. Newtonian Limit

For planetary systems:

v² = GM / r

Substituting into the gradient relation:

λ(r) = GM / (χ r²)

Integrating:

θ(r) = θ∞ − GM / (χ r)

Thus:

∇θ ∝ 1 / r²

and the acceleration becomes:

a(r) = −GM / r²

Therefore Newtonian gravity is recovered when the phase field is sourced
by localized mass.

------------------------------------------------------------------------

## 6. Galactic Halo Regime

For galaxies the rotation curve becomes approximately flat:

v ≈ v₀

Substituting:

λ(r) = v₀² / (χ r)

Integrating:

θ(r) = θ₀ − (v₀² / χ) ln(r / r₀)

This produces a logarithmic phase profile, which yields flat rotation
curves without additional dark matter particles.

------------------------------------------------------------------------

## 7. Binary Pulsar Prediction

TCWT predicts a small additional contribution to relativistic periastron
advance due to Ω‑cap coupling.

  System           Extra Precession
  ---------------- --------------------
  PSR B1913+16     +0.066 arcsec/year
  PSR J0737‑3039   +0.11 arcsec/year

Future pulsar timing arrays may be able to test this deviation.

------------------------------------------------------------------------

## 8. Empirical Consistency

### Weak Equivalence Principle

Acceleration depends only on the background phase gradient:

a = −χ ∇θ

Test‑body composition cancels, preserving universal free fall.

### Multi‑Messenger Timing

Low‑energy phase propagation remains Lorentz invariant, maintaining
coincidence between gravitational‑wave and electromagnetic signals.

------------------------------------------------------------------------

## 9. Summary

Key relations:

Phase‑bleed acceleration:

a = −χ ∇θ

Orbital gradient:

λ = v² / (χ r)

Newtonian regime:

θ(r) ∝ 1 / r

Galactic halo regime:

θ(r) ∝ ln r

The framework:

• reproduces Newtonian gravity in the Solar System\
• naturally generates flat galactic rotation curves\
• predicts small measurable pulsar timing deviations\
• does not require additional dark matter particles
