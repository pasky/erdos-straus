"""O257: fast coverage test of an adelic point by k-witness classes (slices a <= b <= B).
Point: x = vals[l] at the listed primes l (x = vals[2] as a 2-adic integer), x = 1 at all other primes.
Since e | a+b <= 2b < H = k a b (unless tiny), the class condition H | x + e (Type II) / H | x e + 1 (Type I)
has a unique candidate e in [1, H): e = (-x) mod H resp. (-x^{-1}) mod H; we test e | a+b."""
import sys
from math import gcd
def run(k, vals, B):
    hits = []
    for a in range(1, B + 1):
        for b in range(a, B + 1):
            H = k * a * b
            # x mod H by CRT over the listed primes (x = 1 elsewhere)
            x = 1; m = 1; rest = H
            parts = []
            for l, v in vals.items():
                pe = 1
                while rest % l == 0: rest //= l; pe *= l
                if pe > 1: parts.append((pe, v % pe))
            # combine: x ≡ 1 mod rest, x ≡ v mod pe
            x, m = 1 % rest if rest > 1 else 0, rest
            for pe, v in parts:
                if v % (pe if pe % 2 else 2) == 0 and v % pe == 0: break
                t = ((v - x) * pow(m, -1, pe)) % pe
                x, m = x + m * t, m * pe
            x %= H
            if gcd(x, H) != 1: continue
            s = a + b
            e2 = (-x) % H
            if e2 and s % e2 == 0: hits.append(('II', a, b, e2))
            e1 = (-pow(x, -1, H)) % H
            if e1 and s % e1 == 0: hits.append(('I', a, b, e1))
    return hits
if __name__ == '__main__':
    k = int(sys.argv[1]); B = int(sys.argv[2])
    vals = {int(t.split('=')[0]): int(t.split('=')[1]) for t in sys.argv[3:]}
    h = run(k, vals, B); print(k, vals, 'B', B, 'hits', len(h), h[:6])
