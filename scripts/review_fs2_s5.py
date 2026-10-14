"""review_fs2_s5.py (R218, from scratch): FF_STERILE_PUSH §5 reformulation at q = 3. For every Case B tuple (B) with
s = 2n even (enumerated directly from (B)), and c in {1, 2}, compare
  LHS: the tuple covers x*_c, i.e. E ≡ -(1 + cT) (mod T^{n+1})
  RHS: T^n | w1 - c g' v1 (1 + cT) (defines ω), and (S1) T^n | P, (S2) T^{n-2} | P/T^n + c m' g' ω (cT - 1) =: T^{n-2} Ψ,
       (S3) v1 Ψ = -(1 + m' (T ω)^2),  where P = m' g'^2 v1 (1 + cT) + 1.
usage: uv run --with python-flint python scripts/review_fs2_s5.py SMAX"""
import sys
from itertools import product
import flint
p = 3; SMAX = int(sys.argv[1])
Pp = lambda c: flint.nmod_poly(c, p)
T = Pp([0, 1]); one = Pp([1])
def monic(d, cond):
    for low in product(range(p), repeat=d):
        c = list(low) + [1]
        if cond(c): yield Pp(c)
notT = lambda c: c[0] != 0
Tex = lambda c: c[0] == 0 and c[1] != 0
stats = {'tuples': 0, 'lhs': 0, 'rhs': 0, 'mismatch': 0}
for s in range(4, SMAX + 1, 2):
    n = s // 2; Tn = T**n
    for a in range(1, s):
        for b in range(1, s - a + 1):
            z = s - a - b
            for m in (list(monic(z, notT)) if z else [one]):
                for w in monic(a, Tex):
                    for C in monic(b, Tex):
                        v = m * w * C - T**s
                        if v == 0: continue
                        g, rem = divmod(w + C, v)
                        if rem != 0 or g.degree() < 0 or int(g.coeffs()[-1]) != 1 or int(g.coeffs()[0]) == 0: continue
                        stats['tuples'] += 1
                        E = g * m * w - 1
                        v1 = v // T**2; w1 = w // T; C1 = C // T
                        for c in (1, 2):
                            u = one + c * T
                            lhs = (E + u) % T**(n + 1) == 0
                            rhs = False
                            d = w1 - c * g * v1 * u
                            if d % Tn == 0:
                                om = d // Tn
                                assert C1 == -c * g * v1 - Tn * om
                                P = m * g * g * v1 * u + 1
                                if P % Tn == 0:
                                    Q = P // Tn + c * m * g * om * (c * T - 1)
                                    if n >= 2 and Q % T**(n - 2) == 0:
                                        Psi = Q // T**(n - 2)
                                        rhs = v1 * Psi == -(one + m * (T * om)**2)
                            stats['lhs'] += lhs; stats['rhs'] += rhs
                            if lhs != rhs:
                                stats['mismatch'] += 1; print('MISMATCH', s, c, m, w, C, lhs, rhs)
    print(s, stats, flush=True)
