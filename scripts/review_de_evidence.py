"""R168 from-scratch replication of O168 EVIDENCE: §3.4 Jacobi table, §4 Pell splitting, §7 block-witness rates.
Usage: review_de_evidence.py PMAX_JACOBI PMAX_PELL PMAX_JOINT"""
import sys, random
from math import gcd, isqrt, sqrt
from sympy import primerange, factorint, jacobi_symbol


def subgroup_has_minus1(gens, e):
    H = {1}; fr = [1]
    while fr:
        x = fr.pop()
        for g in gens:
            y = x * g % e
            if y not in H: H.add(y); fr.append(y)
    return (e - 1) in H


def box_has_minus1(fac, e):
    S = {1}
    for l, k in fac.items():
        l %= e; li = pow(l, -1, e)
        T = set()
        for s in S:
            t = s
            for _ in range(k + 1): T.add(t); t = t * l % e
            t = s
            for _ in range(k + 1): T.add(t); t = t * li % e
        S = T
    return (e - 1) in S


def pell(D):  # fundamental solution of x^2 - D y^2 = 1 via CF of sqrt(D)
    a0 = isqrt(D); m, d, a = 0, 1, a0
    h0, h1, k0, k1 = 1, a0, 0, 1
    while h1 * h1 - D * k1 * k1 != 1:
        m = d * a - m; d = (D - m * m) // d; a = (a0 + m) // d
        h0, h1 = h1, a * h1 + h0; k0, k1 = k1, a * k1 + k0
    return h1, k1


P1, P2, P3 = map(int, sys.argv[1:4])
es = [e for e in primerange(3, 200) if e % 4 == 3]
# --- §3.4 Jacobi table
st = {1: [0, 0, 0], -1: [0, 0, 0]}
for p in primerange(5, P1):
    if p % 24 != 1: continue
    for e in es:
        if e >= p: continue
        fac = factorint((p + e) // 4); j = jacobi_symbol(p, e)
        st[j][0] += 1; st[j][1] += subgroup_has_minus1(list(fac), e); st[j][2] += box_has_minus1(fac, e)
for j in (1, -1):
    n, h, s = st[j]; print(f"Jacobi p<{P1}: (p/e)={j:+d} slices {n}  -1 in H {h/n:.4f}  -1 in Sigma {s/n:.4f}")

# --- §4 Pell
ok = lambda A, B, e: (A + B) % e == 0 or (A + 1) % e == 0 or (B + 1) % e == 0
n = hit = triv = 0; base = 0.0; hit_nt = n_nt = 0; base_nt = 0.0; nodd = hit_odd = 0
for p in primerange(5, P2):
    if p % 24 != 1: continue
    for e in [e for e in es if e < 60]:
        N = (p + e) // 4; fac = factorint(N)
        if len(fac) < 2 or max(fac.values()) > 1: continue
        x, y = pell(N); D1 = gcd(N, x - 1); D2 = N // D1
        ps = list(fac); allsplits = [ok(A := __import__('math').prod(l for i, l in enumerate(ps) if mask >> i & 1), N // A, e)
                                     for mask in range(1 << len(ps))]
        b = sum(allsplits) / len(allsplits); h = ok(D1, D2, e)
        n += 1; hit += h; base += b
        t = D1 in (1, N) or (N % 2 == 0 and D1 in (2, N // 2)); triv += t
        if not t:
            n_nt += 1; hit_nt += h
            nts = [ok(A, N // A, e) for A in __import__('sympy').divisors(N) if A not in (1, N) and not (N % 2 == 0 and A in (2, N // 2))]
            base_nt += sum(nts) / len(nts) if nts else 0
se = sqrt(base / n * (1 - base / n) / n)
print(f"Pell p<{P2}: slices {n} trivial {triv/n:.4f} Pell hits {hit/n:.4f} all-splittings baseline {base/n:.4f} (binomial s.e. {se:.4f})")
print(f"   nontrivial Pell splits only: {n_nt}, hits {hit_nt/max(n_nt,1):.4f} vs nontrivial-splitting baseline {base_nt/max(n_nt,1):.4f}")

# --- §7 block-witness rates, E = 40
E = 40; B = (E + 1) / 4
small = list(primerange(2, int(B) + 1))
np_ = sol = blk = 0; sl = sl_s = sl_b = 0
for p in primerange(5, P3):
    if p % 24 != 1: continue
    np_ += 1; ps = pb = False
    for e in range(3, E + 1, 4):
        N = (p + e) // 4; fac = factorint(N)
        sfac = {l: k for l, k in fac.items() if l <= B}; P = N
        for l, k in sfac.items(): P //= l ** k
        fs = box_has_minus1(fac, e)
        bf = dict(sfac)
        if P > 1: bf[P] = 1  # P as one block (it may be ≡ 0 mod e only if e | P; gcd(N,e)=1 here)
        fb = box_has_minus1(bf, e)
        assert not fb or fs
        sl += 1; sl_s += fs; sl_b += fb; ps |= fs; pb |= fb
    sol += ps; blk += pb
print(f"Joint p<{P3}, E={E}, slices e≡3(4): primes {np_}, slice success {sl_s/sl:.3f}, block rate {sl_b/sl:.3f}, "
      f"primes solved {sol/np_:.4f}, primes with block witness {blk/np_:.4f}")
