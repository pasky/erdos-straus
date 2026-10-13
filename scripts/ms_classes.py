"""O197: class structure of f_m(p). Normalise f_m(p) by a smooth fit a*log^3 p + b*log^2 p (least squares over primes
in [lo, hi)), then average the normalised count over classes of p:
  'mod8'   : p mod 8
  'sq840'  : p mod 840 in {1} (class of one) / other square classes / non-squares (square = QR mod 3,5,7 and p = 1 mod 8)
  'kq'     : k = #{q in Q : (p/q) = 1} for Q = odd primes 3..23, split by p mod 8 in {1} vs others
usage: ms_classes.py m lo hi"""
import sys, math
import numpy as np
from ms_stats import load

Q = [3, 5, 7, 11, 13, 17, 19, 23]


def leg(a, q):
    r = pow(a % q, (q - 1) // 2, q)
    return 1 if r == 1 else (-1 if r == q - 1 else 0)


def normalised(m, lo, hi):
    D = load(m)
    ps = sorted(p for p in D if lo <= p < hi and m % p)
    L = np.array([math.log(p) for p in ps]); f = np.array([D[p][0] for p in ps], float)
    A = np.vstack([L ** 3, L ** 2]).T
    coef, *_ = np.linalg.lstsq(A, f, rcond=None)
    return ps, f / (A @ coef), f


def square840(p):
    return p % 8 == 1 and all(leg(p, q) == 1 for q in (3, 5, 7))


if __name__ == '__main__':
    m, lo, hi = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    ps, r, f = normalised(m, lo, hi)
    def show(name, key):
        g = {}
        for p, x in zip(ps, r):
            g.setdefault(key(p), []).append(x)
        print(name + ': ' + ' '.join(f"{k}:{np.mean(v):.2f}(n={len(v)},min={min(v):.2f})" for k, v in sorted(g.items())))
    show('mod8', lambda p: p % 8)
    show('sq840', lambda p: 'one' if p % 840 == 1 else ('sq' if square840(p) else 'non'))
    show('kq(p=1 mod 8)', lambda p: (p % 8 == 1, sum(leg(p, q) == 1 for q in Q)))
    idx = np.argsort(r)[:12]
    print('lowest normalised counts: ' + ' '.join(f"{ps[i]}({int(f[i])},{r[i]:.2f},mod840={ps[i]%840})" for i in idx))
