"""Validate the C engine (m13d_wit.c) against m13c_witness.witness_all (complete Python engine, §2 of 13C).

usage: m13d_validate.py tree.json[.gz] nleaves seed [nchild] [dropmin dropmax]
  (optionally each leaf x mod L is replaced by x mod L', L' = L without its k largest prime powers,
   k uniform in [dropmin, dropmax] — to keep the Python reference engine fast)
  * nleaves random open leaves of the tree: full witness SETS must agree (all mode);
  * for nchild of them, a random split prime p: every child y mod L*p, compared with req = p^v_p(Lp):
    C set == Python set restricted to classes with req | M; and first-mode answers must be in the set.
Also: every C witness is checked with mordell_lib.cls_modulus_residues (M | L, x mod M in class).
"""
import sys, json, gzip, random, time
from math import gcd
from m13c_witness import witness_all
from m13d_wit import Engine
import mordell_lib


def opens_of(path):
    T = json.load((gzip.open if path.endswith('.gz') else open)(path, 'rt'))
    out = []; st = list(T['roots'])
    while st:
        nd = st.pop()
        if 'children' in nd: st += nd['children']
        elif nd.get('open'): out.append((nd['x'], nd['L']))
    return out


def modulus(fam, P):
    return mordell_lib.cls_modulus_residues(fam, P)[0]


def check_cls(fam, P, x, L):
    M, R = mordell_lib.cls_modulus_residues(fam, P)
    assert L % M == 0 and x % M in R, (fam, P, x, L)


def vp(n, p):
    e = 0
    while n % p == 0: n //= p; e += 1
    return e


def main():
    path, nl, seed = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    nch = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    random.seed(seed)
    S = random.sample(opens_of(path), nl)
    if len(sys.argv) > 6:
        from sympy import factorint
        d0, d1 = int(sys.argv[5]), int(sys.argv[6]); S2 = []
        for x, L in S:
            F = factorint(L); k = random.randint(d0, d1)
            for p in sorted(F)[len(F) - k:]: L //= p ** F[p]
            S2.append((x % L, L))
        S = S2
    E = Engine(); bad = 0; nonempty = 0; tc = tp = 0.0; nchk = 0
    for i, (x, L) in enumerate(S):
        t0 = time.time(); c = set(E.query(x, L, all=True)); t1 = time.time()
        p = set(witness_all(x, L, first=False)); t2 = time.time()
        tc += t1 - t0; tp += t2 - t1
        for fam, P in c: check_cls(fam, P, x, L)
        if c != p:
            bad += 1; print("MISMATCH", x, L, sorted(c - p), sorted(p - c), flush=True)
        nonempty += bool(c)
        if i < nch:
            q = random.choice([q for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)])
            L2 = L * q; req = q ** vp(L2, q)
            for t in range(q):
                y = (x + L * t) % L2
                if gcd(y, L2) != 1: continue
                c2 = set(E.query(y, L2, req=req, all=True))
                p2 = {w for w in witness_all(y, L2, first=False) if modulus(*w) % req == 0}
                f2 = E.query(y, L2, req=req)
                nchk += 1
                if c2 != p2 or (f2 and f2[0] not in p2) or (not f2 and p2):
                    bad += 1; print("MISMATCH-child", y, L2, req, sorted(c2 ^ p2), flush=True)
        if (i + 1) % 10 == 0:
            print(f"{i+1} leaves, children {nchk}, bad={bad}, nonempty={nonempty}, C {tc:.1f}s Py {tp:.1f}s", flush=True)
    print(f"DONE leaves={nl} children={nchk} mismatches={bad} nonempty={nonempty} C {tc:.1f}s Py {tp:.1f}s")


if __name__ == '__main__':
    main()
