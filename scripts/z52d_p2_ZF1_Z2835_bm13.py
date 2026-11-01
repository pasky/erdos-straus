"""Z2835: at (n,k) = (13,3), 4k + n^3 = 47^2, so the class A = (-q,-d) is unramified (Z52_BANKED §1(a) residue
computation) and lies in Br S_{13,3}.  Test whether it obstructs positive integral points: local invariants of A
at every finite place where a rational point is l-integral (expect all +1 if A obstructs; inv_inf = -1 on positive
points since q, d > 0).  Controls: (n,k) with A ramified (k=3, n=17, 21) should show -1 at some integral places."""
import random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from z52_bank_bm_check import hilbert, primes_of, integral_at
from fractions import Fraction as Fr

def run(n, k, trials, rng, R=400):
    st = {}
    ok = 0
    for _ in range(trials):
        y = rng.randint(-R, R); z = rng.randint(-R, R)
        if rng.random() < 0.5:
            y = Fr(y, rng.randint(1, 30)); z = Fr(z, rng.randint(1, 30))
        q = 4 * Fr(y) - n; d = q * z - n * Fr(y)
        if d == 0 or q == 0: continue
        x = (k + n * Fr(y) * z) / d
        if x == 0: continue
        assert 4 * x * y * z - n * (x * y + y * z + z * x) == k
        prod = hilbert(-q, -d, 0)
        for p in primes_of(x, y, z, q, d, n, k):
            h = hilbert(-q, -d, p); prod *= h
            if integral_at(p, x, y, z):
                key = 'l=2' if p == 2 else ('l|k' if k % p == 0 else ('l|n' if n % p == 0 else 'other odd l'))
                st.setdefault(key, [0, 0]); st[key][0 if h == 1 else 1] += 1
        assert prod == 1
        ok += 1
    return ok, st

rng = random.Random(2835)
for (n, k) in [(13, 3), (17, 3), (21, 3), (13, 2), (13, 7)]:
    ok, st = run(n, k, 20000, rng)
    print(f"(n,k)=({n},{k}) 4k+n^3={4*k+n**3}  points={ok}  [symbol +1, symbol -1] at l-integral places:", st)
