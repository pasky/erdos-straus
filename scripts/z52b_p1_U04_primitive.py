"""Z0866 check: which primes p<=PMAX have NO primitive ES solution (gcd(x,y,z)=1), x<=y<=z, 4/p=1/x+1/y+1/z.
Method: x in [ceil(p/4), floor(3p/4)]; a'/b' = (4x-p)/(px) reduced; two-term 1/y+1/z=a'/b' <=> d=(a'y-b') | b'^2 with
d = (b'^2/d'), i.e. enumerate divisors d of b'^2 with d = -b' (mod a'), y=(b'+d)/a', z=(b'+b'^2/d)/a'. Early exit per prime.
Memory: divisor lists of b'^2 only (small). Run under ulimit -v 4000000."""
import sys, math, json, time
from sympy import primerange, factorint
from math import gcd
PMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
def divisors_from_fac(fac):
    ds = [1]
    for q, e in fac.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds
def has_primitive(p):
    for x in range((p + 3) // 4, (3 * p) // 4 + 1):
        if 4 * x < p: continue
        a, b = 4 * x - p, p * x
        g = gcd(a, b); a1, b1 = a // g, b // g
        fac = factorint(b1)
        fac2 = {q: 2 * e for q, e in fac.items()}
        for d in divisors_from_fac(fac2):
            if (d + b1) % a1: continue          # need d ≡ -b1 (mod a1)
            dd = b1 * b1 // d
            if (dd + b1) % a1: continue
            y = (d + b1) // a1; z = (dd + b1) // a1
            if y < 1 or z < 1: continue
            if y > z: continue
            x_, y_, z_ = x, y, z
            if gcd(gcd(x_, y_), z_) == 1 and y_ >= x_ and z_ >= y_:
                return True, (x, y, z)
    return False, None
t0 = time.time(); fails = []; ok = 0
for p in primerange(5, PMAX + 1):
    if p % 4 != 1: continue
    # sanity: also ensure x<=y<=z ordering handled by loop (x minimal among triple checked via y>=x, z>=y)
    f, sol = has_primitive(p)
    if f: ok += 1
    else: fails.append(p)
res = {"PMAX": PMAX, "n_p1mod4_checked": ok + len(fails), "n_primitive_ok": ok, "fails": fails,
       "fails_mod12": {r: sum(1 for p in fails if p % 12 == r) for r in (1, 5, 9)},
       "fails_mod_12_counts_by_class_all": {}, "seconds": round(time.time() - t0, 1)}
print(json.dumps(res))
json.dump(res, open(f"data/z52b/pass1/U04/primitive_check_{PMAX}.json", "w"), indent=1)
