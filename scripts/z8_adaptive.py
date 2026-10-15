# z8_adaptive.py — adaptive exponent covering for n_s = c0*4^s + k.  Starts from a covering at L0 (ec_cover sets with
# admissible moduli <= Mmax0), then repeatedly takes an uncovered residue u mod L and adds an ET/divisor class
# (modulus <= Mmax, ANY modulus) containing n_s at a representative s = u (mod L); L grows to lcm(L, L_M) with
# L_M = lcm of ord_{q^e}(4) over the odd prime powers of M.  Preference: classes with L_M | L covering most of U.
# Usage: PYTHONPATH=scripts uv run python scripts/z8_adaptive.py c0 k L0 Mmax0 Mmax LCAP [out.json]
import sys, json, functools
from math import lcm
import mordell_lib as ML
import ec_cover as EC
from sympy import n_order, factorint, isprime
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
c0, k, L, Mmax0, Mmax, LCAP = map(int, sys.argv[1:7])
GMAX = 30


@functools.lru_cache(None)
def LM(M):
    out = 1
    for q, e in factorint(M).items():
        if q != 2: out = lcm(out, n_order(4, q ** e))
    return out


def nval(s, M):  # s: exponent residue mod L; representative with large s
    S = s + 64 * LM(M) if s < 64 else s  # ensure 2S >= v2(M); n mod M depends on S mod LM(M) only
    return (c0 * pow(4, S, M) + k) % M


classes = []  # (M, fam, params, set of residues mod M covered)
Ms = sorted([M for M in range(3, Mmax + 1) if M % 4 in (0, 3)])
primes = [q for q in range(3, 20000) if isprime(q)]


def covered(s):
    for M, fam, P, R in classes:
        if nval(s, M) in R: return True
    return False


# seed: all classes found by ec_cover's greedy cover of the coverable part at L0 (rerun with restrict to coverable)
import itertools
from ec_screen import admissible_prime_powers
sets = []
for q, Q in admissible_prime_powers(4, L, QMAX=Mmax0):
    if q > 2:
        st = {m for m in range(L) if nval(m, q) == 0}
        if st: sets.append((q, ('D', (q,)), st))
for M in EC.candidate_moduli(c0, 4, k, L, Mmax0):
    if M % 4 and M % 4 != 3: continue
    W = ML.residue_table(M); cv = {}
    for m in range(L):
        r = nval(m, M)
        if r in W: cv.setdefault(W[r], set()).add(m)
    for cls, st in cv.items(): sets.append((M, cls, st))
unc = set().union(*[st for _, _, st in sets]) if sets else set()
seed = []
while unc:
    M, cls, st = max(sets, key=lambda t: (len(unc & t[2]), -t[0]))
    seed.append((M, cls, st)); unc -= st
for M, cls, s in seed:
    fam, P = cls
    R = {0} if fam == 'D' else set(ML.cls_modulus_residues(fam, P)[1])
    classes.append((M, fam, P, R))
it = 0
U = [s for s in range(L) if not covered(s)]
while True:
    print('iter %d L=%d classes=%d uncovered=%d %s' % (it, L, len(classes), len(U), U[:8]), flush=True)
    if not U: break
    it += 1
    best = None
    sample = U[:12]
    cands = {}
    for u in sample:
        for q in primes:
            if nval(u, q) == 0: cands[(q, 'D', (q,))] = {0}
        for M in Ms:
            W = ML.residue_table(M); r = nval(u, M)
            if r in W and (M,) + tuple(W[r][:1]) not in cands:
                fam, P = W[r]
                cands[(M, fam, P)] = None
    for (M, fam, P) in cands:
        g = lcm(L, LM(M)) // L
        if g > GMAX or g * len(U) > 400000: continue
        R = {0} if fam == 'D' else set(ML.cls_modulus_residues(fam, P)[1])
        cov = sum(1 for u in U for x in range(u, u + g * L, L) if nval(x, M) in R)
        key = (-cov / g, g, M)
        if best is None or key < best[0]: best = (key, (M, fam, P, R))
    if best is None:
        print('no candidate class with M <= %d' % Mmax); sys.exit(1)
    M, fam, P, R = best[1]
    if fam != 'D': R = set(ML.cls_modulus_residues(fam, P)[1])
    classes.append((M, fam, P, R))
    g = lcm(L, LM(M)) // L
    U = [x for u in U for x in range(u, u + g * L, L) if nval(x, M) not in R]
    L = L * g
    print('  add M=%d %s %s (L_M=%d) -> L=%d' % (M, fam, P, LM(M), L), flush=True)
    if L > LCAP:
        print('L cap exceeded'); sys.exit(1)
if len(sys.argv) > 7:
    chosen = [(M, (fam, P), sorted(s for s in range(L) if nval(s, M) in R)) for M, fam, P, R in classes]
    chosen = [c for c in chosen if c[2]]
    json.dump(EC.certificate(c0, L, chosen, 4, k), open(sys.argv[7], 'w'))
    print('certificate written', sys.argv[7])
