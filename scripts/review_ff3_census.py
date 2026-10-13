"""review_ff3_census.py (R173): census of ALL Case B families over the slice {x = 1 off T, u(0) = 1}, via the
(m', w, C, v) parametrisation of Lemma 2.1 (re-derived by R173):  m' w C = T^s + v,  w + C = g' v,
T || w, T || C, T not| m' g', all monic; L' = g' m', E = L' w - 1, E' = L' C - 1, s = k + j + gamma.
Every family arises exactly once from (s, v, m', w, C) plus the choice (j, gamma) with s = k + j + gamma,
0 <= gamma <= j; its cylinder (validity set in u) is u == -E (mod T^(N+1)), N = k + j - 1.

Purpose: test the O173 heuristic "expected number of covering families of level N at a random slice point is
~ poly(N) q^{-N}" against the elementary bound "mass ~ q^{-k/2} q^{o(N)} per level", and cross-validate the
search (planted families must be re-found by review_ff3_search at a point of their cylinder).

usage: review_ff3_census.py p k SMAX
"""
import itertools
import sys
import time
from collections import defaultdict
import review_ff3_poly as F


def triples(fac):
    """ordered (m', w', C') of monic divisors with product = prod fac."""
    per = []
    for f, e in fac:
        opts = []
        for a in range(e + 1):
            for b in range(e + 1 - a):
                opts.append((a, b, e - a - b))
        per.append(opts)
    pw = [[[1]] for _ in fac]
    for i, (f, e) in enumerate(fac):
        for _ in range(e):
            pw[i].append(F.mul(pw[i][-1], f))
    for choice in itertools.product(*per):
        m, w, c = [1], [1], [1]
        for i, (a, b, cc) in enumerate(choice):
            m = F.mul(m, pw[i][a])
            w = F.mul(w, pw[i][b])
            c = F.mul(c, pw[i][cc])
        yield m, w, c


def families_for_s(p, s):
    """all (L', g', E) with E E' = 1 + T^s L' g' as above (independent of k, j, gamma)."""
    out = []
    d = s - 3  # v1 = v / T^2 has degree <= s - 3 (deg v <= max(a, b) - deg g' <= s - 1)
    for idx in range(p ** (d + 1)):
        v1 = []
        x = idx
        for _ in range(d + 1):
            v1.append(x % p)
            x //= p
        if v1[0] == 0:
            continue
        v1 = F.norm(v1)
        f = F.add(F.Tpow(s - 2), v1)  # (T^s + v)/T^2, monic, f(0) = v1(0) != 0
        fac = F.factor(f)
        for m, w1, c1 in triples(fac):
            ssum = F.add(w1, c1)  # (w + C)/T
            q, r = F.divmod_(ssum, [0] + v1)  # g' = (w + C)/v = (w1 + c1)/(T v1)
            if r or not F.monic(q) or q[0] == 0:
                continue
            g = q
            L = F.mul(g, m)
            w = [0] + w1
            E = F.add(F.mul(L, w), [p - 1])
            out.append((tuple(L), tuple(g), tuple(E)))
    return out


def main():
    p, k, smax = map(int, sys.argv[1:4])
    F.setp(p)
    print(f"# review_ff3_census p={p} k={k} s<={smax}", flush=True)
    cyl = defaultdict(set)     # N -> set of cylinders (u mod T^(N+1)) of all families of level N
    nfam = defaultdict(int)    # N -> number of families of level N
    union_cyl = defaultdict(set)  # N -> cylinders from families with j - gamma in {0,1} (Lemma 3.1)
    maxl = defaultdict(int)
    for s in range(k + 1, smax + 1):
        t0 = time.time()
        fl = families_for_s(p, s)
        for (L, g, E) in fl:
            l = len(L) - 1
            for gam in range(0, (s - k) // 2 + 1):
                j = s - k - gam
                N = k + j - 1
                u = tuple((-x) % p for x in (list(E) + [0] * (N + 1))[:N + 1])
                cyl[N].add(u)
                nfam[N] += 1
                maxl[N] = max(maxl[N], l)
                if j - gam <= 1:
                    union_cyl[N].add(u)
                assert l <= 2 * N - k - 1 and l <= N + gam - 2, (s, L, g, E, j, gam)  # Lemma 2.1(c)
        print(f"s={s}: {len(fl)} (L',g',E) triples, {time.time()-t0:.1f}s", flush=True)
    # levels N with s range complete: need all s = N+1+gam, gam <= N+1-k, i.e. s <= 2N+2-k <= smax
    Nmax = (smax + k - 2) // 2
    print("# N complete for N <= %d" % Nmax)
    print("# N  #fam(N)  #cyl(N)  maxl  #fam*q^-N  #cyl*q^-N (cylinder mass, slice u(0)=1 normalised)")
    for N in sorted(cyl):
        if N > Nmax:
            continue
        print(f"{N:3d} {nfam[N]:8d} {len(cyl[N]):8d} {maxl[N]:4d} {nfam[N]*p**(-N):10.4f} {len(cyl[N])*p**(-N):10.4f}"
              f"   union-relevant cyl {len(union_cyl[N])}")
    # cumulative covered mass of the union, computed on residues mod T^(M+1)
    M = Nmax
    covered = set()
    for N in range(1, M + 1):
        for u in union_cyl[N]:
            # expand to all residues mod T^(M+1) with u(0) = 1
            for tail in itertools.product(range(p), repeat=M - N):
                covered.add(u + tail)
        print(f"covered slice mass by Case B families of level <= {N}: {len(covered) / p ** M:.4f}", flush=True)


if __name__ == "__main__":
    main()
