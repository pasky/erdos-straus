"""O72: stand-alone exact checker for a Type-I certificate (c,k,F) at the sign point
x = (w at 2; -1 at r; 1 at every other prime).  Usage: typei3_verify.py r w c k F
Checks: v_r(c) odd; N=1+4ck^2, F | N; F = -1 mod (odd r-free part of ck); F = 1 mod r^{v_r(ck)};
F = -w mod 2^{v_2(4ck)}.  (Then sf(c) is divisible by r, so s not in {1,2,3,6}.)"""
import sys

def v(p, n):
    e = 0
    while n % p == 0:
        n //= p; e += 1
    return e

def check(r, w, c, k, F):
    N = 1 + 4 * c * k * k
    h = 4 * c * k
    t = v(2, h); vr = v(r, c * k)
    mp = h >> t
    mp //= r ** vr
    ok = {
        'v_r(c) odd': v(r, c) % 2 == 1,
        'F | N': N % F == 0,
        'F = -1 mod m_prime': (F + 1) % mp == 0,
        'F = 1 mod r^v': (F - 1) % (r ** vr) == 0,
        'F = -w mod 2^t': (F + w) % (2 ** t) == 0,
    }
    return ok, dict(N=N, t=t, v=vr, mprime=mp)

if __name__ == '__main__':
    r, w, c, k, F = map(int, sys.argv[1:6])
    if min(r, c, k, F) <= 0:
        sys.exit('r, c, k, F must be positive')
    ok, info = check(r, w, c, k, F)
    print(info)
    for key, val in ok.items():
        print(f'{key}: {val}')
    print('CERTIFICATE' if all(ok.values()) else 'NOT a certificate')
    sys.exit(0 if all(ok.values()) else 1)
