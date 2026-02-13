# TCWT Integration Guide for hi_class

This document explains how to add the TimeWave (TCWT) scalar–tensor model
to hi_class by defining the Horndeski/DHOST functions G2, G3, G4 and the
Class I degeneracy function F.

### TCWT Eternal TimeWave – Key Parameters

| Variable            | Value  | Physical Interpretation in TCWT                                                |
|---------------------|--------|-------------------------------------------------------------------------------|
| `phi_initial`       | 1e-2   | **Initial Phase:** Local displacement of the TimeWave when our universe (chestnut) is sampled. |
| `phi_prime_initial` | 1e-5   | **Ambient Velocity:** Pre-existing oscillatory energy; the cosmic “clock” is already ticking. |
| `H0`                | 67.4   | **Hubble Constant:** Sets the expansion rate, here chosen to match Planck 2018. |
| `omega_cdm`         | 0.1200 | **TimeWave Density:** Effective dark-matter density sourced by high-frequency TimeWave oscillations. |
| `gravity_model`     | tcwt   | **Action Selection:** Uses the TCWT DHOST/Beyond-Horndeski sector. |
| `method_linear_perts` | x_functions | **Vainshtein Logic:** Enables derivative-based screening and controlled breaking. |

## 1. Add TCWT to gravity.h

In include/gravity.h:

    typedef enum {
        ...,
        tcwt
    } gravity_model;

Add TCWT parameters to the gravity structure:

    double tcwt_Lambda_scale;
    double tcwt_c3_galileon;
    double tcwt_M_coupling;
    double tcwt_upsilon_breaking;
    short tcwt_apply_degeneracy;

## 2. Register the model in input.c

Add parsing for:

    tcwt_Lambda_scale
    tcwt_c3_galileon
    tcwt_M_coupling
    tcwt_upsilon_breaking
    tcwt_apply_degeneracy

## 3. Implement the model in gravity.c

Add:

    case tcwt:
        gravity_models_tcwt(...);
        break;

Then define the TCWT functions:

    G2 = X - V(phi)
    G3 = c3 * X / Lambda^3
    G4 = M_pl^2/2 + M_coupling * X
    F  = -2 G4_X / G4   (DHOST Class I degeneracy)

## 4. Running TCWT

Use the example configuration:

    examples/tcwt_example.ini

Run with:

    ./class examples/tcwt_example.ini
