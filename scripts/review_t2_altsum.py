"""R24 from-scratch brute force for EXCEPTIONAL_TUPLES2 (1.3), Cor 1.2, Thm 4.1.

Small y, N.  Prime family l = 3 mod 4, l <= y, classes R(l) = {-4D mod l : D | A^2}.
Representatives: residue -1 -> form (1,1); otherwise the form (r,s) (rsm = A, gcd = 1,
-r/s = residue) with smallest (r*s, r).
Checks:
 (i)  Cor 1.2: for every n <= N, the hit set H(n) has every form-group admissible
      (=> every inadmissible tuple has C_T(N) = 0).
 (ii) (1.3): S_j(N) = sum over admissible j-tuples of C_T(N)   (via per-n subset counts).
 (iii) Euler char.: sum_j (-1)^j e_j^A  ==  E_CRT a(H),  a(H) = prod_phi chi_phi(H_phi),
      computed independently (tuple enumeration vs. configuration enumeration).
 (iv) prints e_j, e_j^A, Z_j, S_j/N and the alternating sums.
Usage: review_t2_altsum.py y N
"""
import sys, itertools
from math import gcd, comb, prod
from fractions import Fraction
from sympy import primerange, divisors

y = int(sys.argv[1]); N = int(sys.argv[2])
primes = [l for l in primerange(3, y + 1) if l % 4 == 3]
cls = {}  # l -> list of (residue, (r,s))
for l in primes:
    A = (l + 1) // 4
    forms = {}
    for r in divisors(A):
        for s in divisors(A // r):
            if gcd(r, s) == 1:
                b = (-r * pow(s, -1, l)) % l
                forms.setdefault(b, []).append((r, s))
    lst = []
    for b, fl in forms.items():
        if b == l - 1:
            assert (1, 1) in fl
            f = (1, 1)
        else:
            f = min(fl, key=lambda t: (t[0] * t[1], t[0]))
        lst.append((b, f))
    cls[l] = sorted(lst)

def admissible(pairs):
    """pairs: list of (l, (r,s)). Admissible iff for every form, prod l <= N s + r."""
    g = {}
    for l, f in pairs:
        g[f] = g.get(f, 1) * l
    return all(q <= N * f[1] + f[0] for f, q in g.items())

# (i),(ii): interval side
J = len(primes)
S = [0] * (J + 1); SA = [0] * (J + 1); bad_i = 0
for n in range(1, N + 1):
    H = []
    for l in primes:
        for b, f in cls[l]:
            if n % l == b:
                H.append((l, f))
    if not admissible(H):
        bad_i += 1
    for j in range(len(H) + 1):
        S[j] += comb(len(H), j)
    for k in range(len(H) + 1):
        for T in itertools.combinations(H, k):
            if admissible(list(T)):
                SA[k] += 1
print(f"y={y} N={N} primes={primes}")
print("(i) n with an inadmissible hit-group:", bad_i)
print("(ii) S_j == sum_adm C_T for all j:", S == SA)

# (iii),(iv): CRT side, exact rationals.  Enumerate configurations H (<=1 class per prime).
opts = [[None] + [(l, f) for b, f in cls[l]] for l in primes]
ncfg = prod(len(o) for o in opts)
print("configurations:", ncfg)
e = [Fraction(0)] * (J + 1); eA = [Fraction(0)] * (J + 1); Ea = Fraction(0)
for cfg in itertools.product(*opts):
    T = [c for c in cfg if c is not None]
    d = Fraction(1, prod(l for l, f in T)) if T else Fraction(1)
    e[len(T)] += d
    if admissible(T):
        eA[len(T)] += d
    # probability of H == T under CRT law
    pH = prod(Fraction(1, l) if c is not None else Fraction(l - len(cls[l]), l)
              for l, c in zip(primes, cfg))
    groups = {}
    for l, f in T:
        groups.setdefault(f, []).append((l, f))
    a = 1
    for f, G in groups.items():
        chi = sum((-1) ** k for k in range(len(G) + 1)
                  for U in itertools.combinations(G, k) if admissible(list(U)))
        a *= chi
    Ea += pH * a
alt = sum((-1) ** j * eA[j] for j in range(J + 1))
altfull = sum((-1) ** j * e[j] for j in range(J + 1))
P0 = prod(Fraction(l - len(cls[l]), l) for l in primes)
print("(iii) sum(-1)^j e_j^A == E a(H):", alt == Ea, float(alt), float(Ea))
print("     sum(-1)^j e_j (full) =", float(altfull), " Pi(1-p) =", float(P0))
avoid = sum(1 for n in range(1, N + 1) if all(n % l != b for l in primes for b, f in cls[l]))
print("     #{f=0}/N =", avoid / N, "  sum(-1)^j S_j/N =", sum((-1) ** j * S[j] for j in range(J + 1)) / N)
print(" j   e_j        e_j^A      Z_j        S_j/N      S_j/(N e_j^A)")
for j in range(J + 1):
    if e[j] == 0:
        continue
    r = S[j] / (N * float(eA[j])) if eA[j] else float('nan')
    print(f"{j:2d} {float(e[j]):.4e} {float(eA[j]):.4e} {float(e[j]-eA[j]):.4e} {S[j]/N:.4e} {r:.4f}")

# (v) Thm 4.1 intermediate inequality (no epsilon hypothesis needed):
#   E a(H) - P(H=empty) <= Pi(1-p) [ prod_phi (1 + sum_{k>=u1} e_k(w_phi)) - 1 ],
#   w_phi = (4/l) over primes l <= y, l = -1 mod 4rs;  u1 = floor(log N/log y)+1.
from math import log, floor
u1 = floor(log(N) / log(y)) + 1
formset = set(f for l in primes for b, f in cls[l])
brk = Fraction(1)
for (r, s) in formset:
    ws = [Fraction(4, l) for l in primes if (l + 1) % (4 * r * s) == 0]
    c = [Fraction(1)] + [Fraction(0)] * len(ws)
    for w in ws:
        for k in range(len(ws), 0, -1):
            c[k] += w * c[k - 1]
    brk *= 1 + sum(c[u1:])
lhs = Ea - P0
rhs = P0 * (brk - 1)
print(f"(v) u1={u1}: E a(H)-P(H=0) = {float(lhs):.4e} <= {float(rhs):.4e} : {lhs <= rhs};  "
      f"lower side -rhs <= lhs: {-rhs <= lhs}")
