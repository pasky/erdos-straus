"""z56 K4LIT — numerical illustration of Lemma P (hidden-prime parity barrier for the
semi-linear sieve on parity-forced sequences).  EVIDENCE only; the lemma is proved in Z56_K4LIT.md §3.

Two sequences supported on n = 1 (mod 4) (parity of Omega_Q forced even, Q = primes = 3 mod 4):
  N  ("natural")  : all n <= xN with n = 1 (mod 4);
  A  ("hidden")   : n = q*m <= x, q in Q, q in (D, 2D], m = 3 (mod 4)  (weight = #such q | n).
Both have sieve data |X_d| = X/d + small for squarefree Q-composed d <= D (A: hidden q > D never divides d).
A contains NO element of S (every element has the Q-prime q).  We report
  * relative sieve-data error for small d,
  * S(seq, z)/(X W(z)) against the semi-linear functions F(s) (upper, parity-even model) and f(s)
    (lower, parity-odd model), s = log(level)/log z,
  * #(seq ∩ S).
Usage: uv run --with numpy python scripts/z56_k4lit_lemmaP.py [log10_x=12] [theta=0.45] [log10_xN=8]
"""
import sys, math
import numpy as np

lx = float(sys.argv[1]) if len(sys.argv) > 1 else 12.0
theta = float(sys.argv[2]) if len(sys.argv) > 2 else 0.45
lxN = float(sys.argv[3]) if len(sys.argv) > 3 else 8.0
x = 10 ** lx
D = x ** theta
xN = int(10 ** lxN)
EG = math.exp(0.5772156649015329)


def F(s):  # semi-linear upper function, 0 < s <= 2 (Iwaniec 1976 Thm 1: 1 + F_I/sqrt s)
    return 2 * math.sqrt(EG / (math.pi * s))


def f(s):  # semi-linear lower function, 1 <= s <= 3 (1 - f_I/sqrt s)
    return math.sqrt(EG / (math.pi * s)) * 2 * math.acosh(math.sqrt(s)) if s >= 1 else 0.0


def primes_upto(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for p in range(2, int(n ** 0.5) + 1):
        if s[p]:
            s[p * p::p] = False
    return np.nonzero(s)[0]


Mmax = int(x / D) + 2
P = primes_upto(max(int(2 * D) + 2, xN + 2))  # all primes up to xN so that W(z) is exact for z <= xN
Q = P[(P % 4 == 3)]
qs = Q[(Q > D) & (Q <= 2 * D)]
X = float(np.sum(x / (4.0 * qs)))


def W(z):
    qq = Q[Q < z]
    return float(np.prod(1.0 - 1.0 / qq))


def rough_mask(n_max, z, cls):
    """bool array over m in [0, n_max]: m odd, m = cls (mod 4), no Q-prime factor < z."""
    m = np.zeros(n_max + 1, dtype=bool)
    m[cls::4] = True
    for q in Q[Q < z]:
        q = int(q)
        if q > n_max:
            break
        m[q::q] = False
    return m


out = []
out.append(f"x=1e{lx}, D=x^{theta}={D:.4g}, #hidden q in (D,2D]: {len(qs)}, X=sum x/(4q)={X:.6g}; natural xN=1e{lxN}")
# sieve-data check for A at small Q-composed d
ms = np.arange(Mmax + 1)
cls3 = (ms % 4 == 3)
cum3 = np.cumsum(cls3)
lim = np.floor(x / qs).astype(np.int64)
errs = []
for d in [3, 7, 11, 19, 21, 23, 31, 33, 43, 57, 77, 231, 3 * 7 * 11 * 19]:
    if any((int(p) % 4 == 1) or (d % (int(p) ** 2) == 0) for p in P[P <= d] if d % int(p) == 0):
        continue
    c = np.cumsum(cls3 & (ms % d == 0))
    Ad = float(np.sum(c[lim]))
    errs.append((d, Ad / (X / d) - 1))
out.append("A: sieve data relative error |A_d|/(X/d)-1: " + ", ".join(f"d={d}:{e:+.2e}" for d, e in errs))
out.append("   (bound: |r_d| <= #q, so sum_{d<=D}|r_d|/X <= D*#q/X = %.3g)" % (D * len(qs) / X))
out.append("")
out.append(" s     z(A)       | A: S(A,z)/(X W)  f(s)    f(s')  s'   F(s)  | N: S(N,zN)/(XN W)  F(s)  | #A∩S")
for s in [1.0, 1.1, 1.25, 1.5, 2.0]:
    z = D ** (1.0 / s)
    rm = rough_mask(Mmax, z, 3)
    c = np.cumsum(rm)
    SA = float(np.sum(c[lim]))
    sA = SA / (X * W(z))
    sp = math.log(x / (1.5 * D)) / math.log(z)   # parity-odd model parameter of the m-variable
    zN = xN ** (1.0 / s)                          # natural sequence at the same s = log(size)/log z
    rN = rough_mask(xN, zN, 1)
    SN = float(rN.sum()); XN = xN / 4.0
    out.append(f" {s:4.2f} {z:10.4g}  |  {sA:8.4f}       {f(s):6.4f}  {f(sp):6.4f} {sp:4.2f}  {F(s):6.4f} |  {SN/(XN*W(zN)):8.4f}        {F(s):6.4f} |  0")
# S-count in N (all Q-free n = 1 mod 4 up to xN): sieve to sqrt
rS = rough_mask(xN, xN ** 0.5 + 1, 1)
out.append(f"N: #(N ∩ S) = {int(rS.sum())} of {xN//4} (S-members are exactly the sqrt-rough elements); A ∩ S = ∅ by construction")
print("\n".join(out))
