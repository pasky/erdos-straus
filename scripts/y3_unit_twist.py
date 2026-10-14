"""O211 §6: totally-positive-unit-twisted Type II over K = Q(sqrt 2) (eps0 = 1 + sqrt 2, E+ = <3 + 2 sqrt 2>).
Fire+(n, h): h prime, h = 7 (mod 8), exists c, d >= 1 with 8 | 4cd | h + 1 and k >= 0 with
   n + 4c^2 d * rho(3 + 2 sqrt 2)^k = 0 (mod h)      (rho: sqrt 2 -> a fixed root r of r^2 = 2 mod h;
   the other root gives the inverse unit, same subgroup).
Reports, for 5 <= n < P (primes, and odd squares as the T1 control), the least firing h (search h < Hmax), and the
distribution of least h for primes; for squares, any firing at all (expected: never, since (-d/h) = -1).
Also: does genuine ES Type II (any slice, untwisted) fire at the least E+-firing h?  Usage: PYTHONPATH=scripts uv run python scripts/y3_unit_twist.py P Hmax"""
import sys
from sympy import primerange, sqrt_mod, divisors, isprime

def data(Hmax):
    out = []
    for h in primerange(7, Hmax):
        if h % 8 != 7: continue
        r = sqrt_mod(2, h); e = (3 + 2*r) % h
        sub = set(); x = 1
        while True:
            sub.add(x); x = x*e % h
            if x == 1: break
        k = (h + 1)//4
        sl = [(c, cd//c) for cd in divisors(k) if cd % 2 == 0 for c in divisors(cd)]
        # firing residues: -n in 4c^2d * sub
        fire = set(); fire0 = set()
        for c, d in sl:
            X = 4*c*c*d % h
            fire |= {(-X*s) % h for s in sub}
        for cd in divisors(k):  # genuine ES Type II at h: ALL slices 4cd | h+1 (not only even cd)
            for c in divisors(cd): fire0.add((-4*c*c*(cd//c)) % h)
        out.append((h, fire, fire0))
    return out

if __name__ == "__main__":
    P, Hmax = int(sys.argv[1]), int(sys.argv[2]); D = data(Hmax)
    least = {}; nofire = []; es_same = 0; np_ = 0
    for p in primerange(5, P):
        np_ += 1
        for h, fire, fire0 in D:
            if h != p and p % h in fire:
                least[h] = least.get(h, 0) + 1; es_same += (p % h in fire0); break
        else: nofire.append(p)
    sq = [m*m for m in range(3, int(P**.5) + 1, 2) if any(h != 0 and (m*m) % h and (m*m) % h in f for h, f, _ in D)]
    top = sorted(least.items())[:8]
    print(f"P={P}, h<{Hmax}: primes={np_}, no E+-firing h: {len(nofire)} {nofire[:10]}; least-h distribution {top}")
    print(f"  of which the least E+-firing h is also an ES Type II (k=0) modulus: {es_same}; odd squares firing: {len(sq)} {sq[:5]}")
