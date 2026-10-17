"""O257: is the adelic point x (x = vals[l] at listed primes l (2-adic: residue mod 2^v taken as the integer vals[2]),
x = 1 at every other prime) covered by some k-witness class (Type I/II, slice a <= b <= B)?  Prints the hits."""
import sys
from sympy import divisors, factorint
from sympy.ntheory.modular import crt
def point_mod(H, vals):
    f = factorint(H); mods = []; res = []
    for l, v in f.items():
        mods.append(l**v); res.append(vals.get(l, 1) % l**v)
    return int(crt(mods, res)[0]) if mods else 0
def hits(k, vals, B):
    out = []
    for a in range(1, B + 1):
        for b in range(a, B + 1):
            H = k * a * b; x = point_mod(H, vals)
            if any(x % l == 0 for l in factorint(H)):
                continue
            for e in divisors(a + b):
                if (x + e) % H == 0: out.append(('II', a, b, e))
                if (x * e + 1) % H == 0: out.append(('I', a, b, e))
    return out
if __name__ == "__main__":
    k = int(sys.argv[1]); B = int(sys.argv[2])
    vals = {int(t.split('=')[0]): int(t.split('=')[1]) for t in sys.argv[3:]}
    h = hits(k, vals, B); print(k, vals, 'B', B, 'hits', len(h), h[:4])
