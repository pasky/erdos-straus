"""U04 last checks: Z0915 (p(n) mod 2,3 vs U(p) Spearman over primes <= 20000), Z2696 (signed integer points of U_n with
|x|,|y|,|z|<=B for n=p; growth in B), Z1965 (candidate maps phi on the no-witness primes)."""
import json, numpy as np
from scipy.stats import spearmanr
out = {}
# partitions mod 2,3 via pentagonal recurrence (exact ints up to 20000 are huge; use modular recurrence)
N = 20000
def part_mod(m):
    p = [0] * (N + 1); p[0] = 1
    for n in range(1, N + 1):
        s = 0; k = 1
        while True:
            g1 = k * (3 * k - 1) // 2
            if g1 > n: break
            sign = 1 if k % 2 else -1
            s += sign * p[n - g1]
            g2 = k * (3 * k + 1) // 2
            if g2 <= n: s += sign * p[n - g2]
            k += 1
        p[n] = s % m
    return p
P2 = part_mod(2); P3 = part_mod(3)
A = np.loadtxt('data/z52b/raw/f4_all_30000.txt', dtype=np.int64)
def _isp(n): return n > 1 and all(n % q for q in range(2, int(n ** 0.5) + 1))
A = A[A[:, 0] <= N]; A = A[np.array([_isp(int(v)) for v in A[:, 0]])]
A = A[A[:, 0] % 4 == 1]
U = A[:, 1]; pp = A[:, 0]
out["Z0915"] = dict(n=len(pp), spearman_mod2=round(float(spearmanr(U, [P2[int(x)] for x in pp])[0]), 4),
                    spearman_mod3=round(float(spearmanr(U, [P3[int(x)] for x in pp])[0]), 4))
# Z2696: signed integer points on U_n: 4xyz = n(xy+yz+zx), |x|,|y|,|z|<=B, with z = nxy/(4xy - n(x+y)) integral
def count_pts(n, B):
    cnt = 0
    xs = np.arange(-B, B + 1, dtype=np.int64)
    for x in xs:
        if x == 0: continue
        y = xs[xs != 0]
        den = 4 * x * y - n * (x + y)
        ok = den != 0
        num = n * x * y
        z = np.zeros_like(num)
        z[ok] = num[ok] // den[ok]
        good = ok & (num % np.where(ok, den, 1) == 0) & (z != 0) & (np.abs(z) <= B) & (z * den == num)
        cnt += int(good.sum())
    return cnt
out['Z2696'] = {}
for n in (5, 13, 17, 409):
    out['Z2696'][n] = {B: count_pts(n, B) for B in (100, 300, 1000)}
# Z1965: candidate maps on the no-witness primes (C<=30) and whether images are also no-witness primes
hard = [409, 577, 4357, 4789, 5569, 9601, 12301, 18217, 19141]
maps = {'(p+3)/4': lambda p: (p + 3) // 4, '(p-1)/4 odd part': lambda p: ((p - 1) // 4) // (2 ** (((p - 1) // 4) & -((p - 1) // 4)).bit_length() if False else 1),
        'lpf(p+3)': lambda p: max(f for f in range(2, p + 4) if (p + 3) % f == 0 and _isp(f))}
res = {}
for name, f in maps.items():
    imgs = [(p, f(p)) for p in hard]
    res[name] = dict(images=[(a, b, _isp(b), b in hard) for a, b in imgs][:9])
out['Z1965'] = res
json.dump(out, open('data/z52b/pass1/U04/last_checks.json', 'w'), indent=1, default=str)
print(json.dumps(out, default=str))
