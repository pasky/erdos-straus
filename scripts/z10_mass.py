"""O234: class mass of the full overflow cube at prime moduli, per cap e (Sections 2-3).
omega_e(l) = #{V = c0^2 d0 R^2 < l/4 : c0,d0 odd sqfree coprime, c0 d0 | K=(l+1)/4, rad R | c0, v_s(R) <= e}
(distinct V <-> distinct classes -4V mod l).  Prints S_e(X) = sum_{l<=X, l=3 mod 4} omega_e(l)/l at dyadic X,
for e = 0..emax and e = inf (=99).  usage: z10_mass.py X emax"""
import sys
from sympy import primerange, factorint
X, emax = int(sys.argv[1]), int(sys.argv[2])
caps = list(range(emax + 1)) + [99]
S = {e: 0.0 for e in caps}
def count(odd, bound, e):
    # local options per prime s: d0 (factor s), c0 with R-exponent rho (factor s^(2+2rho)), or absent
    vals = [1]
    for s in odd:
        new = []
        for v in vals:
            new.append(v)
            if v * s < bound: new.append(v * s)
            w = v * s * s; r = 0
            while w < bound and r <= e:
                new.append(w); w *= s * s; r += 1
        vals = new
    return len(vals)
nxt = 2 ** 10
for l in primerange(3, X + 1):
    if l % 4 != 3: continue
    while l > nxt:
        print(nxt, " ".join(f"{S[e]:.3f}" for e in caps)); nxt *= 2
    odd = [s for s in factorint((l + 1) // 4) if s != 2]
    for e in caps:
        S[e] += count(odd, l / 4, e) / l
print(X, " ".join(f"{S[e]:.3f}" for e in caps))
