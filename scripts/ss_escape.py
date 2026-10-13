"""O188 STERILE_STEER §2: which ET classes certify primes near a sterile point?

Builds, once, the residue sets R[M] of all seven ET Prop 1.9 families for every modulus M <= X
(own enumeration, cross-checked against mordell_lib.residue_set for M <= CHECK).
For each prime p reports: the least modulus M of an ET class containing p (Mordell height h(p)),
and the least *escape modulus* E(M,p) = prod_{q^v || M, q^v not | p-1} q^v over classes with M <= X
(Lemma 1.1), plus the witness. Every reported witness class is re-solved at p by mordell_lib.solve.

usage: PYTHONPATH=scripts uv run python scripts/ss_escape.py X NPRIMES SEED [B=23]
"""
import sys, random, pickle, os
from math import gcd
import sympy
import mordell_lib as ml

X = int(sys.argv[1]); NP = int(sys.argv[2]); SEED = int(sys.argv[3]); B = int(sys.argv[4]) if len(sys.argv) > 4 else 23
CHECK = 600


def build(X):
    R = [dict() for _ in range(X + 1)]  # residue -> (fam, params)

    def add(M, r, w):
        if M <= X and r % M not in R[M]:
            R[M][r % M] = w
    # II2: f = M = 3 mod 4, ad | (f+1)/4, residue -4a^2d mod f
    for f in range(3, X + 1, 4):
        A = (f + 1) // 4
        for a in sympy.divisors(A):
            for d in sympy.divisors(A // a):
                add(f, -4 * a * a * d, ('II2', (a, d, f)))
    Qmax = X // 4
    for a in range(1, Qmax + 1):
        for b in range(1, Qmax // a + 1):
            M = 4 * a * b
            # I1 (a,d=b,f): f | 4a^2 b + 1, residue -f mod 4ab
            for f in sympy.divisors(4 * a * a * b + 1):
                add(M, -f, ('I1', (a, b, f)))
            # I4 / II1 (a,b,e): e | a+b, gcd(e,4ab)=1
            for e in sympy.divisors(a + b):
                if gcd(e, M) == 1:
                    add(M, -e, ('II1', (a, b, e)))
                    add(M, -pow(e, -1, M), ('I4', (a, b, e)))
    # I2 (x=a,y=c,z=f), I3 (c,d,f), II3 (a,d,e): modulus 4xyz, gcd(z, 4xy)=1
    for z in range(1, Qmax + 1):
        for x in range(1, Qmax // z + 1):
            for y in range(1, Qmax // (z * x) + 1):
                if gcd(z, 4 * x * y) != 1:
                    continue
                M = 4 * x * y * z
                for fam in ('I2', 'I3', 'II3'):
                    MM, res = ml.cls_modulus_residues(fam, (x, y, z))
                    assert MM == M
                    for r in res:
                        add(M, r, (fam, (x, y, z)))
    return R


cache = f'/tmp/ss_R_{X}.pkl'
if os.path.exists(cache):
    R = pickle.load(open(cache, 'rb'))
else:
    R = build(X)
    for M in range(1, min(CHECK, X) + 1):
        assert set(R[M]) == ml.residue_set(M), M
    pickle.dump(R, open(cache, 'wb'))
print('table built; total residues', sum(len(t) for t in R), flush=True)


def escape(M, p):
    E = 1
    for q, v in sympy.factorint(M).items():
        if (p - 1) % q ** v:
            E *= q ** v
    return E


def scan(p):
    h = None; best = None
    for M in range(2, X + 1):
        t = R[M]
        if t and p % M in t:
            if h is None:
                h = M
            E = escape(M, p)
            if best is None or E < best[0]:
                best = (E, M, t[p % M])
    for (E, M, w) in ([best] if best else []):
        assert ml.solve(w[0], w[1], p) is not None, (p, w)
    return h, best


r, u, L = 17, 5, 4
Qb = int(sympy.ilcm(*range(1, B + 1))) // 17 ** sympy.multiplicity(17, int(sympy.ilcm(*range(1, B + 1))))  # lcm(1..B) without 17
rng = random.Random(SEED)


def prime_in(mod, res, lo):
    while True:
        k = rng.randrange(lo // mod, 2 * lo // mod)
        p = k * mod + res
        if sympy.isprime(p):
            return p


def crt(a1, m1, a2, m2):
    return int(sympy.ntheory.modular.crt([m1, m2], [a1, a2])[0])


lo = max(10**16, Qb * r**L * 1000)
cats = {
    'A_near_x5': (Qb * r**L, crt(1, Qb, u, r**L)),
    'B_near_1': (Qb * r**L, 1),
    'C_hard_nonsterile': None,   # p = 1 mod Qb, p mod 17 random non-residue (not 5 mod 17^4)
    'D_random_1mod24': (24, 1),
}
NR = [v for v in range(1, 17) if pow(v, 8, 17) == 16]
for name, spec in cats.items():
    rows = []
    for i in range(NP):
        if spec is None:
            v = rng.choice(NR); mod, res = Qb * r, crt(1, Qb, v, r)
        else:
            mod, res = spec
        p = prime_in(mod, res, lo)
        h, best = scan(p)
        E, M, w = best if best else (None, None, None)
        bigq = max(sympy.factorint(E)) if E else None
        rows.append((p, h, E, M, w, bigq))
        print(name, p, 'h=', h, 'E=', E, 'M=', M, w, 'maxq(E)=', bigq, flush=True)
    hs = sorted(x[1] for x in rows if x[1]); Es = sorted(x[2] for x in rows if x[2])
    miss = sum(1 for x in rows if x[1] is None)
    print(f'SUMMARY {name}: n={NP} none<=X: {miss}  median h={hs[len(hs)//2] if hs else None}  '
          f'median E={Es[len(Es)//2] if Es else None}', flush=True)
