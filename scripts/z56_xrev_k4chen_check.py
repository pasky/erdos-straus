#!/usr/bin/env python3
"""Independent K4CHEN witness audit; no imports from the memo's code.

Run: ulimit -v 6000000 -t 180; timeout 180s env OPENBLAS_NUM_THREADS=1 \
  uv run --with numpy --with scipy python scripts/z56_xrev_k4chen_check.py

The mass calculation encloses the integral by positive log-bin convolution,
not the memo's point-value recursion. Enclosures are exact in real arithmetic;
this implementation uses ordinary floats, NOT certified interval arithmetic.
Arrays have O(n) storage; np.convolve has O(n^2) work and positive summands.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

F1 = 2 * math.sqrt(math.exp(0.5772156649015329) / math.pi)


def lower(s):
    assert 1 <= s <= 3
    return F1 * math.acosh(math.sqrt(s)) / math.sqrt(s)


def upper(s):
    assert 0 < s <= 4
    integral = 0 if s <= 2 else quad(
        lambda t: lower(t - 1) / (2 * math.sqrt(t)),
        2, s, epsabs=2e-13, epsrel=2e-13,
    )[0]
    return (F1 + integral) / math.sqrt(s)


def tail(zeta, j0):
    return sum(math.exp(math.log(F1 / math.sqrt(zeta))
                        + (j - 1) * math.log(math.log(1 / zeta) / 2)
                        - math.lgamma(j + 1)) for j in range(j0, j0 + 300))


def mass_bounds(zeta, n, jmax=26):
    """Integrate one alpha exactly, then bound its kernel on each sum-bin.

    g(H) = integral_zeta^H da / (a sqrt(H-a)). It is zero below zeta,
    increases to its unique maximum H*, and decreases thereafter.
    For each remaining alpha in [t*h,(t+1)*h], the exact measure is
    log1p(1/t). With j-1 factors, a discrete sum index t gives
    H in [1-(t+j-1)*h, 1-t*h]. Positive convolution gives its weight.
    """
    assert abs(zeta * n - round(zeta * n)) < 1e-9
    h = 1 / n
    start = round(zeta * n)
    w = np.zeros(n + 1)
    indices = np.arange(start, n, dtype=float)
    w[start:n] = np.log1p(1 / indices)
    power = np.zeros(n + 1)
    power[0] = 1
    root = brentq(lambda y: y * math.atanh(y) - 1, 0.8, 0.9)
    peak = zeta / (1 - root * root)

    def g(H):
        H = np.asarray(H)
        result = np.zeros_like(H, dtype=float)
        valid = H > zeta
        result[valid] = (2 * np.arctanh(np.sqrt(1 - zeta / H[valid]))
                         / np.sqrt(H[valid]))
        return result

    total_lo = total_hi = 0.0
    for factors in range(1, jmax):
        power = np.convolve(power, w)[:n + 1]
        j = factors + 1
        if j < 8 or j % 2:
            continue
        Hhi = 1 - np.arange(n + 1) * h
        Hlo = Hhi - factors * h
        glo, ghi = g(Hlo), g(Hhi)
        low = np.minimum(glo, ghi)
        high = np.maximum(glo, ghi)
        high[(Hlo <= peak) & (peak <= Hhi)] = float(g(peak))
        scale = F1 * math.sqrt(zeta) / (2**j * math.factorial(j))
        total_lo += scale * float(np.dot(power, low))
        total_hi += scale * float(np.dot(power, high))
    return total_lo, total_hi + tail(zeta, jmax + 1)


def main():
    th1, zeta, lam, pen = 0.45, 0.008, 0.499, 2.35
    s1 = 1.058538888888889
    s2 = (lam - th1 * s1) / zeta
    main_term = lower(s1) * upper(s2) + upper(s1) * lower(s2) - upper(s1) * upper(s2)
    B = upper(1 / th1) - F1 * math.sqrt(th1)
    # Fixed admissible split, deliberately not the source's optimiser.
    a, b = 0.470, 0.029
    T1 = pen * 2 / a * upper(b / zeta) * B
    L = 3 * math.sqrt(3) / lam**1.5
    coefficient = pen * L * F1 * math.sqrt(th1)
    print(f'F1={F1:.12f}; s1={s1:.12f}; s2={s2:.12f}')
    print(f'main={main_term:.12f}; B={B:.12f}; T1_fixed={T1:.12f}; L={L:.12f}')
    print(f'M_ceiling_for_positive_margin={(main_term-T1)/coefficient:.12f}')
    print(f'omitted_j_ge_27_bound={tail(zeta,27):.12g}')
    for n in (2000, 4000, 8000):
        lo, hi = mass_bounds(zeta, n)
        margin = main_term - T1 - coefficient * hi
        print(f'n={n}: real_arithmetic_mass_bracket=[{lo:.12f},{hi:.12f}]; '
              f'lower_margin_float={margin:.12f}', flush=True)


if __name__ == '__main__':
    main()
