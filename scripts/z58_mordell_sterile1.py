# z58 MORDELL: brute-force check of Lemma S1 — the profinite point x_{l,R} (x = R at l, x = 1 at every other prime)
# lies in no (★) hit class H_d (d ≡ 3 mod 4, d ≤ DMAX) iff ... ; prints, for each odd prime l and R in 1..l-1,
# the smallest d ≤ DMAX with x mod d in H_d (or '-' if none), and whether R ≤ (l-1)/2.
# x mod d for d = l^a m (gcd(m,l)=1) is the CRT of (R mod l^a, 1 mod m).
import sys
from sympy import primerange, legendre_symbol
DMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
LMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 60
def first_hit(l, R):
    for d in range(3, DMAX + 1, 4):
        a, m = 0, d
        while m % l == 0: m //= l; a += 1
        la = d // m
        # x ≡ R (mod la), x ≡ 1 (mod m)
        if la == 1: x = 1 % d
        else:
            # x = 1 + m * t, 1 + m t ≡ R (mod la)
            t = ((R - 1) * pow(m, -1, la)) % la
            x = (1 + m * t) % d
        k = (-x) % d
        if k and ((d + 1) // 4) % k == 0:
            return d
    return None
bad = 0
for l in primerange(3, LMAX):
    row = []
    for R in range(1, l):
        h = first_hit(l, R)
        qnr = legendre_symbol(R, l) == -1
        low = R <= (l - 1) // 2
        if low and h is not None: bad += 1
        row.append(f"{R}{'*' if qnr else ''}:{h if h else '-'}")
    print(f"l={l}: " + " ".join(row), flush=True)
print("violations of Lemma S1 (R <= (l-1)/2 but hit found):", bad)
