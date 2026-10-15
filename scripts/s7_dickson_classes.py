"""s7_dickson_classes: admissible all-fail classes for windows m <= M.
For an integer r ≡ 1 (4) coprime to all primes <= M, write K_m = (r+m)/4 = S_m * R_m (S_m = M-smooth part).
'Pretend' R_m is a prime ≡ R_m (mod m). If then every window m <= M (gcd(m,r)=1) fails at cap 0, the class
r mod L (L = 4 * prod_{l<=M} l^{max_m v_l(K_m)+1} * prod m) is an all-fail class: under Dickson's prime k-tuples
conjecture it contains infinitely many primes p with every (p+m)/(4 S_m) prime, hence m0(p) > M.
Usage: python s7_dickson_classes.py M START COUNT
"""
import sys, math
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from s7_window_shuffle import fires_f

def smallprimes(M):
    return [l for l in range(2, M + 1) if all(l % q for q in range(2, int(l ** 0.5) + 1))]

def pretend_fail_all(r, M, SP):
    for m in range(3, M + 1, 4):
        if math.gcd(m, r) != 1:
            continue
        K = (r + m) // 4; fac = {}; R = K
        for l in SP:
            e = 0
            while R % l == 0:
                R //= l; e += 1
            if e:
                fac[l] = e
        if R > 1:
            fac[('P', R % m)] = 1  # pretend prime; only residue matters
        fac2 = {}
        for s, e in fac.items():
            fac2[s if isinstance(s, int) else s[1] + m * 10 ** 9] = e  # residue-preserving stand-in
        if fires_f(fac2, K, m):
            return False
    return True

if __name__ == "__main__":
    M = int(sys.argv[1]); start = int(sys.argv[2]); count = int(sys.argv[3])
    SP = smallprimes(M); found = []
    r = start - (start % 4) + 1
    tested = 0
    while len(found) < 5 and tested < count:
        if all(r % l for l in SP):
            tested += 1
            if pretend_fail_all(r, M, SP):
                found.append(r)
        r += 4
    print("M", M, "tested", tested, "all-fail class representatives:", found)
