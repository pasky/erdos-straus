# z52b pass1 U00 — batch 2: checks for Z1513 (QNR lemma), Z1476 (parity), Z3051 (p^3), Z1503 (near-squares), Z0190 (pronic/triangular)
import numpy as np, json
from sympy import factorint, primerange, legendre_symbol, divisors
from collections import Counter
R = '/home/pasky/projects/math/erdos-straus-claude/data/z52b/raw/'
F = np.loadtxt(R + 'f4_all_30000.txt', dtype=np.int64)
Ud = dict(zip(F[:, 0].tolist(), F[:, 1].tolist()))
out = {}
# Z1513: for C-form divisors a of 4Cp+1 with a ≡ -1 (mod 4C), a>1 and cofactor b=(4Cp+1)/a: is (a/p) forced to -1?
P = [p for p in primerange(5, 3000) if p % 4 == 1]
cnt = Counter(); ex = []
for p in P:
    for C in range(1, 301):
        N = 4 * C * p + 1
        for a in divisors(N):
            if a > 1 and a % (4 * C) == (4 * C - 1) % (4 * C) and a != N:
                s = legendre_symbol(a % p, p)
                cnt[s] += 1
                if s == 1 and len(ex) < 8: ex.append((p, C, a))
out['Z1513_cform_divisors_by_legendre'] = {str(k): v for k, v in cnt.items()}
out['Z1513_examples_with_QR'] = ex
# Z1476 / parity: parity of U(p) for primes p ≡ 1 mod 4 ≤ 30000
Pall = [p for p in primerange(5, 30001) if p % 4 == 1]
par = Counter(Ud[p] % 2 for p in Pall)
out['Z1476_parity_U_primes_1mod4'] = {str(k): v for k, v in par.items()}
out['Z1476_parity_U_primes_1mod4_by_mod8'] = {str(r): dict(Counter(Ud[p] % 2 for p in Pall if p % 8 == r)) for r in (1, 5)}
# Z3051: U(p) and U(p^3) for p ≡ 1 mod 4, p^3 ≤ 30000
out['Z3051'] = {str(p): {'U(p)': Ud[p], 'U(p^3)': Ud.get(p ** 3)} for p in primerange(5, 32) if p % 4 == 1}
# Z1503: U(m^2 + 24k) for k=1..5 (n ≡ 1 mod 4 only) vs all n ≡ 1 mod 4 in the same range
vals = {}
for k in range(1, 6):
    v = []
    for m in range(2, 175):
        n = m * m + 24 * k
        if n % 4 == 1 and n in Ud: v.append(Ud[n] / np.log(n) ** 3)
    vals[k] = (len(v), float(np.mean(v)) if v else None)
allv = [Ud[n] / np.log(n) ** 3 for n in range(5, 30001, 4) if n in Ud and n > 100]
out['Z1503'] = {'near_square_means_U_over_log3': vals, 'all_1mod4_mean': float(np.mean(allv))}
# Z0190: pronic (k(k+1)) and triangular (k(k+1)/2) denominators: 4/p = 1/x+1/y+1/z with x,y,z in S, for p ≡ 1 mod 4 ≤ 2000
def solvable(p, S):
    Sset = set(S)
    for x in S:
        if 4 * x < p or x > 3 * p: continue
        # 4/p - 1/x = (4x - p)/(p x) = r/s
        num = 4 * x - p; den = p * x
        if num <= 0: continue
        for y in S:
            if y < x: continue
            # 1/z = num/den - 1/y
            n2 = num * y - den; d2 = den * y
            if n2 <= 0: continue
            if d2 % n2 == 0 and (d2 // n2) in Sset: return True
    return False
pron = [k * (k + 1) for k in range(1, 3000)]
tri = [k * (k + 1) // 2 for k in range(1, 3000)]
Pz = [p for p in primerange(5, 2001) if p % 4 == 1]
fp = [p for p in Pz if not solvable(p, pron)]
ft = [p for p in Pz if not solvable(p, tri)]
out['Z0190'] = {'n_primes': len(Pz), 'pronic_fail_count': len(fp), 'pronic_fail_first': fp[:15],
                'triangular_fail_count': len(ft), 'triangular_fail_first': ft[:15]}
json.dump(out, open('data/z52b/pass1/U00/batch2.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:5000])
