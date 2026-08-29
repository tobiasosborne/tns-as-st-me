# Checker outputs

Provenance/scope: the Kähler/TDVP observation is TJO's and requires his
sign-off before any paper use.  These checks concern companion-paper geometry.

## Green

Command:

`python3 theory/lanes/blitz-2026-08-29/kaehler-dh/check_kaehler_dh.py`

```text
G1 sphere: identity=1.304e-13, area/(2pi)-2s=1.377e-14, pushforward-density error=4.441e-15
G2 D16/product: max relative |Omega+mu'|=2.199e-15
G3 period: quadrature-boundary=1.332e-15, finite-window edge error vs 2s=0.000e+00
G4 regularisation: growth exponent=1.956321, |Omega80-Omega40|=0.000e+00
G5 L2 obstruction audit: orbit period=0.0, nonscalar-V distance=1.000000
PASS: all five gates
```

Exit code: `0`.

The same output and exit code were obtained under `python3 -O`.

## Red mutation

Command:

`python3 theory/lanes/blitz-2026-08-29/kaehler-dh/check_kaehler_dh.py --red`

```text
G1 sphere: identity=5.000e-01, area/(2pi)-2s=1.377e-14, pushforward-density error=4.441e-15
G2 D16/product: max relative |Omega+mu'|=1.000e+00
G3 period: quadrature-boundary=1.332e-15, finite-window edge error vs 2s=0.000e+00
G4 regularisation: growth exponent=1.956321, |Omega80-Omega40|=0.000e+00
G5 L2 obstruction audit: orbit period=0.0, nonscalar-V distance=1.000000
RED-OK: calibration mutation caught by G1,G2
```

Exit code: `1`, as required for a caught mutation.
