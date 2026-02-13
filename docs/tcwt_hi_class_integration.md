# TCWT Integration Guide for hi_class

This document explains how to add the TimeWave (TCWT) scalar–tensor model
to hi_class by defining the Horndeski/DHOST functions G2, G3, G4 and the
Class I degeneracy function F.

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
