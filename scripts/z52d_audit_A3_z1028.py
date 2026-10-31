"""z52d audit A3, Z1028: character expansion of #{d | N : d = -1 (mod 12)} for N = 12p+1 (level t=12, C=3).
(Z/12)^* = {1,5,7,11} is elementary 2-group: chars 1, chi_{-4} (odd), chi_{-3} (odd), chi_{12} (even).
D^-(N) = (1/4) sum_chi chi(-1) sigma_chi(N) = (tau - s_{-4} - s_{-3} + s_{12})/4 ; compare with enumeration."""
from sympy import divisors, primerange
def chi(a, d):  # characters mod 12 on d coprime to 6
    r = d % 12
    c4 = 1 if r % 4 == 1 else -1; c3 = 1 if r % 3 == 1 else -1
    return {1: 1, -4: c4, -3: c3, 12: c4 * c3}[a]
bad = zero = tot = 0; zero_pattern = {}
for p in primerange(5, 10**5):
    N = 12 * p + 1; ds = divisors(N)
    direct = sum(1 for d in ds if d % 12 == 11)
    s = {a: sum(chi(a, d) for d in ds) for a in (1, -4, -3, 12)}
    via = (s[1] - s[-4] - s[-3] + s[12])
    assert via % 4 == 0
    bad += (via // 4 != direct); tot += 1
    if direct == 0:
        zero += 1
        key = (s[-4] == s[1], s[-3] == s[1], s[12] == s[1]); zero_pattern[key] = zero_pattern.get(key, 0) + 1
print("primes", tot, "mismatches", bad, "zeros of D^-(12p+1)", zero)
print("zero pattern (sigma_-4==tau, sigma_-3==tau, sigma_12==tau): count", zero_pattern)
