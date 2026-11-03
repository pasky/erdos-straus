# z55 TDCAL: consecutive-prime inputs gen8/gen12/gen14 (1500/600/150 primes after 10^8/10^12/10^14).
import sys
from sympy import nextprime
out = sys.argv[1]
for e, cnt in [(8, 1500), (12, 600), (14, 150)]:
    p = 10**e; L = []
    while len(L) < cnt:
        p = nextprime(p); L.append(p)
    open(f"{out}/gen{e}.txt", "w").write("\n".join(map(str, L)) + "\n")
