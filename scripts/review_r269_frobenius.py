"""R269 from-scratch checks for BALANCED_LATTICE §2.
(A) Prop 2.2: for real primes q, build the fake a' (a' = a mod N1, a'_{s0} = 1, a'_s = 0 mod N2), check it generates Z/N,
    agrees with a mod N1, and that its discrete covering number L'_min satisfies L'_min + 1 >= N2; compare with the true L_min.
(B) Prop 2.1(b)/(a): the m-th power residue vector b_s = (s^{(q-1)/m} -> log) equals a mod m up to a unit, for m | N1.
(C) Lemma 2.5: density of {q in class sigma0 : l | q-1, S in (F_q^*)^l} vs the Kummer prediction 1/(phi-part * l^k).
Usage: PYTHONPATH=scripts uv run --with sympy --with numpy python scripts/review_r269_frobenius.py A|B|C ...
"""
import sys, math, random
import numpy as np
from sympy import isprime, primerange, primitive_root, factorint, legendre_symbol


def dlog_table(q):
    N = (q - 1) // 2
    g = pow(primitive_root(q), 2, q)
    tab = np.full(q, -1, dtype=np.int64)
    x = 1
    for i in range(N):
        tab[x] = i; x = x * g % q
    return N, g, tab


def covers(N, a, L):
    R = np.zeros(N, dtype=bool); R[0] = True
    for s in a:
        acc = R.copy(); cur = R
        for _ in range(L):
            cur = np.roll(cur, int(s) % N); acc |= cur
        R = acc
    return bool(R.all())


def lmin(N, a, cap):
    for L in range(0, cap + 1):
        if covers(N, a, L): return L
    return None


def smooth_split(N, M):
    N1 = 1
    for l, e in factorint(N).items():
        if l <= M: N1 *= l ** e
    return N1, N // N1


def partA(y, M, qlo, qhi, ns, seed):
    S = list(primerange(3, y + 1)); k = len(S); rnd = random.Random(seed); done = 0; bad = 0
    while done < ns:
        q = rnd.randrange(qlo, qhi)
        if q % 8 != 3 or not isprime(q): continue
        N, g, tab = dlog_table(q)
        a = [int(tab[s * s % q]) for s in S]
        if math.gcd(N, *a) != 1: continue
        N1, N2 = smooth_split(N, M)
        if N2 == 1: continue
        # CRT a' : = a mod N1 ; = (1,0,...,0) mod N2
        ap = []
        for i, s in enumerate(S):
            t = 1 if i == 0 else 0
            # x = a_i mod N1, x = t mod N2
            x = (a[i] * N2 * pow(N2, -1, N1) + t * N1 * pow(N1, -1, N2)) % N if N1 > 1 else t % N
            ap.append(x)
        gen = math.gcd(N, *ap) == 1
        agree = all((ap[i] - a[i]) % N1 == 0 for i in range(k))
        Lt = lmin(N, a, N)
        Lf = lmin(N, ap, N)
        ok = gen and agree and Lf + 1 >= N2
        bad += not ok; done += 1
        print(f"q={q} N={N} N1={N1} N2={N2} Ltrue={Lt} Lfake={Lf} gen={gen} agree={agree} ok={ok}")
    print(f"partA: {done} samples, {bad} failures")


def partB(y, qlo, qhi, ns, seed):
    S = list(primerange(3, y + 1)); rnd = random.Random(seed); done = 0; bad = 0
    while done < ns:
        q = rnd.randrange(qlo, qhi)
        if q % 8 != 3 or not isprime(q): continue
        N, g, tab = dlog_table(q)
        a = [int(tab[s * s % q]) for s in S]
        for m in [d for d in range(3, 200, 2) if N % d == 0]:
            # chi_m(s) = s^{(q-1)/m}; its log base zeta := gamma^{(q-1)/m} where gamma^2 = g (gamma = primitive root)
            gam = primitive_root(q)
            z = pow(gam, (q - 1) // m, q)
            zl = {pow(z, j, q): j for j in range(m)}
            b = [zl[pow(s, (q - 1) // m, q)] for s in S]
            # claim: b = a mod m (same generator) -> check
            if [x % m for x in a] != b: bad += 1
        done += 1
    print(f"partB: {done} q, mismatches {bad}")


def partC(y, l, p, X):
    S = list(primerange(3, y + 1)); k = len(S); P = math.prod(S)
    # sigma0: q = 3 mod 8, q = -p mod P, chi_p(q) = -1
    tot = hit = 0
    for q in primerange(max(S) + 2, X):
        if q % 8 != 3 or q % P != (-p) % P or legendre_symbol(q % p, p) != -1: continue
        tot += 1
        if (q - 1) % l: continue
        e = (q - 1) // l
        if all(pow(s, e, q) == 1 for s in S): hit += 1
    lin = l in S
    dens = (1.0 if ((-p - 1) % l == 0) else 0.0) / l ** k if lin else 1.0 / ((l - 1) * l ** k)
    print(f"partC y={y} k={k} l={l} p={p} X={X}: class count {tot}, hits {hit}, ratio {hit/max(tot,1):.5f}, Kummer prediction {dens:.5f}")


if __name__ == '__main__':
    w = sys.argv[1]; args = list(map(int, sys.argv[2:]))
    {'A': partA, 'B': partB, 'C': partC}[w](*args)
