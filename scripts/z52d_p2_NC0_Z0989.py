"""Z0989: resultants between two exact ES identity families for n = 4k+1.
Step 1 (ansatz): n(k) = m k + r (m <= 12, 1 <= r <= m, gcd(m,r)=1), x = a1 k + a0, y = b1 k + b0 (integers in [-R,R], R=3);
        z := n x y / (4xy - n(x+y)) must be a
        polynomial in k (checked exactly: z(k) integer-valued at k=1..12 and degree <= 3 by finite differences).
        Positive families for k >= 1 are kept.  (Degree-2 all-coefficient search without denominators found nothing.)
Step 2: for pairs of families, resultants in k of the coordinate differences (x_a-x_b, y_a-y_b, z_a-z_b); a zero
        resultant means the two families share a denominator at a common (complex) k; integer roots >= 1 are reported.
Output: data/z52b/pass2/NC0/sub/Z0989_resultants.json
Run: ulimit -v 4000000; uv run --with sympy python scripts/z52d_p2_NC0_Z0989.py
"""
import itertools, json, os
from fractions import Fraction as Fr
import sympy as sp
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
k = sp.symbols('k')
R = 3
def is_poly_int(vals):
    # vals: list of Fractions at k=1..len; must be integers and finite differences vanish beyond degree 3
    if any(v.denominator != 1 for v in vals): return False
    d = [int(v) for v in vals]
    for _ in range(4):
        d = [d[i + 1] - d[i] for i in range(len(d) - 1)]
    return all(x == 0 for x in d[:len(d)])  # degree <= 3 fits 12 points easily
import math
fams = []
MR = []  # (m,r) pairs
for m in range(1, 13):
    for r in range(1, m + 1):
        if math.gcd(m, r) == 1: MR.append((m, r))
def fam_search(m, r, a1, a0, b1, b0):
    ok = True; zs = []
    for kv in range(1, 13):
        n = m * kv + r; x = a1 * kv + a0; y = b1 * kv + b0
        if x <= 0 or y <= 0: ok = False; break
        den = 4 * x * y - n * (x + y)
        if den <= 0: ok = False; break
        zs.append(Fr(n * x * y, den))
    if not ok: return None
    if not is_poly_int(zs): return None
    pts = [(kv, int(zs[kv - 1])) for kv in range(1, 5)]
    z = sp.expand(sp.interpolate(pts, k))
    if any(z.subs(k, kv) != int(zs[kv - 1]) for kv in range(1, 13)): return None
    x = a1 * k + a0; y = b1 * k + b0; nk = m * k + r
    assert sp.expand(4 * x * y * z - nk * (x * y + y * z + z * x)) == 0
    return (sp.expand(x), sp.expand(y), sp.expand(z), nk)
for (m, r) in MR:
    for a1, a0, b1, b0 in itertools.product(range(-R, R + 1), repeat=4):
        if (a1 == 0 and a0 == 0) or (b1 == 0 and b0 == 0): continue
        g = fam_search(m, r, a1, a0, b1, b0)
        if g: fams.append(g)
# dedupe by sorted triple of expressions
uniq = {}
for f in fams:
    key = tuple(sorted(str(t) for t in f[:3])) + (str(f[3]),)
    uniq.setdefault(key, f)
fams = list(uniq.values())
fams_by_n = {}
for f in fams: fams_by_n.setdefault(str(f[3]), []).append(f)
print('n(k) classes with families:', {kk: len(v) for kk, v in fams_by_n.items()})
out = {'n_polynomial_families_found (x,y linear; z poly)': len(fams), 'n_classes': {kk: len(v) for kk, v in fams_by_n.items()}, 'families': [[str(t) for t in f] for f in fams[:30]]}
print('families:', len(fams))
for f in fams[:12]: print([str(t) for t in f])
fams_full = list(fams)
fams = [f[:3] for f in fams]
# Step 2 (correct comparison): the families live on different progressions n = m k + r, so compare them at a COMMON n:
# k_A = (n - r_A)/m_A, k_B = (n - r_B)/m_B. Denominators of A and B as functions of n; coincidences = roots n in the
# joint progression (n = r_A mod m_A and n = r_B mod m_B, n>1). Resultant in n of the two coincidence equations.
nn = sp.symbols('n')
Mr = {}
for f_ in fams_full: Mr[str(f_[3])] = f_
res = []
keysn = list(Mr.keys())
for A_key, B_key in itertools.combinations(keysn, 2):
    FA, FB = Mr[A_key], Mr[B_key]
    mA, rA = [int(t) for t in str(FA[3]).replace('*k', '').replace(' ', '').split('+')] if '+' in str(FA[3]) else (None, None)
    mB, rB = [int(t) for t in str(FB[3]).replace('*k', '').replace(' ', '').split('+')] if '+' in str(FB[3]) else (None, None)
    kA = (nn - rA) / sp.Integer(mA); kB = (nn - rB) / sp.Integer(mB)
    dA = [sp.expand(t.subs(k, kA)) for t in FA[:3]]; dB = [sp.expand(t.subs(k, kB)) for t in FB[:3]]
    eqs = {}
    for ia, a in enumerate(dA):
        for ib, b in enumerate(dB):
            e = sp.together(a - b); num = sp.numer(e)
            if num != 0 and sp.degree(sp.Poly(num, nn), nn) >= 0:
                eqs[f'x{ia}=y{ib}'] = sp.factor(num)
    sols = {}
    for kk, e in eqs.items():
        rts = sp.roots(sp.Poly(e, nn))
        sols[kk] = [str(r_) for r_ in rts.keys() if r_.is_integer and r_ > 1 and (int(r_) - rA) % mA == 0 and (int(r_) - rB) % mB == 0]
    res.append(dict(A=[str(t) for t in FA], B=[str(t) for t in FB], joint_n_coincidences={a: b for a, b in sols.items() if b},
                    n_equations=len(eqs), example_equations={a: str(b) for a, b in list(eqs.items())[:4]}))
out['pairs'] = len(res)
out['pairs_with_common_n_coincidence'] = sum(1 for r in res if r['joint_n_coincidences'])
out['examples'] = res[:10]
json.dump(out, open(ROOT + '/data/z52b/pass2/NC0/sub/Z0989_resultants.json', 'w'), indent=1)
print('pairs', out['pairs'], 'common-n coincidences', out['pairs_with_common_n_coincidence'])
for r in res[:5]: print(r)
