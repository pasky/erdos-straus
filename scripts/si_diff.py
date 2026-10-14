"""si_diff: for words w of odd n <= NMAX, the pair (i, j) in C0(L_w) with Gram T_w = [[A*,1],[1,A]] (det tn) generates
the quaternion algebra (-A*, -t n A*) (CONSTRUCTIVE Prop 4.1(b)). Check: its finite ramification set Diff(T_w) equals
{2 if chi=+1} U {l | n : (-A/l)^{v_l(n)} = -1}, has odd size, and T_w = t*diag(v,u) - [[1,-1],[-1,1]].
usage: si_diff.py NMAX"""
import sys
from sympy import factorint, jacobi_symbol as J


def hilbert(a, b, p):
    # Hilbert symbol (a,b)_p for p prime (incl. 2), a,b nonzero integers
    def split(x):
        v = 0
        while x % p == 0:
            x //= p; v += 1
        return v, x
    va, ua = split(a); vb, ub = split(b)
    if p != 2:
        s = (-1) ** (va * vb * ((p - 1) // 2) % 2)
        s *= J(ua % p, p) ** vb * J(ub % p, p) ** va
        return s
    eps = lambda u: ((u - 1) // 2) % 2
    om = lambda u: ((u * u - 1) // 8) % 2
    e = eps(ua) * eps(ub) + va * om(ub) + vb * om(ua)
    return (-1) ** (e % 2)


N = int(sys.argv[1])
cnt = bad = 0
for n in range(3, N + 1, 2):
    fn = factorint(n)
    for u in range(1, n + 3):
        for v in range(1, n + 3):
            if u * v > n + u + v:
                break
            if (n + u + v) % (u * v):
                continue
            t = (n + u + v) // (u * v)
            A, As = t * u - 1, t * v - 1
            T = [[As, 1], [1, A]]
            assert T == [[t * v - 1, 1], [1, t * u - 1]] and As * A - 1 == t * n
            a, b = -As, -t * n * As
            primes = set(factorint(abs(a)).keys()) | set(factorint(abs(b)).keys()) | {2}
            diff = {p for p in primes if hilbert(a, b, p) == -1}
            chi = J((-A) % n, n)
            pred = ({2} if chi == 1 else set()) | {l for l, e in fn.items() if J((-A) % l, l) ** e == -1}
            cnt += 1
            if diff != pred or len(diff) % 2 == 0:
                bad += 1
print(f"words={cnt} mismatches={bad}")
