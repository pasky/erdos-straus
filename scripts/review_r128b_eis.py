"""R128b from-scratch check of Props 9.1-9.2 (POINTWISE_TYPEII_SPECTRAL §9), all n <= NMAX.

For every n <= NMAX and every (c,d) with 2cd-1 <= n (outside this range the count is 0; checked too for a
margin), M = 4cd, N = 4c^2 d n + 1:
  cnt  = #{f | N : f = -1 mod M}
  (9.1) cnt = (1/phi(M)) sum_eta eta(-1) sigma_eta(N)        [explicit character table, M <= MCHAR]
  (9.2) cnt = (1/phi(M)) sum_{eta even} sum_{f|N} eta(f)(1 - (n/f))   [character table, M <= MCHAR]
        and its character-free form cnt = #{f|N : f = +-1 mod M, (n/f) = -1}  [all M]
  psi(f) := kronecker(-4d, f) equals jacobi(n, f) for all f | N.
  odd squares: cnt = 0 for every (c,d).
"""
import cmath
from math import gcd, isqrt

def jacobi(a, m):
    assert m > 0 and m % 2 == 1
    a %= m
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if m % 8 in (3, 5):
                r = -r
        a, m = m, a
        if a % 4 == 3 and m % 4 == 3:
            r = -r
        a %= m
    return r if m == 1 else 0

def kron_m4d(d, f):  # Kronecker (-4d / f), f odd positive
    return jacobi(-4 * d, f)  # (4/f)=1 so equals (-d/f) for odd f

def divisors(n):
    ds, i = [], 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i * i != n:
                ds.append(n // i)
        i += 1
    return ds

def factor(n):
    fs, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            fs[p] = fs.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        fs[n] = fs.get(n, 0) + 1
    return fs

def char_table(M):
    """Return list of characters mod M as dicts residue->complex (units only), built by CRT."""
    units = [u for u in range(M) if gcd(u, M) == 1]
    comps = []  # list of (modulus, generator list with orders)
    for p, k in factor(M).items():
        pk = p ** k
        if p == 2:
            gens = []
            if k >= 2:
                gens.append((pk - 1, 2))  # -1
            if k >= 3:
                gens.append((5, pk // 4))
        else:
            phi = pk - pk // p
            g = next(g for g in range(2, pk) if gcd(g, p) == 1 and all(pow(g, phi // r, pk) != 1 for r in factor(phi)))
            gens = [(g, phi)]
        comps.append((pk, gens))
    # discrete logs per component
    def logs(u):
        out = []
        for pk, gens in comps:
            x = u % pk
            if len(gens) == 0:
                continue
            if len(gens) == 1:
                g, o = gens[0]
                e = next(e for e in range(o) if pow(g, e, pk) == x)
                out.append((e, o))
            else:
                (g1, o1), (g2, o2) = gens
                done = False
                for e1 in range(o1):
                    for e2 in range(o2):
                        if pow(g1, e1, pk) * pow(g2, e2, pk) % pk == x:
                            out += [(e1, o1), (e2, o2)]
                            done = True
                            break
                    if done:
                        break
        return out
    L = {u: logs(u) for u in units}
    orders = [o for (_, o) in L[1]]
    chars = []
    def rec(i, cur):
        if i == len(orders):
            chars.append(tuple(cur))
            return
        for t in range(orders[i]):
            rec(i + 1, cur + [t])
    rec(0, [])
    tab = []
    for ch in chars:
        tab.append({u: cmath.exp(2j * cmath.pi * sum(t * e / o for t, (e, o) in zip(ch, L[u]))) for u in units})
    return tab

def main(NMAX=500, MCHAR=96):
    tabs = {}
    nchar = nall = 0
    for n in range(1, NMAX + 1):
        sq = isqrt(n) ** 2 == n and n % 2 == 1
        tot = 0
        for c in range(1, n + 2):
            for d in range(1, n + 2):
                if 2 * c * d - 1 > n + 4:
                    break
                M, N = 4 * c * d, 4 * c * c * d * n + 1
                Ds = divisors(N)
                cnt = sum(1 for f in Ds if f % M == M - 1)
                if 2 * c * d - 1 > n:
                    assert cnt == 0
                for f in Ds:
                    assert kron_m4d(d, f) == jacobi(n, f)
                alt = sum(1 for f in Ds if f % M in (1, M - 1) and jacobi(n, f) == -1)
                assert cnt == alt, (n, c, d)
                if sq:
                    assert cnt == 0
                if M <= MCHAR:
                    if M not in tabs:
                        tabs[M] = char_table(M)
                    T = tabs[M]
                    phi = len(T)
                    s91 = sum(ch[M - 1] * sum(ch[f % M] for f in Ds) for ch in T) / phi
                    s92 = sum(sum(ch[f % M] * (1 - jacobi(n, f)) for f in Ds)
                              for ch in T if abs(ch[M - 1] - 1) < 1e-9) / phi
                    assert abs(s91 - cnt) < 1e-6 and abs(s92 - cnt) < 1e-6, (n, c, d, s91, s92, cnt)
                    nchar += 1
                nall += 1
                tot += cnt
            if 2 * c - 1 > n + 4:
                break
    print(f"n<={NMAX}: {nall} (n,c,d) triples checked (9.2 char-free form, psi=(n/.)); "
          f"{nchar} with explicit character tables (M<={MCHAR}); odd squares: all counts 0. OK")

if __name__ == "__main__":
    main()
