# review_r235_k105.py -- R235 independent checks of SIGN_FIELDS §1.4 (OPEN offsets, k = 105 screen, mixed point).
from sympy import primerange, n_order, legendre_symbol, factorint
from math import isqrt


def is_sq(x):
    return x >= 0 and isqrt(x) ** 2 == x


# (a) integer square points 4^l + k = a^2 (l >= 0) and 1 + k 4^a = b^2 (l = -a < 0), a up to 60
for k in [33, 105, 273, 297]:
    pos = [(l, isqrt(4 ** l + k)) for l in range(0, 80) if is_sq(4 ** l + k)]
    neg = [(-a, isqrt(1 + k * 4 ** a)) for a in range(1, 80) if is_sq(1 + k * 4 ** a)]
    print('k=%d square points: pos %s neg %s' % (k, pos, neg))

# (b) k = 105: all members s >= 2 in Mordell hard classes; square mod 3,5,7
H = {1, 121, 169, 289, 361, 529}
occ = set()
for s in range(2, 400):
    r = (4 ** s + 105) % 840
    assert r in H
    occ.add(r)
print('k=105 hard classes occurring:', sorted(occ))


# (c) unit-square screen at L: residues s mod L not killed by any prime q < Q with ord_q(4) | L
def screen(k, L, Q):
    alive = set(range(L))
    used = []
    for q in primerange(3, Q):
        if pow(4, L, q) != 1:
            continue
        o = n_order(4, q)
        kill = set()
        for s in range(o):
            v = (pow(4, s, q) + k) % q
            if v == 0 or legendre_symbol(v, q) == -1:
                kill.add(s)
        if kill:
            alive = {s for s in alive if s % o not in kill}
            used.append(q)
        if not alive:
            break
    return alive, used


al, used = screen(105, 360, 3_000_000)
print('k=105 L=360 unit-square survivors:', sorted(al), 'primes used up to', used[-1] if used else None)
for L in [60, 120, 180, 360, 720]:
    al, _ = screen(33, L, 3_000_000)
    print('k=33 L=%d survivors' % L, sorted(al), [(-2) % L])

# (d) mixed point mu* = 4 off 3, -2 at 3
print('ord_181(4)=', n_order(4, 181), factorint(n_order(4, 181)))
# mu* mod 90: ≡ 4 mod 2, 4 mod 5, -2 mod 9
mu90 = [m for m in range(90) if m % 2 == 0 and m % 5 == 4 and m % 9 == 7][0]
v = (pow(4, mu90, 181) + 105) % 181
print('mu* mod 90 =', mu90, 'n mod 181 =', v, 'legendre', legendre_symbol(v, 181))
o919 = n_order(4, 919)
mu = [m for m in range(o919) if m % 17 == 4 and m % 9 == 7][0]
print('ord_919(4)=', o919, 'mu* mod', o919, '=', mu, 'n mod 919 =', (pow(4, mu, 919) + 105) % 919,
      'II2(2,23,919) residue', (-4 * 4 * 23) % 919, '(919+1)%(4*2*23)=', 920 % 184)
print('124 mod 8,9,5:', 124 % 8, 124 % 9, 124 % 5, ' 844 mod 8,9,5,7:', 844 % 8, 844 % 9, 844 % 5, 844 % 7)
