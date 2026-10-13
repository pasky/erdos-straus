"""O181 DRINFELD_ES §1: check Prop 1.2 / Thm 1.3 (k-th power law of Type II moduli over F_p[T]) and the
T1_k control (Type II data at P = Q^k composite).
usage: bsH_kpower_law.py p gen k A(high->low digits) n [mode]
  mode 'irr' (default): all irreducible P of degree n;  mode 'pow': all P = Q^k (Q irreducible, k*deg Q = n),
  and also P = Q^2 if 2 | n.
Prints: #data, #mismatches of (P/f)_k vs formula, distribution of (f/P)_k, control distribution of (g/P)_k for
random monic g of the same degrees."""
import sys, random
from bsH_ff import FF

p, gen, k = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
Adig = sys.argv[4]
n = int(sys.argv[5])
mode = sys.argv[6] if len(sys.argv) > 6 else 'irr'
F = FF(p)
A = tuple(int(c) for c in reversed(Adig))
kA = len(A) - 1
eps = (-1) ** ((p - 1) // k)


def typeII_data(P):
    out = []
    for da in range(0, n - kA + 1):
        for db in range(0, n - kA - da + 1):
            for a in F.monics(da):
                for b in F.monics(db):
                    if F.gcd(a, b) != (1,):
                        continue
                    s = F.add(a, b)
                    if not s:
                        continue
                    for c in F.monic_divisors(F.scal(pow(s[-1], p - 2, p), s)):
                        E = F.divmod(s, c)[0]
                        if len(E) - 1 >= n:
                            continue
                        Aab = F.mul(A, F.mul(a, b))
                        d, r = F.divmod(F.add(P, E), Aab)
                        if r or not d or d[-1] != 1:
                            continue
                        out.append((a, b, c, d, E))
    return out


def check(P, stats, rng):
    for a, b, c, d, E in typeII_data(P):
        f = F.sub(F.mul(A, F.mul(a, F.mul(c, d))), (1,))
        # identity checks
        assert F.mul(E, f) == F.add(P, F.mul(A, F.mul(a, F.mul(a, d))))
        X = F.mul(a, F.mul(b, d)); Y = F.mul(F.mul(a, c), F.mul(d, P)); Z = F.mul(F.mul(b, c), F.mul(d, P))
        # A*XYZ == P*(XY+YZ+ZX)
        lhs = F.mul(A, F.mul(X, F.mul(Y, Z)))
        rhs = F.mul(P, F.add(F.add(F.mul(X, Y), F.mul(Y, Z)), F.mul(Z, X)))
        assert lhs == rhs
        stats['data'] += 1
        if len(f) == 1:
            continue
        s = F.psym(P, f, k, gen)
        if s is None:
            stats['noncoprime'] += 1
            continue
        df, dAd = len(f) - 1, len(F.mul(A, d)) - 1
        pred = 0 if eps == 1 or ((1 + df) * (1 + dAd) - 1) % 2 == 0 else k // 2
        if s != pred:
            stats['mismatch'] += 1
        t = F.psym(f, P, k, gen)
        stats['fP'][t] = stats['fP'].get(t, 0) + 1
        g = tuple(rng.randrange(p) for _ in range(df)) + (1,)
        u = F.psym(g, P, k, gen)
        if u is not None:
            stats['ctl'][u] = stats['ctl'].get(u, 0) + 1


rng = random.Random(1)
if mode == 'irr':
    Ps = [('irr', P) for P in F.irreds(n) if F.mod(P, A)]
else:
    Ps = []
    for e in (k, 2):
        if n % e == 0:
            Ps += [('Q^%d' % e, F.mul(*([Q] * 2)) if e == 2 else _pw) for Q in F.irreds(n // e)
                   for _pw in [Q if e == 1 else None] if False]
    # build powers explicitly
    Ps = []
    for e in sorted({k, 2}):
        if n % e:
            continue
        for Q in F.irreds(n // e):
            P = (1,)
            for _ in range(e):
                P = F.mul(P, Q)
            if F.mod(P, A):
                Ps.append(('Q^%d' % e, P))
groups = {}
for lab, P in Ps:
    st = groups.setdefault(lab, {'P': 0, 'Pzero': 0, 'data': 0, 'mismatch': 0, 'noncoprime': 0, 'fP': {}, 'ctl': {}})
    before = st['data']
    check(P, st, rng)
    st['P'] += 1
    if st['data'] == before:
        st['Pzero'] += 1
for lab, st in groups.items():
    print(f"p={p} k={k} A={Adig} n={n} {lab}: #P={st['P']} #P_with_no_TypeII={st['Pzero']} #data={st['data']} "
          f"mismatch={st['mismatch']} noncoprime={st['noncoprime']} (f/P)_k dist={sorted(st['fP'].items())} "
          f"control={sorted(st['ctl'].items())}")
