"""O168 §6-7: joint structure of Type II slices e <= E at p ≡ 1 (mod 24).

Per slice e ≡ 3 (4), N_e = (p+e)/4, Σ_e(N) = image of the box ∏[-k_i,k_i] (Prop 6.2).
 * success: -1 ∈ Σ_e(N_e);
 * shared-type success: some witness (a,b) with every prime of ab < E/4 (such primes may divide several N_e);
 * private-only success: every witness uses a prime >= E/4 (divides at most one N_e, e <= E).
Hall test on Jacobi-forced slices F = {prime e <= E, e ≡ 3 (4), (p/e) = -1}: edges e—l for l | N_e with
(l/e) = -1; nu = maximum matching; deficiency |F| - nu (Hall fails iff deficiency > 0).
Usage: de_joint_slices.py PMAX E [HARD_E0]   (hard primes: no Type II slice e < HARD_E0 succeeds)
"""
import sys
from sympy import primerange, legendre_symbol, isprime


def spf_table(n):
    s = list(range(n + 1))
    i = 2
    while i * i <= n:
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
        i += 1
    return s


def factor(n, spf):
    f = {}
    while n > 1:
        q = spf[n]
        f[q] = f.get(q, 0) + 1
        n //= q
    return f


def witnesses(N, e, fac):
    """yield the set of primes used by each witness pair (a,b), ab | N, e | a+b"""
    items = list(fac.items())
    # enumerate (alpha, beta) per prime with alpha+beta <= k
    def rec(i, a, b, used):
        if i == len(items):
            if (a + b) % e == 0:
                yield used
            return
        l, k = items[i]
        for al in range(k + 1):
            for be in range(k + 1 - al):
                yield from rec(i + 1, a * l**al, b * l**be, used | ({l} if al + be else set()))
    yield from rec(0, 1, 1, frozenset())


def max_matching(adj):
    match = {}
    def aug(u, seen):
        for v in adj[u]:
            if v in seen:
                continue
            seen.add(v)
            if v not in match or aug(match[v], seen):
                match[v] = u
                return True
        return False
    return sum(aug(u, set()) for u in adj)


def main():
    PMAX, E = int(sys.argv[1]), int(sys.argv[2])
    E0 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    spf = spf_table((PMAX + E) // 4 + 1)
    es = [e for e in range(3, E + 1) if e % 4 == 3]
    cut = E / 4
    tot = {"p": 0, "sl": 0, "succ": 0, "shared": 0, "private_only": 0, "Fsize": 0, "defic": 0, "hallfail": 0,
           "anysucc_p": 0, "shared_p": 0, "block": 0, "block_p": 0}
    for p in primerange(5, PMAX):
        if p % 24 != 1:
            continue
        if E0:
            if any(next(witnesses((p + e) // 4, e, factor((p + e) // 4, spf)), None) is not None
                   for e in es if e < E0):
                continue
        tot["p"] += 1
        adj = {}
        anyS = anyShared = anyBlock = False
        for e in es:
            N = (p + e) // 4
            fac = factor(N, spf)
            ws = list(witnesses(N, e, fac))
            sm = {l: k for l, k in fac.items() if l < cut}
            P = N
            for l, k in sm.items():
                P //= l**k
            blk = dict(sm)
            if P > 1:
                blk[P] = 1
            if next(witnesses(N, e, blk), None) is not None:
                anyBlock = True
                tot["block"] += 1
            tot["sl"] += 1
            if ws:
                tot["succ"] += 1
                anyS = True
                if any(all(l < cut for l in w) for w in ws):
                    tot["shared"] += 1
                    anyShared = True
                else:
                    tot["private_only"] += 1
            if isprime(e) and legendre_symbol(p % e, e) == -1:
                adj[e] = [l for l in fac if legendre_symbol(l % e, e) == -1]
        tot["anysucc_p"] += anyS
        tot["shared_p"] += anyShared
        tot["block_p"] += anyBlock
        nu = max_matching(adj)
        tot["Fsize"] += len(adj)
        tot["defic"] += len(adj) - nu
        tot["hallfail"] += (len(adj) - nu) > 0
    t = tot
    print(f"PMAX={PMAX} E={E} hardE0={E0} primes={t['p']} slices={t['sl']}")
    print(f"slice success={t['succ']/t['sl']:.4f} shared-type={t['shared']/t['sl']:.4f} "
          f"private-only={t['private_only']/t['sl']:.4f}")
    print(f"primes solved by some slice<=E: {t['anysucc_p']/t['p']:.4f}; by a shared-type witness: "
          f"{t['shared_p']/t['p']:.4f}")
    print(f"block-witness (residue+shared-forced) slice rate={t['block']/t['sl']:.4f}; primes={t['block_p']/t['p']:.4f}")
    print(f"forced slices/prime={t['Fsize']/t['p']:.2f} mean Hall deficiency={t['defic']/t['p']:.3f} "
          f"primes with Hall failure={t['hallfail']/t['p']:.4f}")


if __name__ == "__main__":
    main()
