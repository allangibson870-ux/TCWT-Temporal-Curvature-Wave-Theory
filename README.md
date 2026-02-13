# TCWT: Temporal Curvature Wave Theory  
### A Scalar–Tensor TimeWave Dark Matter Framework with Vainshtein Screening

Temporal Curvature Wave Theory (TCWT) is a scalar–tensor cosmological model in which a single scalar field \(\phi\) generates a coherent “TimeWave.”  
This oscillatory field behaves as ultra-light dark matter while modifying the growth of structure through additional friction terms.  

TCWT is constructed within **DHOST Class I**, the only surviving branch of scalar–tensor gravity compatible with the GW170817 constraint on the speed of gravitational waves.

This repository provides:
- The theoretical foundations of TCWT  
- A Vainshtein screening mechanism ensuring local viability  
- Example `.ini` files for running TCWT in **hi_class/CLASS**  
- A roadmap for numerical implementation and testing  

---

## 📘 Documentation

All documentation is located in the `docs/` directory:

- **TCWT Theory Overview**  
  [`docs/tcwt_theory.md`](docs/tcwt_theory.md)

- **Vainshtein Screening & Local Viability**  
  [`docs/tcwt_screening.md`](docs/tcwt_screening.md)

- **hi_class Integration Guide**  
  [`docs/tcwt_hi_class_integration.md`](docs/tcwt_hi_class_integration.md)

These documents explain the action, perturbation structure, screening mechanism, and how to integrate TCWT into hi_class.

---

## 🧪 Example hi_class Configuration Files

Example `.ini` files are provided in the `examples/` directory:

- **Standard TCWT cosmology run**  
  [`examples/tcwt_example.ini`](examples/tcwt_example.ini)

- **Cluster-scale Vainshtein-breaking test**  
  [`examples/tcwt_cluster_test.ini`](examples/tcwt_cluster_test.ini)

These files define:
- TCWT scalar-field parameters  
- DHOST Class I degeneracy condition (ensuring \(c_{\rm GW} = c\))  
- Vainshtein screening parameters  
- Output settings for CMB and matter power spectra  

To run:




