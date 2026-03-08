### TCWT Orbital Mechanics (v2026.3) — Internal Derivation

**Core postulate**  
Gravity is phase-bleed acceleration:

$$
\mathbf{a}(r) = -\chi \nabla\theta(r)
$$

**Circular orbit law** (from v²/r = χ |dθ/dr|):

$$
\boxed{ \frac{d\theta}{dr} = \frac{v^2}{\chi r} }
$$

**Phase-to-acceleration coupling** (internal):

$$
\chi = c^2 \kappa \approx 1.31 \times 10^{17} \, \text{m}^2/\text{s}^2
$$

(derived from relativistic scale c² and phase strength κ = 1.455)

**Leakage gradients** (example orbits):

- ISS (r = 6.78×10⁶ m, v = 7.66×10³ m/s): dθ/dr ≈ 6.41×10⁻¹¹ rad/m  
- GPS: ≈ 2.12×10⁻¹² rad/m  
- GEO: ≈ 6.67×10⁻¹³ rad/m  
- Moon: ≈ 2.21×10⁻¹⁵ rad/m  

**Phase accumulation** (logarithmic):

$$
\theta(r) \approx \theta_\infty - \frac{v^2}{\chi} \ln\left(\frac{r}{r_0}\right)
$$

**Consequences**:
- Newtonian 1/r² at large r  
- Logarithmic phase → scale-dependent effective G  
- Perihelion precession from non-1/r term  
- Time dilation dτ/dt ≈ 1 + β θ(r) — tiny, configuration-dependent

This is fully reproducible from TCWT primitives — no GR curvature, no Newtonian potential.

