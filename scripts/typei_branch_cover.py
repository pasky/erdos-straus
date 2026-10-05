"""O31 (POINTWISE_TYPEI.md §6.2): branching search for a finite Type-I covering of
S_r = {p : p = 1 (24), (p/l)=1 for 5<=l<r, (p/r)=-1}  (= hard primes with n_p = r).

Certificate (c,k,F): (F,4ck)=1, sf(c) not in {1,2,3,6}; it covers {p = -F (mod 4ck), p^2 = -4ck^2 (mod F)}
(Lemma 1.1 / ET Prop 1.9 family 3 / Salez (15d)); on it M_{c,k}(p) >= 1, so ck_min(p) <= ck.

Search: the residue of p is fixed modulo M0 = prod_{l<=r} l^{E_l} (base nodes, restricted to S_r), then
branched prime by prime over 'new' primes q in (r, Qmax] (exponent 1).  At a node, a certificate whose
primes (of 4ck and F) are all assigned is decided; if exactly one prime l of F is unassigned (exponent 1),
it covers the roots of x^2 = -4ck^2 (mod l): these go into E_l.  The node is covered iff a decided
certificate holds or some unassigned l has E_l = (Z/l)^*.  Otherwise branch on an unassigned new prime q
over the residues NOT in E_q (those are covered).  Only certificates with ck<=X, F<=Fmax, 4ck with
l^2 | 4ck only for l<=r, and F's new-prime part squarefree are used (sound restriction).

Output: either 'COVERED' with the certificate tree written to a JSON file (checked by
typei_cover_check.py), or the list of uncovered leaves (classes mod M0*prod q) = escape candidates."""
import sys, json, time
from math import gcd

r, X, Fmax, Qmax = (int(a) for a in sys.argv[1:5])
Eexp = [int(a) for a in sys.argv[5].split(',')]          # exponents for primes 2,3,5,...,r
out = sys.argv[6] if len(sys.argv) > 6 else None
maxleaves = 50


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(n ** .5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


N = max(Fmax, 4 * X) + 1
spf = list(range(N))
for i in range(2, int(N ** .5) + 1):
    if spf[i] == i:
        for j in range(i * i, N, i):
            if spf[j] == j:
                spf[j] = i


def fac(n):
    f = {}
    while n > 1:
        q = spf[n]
        f[q] = f.get(q, 0) + 1
        n //= q
    return f


small = primes_upto(r)
assert len(Eexp) == len(small)
SM = {q: q ** e for q, e in zip(small, Eexp)}
newp = [q for q in primes_upto(Qmax) if q > r]


def leg(a, q):
    a %= q
    return 0 if a == 0 else (1 if pow(a, (q - 1) // 2, q) == 1 else -1)


def sf(c):
    s = 1
    for q, e in fac(c).items():
        if e % 2:
            s *= q
    return s


# slices: (c,k) with ck<=X, unforced-capable (core not made only of primes < r), prime-power fit
slices = []
for P in range(1, X + 1):
    fP = fac(4 * P)
    if any(e > 1 and q > r for q, e in fP.items()):
        continue
    if any(q <= r and q ** e > SM[q] for q, e in fP.items()):
        continue
    if any(q > Qmax for q in fP):
        continue
    for c in range(1, P + 1):
        if P % c:
            continue
        k = P // c
        s = sf(c)
        if s in (1, 2, 3, 6) or all(q < r for q in fac(s)):
            continue
        slices.append((c, k, 4 * c * k, set(fP)))
print(f"r={r} X={X} Fmax={Fmax} Qmax={Qmax} E={Eexp} slices={len(slices)}", flush=True)

# F table: factorisation; allowed: F odd, new-prime part squarefree, small part fits SM
Finfo = [None] * (Fmax + 1)
for F in range(1, Fmax + 1, 2):
    f = fac(F)
    if any(q > r and e > 1 for q, e in f.items()):
        continue
    if any(q <= r and q ** e > SM[q] for q, e in f.items()):
        continue
    Finfo[F] = f


def crt_add(res, mod, a, m):
    # combine x=res (mod), x=a (m), coprime
    t = ((a - res) * pow(mod, -1, m)) % m
    return res + mod * t, mod * m


sqrt_cache = {}


def roots(l, a):
    a %= l
    key = (l, a)
    if key not in sqrt_cache:
        sqrt_cache[key] = frozenset(x for x in range(1, l) if (x * x - a) % l == 0)
    return sqrt_cache[key]


stats = {'nodes': 0, 'leaves': 0}
uncovered = []


def solve(p, M, assigned):
    """p mod M is fixed; assigned = set of primes whose residue is fixed. Returns certificate tree or None."""
    stats['nodes'] += 1
    E = {}
    for (c, k, h, hp) in slices:
        if not hp <= assigned:
            continue
        t = (-p) % h
        if t == 0:
            continue
        F = t
        while F <= Fmax:
            f = Finfo[F]
            if f is not None and gcd(F, h) == 1:
                ok, new = True, []
                for q, e in f.items():
                    if q in assigned:
                        if (p * p + 4 * c * k * k) % (q ** e):
                            ok = False
                            break
                    else:
                        new.append(q)
                if ok:
                    if not new:
                        return {'cert': [c, k, F]}
                    if len(new) == 1:
                        l = new[0]
                        R = roots(l, -4 * c * k * k)
                        if R:
                            El = E.setdefault(l, {})
                            for x in R:
                                El.setdefault(x, [c, k, F])
                            if len(El) == l - 1:
                                return {'split': l, 'all': {str(x): v for x, v in El.items()}}
            F += h
    # branch
    cand = [q for q in newp if q not in assigned]
    if not cand:
        stats['leaves'] += 1
        if len(uncovered) < maxleaves:
            uncovered.append((p, M))
        return None
    q = max(cand[:6], key=lambda l: len(E.get(l, {})) / (l - 1))
    El = E.get(q, {})
    node = {'split': q, 'all': {str(x): v for x, v in El.items()}, 'sub': {}}
    good = True
    for x in range(1, q):
        if x in El:
            continue
        p2, M2 = crt_add(p, M, x, q)
        sub = solve(p2, M2, assigned | {q})
        if sub is None:
            good = False
            if len(uncovered) >= maxleaves:
                return None
            continue
        node['sub'][str(x)] = sub
    return node if good else None


M0 = 1
for q in small:
    M0 *= SM[q]
t0 = time.time()
tree = {}
allgood = True
for p in range(1, M0, 2):
    if gcd(p, M0) != 1 or p % 24 != 1:
        continue
    if any(leg(p, q) != 1 for q in small if 5 <= q < r) or leg(p, r) != -1:
        continue
    sub = solve(p, M0, set(small))
    if sub is None:
        allgood = False
        if len(uncovered) >= maxleaves:
            break
    else:
        tree[str(p)] = sub
print(f"nodes={stats['nodes']} uncovered leaves={stats['leaves']} time={time.time()-t0:.0f}s", flush=True)
if allgood:
    print("COVERED")
    if out:
        json.dump({'r': r, 'E': Eexp, 'M0': M0, 'tree': tree}, open(out, 'w'))
else:
    print("NOT COVERED; first uncovered classes (p mod M):", uncovered[:10])
