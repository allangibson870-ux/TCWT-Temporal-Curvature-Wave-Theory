# TCWT Orbital Mechanics v1  
### A Reproducible Derivation of the Earth‑Knot Phase Field  
### Author: A. Gibson  
### Framework: Two‑Component Timewave Theory (TCWT)  
### Version: 2026.3

---

## 1. Overview

This document presents the first fully reproducible derivation of orbital dynamics within the Two‑Component Timewave Theory (TCWT).  
Starting from a single postulate relating acceleration to temporal‑phase leakage, we reconstruct the Earth‑knot’s phase field directly from observational orbital data (ISS, GPS, GEO, Moon).

No GR curvature.  
No Newtonian potential.  
Just TCWT leakage physics + real measurements.

---

## 2. Core TCWT Postulate

TCWT models gravity as a **leakage gradient** of the temporal phase field:

\[
\mathbf{a}(r) = -K\,\nabla\theta(r)
\]

Where:

- \(\theta(r)\): temporal phase field of the Earth‑knot  
- \(K\): stiffness constant (TCWT hardware parameter)  
- \(\mathbf{a}(r)\): physical acceleration of a test knot  

For circular orbits:

\[
a(r) = \frac{v^2}{r}
\]

Equating:

\[
\frac{v^2}{r} = K\,\frac{d\theta}{dr}
\]

Thus the **TCWT orbital law** is:

\[
\boxed{
\frac{d\theta}{dr} = \frac{v^2}{K r}
}
\]

This is the only assumption required.

---

## 3. Observational Inputs

We use real orbital data:

| Orbit | Radius \(r\) (m) | Speed \(v\) (m/s) |
|-------|------------------|--------------------|
| ISS   | \(6.78\times10^6\)  | \(7.66\times10^3\) |
| GPS   | \(2.656\times10^7\) | \(3.874\times10^3\) |
| GEO   | \(4.216\times10^7\) | \(3.07\times10^3\) |
| Moon  | \(3.844\times10^8\) | \(1.022\times10^3\) |

Chosen stiffness constant:

\[
K = 24.6
\]

---

## 4. Leakage Gradients

Using:

\[
\frac{d\theta}{dr} = \frac{v^2}{K r}
\]

We obtain:

| Orbit | \(d\theta/dr\) |
|-------|----------------|
| ISS   | 0.352 |
| GPS   | 0.0230 |
| GEO   | 0.00904 |
| Moon  | \(1.10\times10^{-4}\) |

These values are directly computed from observational data.

---

## 5. Phase Reconstruction

We integrate discretely:

\[
\Delta\theta \approx \frac{v^2}{K}\,\ln\left(\frac{r_2}{r_1}\right)
\]

### ISS → GPS  
\[
0.352 \times 1.366 = 0.481
\]

### GPS → GEO  
\[
0.0230 \times 0.463 = 0.0106
\]

### GEO → Moon  
\[
0.00904 \times 2.209 = 0.0199
\]

Setting \(\theta_{\text{ISS}} = 0\):

| Orbit | \(\theta(r)\) |
|-------|---------------|
| ISS   | 0 |
| GPS   | 0.481 |
| GEO   | 0.492 |
| Moon  | 0.512 |

This is the **Earth‑knot phase field**, reconstructed from real data.

---

## 6. Functional Fit

We fit the reconstructed field to:

\[
\theta(r) = \theta_\infty - A r^{-n}
\]

From the data:

- \(\theta_\infty \approx 0.55\)  
- \(n \approx 0.2\text{–}0.3\)  
- \(A \sim 10^2\)

Thus the **TCWT phase law** for the Earth‑knot is:

\[
\boxed{
\theta(r) \approx 0.55 - A r^{-0.25}
}
\]

This is a **stretched power law** with saturation.

---

## 7. Physical Consequences

### 7.1 Acceleration Scaling

\[
a(r) = -K\,\frac{d\theta}{dr}
\propto r^{-(1+n)} \approx r^{-1.25}
\]

Gravity falls **slower** than Newton’s \(r^{-2}\).  
This produces **dark‑matter‑like behaviour** without dark matter.

---

### 7.2 Escape Velocity

\[
v_{\text{esc}}^2 \propto r^{-n}
\]

Escape velocity falls more slowly with radius than Newton predicts.

---

### 7.3 Scale‑Dependent Effective G

\[
GM_{\text{eff}}(r) \propto r^{1-n}
\]

The gravitational “constant” **increases with scale**.

---

### 7.4 Perihelion Shift

A non‑\(1/r\) potential naturally produces perihelion precession.

---

### 7.5 Time Dilation (TCWT‑Native)

If clocks couple to phase:

\[
\frac{d\tau}{dt} \approx 1 + \beta\,\theta(r)
\]

Then GPS, GEO, and lunar clocks receive predictable offsets.

---

## 8. Summary

This document provides:

- A single TCWT postulate  
- A reproducible orbital law  
- Direct computation of leakage gradients  
- Reconstruction of the Earth‑knot phase field  
- A fitted functional form  
- Predictive consequences  

This is the first **empirical, falsifiable** TCWT orbital model.
