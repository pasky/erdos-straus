#!/usr/bin/env python3
"""z62 PARITY — H2: signed (Z-valued) indices with quadratic-character signs.

For each n, words (t,u,v) (unordered u <= v) of X(n); families STAR, U7, ALLX as in z62_parity_river.py.
Per-word signs (values in {-1,0,1}): chi(z) = Jacobi (z/n) for z in {t,u,v,u+v,A=tu-1,A*=tv-1,t*u*v}, the parities
(-1)^t,(-1)^u,(-1)^v, and all pairwise products of these 10 base signs; plus the constant 1.
Signed counts S_w(n) = sum over family words of w(word).
Then: nullspace over F_P (P = 2^61-1; a rational relation reduces to one mod P, so "no excess mod P" => none over Q) of [S_w(p) | indicator(p mod M)] over TRAIN primes p = 1 (24),
quotiented by per-word identities (nullspace of the per-word pattern matrix); report non-trivial relations and their
held-out exactness on TEST primes.
Usage: z62_parity_signed.py NMAX split [M]
"""
import sys
from math import isqrt
sys.path.insert(0, "scripts")
import z62_parity_river as Z

P = (1 << 61) - 1


def jacobi(a, n):
    a %= n
    if a == 0:
        return 0
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


BASE = ["c_t", "c_u", "c_v", "c_s", "c_A", "c_As", "c_tuv", "e_t", "e_u", "e_v"]


def word_signs(n, t, u, v):
    A, As = t * u - 1, t * v - 1
    b = {"c_t": jacobi(t, n), "c_u": jacobi(u, n), "c_v": jacobi(v, n), "c_s": jacobi(u + v, n),
         "c_A": jacobi(A, n), "c_As": jacobi(As, n), "c_tuv": jacobi(t * u * v, n),
         "e_t": (-1) ** t, "e_u": (-1) ** u, "e_v": (-1) ** v}
    w = {"one": 1}
    w.update(b)
    for i, x in enumerate(BASE):
        for y in BASE[i + 1:]:
            w[x + "*" + y] = b[x] * b[y]
    return w


WN = ["one"] + BASE + [x + "*" + y for i, x in enumerate(BASE) for y in BASE[i + 1:]]
FAMS = ("STAR", "U7", "ALLX")
COLS = [(f, w) for f in FAMS for w in WN]


def counts(n, pats=None):
    S = [0] * len(COLS)
    for (t, u, v) in Z.words(n):
        fl = Z.fam_flags(n, t, u, v)
        ws = word_signs(n, t, u, v)
        vec = [ws[w] if fl[f] else 0 for (f, w) in COLS]
        for j, x in enumerate(vec):
            S[j] += x
        if pats is not None:
            pats.add(tuple(vec))
    return S


def nullspace_modp(rows, ncols):
    """basis of {x : rows . x = 0 mod P}."""
    piv_rows = []  # list of (col, row) with row normalised pivot 1, fully reduced
    pivcols = {}
    for r in rows:
        r = [x % P for x in r]
        for c, pr in pivcols.items():
            if r[c]:
                f = r[c]
                r = [(a - f * b) % P for a, b in zip(r, pr)]
        c = next((j for j in range(ncols) if r[j]), None)
        if c is None:
            continue
        inv = pow(r[c], P - 2, P)
        r = [(a * inv) % P for a in r]
        for c2 in list(pivcols):
            pr = pivcols[c2]
            if pr[c]:
                f = pr[c]
                pivcols[c2] = [(a - f * b) % P for a, b in zip(pr, r)]
        pivcols[c] = r
    free = [j for j in range(ncols) if j not in pivcols]
    basis = []
    for fcol in free:
        x = [0] * ncols
        x[fcol] = 1
        for c, pr in pivcols.items():
            x[c] = (-pr[fcol]) % P
        basis.append(x)
    return basis


def rank_modp(vecs, ncols):
    return ncols - len(nullspace_modp(vecs, ncols)) if vecs else 0


def main():
    N, split = int(sys.argv[1]), int(sys.argv[2])
    M = int(sys.argv[3]) if len(sys.argv) > 3 else 840
    Z.SPF = Z.spf_sieve(N + isqrt(N) + 10)
    primes = [p for p in range(25, N + 1, 24) if Z.is_prime(p)]
    pats = set()
    data = {}
    for p in primes:
        data[p] = counts(p, pats if p <= split else None)
    nf = len(COLS)
    classes = sorted({p % M for p in primes})
    cidx = {c: i for i, c in enumerate(classes)}
    ncl = len(classes)
    rows = []
    for p in primes:
        if p <= split:
            r = data[p] + [0] * ncl
            r[nf + cidx[p % M]] = 1
            rows.append(r)
    pnull = nullspace_modp(rows, nf + ncl)
    wnull = nullspace_modp([list(v) for v in pats], nf)  # per-word identities (feature part only)
    # exact rational rank of the per-word pattern matrix (rank sandwich: rank_Q >= rank_P; equality => kernels agree in dim)
    import sympy as sp
    rq = sp.Matrix([list(v) for v in sorted(pats)]).rank()
    print(f"# exact rational rank of per-word pattern matrix: {rq} (mod-P rank {nf - len(wnull)})")
    print(f"# {len(rows)} train primes, {len(primes)-len(rows)} test primes, {nf} signed counts, {ncl} classes mod {M}")
    print(f"# distinct per-word patterns {len(pats)}; per-word identity dim {len(wnull)}; prime-level nullspace dim {len(pnull)}")
    # nontrivial = pnull vectors not in span(wnull x {g=0})
    ext = [w + [0] * ncl for w in wnull]
    base_rank = rank_modp(ext, nf + ncl)
    nontriv = []
    cur = list(ext)
    r0 = base_rank
    for x in pnull:
        r1 = rank_modp(cur + [x], nf + ncl)
        if r1 > r0:
            nontriv.append(x)
            cur.append(x)
            r0 = r1
    print(f"# non-trivial excess dimension: {len(nontriv)}")
    for x in nontriv[:40]:
        ok = 0
        tst = [p for p in primes if p > split]
        for p in tst:
            val = (sum(a * b for a, b in zip(x[:nf], data[p])) + x[nf + cidx[p % M]]) % P
            ok += (val == 0)
        supp = [f"{COLS[j][0]}:{COLS[j][1]}" for j in range(nf) if x[j]]
        print(f"  relation held-out exact on {ok}/{len(tst)}; support size {len(supp)}: {supp[:12]}{' ...' if len(supp)>12 else ''}")


if __name__ == "__main__":
    main()
