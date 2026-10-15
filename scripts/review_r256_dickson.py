"""R256 from-scratch check of the Dickson all-fail classes (s7_dickson_classes claim).

For r and M: L = 4 * prod_{l<=M} l^(max_m v_l(K_m)+1) * prod_m m.  Forms f_0(t) = L t + r, f_m(t) = (L t + r + m)/(4 S_m)
(S_m = M-smooth part of K_m = (r+m)/4).  If all forms are prime at t, then K_m(t) = S_m * prime with prime = R_m (mod m),
and we check that no window m <= M (m = 3 mod 4) fires: -K_m not in {d mod m : d | K_m^2}.
Also checks Dickson admissibility of the forms for all primes l <= 500.
usage: review_r256_dickson.py M r [r ...]
"""
import sys
from math import gcd, prod


def primes(n):
    return [l for l in range(2, n + 1) if all(l % q for q in range(2, int(l**.5) + 1))]


def vl(x, l):
    e = 0
    while x % l == 0:
        x //= l; e += 1
    return e


def check(M, r):
    SP = primes(M)
    assert r % 4 == 1 and all(r % l for l in SP)
    ms = list(range(3, M + 1, 4))
    data = {}
    for m in ms:
        K = (r + m)//4
        S = prod(l**vl(K, l) for l in SP)
        data[m] = (K, S, K//S)
    L = 4*prod(l**(max(vl(data[m][0], l) for m in ms) + 1) for l in SP)*prod(ms)
    fires = []
    for m in ms:
        K, S, R = data[m]
        res = {1}
        for l in SP:
            e = vl(S, l)
            if e:
                res = {(x*pow(l, j, m)) % m for x in res for j in range(2*e + 1)}
        res = {(x*pow(R, j, m)) % m for x in res for j in range(3)}   # R prime (or 1): d-part R^0..R^2
        # residue of rough part along the progression is constant:
        assert (L//(4*S)) % m == 0 and all((L//(4*S)) % l == 0 for l in SP)
        if (-K) % m in res:
            fires.append(m)
    # admissibility of the system {f_0} u {f_m}
    forms = [(L, r)] + [(L//(4*data[m][1]), data[m][2]) for m in ms]
    bad = [l for l in primes(500) if all(any((a*t + b) % l == 0 for a, b in forms) for t in range(l))]
    return fires, bad, len(forms), L


if __name__ == '__main__':
    M = int(sys.argv[1])
    for r in map(int, sys.argv[2:]):
        fires, bad, nf, L = check(M, r)
        print(f'M={M} r={r}: firing windows {fires}  non-admissible primes {bad}  #forms {nf}  log10 L = {len(str(L))-1}')
