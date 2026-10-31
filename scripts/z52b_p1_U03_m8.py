"""z52b Pass-1 U03 Z1907: failures of 8/p = 1/x+1/y+1/z among odd primes p<=6000 (m8_failure returns True iff NO
representation is found). Sum of 1/(p log p) over failures; also the same for 4/p as control (should be empty)."""
import importlib.util, sys, math
from multiprocessing import Pool
from math import isqrt
spec = importlib.util.spec_from_file_location("fnmod", "scripts/z52b_p1_U03_fn.py")
mod = importlib.util.module_from_spec(spec); sys.argv = ["x", "10"]; spec.loader.exec_module(mod)
def fail(args):
    m, p = args
    from math import gcd
    for x in range(p // m + 1, (3 * p) // m + 1):
        num = m * x - p; den = p * x
        if num <= 0: continue
        g = gcd(num, den); a, b = num // g, den // g
        fb2 = {q: 2 * e for q, e in mod.fac(b).items()}
        for D in mod.divisors(fb2):
            if (D + b) % a == 0 and (b * b // D + b) % a == 0: return (m, p, False)
    return (m, p, True)
if __name__ == "__main__":
    ps = [q for q in range(3, 6001, 2) if all(q % r for r in range(2, isqrt(q) + 1))]
    with Pool(24) as pool:
        res = pool.map(fail, [(8, p) for p in ps] + [(4, p) for p in ps], chunksize=20)
    f8 = [p for m, p, bad in res if m == 8 and bad]; f4 = [p for m, p, bad in res if m == 4 and bad]
    print("Z1907 m=8 failures among odd primes <=6000:", len(f8), f8[:25])
    print("control m=4 failures:", len(f4))
    print("Z1907 sum 1/(p log p) over m=8 failures:", round(sum(1/(p*math.log(p)) for p in f8), 6),
          "; over all odd primes <=6000:", round(sum(1/(p*math.log(p)) for p in ps), 4))
