# z8_point.py — is a profinite exponent point mu* of n_s = c0*4^s + k in some ET class / divisor class?
# mu* is given by its residues in the l-adic components: "default value D, and value V_l for listed primes l",
# i.e. mu* = D at every prime l not listed, mu* = V_l in Z_l for listed l (integers suffice for these tests).
# nu(mu*) mod M: 2-part k (mod 2^a); odd part via mu* mod ord_{q^e}(4) by CRT over the prime factors of the order.
# Usage: PYTHONPATH=scripts uv run python scripts/z8_point.py c0 k Mmax D l1:V1 l2:V2 ...
import sys, functools
import mordell_lib as ML
from sympy import n_order, factorint
from sympy.ntheory.modular import crt

c0, k, Mmax, D = map(int, sys.argv[1:5])
V = {int(a.split(':')[0]): int(a.split(':')[1]) for a in sys.argv[5:]}


@functools.lru_cache(None)
def mu_mod(o):
    mods, res = [], []
    for l, e in factorint(o).items():
        mods.append(l ** e); res.append(V.get(l, D) % l ** e)
    return int(crt(mods, res)[0]) if mods else 0


def nu_mod(M):
    a = 0
    while M % 2 == 0:
        M //= 2; a += 1
    rs, ms = [], []
    if a: rs.append(k % 2 ** a); ms.append(2 ** a)
    for q, e in factorint(M).items():
        Q = q ** e
        if c0 % q == 0 and k % q == 0: return None
        o = n_order(4, Q)
        rs.append((c0 * pow(4, mu_mod(o), Q) + k) % Q); ms.append(Q)
    return int(crt(ms, rs)[0]) if ms else 0


hits = 0
# divisor classes: q | nu(mu*)
for q in range(3, 200000, 2):
    if all(q % p for p in range(3, int(q ** .5) + 1, 2)) and nu_mod(q) == 0:
        print('DIVISOR class D_%d contains the point' % q); hits += 1; break
for M in range(3, Mmax + 1):
    if M % 4 and M % 4 != 3: continue
    r = nu_mod(M)
    if r is None: continue
    W = ML.residue_table(M)
    if r in W:
        print('M=%d class %s contains the point (n = %d mod M)' % (M, W[r], r), flush=True); hits += 1
        if hits >= 5: break
print('hits', hits)
