"""O31 (POINTWISE_TYPEI.md §6): sound (incomplete) search for a finite Type-I covering of
S_r = {p hard : n_p = r}.  A certificate (c,k,D), (D,4ck)=1, sf(c) not in {1,2,3,6}, covers the class
{p = -D (mod 4ck), p^2 = -4ck^2 (mod D)} (Lemma 1.1: M_{c,k}(p)>=1 there).

Restriction (soundness only needs validity of each used certificate): c,k are SMOOTH over the
'small' primes {2,3,..,r}; D = d0*l with d0 | prod small^E and at most one further prime l (exponent 1).
Nodes = residues of p modulo prod small^E (constrained to S_r).  At a node, a certificate with d0 only is
decided; one with a new prime l contributes its roots mod l to E_l.  The node is covered iff some
certificate is decided-true or some E_l is all of (Z/l)^*  (exact for this certificate family, since the
uncovered set at the node is prod_l ((Z/l)^* minus E_l)).
Usage: typei_cover.py r X Dmax  [E2 E3 E5 ...]  -> prints uncovered nodes (if any)."""
import sys, itertools
from math import gcd
from sympy import primerange, factorint, legendre_symbol, sqrt_mod

r, X, Dmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
small = list(primerange(2, r + 1))
Eexp = [int(a) for a in sys.argv[4:]] or [5, 3] + [2] * (len(small) - 2)
mods = [q ** e for q, e in zip(small, Eexp)]
M0 = 1
for m in mods:
    M0 *= m


def sf(c):
    s = 1
    for q, e in factorint(c).items():
        if e % 2:
            s *= q
    return s


def smooth(n):
    for q in small:
        while n % q == 0:
            n //= q
    return n == 1


# certificates
certs = []
for P in range(1, X + 1):
    if not smooth(P):
        continue
    for c in range(1, P + 1):
        if P % c:
            continue
        k = P // c
        s = sf(c)
        if s in (1, 2, 3, 6) or s % r:      # unforced needs r | s (all other small primes are residues)
            continue
        h = 4 * c * k
        for D in range(1, Dmax + 1):
            if gcd(D, h) != 1:
                continue
            d0, rest = 1, D
            for q, e in zip(small, Eexp):
                while rest % q == 0:
                    rest //= q
                    d0 *= q
            if rest > 1 and not (len(factorint(rest)) == 1 and max(factorint(rest).values()) == 1):
                continue
            if rest > 1 and rest in small:
                continue
            # d0 must be determined mod M0 (exponents fit)
            if M0 % d0:
                continue
            certs.append((c, k, D, d0, rest))
print(f"r={r} X={X} Dmax={Dmax} M0={M0} certificates={len(certs)}")
# group certificates by h and d0 for speed
rootcache = {}


def roots(l, a):  # solutions x mod l of x^2 = a
    key = (l, a % l)
    if key not in rootcache:
        rr = sqrt_mod(a % l, l, all_roots=True) or []
        rootcache[key] = frozenset(x for x in rr if x % l)
    return rootcache[key]


def in_Sr(p):
    if p % 24 != 1:
        return False
    for q in small:
        if q in (2, 3):
            continue
        ls = legendre_symbol(p % q, q)
        if (q < r and ls != 1) or (q == r and ls != -1):
            return False
    return True


unc = []
nodes = 0
for p in range(1, M0):
    if gcd(p, M0) != 1 or not in_Sr(p):
        continue
    nodes += 1
    E = {}
    done = False
    for (c, k, D, d0, l) in certs:
        h = 4 * c * k
        if (p + D) % h:
            continue
        if (p * p + 4 * c * k * k) % d0:
            continue
        if l == 1:
            done = True
            break
        E.setdefault(l, set()).update(roots(l, -4 * c * k * k))
        if len(E[l]) == l - 1:
            done = True
            break
    if not done:
        unc.append(p)
print(f"nodes={nodes} uncovered={len(unc)}", unc[:20])
