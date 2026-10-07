# O89 (POINTWISE_TYPEI4.md §1): check the Pell reformulation on near misses from
#   typei3_nmdump 7 9 X > file      (rows: c k alpha gamma t F e d)
# For each oriented (F<e) near miss with L=alpha+2*gamma>=5:
#   delta=(e-F)/(16 n), c_o, k_o odd parts, M=c_o*delta^2+2^(L-4) (L>=4), d=c_o*M,
#   A=(F+e)/2; check A^2 - d*(8 k_o)^2 == 1, and record the sign pattern of A modulo the
#   odd prime factors of d (A = +-1 mod q^{v_q(d)}).
# Usage: PYTHONPATH=scripts uv run --with sympy python scripts/typei4_pell.py file [L_min]
import sys
from sympy import factorint

def odd(x):
    while x % 2 == 0: x //= 2
    return x

def v2(x):
    e = 0
    while x % 2 == 0: x //= 2; e += 1
    return e

rows = [list(map(int, l.split())) for l in open(sys.argv[1])]
Lmin = int(sys.argv[2]) if len(sys.argv) > 2 else 5
bad = 0; seen = 0
for c, k, al, ga, t, F, e, dd in rows:
    L = al + 2 * ga
    if F >= e or L < Lmin: continue
    co, ko = odd(c), odd(k); n = co * ko
    assert (e - F) % (16 * n) == 0
    delta = (e - F) // (16 * n)
    M = co * delta * delta + 2 ** (L - 4)
    d = co * M
    A = (F + e) // 2
    ok = A * A - d * (8 * ko) ** 2 == 1
    if not ok: bad += 1
    pat = []
    for q, ex in sorted(factorint(d).items()):
        qe = q ** ex
        s = '+' if (A - 1) % qe == 0 else ('-' if (A + 1) % qe == 0 else '?')
        tag = 'c' if co % q == 0 else 'M'
        pat.append(f"{q}^{ex}{tag}{s}")
    seen += 1
    print(c, k, 'L', L, 't', t, 'delta', delta, 'v2(F+9)', dd, 'd%8', d % 8, 'pell', ok, ' '.join(pat))
print('# rows', seen, 'pell failures', bad)
