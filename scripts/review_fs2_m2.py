"""review_fs2_m2.py (R218, from scratch): checks the M2-repair claim of FF_STERILE_PUSH §5(b): over F_3, s = 3^h + 1,
v1 = -1 (v = -T^2), the number of Case B tuples is exp(Ω(s/log s)), e.g. >= 7.8e10 at s = 244.
With v1 = -1: m' w1 C1 = T^{s-2} - 1 (product of all monic irreducibles of degree | h except T), lc(v) = 2 forces
deg w = deg C (a = b), and g' = -(w1 + C1)/T is a monic polynomial prime to T iff w1(0) + C1(0) = 0 and
w1'(0) + C1'(0) != 0. Exact count by dynamic programming over the factors, tracking (deg w1 - deg C1, w1(0), C1(0),
w1'(0)/w1(0), C1'(0)/C1(0)); cross-checked against direct enumeration for h = 2, 3.
usage: uv run --with python-flint python scripts/review_fs2_m2.py"""
import flint
from collections import defaultdict
from itertools import product
p = 3
def factors(h):
    F = flint.nmod_poly([p - 1] + [0] * (p**h - 2) + [1], p)  # T^{3^h - 1} - 1
    lc, fac = F.factor()
    assert all(e == 1 for _, e in fac)
    return [f for f, _ in fac]
def inv(x): return pow(x, -1, p)
def dp_count(h):
    fs = factors(h)
    st = defaultdict(int); st[(0, 1, 1, 0, 0)] = 1    # (dw - dC, w(0), C(0), w'(0)/w(0), C'(0)/C(0))
    for f in fs:
        c = [int(x) for x in f.coeffs()] + [0]
        f0, f1, df = c[0], c[1], f.degree(); L = f1 * inv(f0) % p
        new = defaultdict(int)
        for (dd, w0, c0, lw, lc_), k in st.items():
            new[(dd, w0, c0, lw, lc_)] += k                                        # to m'
            new[(dd + df, w0 * f0 % p, c0, (lw + L) % p, lc_)] += k                # to w1
            new[(dd - df, w0, c0 * f0 % p, lw, (lc_ + L) % p)] += k                # to C1
        st = new
    tot = 0
    for (dd, w0, c0, lw, lc_), k in st.items():
        if dd == 0 and (w0 + c0) % p == 0 and (w0 * lw + c0 * lc_) % p != 0:
            tot += k
    return tot, len(fs)
def brute(h):
    fs = factors(h); s = p**h + 1; T = flint.nmod_poly([0, 1], p); cnt = 0
    for asg in product(range(3), repeat=len(fs)):
        parts = [flint.nmod_poly([1], p) for _ in range(3)]
        for f, j in zip(fs, asg): parts[j] *= f
        m, w1, C1 = parts
        if w1.degree() != C1.degree(): continue
        w, C = T * w1, T * C1; v = m * w * C - T**s
        g, r = divmod(w + C, v)
        if r == 0 and int(g.coeffs()[-1]) == 1 and int(g.coeffs()[0]) != 0: cnt += 1
    return cnt
for h in (2, 3):
    print('h', h, 's', p**h + 1, 'DP', dp_count(h), 'brute', brute(h))
for h in (4, 5):
    tot, nf = dp_count(h); print('h', h, 's', p**h + 1, 'factors', nf, 'DP count (all a = b, v1 = -1)', tot, f'{tot:.3e}')
