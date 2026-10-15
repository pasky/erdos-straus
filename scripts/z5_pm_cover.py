"""z5_pm_cover.py — primes h ≡ 3 (mod 4) ≤ H whose PM-II firing classes {−4c²d : cd | (h+1)/4} (mod h) contain
every quadratic non-residue mod h (then every PM-II failure is a QR mod h). usage: z5_pm_cover.py H"""
import sys
from sympy import primerange, divisors
H = int(sys.argv[1]); out = []
for h in primerange(3, H + 1):
    if h % 4 != 3: continue
    K = (h + 1) // 4
    cls = {(-4 * c * c * (m // c)) % h for m in divisors(K) for c in divisors(m)}
    qnr = {a for a in range(1, h) if pow(a, (h - 1) // 2, h) == h - 1}
    if qnr <= cls: out.append(h)
print("covering h <=", H, ":", out)
