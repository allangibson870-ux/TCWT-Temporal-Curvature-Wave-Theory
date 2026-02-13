# TCWT Contributor Checklist  
### Integrating the TCWT `.ini` Parameters into hi_class

This checklist describes the exact steps required to integrate the TCWT model into hi_class so that the example `.ini` files in `/examples` are fully functional.

---

## ✔ 1. Add TCWT to the gravity model enum

In `include/gravity.h`, add:

```c
typedef enum {
    ...,
    tcwt
} gravity_model;
