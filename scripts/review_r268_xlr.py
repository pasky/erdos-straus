"""R268 from-scratch: which non-residues r mod l make the point x_{l,r} (x = r in Z_l, x = 1 in Z_q for q != l)
lie in some numerator-k Type I/II witness class (slice a <= b <= B, c | a + b, e = (a+b)/c, modulus H = k a b):
Type II: H | x + e;  Type I: H | x e + 1  (x the integer = x_{l,r} mod H)."""
import sys
from sympy.ntheory.modular import crt
from sympy import primerange


def xmod(H, l, r):
    v = 0; t = H
    while t % l == 0: t //= l; v += 1
    if v == 0: return 1 % H
    L = l ** v
    return int(crt([L, t], [r % L, 1])[0]) if t > 1 else r % L


def covered(k, l, B):
    nr = [r for r in range(2, l) if pow(r, (l - 1) // 2, l) == l - 1]
    cov = set()
    for a in range(1, B + 1):
        for b in range(a, B + 1):
            H = k * a * b
            for c in range(1, a + b + 1):
                if (a + b) % c: continue
                e = (a + b) // c
                for r in nr:
                    if r in cov: continue
                    x = xmod(H, l, r)
                    if (x + e) % H == 0 or (x * e + 1) % H == 0: cov.add(r)
    return nr, sorted(cov)


if __name__ == "__main__":
    B = int(sys.argv[1])
    for k in (4, 8):
        for l in primerange(3, 20):
            if k % l == 0: continue
            nr, cov = covered(k, l, B)
            print(f"k={k} l={l}: non-residues {nr}; covered {cov}; r=2 covered: {2 in cov}")
