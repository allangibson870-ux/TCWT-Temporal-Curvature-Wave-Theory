# TCWT: Temporal Curvature Wave Theory  
### A Scalar–Tensor TimeWave Dark Matter Model

**Temporal Curvature Wave Theory (TCWT)** is a scalar–tensor cosmological framework in which a scalar field \( \phi \) encodes a “TimeWave” that both:

- behaves as ultra‑light dark matter on cosmological scales, and  
- modifies the growth of structure in a way that can address the \( \sigma_8 \) tension,

while remaining compatible with Solar‑System tests and the GW170817 speed‑of‑gravity constraint via a Vainshtein‑type screening mechanism.

This repository is a **conceptual and mathematical blueprint**, aimed at collaborators who can help implement TCWT in Boltzmann codes such as CLASS / hi\_class and test it against data.

---

## 1. Theory class and motivation

TCWT lives in the space of:

- **Scalar–tensor gravity** (Horndeski / DHOST‑like)  
- **k‑essence / Galileon‑type** kinetic structure  
- **Ultra‑light scalar dark matter** (fuzzy DM–scale mass)  

The core idea:

- A scalar field \( \phi \) acts as a **TimeWave**, with its oscillations providing an effective dark matter component.  
- The dynamics of \( \phi \) introduce a **scale‑dependent friction term** in the growth of structure, potentially resolving the \( \sigma_8 \) tension.  
- A **Vainshtein screening mechanism** ensures that any fifth force or modification of the GW speed is suppressed in high‑density regions, keeping the theory compatible with local tests of gravity.

---

## 2. Core ingredients

### 2.1 Scalar field and action

At the schematic level, TCWT uses a scalar–tensor action of the form:

\[
S = \int d^4x \sqrt{-g} \left[ \frac{M_{\rm Pl}^2}{2} R + \mathcal{L}_\phi + \mathcal{L}_{\text{V}} + \mathcal{L}_{\text{matter}} \right]
\]

where:

- \( \mathcal{L}_\phi \) is a k‑essence–type scalar Lagrangian (kinetic + potential),  
- \( \mathcal{L}_{\text{V}} \) is a non‑linear derivative self‑interaction (Vainshtein / Galileon term),  
- \( \mathcal{L}_{\text{matter}} \) is the standard matter sector.

The scalar field \( \phi \) is interpreted as the generator of a **TimeWave**: its background evolution and oscillations define an effective time structure and dark matter component.

### 2.2 Effective dark matter behaviour

For suitable choices of potential and mass scale \( m_\phi \sim 10^{-22}\,\text{eV} \), the field:

- oscillates rapidly on microscopic timescales,  
- averages to an effective pressureless component on cosmological timescales,  
- behaves like ultra‑light dark matter (fuzzy DM–like phenomenology).

This links TCWT directly to known scalar‑field dark matter models, but with an additional time‑structured interpretation.

---

## 3. Linear perturbations and the \( \sigma_8 \) tension

In the linear regime, the dark matter density contrast \( \delta \) obeys a modified growth equation of the form:

\[
\ddot{\delta} + (2H + \gamma)\dot{\delta} - 4\pi G_{\rm eff}\rho\,\delta = 0
\]

where:

- \( H \) is the Hubble parameter,  
- \( \gamma \) is an **extra friction term** sourced by the TimeWave field,  
- \( G_{\rm eff} \) is an effective gravitational coupling.

### 3.1 Role of \( \gamma \) (growth damping)

The \( \sigma_8 \) tension is a mismatch between:

- CMB‑inferred clustering (\( \sigma_8 \approx 0.83 \)), and  
- weak‑lensing / large‑scale structure (\( \sigma_8 \approx 0.76 \)),

corresponding to a **5–10% suppression** in the growth of structure.

In TCWT, the TimeWave field introduces an additional friction term \( \gamma \), which can:

- **suppress the growth factor** \( D(a) \),  
- reduce \( \sigma_8 \) by the required amount,  
- do so in a **scale‑dependent** way.

A rough target is:

\[
\gamma \sim 0.05\,H
\]

over the relevant structure‑formation epoch. This is one of the main phenomenological motivations for TCWT.

---

## 4. Gravitational waves and the GW170817 constraint

TCWT allows for an **effective metric** for gravitational waves of the disformal form:

\[
g^{\text{eff}}_{\mu\nu} = g_{\mu\nu} + B(\phi)\,\partial_\mu\phi\,\partial_\nu\phi
\]

This can, in principle, modify the propagation speed of gravitational waves.

### 4.1 GW170817 bound

The neutron‑star merger GW170817, together with its electromagnetic counterpart, constrains the GW speed to:

\[
\left|\frac{c_{\text{GW}}}{c} - 1\right| < 10^{-15}
\]

This implies that **viable TCWT parameter choices must satisfy**:

\[
B(\phi)\,(\partial\phi)^2 \approx 0
\]

in the **late universe** and in the **local environment** where GW detectors operate.

This is enforced in TCWT via a **Vainshtein screening mechanism**, described next.

---

## 5. Phase 2: Vainshtein screening & local viability

To remain compatible with Solar‑System tests, binary pulsars, Cassini Shapiro delay, and GW170817, TCWT incorporates a **Vainshtein‑type screening mechanism**.

### 5.1 Non‑linear Vainshtein term

We introduce a derivative self‑interaction (Galileon‑like) term:

\[
\mathcal{L}_{\text{V}} = \frac{1}{\Lambda^3}(\partial\phi)^2 \Box\phi
\]

where \( \Lambda \) is a strong‑coupling scale.

- In **low‑density / cosmological** regions, this term is subdominant.  
- In **high‑density** regions (near stars, galaxies), it becomes important and suppresses the scalar gradients.

### 5.2 Vainshtein radius \( r_V \)

For a source of mass \( M \), the Vainshtein radius is:

\[
r_V = \left(\frac{M}{16\pi M_{\rm Pl}\Lambda^3}\right)^{1/3}
\]

- **Outside \( r_V \)** (cosmological scales):  
  - Non‑linearities are negligible.  
  - The TimeWave field evolves freely and contributes to dark matter and growth damping (\( \gamma \)).

- **Inside \( r_V \)** (Solar System, local galaxy):  
  - Non‑linearities dominate.  
  - Field gradients satisfy \( \partial_\mu\phi \approx 0 \).  
  - Fifth forces and disformal effects are strongly suppressed.

### 5.3 Resolving GW170817

Because the disformal coupling depends on \( \partial_\mu\phi \), the screening enforces:

\[
\partial_\mu\phi \to 0 \quad \Rightarrow \quad g^{\text{eff}}_{\mu\nu} \to g_{\mu\nu}
\]

in the local universe.

Result:

\[
c_{\text{GW}} = c
\]

within the detection range of LIGO/Virgo and future ground‑based detectors, keeping TCWT consistent with GW170817 and related constraints.

---

## 6. Parameter summary

| Parameter | Role | Target / Behaviour | Status |
|----------|------|--------------------|--------|
| \( m_\phi \) | Scalar mass scale | \( \sim 10^{-22}\,\text{eV} \) | Fuzzy DM–like, sets oscillation frequency |
| \( \gamma \) | Growth damping | \( \sim 0.05\,H \) over structure‑formation epoch | Promising for resolving \( \sigma_8 \) |
| \( \Lambda \) | Vainshtein scale | Sets strength of non‑linear term | Chosen to give Solar‑System‑scale \( r_V \) |
| \( r_V \) | Vainshtein radius | \( r_V(M_\odot) \gg \text{AU} \) | Ensures local screening |
| \( B(\phi) \) | Disformal coupling | Must satisfy \( B(\phi)(\partial\phi)^2 \approx 0 \) today | Enforced via screening / decay |

---

## 7. Observational “smoking gun” tests

TCWT is falsifiable through three main observational channels:

1. **\( \sigma_8 \) growth suppression**  
   - Prediction: scale‑dependent suppression of the matter power spectrum at intermediate scales.  
   - Test: compare TCWT predictions (via CLASS/hi\_class) to weak‑lensing and RSD data.

2. **Gravitational‑wave propagation**  
   - Prediction: \( c_{\text{GW}} = c \) locally, with possible tiny, frequency‑dependent dispersion at cosmological scales.  
   - Test: future detectors (LISA, ET) could search for small phase shifts correlated with the TimeWave background.

3. **Strong‑gravity “clock” effects (conceptual)**  
   - Interpretation: \( \phi \) as a time generator suggests subtle deviations in clock rates in strong fields.  
   - Test: anomalies in pulsar timing / Shapiro delay would be a dramatic signal, but this is a longer‑term, high‑precision frontier.

---

## 8. Roadmap and collaboration

This repo is **not** a finished model implementation. It is a **blueprint** designed to be:

- mathematically consistent,  
- observationally motivated,  
- clearly positioned within scalar–tensor theory,  
- ready for numerical implementation.

### Phase 1: Mathematical consistency

- [ ] Finalise the scalar–tensor action and EOMs.  
- [ ] Derive the linear perturbation equations in






