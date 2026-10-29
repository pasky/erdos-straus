"""z50 lsmass: character data of exceptional points (EVIDENCE for §4).
For the six non-square U-exceptions and the 14 (*)-failure primes <= 1e10 (B1_LINE §3.6 list, as quoted in FRONTIER §4
line 14 plus BM_CORRECTED_COUNT), record the Legendre/Jacobi pattern at odd primes l <= 47 coprime to n and the least
prime l with (n/l) = -1; compare with the distribution over all n == 1 mod 8 (resp. primes == 1 mod 4) in a window."""
import json, math
from sympy import jacobi_symbol, isprime, primerange
PR = [l for l in primerange(3, 48)]
def pattern(n):
    return {l: (jacobi_symbol(n, l) if n % l else 0) for l in PR}
def lqnr(n):
    for l in primerange(3, 10**6):
        if n % l and jacobi_symbol(n, l) == -1: return l
six = [105, 2961, 3985, 25305, 111969, 978145]
star = [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 8813281]
out = {"U_exceptions": {n: {"lqnr": lqnr(n), "frac_plus": sum(1 for l in PR if n % l and jacobi_symbol(n, l) == 1)/sum(1 for l in PR if n % l)} for n in six},
       "star_failures": {p: {"lqnr": lqnr(p)} for p in star}}
# baselines
base = [lqnr(n) for n in range(10**6 + 1, 10**6 + 8 * 20000, 8) if math.isqrt(n)**2 != n]
out["baseline_U_lqnr_mean"] = sum(base)/len(base)
out["baseline_U_frac_lqnr_ge_11"] = sum(1 for b in base if b >= 11)/len(base)
bp = [lqnr(p) for p in range(10**6 + 1, 10**6 + 4 * 50000, 4) if isprime(p)]
out["baseline_prime_lqnr_mean"] = sum(bp)/len(bp)
out["baseline_prime_frac_lqnr_ge_11"] = sum(1 for b in bp if b >= 11)/len(bp)
print(json.dumps(out, indent=1, default=str))
json.dump(out, open("data/z50_lsmass/chars.json", "w"), indent=1, default=str)
