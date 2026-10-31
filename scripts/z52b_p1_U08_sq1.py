"""z52b pass-1 batch U08, item Z0143: 4/n = 1/x + 1/y + 1/z^2. Extend the z-search for the n <= 300 that failed with z <= 60.
Two-term reduction: a/b = 1/x+1/y with a = 4z^2 - n, b = n z^2, solutions <-> divisors u of b^2 with u ≡ -b (mod a)."""
import json, os
from sympy import divisors
OUT = "data/z52b/pass1/U08"
def two_term(a, b):
    out = []
    for u in divisors(b * b):
        if (u + b) % a:
            continue
        v = (b * b) // u
        if (v + b) % a:
            continue
        out.append(((u + b) // a, (v + b) // a))
    return out
unsolved = [17, 29, 41, 73, 89, 101, 109, 149, 173, 197, 241, 269, 277, 281]
res = {}
for n in unsolved:
    hit = None
    for z in range(61, 3001):
        a = 4 * z * z - n
        if a <= 0:
            continue
        if two_term(a, n * z * z):
            hit = z
            break
    res[n] = hit
    print(n, hit, flush=True)
os.makedirs(OUT, exist_ok=True)
json.dump(res, open(os.path.join(OUT, "z0143_unsolved_ext.json"), "w"), indent=1)
