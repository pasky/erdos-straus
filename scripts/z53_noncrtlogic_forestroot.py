#!/usr/bin/env python3
"""Z53_NONCRTLOGIC -- the cheapest escaping primitive with full factorisation control (the least non-residue n_p)
used as a ROOT of the word forest F_p (edge uv <=> uv | p+u+v; colour chi(v) = (v/p); for p = 1 (4) a bichromatic
edge is exactly a five-slice ES certificate, LOWER_TAIL_ASTRA Lemmas 2.1-2.2).

For each test prime p we explore the component of a root by BFS (depth <= DEPTH, at most VMAX vertices) and report
whether a bichromatic edge is met.  Roots compared:
   n_p                         (escaping, QNR, prime)
   q_p = least prime QR > 3    (the formal analogue: a residue of the same size scale)
   1                           (the fixed root; dead under Dickson, LOWER_TAIL_ASTRA Thm 3.1)
   the next two non-residue primes after n_p (n_p is "least" only by parity data)
Test primes: the (*)-zero primes, the b=1 failures 193, 2521, 66529, 3361, Mordell-hard primes, plus controls.
At an odd square n = m^2 every unit vertex has colour +1 (no QNR exists): every root fails (T1).

Usage: uv run --with sympy --with gmpy2 python scripts/z53_noncrtlogic_forestroot.py DEPTH VMAX OUT
"""
import sys
import json
from collections import deque
import gmpy2
from sympy import factorint


def divisors_of(n):
    ds = [1]
    for l, e in factorint(n).items():
        ds = [d * l ** k for d in ds for k in range(e + 1)]
    return ds


def neighbours(p, v):
    out = []
    if v > 1:
        r = (-p) % v
        if r > 0 and (p + v) % r == 0 and r != v:
            out.append(r)
    for w in divisors_of(p + v):
        if w > v and w <= p + 2 and (w + p) % v == 0 and w != p:
            out.append(w)
    return out


def chi(v, p):
    return gmpy2.jacobi(v % p, p)


def explore(p, root, depth, vmax):
    seen = {root: 0}
    dq = deque([root])
    edges = 0
    while dq:
        v = dq.popleft()
        if seen[v] >= depth:
            continue
        for w in neighbours(p, v):
            edges += 1
            cv, cw = chi(v, p), chi(w, p)
            if cv != 0 and cw != 0 and cv != cw:   # unit endpoints only
                return True, len(seen), (v, w)
            if w not in seen:
                if len(seen) >= vmax:
                    return False, len(seen), 'cap'
                seen[w] = seen[v] + 1
                dq.append(w)
    return False, len(seen), None


def qnr_primes(p, k):
    out, l = [], 2
    while len(out) < k:
        if gmpy2.is_prime(l) and gmpy2.legendre(l, p) == -1:
            out.append(l)
        l += 1
    return out


def least_qr_prime(p):
    l = 5
    while True:
        if gmpy2.is_prime(l) and gmpy2.legendre(l, p) == 1:
            return l
        l += 1


def mordell_hard(N, step):
    out = []
    p = 1009
    while p < N and len(out) < 400:
        if gmpy2.is_prime(p) and p % 840 in (1, 121, 169, 289, 361, 529):
            out.append(p)
            p += step
        p += 1
    return out


def main():
    depth, vmax, outp = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    star_zero = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 1134241, 1724209, 1726201, 5212561,
                 8813281]  # all 14 (*)-zero primes p = 1 (4) <= 1e10
    special = star_zero + [193, 2521, 66529, 3361, 5101441]
    near = [m * m + 1 for m in range(24, 20000, 24) if gmpy2.is_prime(m * m + 1)][:300]   # trap-family primes q^2+1, 24 | q
    tests = [('special', p) for p in special] + [('mordell', p) for p in mordell_hard(10 ** 7, 20011)] + \
        [('near_sq_q2+1', p) for p in near]
    res = []
    for tag, p in tests:
        qn = qnr_primes(p, 3)
        roots = {'n_p': qn[0], 'qnr2': qn[1], 'qnr3': qn[2], 'least_QR_prime': least_qr_prime(p), 'one': 1}
        row = {'tag': tag, 'p': p, 'np_value': qn[0]}
        for name, r in roots.items():
            ok, size, ed = explore(p, r, depth, vmax)
            row[name] = [ok, size, str(ed)]
        res.append(row)
    # odd-square control (unit vertices all colour +1 -> no bichromatic edge at any root)
    sq = []
    for m in (21, 33, 39, 51, 57, 69, 87, 93, 111, 123):
        n = m * m
        ok, size, _ = explore(n, 1, depth, vmax)
        sq.append((n, ok, size))
    with open(outp, 'w') as fh:
        json.dump({'depth': depth, 'vmax': vmax, 'rows': res, 'odd_squares_root1': sq}, fh)
    names = ['n_p', 'qnr2', 'qnr3', 'least_QR_prime', 'one']
    for tag in ('special', 'mordell', 'near_sq_q2+1'):
        rows = [r for r in res if r['tag'] == tag]
        print(f"[{tag}] {len(rows)} primes; success rate by root (depth<={depth}, <= {vmax} vertices):")
        for nm in names:
            s = sum(1 for r in rows if r[nm][0])
            print(f"   {nm:15s} {s}/{len(rows)}")
    for r in res:
        if r['tag'] == 'special':
            print(f"   p={r['p']:8d} n_p={r['np_value']:3d}  " + "  ".join(f"{nm}:{'Y' if r[nm][0] else 'n'}({r[nm][1]})" for nm in names))
    print("odd squares, root 1 (T1 control; must be all 'False'):", sq)


if __name__ == '__main__':
    main()
