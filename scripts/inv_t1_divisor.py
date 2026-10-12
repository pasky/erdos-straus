"""T1 test for divisor-type parity right sides (O158).

Model: D(n) = sum_{uv=n, u<v} phi(u mod M, v mod M) + [n=u^2] psi(u mod M)   (mod 2).
Question: is there (phi, psi) with D(p) = 1 for primes p = h (mod M) and D(m^2) = 0
for every m coprime to M (or every m with m^2 = h mod M)?

Constraints at m^2 come from *generic* prime patterns m = prod q_i^{e_i}, q_1 << q_2 << ...
(lexicographic size order; realisable by Dirichlet), so every constraint used is a genuine
necessary condition. Solve over GF(2) with python-int bitsets.

usage: inv_t1_divisor.py M h kmax emax [only_h]
"""
import sys, itertools
from math import gcd

def units(M):
    return [a for a in range(1, M + 1) if gcd(a, M) == 1] if M > 1 else [1]

def main():
    M, h, kmax, emax = map(int, sys.argv[1:5])
    only_h = len(sys.argv) > 5 and sys.argv[5] == '1'
    U = units(M)
    idx = {a % M: i for i, a in enumerate(U)}
    nU = len(U)
    nphi = nU * nU
    nvar = nphi + nU
    def phi(a, b): return idx[a % M] * nU + idx[b % M]
    def psi(c): return nphi + idx[c % M]
    rows = []  # (bitmask, rhs)
    rows.append((1 << phi(1, h), 1))
    seen = set()
    for k in range(1, kmax + 1):
        for res in itertools.product(U, repeat=k):
            for exps in itertools.product(range(1, emax + 1), repeat=k):
                mres = 1
                for a, e in zip(res, exps):
                    mres = mres * pow(a, e, M) % M if M > 1 else 0
                if only_h and (mres * mres - h) % M:
                    continue
                mask = 0
                # enumerate divisors d of m^2 by exponent vector f
                for f in itertools.product(*[range(0, 2 * e + 1) for e in exps]):
                    g = tuple(2 * e - x for e, x in zip(exps, f))
                    if f == g:
                        continue
                    # d < m^2/d ?  compare from largest prime index
                    small = None
                    for i in range(k - 1, -1, -1):
                        if f[i] != g[i]:
                            small = f[i] < g[i]
                            break
                    if not small:
                        continue
                    dres = 1; cres = 1
                    for a, x, y in zip(res, f, g):
                        dres = dres * pow(a, x, M) % M if M > 1 else 0
                        cres = cres * pow(a, y, M) % M if M > 1 else 0
                    mask ^= 1 << phi(dres, cres)
                mask ^= 1 << psi(mres)
                if mask not in seen:
                    seen.add(mask)
                    rows.append((mask, 0))
    # GF(2) elimination
    piv = {}  # pivot bit -> (mask, rhs)
    incons = False
    for mask, rhs in rows:
        while mask:
            b = mask.bit_length() - 1
            if b in piv:
                pm, pr = piv[b]
                mask ^= pm; rhs ^= pr
            else:
                piv[b] = (mask, rhs)
                break
        else:
            if rhs:
                incons = True
    print(f"M={M} h={h} kmax={kmax} emax={emax} only_h={only_h}: vars={nvar} rows={len(rows)} rank={len(piv)} "
          f"{'INCONSISTENT (no admissible D)' if incons else 'consistent'}")

if __name__ == '__main__':
    main()
