"""z67 ELL0 (Assessment support, not a proof): exponent bookkeeping for counting I-1 (A) events by dyadic boxes.

A-event at n = ell^{2k-1}: positive integers d', C, C*, s, a' with 4 d' C C* = n + s, C + C* = a' s, C <= C*.
Write d' = n^dl, C = n^g, a' = n^a, s = n^s (dl + g + a + s = 1 up to O(1/log n); g <= a + s).  For each box we take
the cheapest available counting method (exponent of n):
  * residue-trivial: rho = 1 - 4 a'd'C is determined by m = a'd'C <= n/s       -> 1 - s
  * three of (d', C, a', s) fixed determine the rest                          -> 1 - max
  * pair fixed + Lenstra (divisors of X in a residue class mod q, q > X^{1/3}: <= 11):
      (C, d'): t | n + 4d'C^2, t = -1 mod 4d'C        (q^3 > X iff g + dl >= 1/3)
      (C, a'): t | n a' + C,   t = -1 mod 4a'C        (g + a >= (1 + a)/3)
      (a', d'): f | 4 n a'^2 d' + 1, f = -1 mod 4a'd' (a + 2 dl >= 1)
      (d', s): C | M/d' in <= 2^{omega(s)+1} classes mod s (s >= (1 - dl)/3);  (C, s): C* | M/C, class -C mod s
  * with divisor maxima tau <= C(eps) m^eps: any pair + eps*(log-size of the argument); s alone + eps (tau_3).
Prints the worst box (max over boxes of the min cost) without divisor input, with s >= n^0.2, and with tau-maxima.
Usage: python3 scripts/z67_ell0_boxlp.py
"""
import numpy as np

L3 = 1 / 3


def cost(dl, g, a, s, eps=None):
    c = [1 - s, 1 - max(dl, g, a, s)]
    if g + dl >= L3: c.append(g + dl)
    if g + a >= L3 * (1 + a): c.append(g + a)
    if a + 2 * dl >= 1: c.append(a + dl)
    if s >= L3 * (1 - dl): c.append(dl + s)
    if s >= L3 * (1 - g): c.append(g + s)
    if eps is not None:
        c += [g + dl + eps, g + a + eps * (1 + a), a + dl + eps * (1 + 2 * a + dl), dl + s + eps * (1 - dl),
              g + s + eps * (1 - g), a + s + eps, s + 2 * eps]
    return min(c)


def worst(eps=None, smin=0.0, st=1 / 60):
    r = np.arange(0, 1 + 1e-9, st)
    best, arg = -1, None
    for dl in r:
        for g in r:
            for a in r:
                s = 1 - dl - g - a
                if s < smin - 1e-12 or g > a + s + 1e-12:
                    continue
                v = cost(dl, g, a, s, eps)
                if v > best:
                    best, arg = v, (round(dl, 3), round(g, 3), round(a, 3), round(s, 3))
    return best, arg


if __name__ == "__main__":
    print("divisor-free methods only:", worst())
    print("divisor-free, s >= n^0.2 :", worst(smin=0.2))
    for e in (0.0, 0.05, 0.1):
        print(f"with tau-maxima at eps={e}:", worst(eps=e))
