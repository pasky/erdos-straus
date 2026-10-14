# y8: unclean levels vs admissibly unclean levels (= levels carrying a chi=-1 word).
# Level t of p: N = tp+1; admissible divisors A | N with A = -1 (mod t) (then A* = N/A = -1 automatically).
# unclean: some prime l | N with (l/p) = -1. adm-unclean: some admissible A with (A/p) = -1.
import sys
from sympy import factorint, legendre_symbol as L, isprime, divisors
lo, hi, T = map(int, sys.argv[1:4])
tot=uncl=adm=0; lnrlev=lnrhit=0; firstk={}
for p in range(lo, hi, 4):
    if not isprime(p): continue
    q = next(r for r in range(2, p) if L(r, p) == -1)
    for t in range(1, T+1):
        N = t*p+1; f = factorint(N)
        u = any(L(l % p, p) == -1 for l in f)
        a = u and any(L(A % p, p) == -1 for A in divisors(N) if (A+1) % t == 0)
        tot += 1; uncl += u; adm += a
    # the lnr levels t = t0 + k q (q | tp+1), k = 0..9: first k carrying a chi=-1 word with q || A (odd power)
    t0 = (-pow(p, -1, q)) % q
    for k in range(10):
        t = t0 + k*q
        if t == 0: continue
        N = t*p+1
        if any(L(A % p, p) == -1 for A in divisors(N) if (A+1) % t == 0 and (A % q == 0)):
            firstk[k] = firstk.get(k, 0) + 1; break
    else: firstk['none'] = firstk.get('none', 0) + 1
print(f"levels t<={T}: total {tot}, unclean {uncl} ({uncl/tot:.3f}), carrying a chi=-1 word {adm} ({adm/tot:.3f}); adm/unclean {adm/uncl:.3f}")
print("lnr levels t0+kq: first k with a chi=-1 word whose A contains q:", dict(sorted(firstk.items(), key=str)))
