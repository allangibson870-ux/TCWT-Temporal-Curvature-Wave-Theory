# TCWT Lagrangian Formulation
### Corrected Field Theory Formulation

Version: 2026.5  
Author: A. Gibson  
Revision: mathematical consistency update

---

# 1. Core Fields

TCWT is formulated in terms of three scalar fields defined on an emergent spacetime manifold in the low-energy limit.

| Field | Meaning |
|------|--------|
| $\theta(x,t)$ | temporal phase field |
| $G(x,t)$ | ghost / leakage field |
| $\Omega(x,t)$ | informational drag density |

Derived quantity:

$$
\lambda = \nabla \theta
$$

which represents the **phase gradient responsible for gravitational acceleration**.

---

# 2. Lagrangian Density

The TCWT Lagrangian density is

$$
\mathcal{L}
=
C_0(\dot{\theta}-\Omega)^2
+
\kappa (\nabla\theta)^2
+
\alpha (\dot G - \nabla^2 \theta)^2
-
V_{\Omega}(\Omega)
$$

where

| Parameter | Meaning |
|----------|--------|
| $C_0$ | temporal coherence coefficient |
| $\kappa$ | spatial phase stiffness |
| $\alpha$ | ghost-coupling strength |

The Ω-cap potential limits informational drag:

$$
V_{\Omega}(\Omega)
=
\frac{\lambda_\Omega}{4}
(\Omega^2-\Omega_{max}^2)^2
$$

This prevents runaway gradients.

---

# 3. Action

The action is

$$
S =
\int \mathcal{L}\, d^3x\, dt
$$

Stationary action condition:

$$
\delta S = 0
$$

which yields the field equations.

---

# 4. Euler–Lagrange Equations

For a field $\phi$:

$$
\frac{\partial \mathcal L}{\partial \phi}
-
\partial_\mu
\left(
\frac{\partial \mathcal L}{\partial(\partial_\mu \phi)}
\right)
+
\partial_\mu\partial_\nu
\left(
\frac{\partial \mathcal L}{\partial(\partial_\mu\partial_\nu \phi)}
\right)
=0
$$

---

# 5. Phase Field Equation

Applying the Euler–Lagrange equation to $\theta$ gives

$$
\partial_t
\big[2C_0(\dot\theta-\Omega)\big]
-
\nabla\!\cdot
\big[2\kappa\nabla\theta\big]
+
\nabla^2
\big[2\alpha(\dot G-\nabla^2\theta)\big]
=
0
$$

This governs propagation of the **Hum phase field**.

---

# 6. Ω Evolution Equation

Variation with respect to $\Omega$ yields

$$
-2C_0(\dot\theta-\Omega)
-
\frac{dV_\Omega}{d\Omega}
=
0
$$

Low-energy regime (cap inactive):

$$
\Omega \approx \dot{\theta}
$$

Thus the auxiliary field tracks the temporal phase rate.

---

# 7. Ghost Field Equation

Variation with respect to $G$ produces

$$
\partial_t
\big[2\alpha(\dot G - \nabla^2 \theta)\big]
=
0
$$

Low-energy limit:

$$
\dot G \approx \nabla^2 \theta
$$

The ghost field therefore acts as a **leakage regulator for phase curvature**.

---

# 8. Effective Gravitational Acceleration

The phase gradient generates acceleration:

$$
a = -\chi \nabla \theta
$$

with coupling constant

$$
\chi =
\frac{c^2 \kappa}{C_0 \Omega_{max}}
$$

This connects the **field theory to orbital dynamics**.

---

# 9. Noether Current

The Lagrangian is invariant under the global phase shift

$$
\theta \rightarrow \theta + \epsilon
$$

The Noether current is

$$
J^\mu
=
\frac{\partial \mathcal L}{\partial(\partial_\mu \theta)}
$$

Temporal component:

$$
J^0 = 2C_0(\dot\theta-\Omega)
$$

Spatial component:

$$
\vec J = 2\kappa \nabla \theta
$$

Conservation law:

$$
\partial_\mu J^\mu = 0
$$

This expresses **conservation of global phase flux**.

---

# 10. Hamiltonian Density

Canonical momenta:

$$
\pi_\theta = 2C_0(\dot\theta-\Omega)
$$

$$
\pi_G = 2\alpha(\dot G-\nabla^2\theta)
$$

Hamiltonian density:

$$
\mathcal H
=
\pi_\theta \dot\theta
+
\pi_G \dot G
-
\mathcal L
$$

which simplifies to

$$
\mathcal H =
C_0(\dot\theta-\Omega)^2
+
\kappa (\nabla\theta)^2
+
\alpha(\dot G-\nabla^2\theta)^2
+
V_\Omega(\Omega)
$$

All terms are non-negative:

$$
\mathcal H \ge 0
$$

ensuring **vacuum stability**.

---

# 11. Low-Energy Limit

In vacuum:

$$
\Omega \rightarrow 0
$$

$$
G \rightarrow 0
$$

The phase equation reduces to

$$
C_0 \ddot\theta
-
\kappa \nabla^2 \theta
=
0
$$

This is a wave equation:

$$
\ddot\theta - c_{eff}^2 \nabla^2\theta = 0
$$

with effective speed

$$
c_{eff} = \sqrt{\kappa/C_0}
$$

Identifying

$$
c_{eff} = c
$$

yields the emergent Lorentz-invariant limit.

---

# 12. Physical Interpretation

| Field | Interpretation |
|------|---------------|
| $\theta$ | background Hum phase |
| $\Omega$ | informational drag |
| $G$ | ghost leakage / vacuum relaxation |

Gravity emerges because **phase gradients accelerate knots embedded in the field**.

---

# 13. Connection to Orbital Dynamics

The orbital mechanics document derives

$$
\lambda = \frac{v^2}{\chi r}
$$

which determines the phase field around astrophysical objects.

This connects the **microscopic Lagrangian** to **macroscopic gravitational motion**.

---

# 14. Summary

The TCWT field theory consists of

- phase field $\theta$
- auxiliary drag field $\Omega$
- ghost leakage field $G$

governed by the Lagrangian

$$
\mathcal L =
C_0(\dot{\theta}-\Omega)^2
+
\kappa (\nabla\theta)^2
+
\alpha (\dot G - \nabla^2\theta)^2
-
V_\Omega(\Omega)
$$

Key consequences:

- wave-like propagation of the phase field  
- conserved phase current  
- bounded energy density  
- emergent gravitational acceleration  

$$
a = -\chi \nabla\theta
$$

which reproduces Newtonian gravity in the appropriate limit.
