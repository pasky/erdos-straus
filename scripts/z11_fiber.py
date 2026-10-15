# z11_fiber.py — fibre coverage at a frozen point: fix mu_l = V_l exactly for every l in a small set S0 (default value D
# for l in S0 not listed), and for each larger prime l (one at a time) let mu_l = c range over Z/l.  Count the residues
# c mod l for which n = c0*4^mu + k lies in some ET/divisor class whose period has support in S0 + {l} with v_l(L_M) <= 1.
# Usage: PYTHONPATH=scripts uv run python scripts/z11_fiber.py c0 k S0MAX D LMIN LMAX QMAX MMAX l1:V1 ...
import sys, time, itertools
from collections import defaultdict
from sympy import n_order, factorint, primerange
from sympy.ntheory.modular import crt
import mordell_lib as ML

c0, k, S0MAX, D, LMIN, LMAX, QMAX, MMAX = map(int, sys.argv[1:9])
V = {int(a.split(':')[0]): int(a.split(':')[1]) for a in sys.argv[9:] if ':' in a}
S0 = list(primerange(2, S0MAX + 1))
BIG = list(primerange(LMIN, LMAX + 1))
t0 = time.time()
pps = []
for q in primerange(3, QMAX + 1):
    if (c0 * 4) % q == 0: continue
    Q = q
    while Q <= QMAX:
        o = n_order(4, Q)
        f = factorint(o)
        big = [l for l in f if l not in S0]
        if len(big) > 1 or (big and (big[0] not in BIG or f[big[0]] > 1)): break
        pps.append((q, Q, o, big[0] if big else None))
        Q *= q
print('prime powers', len(pps), flush=True)


def val(Q, o, c, l):
    f = factorint(o)
    if not f: return (c0 + k) % Q
    ms = [p ** e for p, e in f.items()]
    rs = [(c if p == l else V.get(p, D)) % (p ** e) for p, e in f.items()]
    return (c0 * pow(4, int(crt(ms, rs)[0]), Q) + k) % Q


# odd parts with at most one big prime l
odd = [(1, (), None)]
byq = defaultdict(list)
for q, Q, o, b in pps: byq[q].append((Q, o, b))
for q in sorted(byq):
    new = []
    for m, parts, b in odd:
        for Q, o, b2 in byq[q]:
            if m * Q > MMAX: continue
            if b and b2 and b != b2: continue
            new.append((m * Q, parts + ((Q, o),), b or b2))
    odd += new
print('odd parts', len(odd), '%.1fs' % (time.time() - t0), flush=True)
covered = defaultdict(dict)
frozen_hit = []
for m, parts, b in odd:
    for a in (0, 2, 3, 4, 5, 6, 7):
        M = 2 ** a * m
        if M > MMAX or M < 3 or (a == 0 and M % 4 != 3): continue
        W = ML.residue_table(M)
        if not W: continue
        cs = range(b) if b else [0]
        for c in cs:
            ms, rs = ([2 ** a], [k % 2 ** a]) if a else ([], [])
            for Q, o in parts:
                ms.append(Q); rs.append(val(Q, o, c, b))
            r = int(crt(ms, rs)[0])
            if r in W:
                if b is None: frozen_hit.append((M, W[r]))
                elif c not in covered[b]: covered[b][c] = (M, W[r])
for q, Q, o, b in pps:
    if Q == q and k % q:
        for c in (range(b) if b else [0]):
            if val(q, o, c, b) == 0:
                if b is None: frozen_hit.append((q, 'D'))
                elif c not in covered[b]: covered[b][c] = (q, 'D')
print('classes with support in S0 containing the frozen point:', frozen_hit[:5])
for l in BIG:
    cv = covered.get(l, {})
    print('l=%d covered %d/%d  missing %s' % (l, len(cv), l, [c for c in range(l) if c not in cv][:12]), flush=True)
print('%.1fs' % (time.time() - t0))
