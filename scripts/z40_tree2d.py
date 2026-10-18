# z40_tree2d.py (O270): per-cell refinement tree for the residual of z40_pierpont_cover.py.
# A cell (i, j) mod L (a = i, b = j mod L, a, b >= A0) is lifted along the chain of periods given on the command line;
# each child is tested against divisor classes q | n and ET classes mod M (M = 2^u 3^v M', u, v <= A0, M <= Mmax,
# ord_q(2), ord_q(3) | L' for q | M'). Prints the leaves still open at the end.
# Usage: z40_tree2d.py RESIDUAL_IN.json Mmax A0 L1,L2,... [OUT.json]
import sys, json, functools
import mordell_lib as ML
from sympy import primerange
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
R = json.load(open(sys.argv[1])); Mmax = int(sys.argv[2]); A0 = int(sys.argv[3])
chain = [int(x) for x in sys.argv[4].split(',')]; OUT = sys.argv[5] if len(sys.argv) > 5 and not sys.argv[5].startswith('--') else None
def rep(i, L): return i + L * (64 // L + 2)
@functools.lru_cache(None)
def moduli(L):
    pp = []
    for q in primerange(5, Mmax + 1):
        if pow(2, L, q) == 1 and pow(3, L, q) == 1:
            Q = q
            while Q * q <= Mmax and pow(2, L, Q * q) == 1 and pow(3, L, Q * q) == 1: Q *= q
            pp.append((q, Q))
    odd = [1]
    for q, Q in pp:
        new = []
        for d in odd:
            x = d
            while x * q <= Mmax and Q % (x * q // d) == 0:
                x *= q; new.append(x)
        odd += new
    Ms = sorted({2 ** u * 3 ** v * d for u in range(A0 + 1) for v in range(A0 + 1) for d in odd if 2 < 2 ** u * 3 ** v * d <= Mmax})
    return [q for q, _ in pp], [M for M in Ms if M % 4 in (0, 3)]
import itertools, math
from sympy import n_order, cyclotomic_poly, symbols, Poly
_U = symbols('U')
@functools.lru_cache(None)
def cyc(f): return [int(x) for x in Poly(cyclotomic_poly(2 * f, _U), _U).all_coeffs()[::-1]]
WR = []                       # window rules (i, j, e, w): m = 2^i 3^j w^e - 1 (e odd, or e = 'SG': 2^a3^b = 4*2^i3^j Z^4)
def build_rules(IMAX=8, JMAX=5, WMAX=13, ES=(1, 3, 5, 7)):
    for i in range(2, IMAX + 1):
        for j in range(JMAX + 1):
            for w in range(1, WMAX + 1, 2):
                if w % 3 == 0: continue
                for e in ('SG',) + tuple(ES):
                    m = 2 ** i * 3 ** j * w ** (4 if e == 'SG' else e) - 1
                    if m < 5 or m % 3 == 0 or m > 10 ** 7: continue
                    WR.append((i, j, e, w, m, n_order(2, m), n_order(3, m)))
@functools.lru_cache(None)
def rules_at(L):
    out = []
    for (i, j, e, w, m, o2, o3) in WR:
        E = 4 if e == 'SG' else e
        if L % (E * o2) == 0 and L % (E * o3) == 0: out.append((i, j, e, w, m, o2, o3))
    return out
def win(a, b, L):
    for (i, j, e, w, m, o2, o3) in rules_at(L):
        if e == 'SG':
            if (a - i - 2) % 4 or (b - j) % 4: continue
            Z = pow(2, (a - i - 2) // 4, m) * pow(3, (b - j) // 4, m) % m
            fac = [(2 * Z * Z + 2 * Z * w + w * w) % m, (2 * Z * Z - 2 * Z * w + w * w) % m]
        else:
            if (a - i) % e or (b - j) % e: continue
            Z = pow(2, (a - i) // e, m) * pow(3, (b - j) // e, m) % m
            fac = []
            for f in range(1, e + 1, 2):
                if e % f == 0:
                    co = cyc(f); dg = len(co) - 1
                    fac.append(sum(c * pow(Z, t, m) * pow(w, dg - t, m) for t, c in enumerate(co)) % m)
        at = ([(2, i - 2)] if i > 2 else []) + ([(3, j)] if j else []) + [(x, 1) for x in fac]
        K = (pow(2, a, m) * pow(3, b, m) + 1 + m) * pow(4, -1, m) % m
        if math.gcd(K, m) != 1 or any(math.gcd(x, m) != 1 for x, _ in at): continue
        tgt = (-K) % m
        for ex in itertools.product(*[range(2 * v + 1) for _, v in at]):
            d = 1
            for (x, _), y in zip(at, ex): d = d * pow(x, y, m) % m
            if d == tgt: return ('W', (i, j, e, w, m), ex)
    return None
USEWIN = '--win' in sys.argv
if USEWIN: build_rules(); print('window rules', len(WR), flush=True)
def hit(i, j, L):
    qs, Ms = moduli(L); a, b = rep(i, L), rep(j, L)
    for q in qs:
        if (pow(2, a, q) * pow(3, b, q) + 1) % q == 0: return ('D', q)
    for M in Ms:
        r = (pow(2, a, M) * pow(3, b, M) + 1) % M
        W = ML.residue_table(M)
        if r in W: return (M, W[r])
    if USEWIN: return win(a, b, L)
    return None
L = R['L']; open_ = [tuple(c) for c in R['left']]; log = []
for L2 in chain:
    assert L2 % L == 0; f = L2 // L; nxt = []; nh = 0
    for i, j in open_:
        for u in range(f):
            for v in range(f):
                c = (i + L * u, j + L * v)
                if hit(*c, L2) is None: nxt.append(c)
                else: nh += 1
    print('L=%d: children %d, covered %d, open %d (density %.3g)' % (L2, nh + len(nxt), nh, len(nxt), len(nxt) / L2 ** 2), flush=True)
    log.append((L2, len(nxt))); open_ = nxt; L = L2
    if not open_: break
print('open sample', open_[:20])
if OUT: json.dump({'L': L, 'left': open_, 'log': log}, open(OUT, 'w'))
