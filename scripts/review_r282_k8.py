"""R282 from-scratch: k-union census over primes via words (Cor 1.2): fails iff no word coordinate = 0 mod k."""
import sys
from sympy import primerange
PB = int(sys.argv[1]); K = int(sys.argv[2])
fails = []; c1f = []; b1f = []
for p in primerange(3, PB):
    anyt = anyv = False
    for t in range(1, p + 3):
        u = 1
        while True:
            den = t*u - 1
            if den > p + u: break
            if den > 0 and (p + u) % den == 0:
                v = (p + u)//den
                if t % K == 0: anyt = True
                if v % K == 0 or u % K == 0: anyv = True
            u += 1
        if anyt and anyv: break
    if not anyt: c1f.append(p)
    if not anyv: b1f.append(p)
    if not (anyt or anyv): fails.append(p)
print(f"k={K}, primes 3<=p<{PB}: union failures {len(fails)}: {fails[:40]}")
print(f"  c=1 failures {len(c1f)} (first {c1f[:20]}); b=1 failures {len(b1f)} (first {b1f[:12]})")
