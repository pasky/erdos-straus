# z11_cantor.py — cover the binary Cantor core C_S = prod_{l in S} {P_A, P_B} of the exponent space of n_s = c0*4^s + k
# (P_A, P_B integer exponents, e.g. 4 and -2 for k = 105: square points 19^2 and (41/4)^2).
# On C the l-adic component is exact, so a class of modulus M = 2^a M' meets C in a cylinder over supp(L_M): for each
# pattern on supp(L_M) the value n mod M is determined.  Classes: ET families (mordell_lib.residue_table) and divisor
# classes D_q, with odd prime powers Q <= QMAX whose ord_Q(4) is S-smooth.  Reports the uncovered patterns in {A,B}^S.
# Usage: PYTHONPATH=scripts uv run python scripts/z11_cantor.py c0 k LMAX QMAX MMAX LABELS(comma list) [-v] [-g]
# (labels = the integer square points, e.g. 4,-2,2,3 for k = 105; patterns are |LABELS|^|S|)
import sys, time, functools, itertools
from math import lcm
from collections import defaultdict
import numpy as np
from sympy import n_order, factorint, primerange
from sympy.ntheory.modular import crt
import mordell_lib as ML

c0, k, LMAX, QMAX, MMAX = map(int, sys.argv[1:6])
LAB = [int(x) for x in sys.argv[6].split(',')]  # label values, e.g. 4,-2,2,3
NL = len(LAB)
S = list(primerange(2, LMAX + 1))
idx = {l: i for i, l in enumerate(S)}
t0 = time.time()

pps = []  # (q, Q, o, supp)
for q in primerange(3, QMAX + 1):
    if (c0 * 4) % q == 0: continue
    Q = q
    while Q <= QMAX:
        o = n_order(4, Q)
        f = factorint(o)
        if any(l not in idx for l in f): break
        pps.append((q, Q, o, tuple(sorted(f))))
        Q *= q
print('S =', S, ' admissible prime powers:', len(pps), flush=True)


def mu_mod(o, pat):  # pat: dict l -> 0/1
    f = factorint(o)
    if not f: return 0
    ms = [l ** e for l, e in f.items()]
    rs = [LAB[pat[l]] % (l ** e) for l, e in f.items()]
    return int(crt(ms, rs)[0])


def nmod(M, a, parts, pat):
    # n mod M for s large in the class of the pattern; parts = [(Q, o)]
    ms, rs = [], []
    if a: ms.append(2 ** a); rs.append(k % 2 ** a)
    for Q, o in parts:
        ms.append(Q); rs.append((c0 * pow(4, mu_mod(o, pat), Q) + k) % Q)
    return int(crt(ms, rs)[0])


cov = defaultdict(set)  # support tuple -> set of covered patterns (tuples of bits)
wit = {}
odd = [(1, (), ())]  # (M', parts, supp)
byq = defaultdict(list)
for q, Q, o, sp in pps: byq[q].append((Q, o, sp))
for q in sorted(byq):
    new = []
    for m, parts, sp in odd:
        for Q, o, sq in byq[q]:
            if m * Q <= MMAX: new.append((m * Q, parts + ((Q, o),), tuple(sorted(set(sp) | set(sq)))))
    odd += new
print('odd parts', len(odd), flush=True)
nM = 0
for m, parts, sp in odd:
    for a in (0, 2, 3, 4, 5, 6, 7):
        M = 2 ** a * m
        if M > MMAX or M < 3 or (a == 0 and M % 4 != 3): continue
        W = ML.residue_table(M)
        if not W: continue
        nM += 1
        for bits in itertools.product(range(NL), repeat=len(sp)):
            pat = dict(zip(sp, bits))
            r = nmod(M, a, parts, pat)
            if r in W and bits not in cov[sp]:
                cov[sp].add(bits); wit[(sp, bits)] = (M, r, W[r])
# divisor classes
for q, Q, o, sp in pps:
    if Q != q or k % q == 0: continue
    for bits in itertools.product(range(NL), repeat=len(sp)):
        pat = dict(zip(sp, bits))
        if nmod(q, 0, [(q, o)], pat) == 0 and bits not in cov[sp]:
            cov[sp].add(bits); wit[(sp, bits)] = (q, 0, ('D', (q,)))
print('moduli tested %d, supports %d, %.1fs' % (nM, len(cov), time.time() - t0), flush=True)

N = len(S)
sig = np.arange(NL ** N, dtype=np.int64)
covered = np.zeros(NL ** N, dtype=bool)
dig = lambda l: (sig // NL ** idx[l]) % NL
for sp, pats in cov.items():
    key = np.zeros(NL ** N, dtype=np.int64)
    for j, l in enumerate(sp):
        key += dig(l) * NL ** j
    tab = np.zeros(NL ** len(sp), dtype=bool)
    for bits in pats:
        tab[sum(b * NL ** j for j, b in enumerate(bits))] = True
    covered |= tab[key]
unc = np.nonzero(~covered)[0]
print('patterns %d, uncovered %d' % (NL ** N, len(unc)))
for x in unc[:30]:
    print('  ', ' '.join('%d:%d' % (l, LAB[(x // NL ** idx[l]) % NL]) for l in S))
if '-v' in sys.argv:
    for sp, pats in sorted(cov.items(), key=lambda t: len(t[0])):
        if len(sp) <= 2: print(sp, sorted(pats), [wit[(sp, b)] for b in sorted(pats)][:4])
if '-g' in sys.argv and len(unc) == 0:
    # greedy minimal subcover of C_S by single (support, pattern) witnesses
    ents = []
    for (sp, bits), w in wit.items():
        key = np.zeros(NL ** N, dtype=np.int64)
        for j, l in enumerate(sp):
            key += dig(l) * NL ** j
        ents.append((sp, bits, w, key == sum(b * NL ** j for j, b in enumerate(bits))))
    left = np.ones(NL ** N, dtype=bool)
    chosen = []
    while left.any():
        sp, bits, w, m = max(ents, key=lambda e: (int((e[3] & left).sum()), -e[2][0]))
        chosen.append((sp, bits, w)); left &= ~m
        print('  %-14s %-20s M=%-8d %s L_M=%s gain' % (sp, bits, w[0], w[2], factorint(
            lcm(*[n_order(4, q ** e) for q, e in factorint(w[0]).items() if q != 2] or [1]))), int(m.sum()), flush=True)
    print('greedy subcover size', len(chosen))
