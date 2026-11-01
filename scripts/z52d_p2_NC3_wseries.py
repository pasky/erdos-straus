# Z3026: W(q) = sum_{t,u,v>=2} q^{tuv-u-v} (all words, all levels; FRONTIER §2.3 identity). Coefficients c(n) = #words with
# tuv-u-v = n. Mod 2 / mod 3 structure: density, residues, and a few 'lacunary' tests (are odd n supported on a square-type set?).
import sys, numpy as np
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
c = np.zeros(N+1, dtype=np.int64)
for u in range(2, N+3):
    for v in range(2, N+3):
        e0 = -u - v
        if 2*u*v + e0 > N: break
        uv = u*v
        t = 2
        while True:
            n = t*uv + e0
            if n > N: break
            c[n] += 1; t += 1
np.save('data/z52b/pass2/NC3/wseries_c_%d.npy' % N, c)
odd = np.nonzero(c[1:] % 2)[0] + 1
print("N", N, "total words", int(c.sum()), "odd-coefficient count", len(odd), "density", round(len(odd)/N, 4))
print("first odd n:", odd[:40].tolist())
# test: is n odd-coefficient iff 8n+1 or 4n+1 or 2n+1 is a square/triangular type?  check mod classes
def issq(x): 
    r = int(round(x**0.5)); return r*r == x
for name, f in [("8n+1 square", lambda n: issq(8*n+1)), ("4n+1 square", lambda n: issq(4*n+1)), ("n square", lambda n: issq(n)), ("n+1 square", lambda n: issq(n+1))]:
    ncls = sum(1 for n in range(2, 20000) if f(n))
    hit = sum(1 for n in range(2, 20000) if f(n) and c[n] % 2)
    print(f"{name}: class size {ncls}, of which odd-coefficient {hit}")
# residue distribution of odd n mod 24
from collections import Counter
print("odd coefficient residues mod 24 (counts):", sorted(Counter(int(n) % 24 for n in odd).items())[:24])
