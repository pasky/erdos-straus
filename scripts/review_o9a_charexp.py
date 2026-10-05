"""R34a from-scratch check of the character expansion in OMEGA9 Thm 1.1.

For random small (Q, {d_i}, {b_i}, {c_i}) with gcd(d_i,Q)=1, gcd(b_i,d_i)=1:
  * build ALL characters mod N=QD by brute force (prime-power generators),
  * compute c(chi) = phi(N)^-1 sum_{n in G} f(n) conj(chi(n)), f = B * 1[n=1 mod Q],
  * check c(chi) = E_D[B conj(chi_D)]/phi(Q),
  * check c(chi)!=0 => cond(chi_D) | some d_i, cond(chi) <= Z,
  * check |c(chi)| <= E_D|B|/phi(Q), c(chi0) = mu/phi(Q),
  * check #supp <= Z^2 and injectivity chi -> chi* (distinct conductor/primitive pairs),
  * check mu = sum c_i/phi(d_i), mu_psi (PO def) = E_D[B psi] for real chi_D.
"""
import cmath
import itertools
import math
import random

from sympy import factorint, primitive_root, totient


def gens_prime_power(p, k):
    """Return list of (generator g, order) for (Z/p^k)^*, as residues mod p^k."""
    m = p ** k
    if p == 2:
        if k == 1:
            return []
        if k == 2:
            return [(m - 1, 2)]
        return [(m - 1, 2), (5, 2 ** (k - 2))]
    return [(primitive_root(m), (p - 1) * p ** (k - 1))]


def dlog_table(N):
    """Map n (unit mod N) -> exponent vector wrt generators lifted via CRT."""
    fac = factorint(N)
    comps = []  # (modulus, [(g, ord)])
    for p, k in fac.items():
        comps.append((p ** k, gens_prime_power(p, k)))
    gens = []  # (modulus m, g, ord)
    for m, gl in comps:
        for g, o in gl:
            gens.append((m, g, o))
    # for each component, table residue -> exponents
    tables = []
    for m, gl in comps:
        tab = {}
        ranges = [range(o) for _, o in gl]
        for es in itertools.product(*ranges):
            r = 1
            for (g, _), e in zip(gl, es):
                r = r * pow(g, e, m) % m
            tab[r] = es
        tables.append((m, tab))
    units = [n for n in range(N) if math.gcd(n, N) == 1]
    dl = {}
    for n in units:
        v = []
        for m, tab in tables:
            v.extend(tab[n % m])
        dl[n] = tuple(v)
    orders = [o for (_, _, o) in gens]
    return units, dl, orders


def all_chars(N):
    units, dl, orders = dlog_table(N)
    chars = []
    for ks in itertools.product(*[range(o) for o in orders]):
        vals = {}
        for n in units:
            ang = sum(k * e / o for k, e, o in zip(ks, dl[n], orders))
            vals[n] = cmath.exp(2j * math.pi * ang)
        chars.append(vals)
    return units, chars


def conductor(chi, N, units):
    for f in sorted(d for d in range(1, N + 1) if N % d == 0):
        if all(abs(chi[n] - 1) < 1e-9 for n in units if n % f == 1 % f):
            return f
    raise AssertionError


def run(seed):
    rnd = random.Random(seed)
    Q = rnd.choice([3, 4, 5, 7, 8])
    pool = [d for d in range(2, 40) if math.gcd(d, Q) == 1]
    ds = rnd.sample(pool, rnd.randint(1, 3))
    D = 1
    for d in ds:
        D = D * d // math.gcd(D, d)
    N = Q * D
    if N > 700:
        return None
    cells = []
    for d in ds:
        for _ in range(rnd.randint(1, 2)):
            b = rnd.choice([b for b in range(1, d + 1) if math.gcd(b, d) == 1])
            cells.append((d, b, rnd.uniform(-2, 2)))
    B = lambda n: sum(c for d, b, c in cells if n % d == b % d)
    phi = lambda n: int(totient(n))
    unitsD = [n for n in range(D) if math.gcd(n, D) == 1]
    ED_B = sum(B(n) for n in unitsD) / len(unitsD)
    ED_absB = sum(abs(B(n)) for n in unitsD) / len(unitsD)
    mu = sum(c / phi(d) for d, b, c in cells)
    assert abs(mu - ED_B) < 1e-9
    units, chars = all_chars(N)
    Z = Q * max(ds)
    supp = 0
    prim = set()
    for chi in chars:
        c = sum(B(n) * chi[n].conjugate() for n in units if n % Q == 1 % Q) / phi(N)
        # chi_D: restriction to n = 1 mod Q (CRT): chi_D(m) = chi(n) with n=1 mod Q, n=m mod D
        def lift(m):
            for n in range(m % D, N, D):
                if n % Q == 1 % Q:
                    return n
        chiD = {m: chi[lift(m)] for m in unitsD}
        c2 = sum(B(m) * chiD[m].conjugate() for m in unitsD) / len(unitsD) / phi(Q)
        assert abs(c - c2) < 1e-9, (c, c2)
        assert abs(c) <= ED_absB / phi(Q) + 1e-9
        if abs(c) > 1e-9:
            supp += 1
            fD = conductor(chiD, D, unitsD) if D > 1 else 1
            assert any(d % fD == 0 for d in ds), (fD, ds)
            f = conductor(chi, N, units)
            assert f <= Z
            # chi* identified by (f, values on units mod f): injective chi->chi*
            key = (f, tuple(round(chi[[n for n in units if n % f == r][0]].real, 6) +
                            1j * round(chi[[n for n in units if n % f == r][0]].imag, 6)
                            for r in range(f) if math.gcd(r, f) == 1))
            assert key not in prim
            prim.add(key)
            real = all(abs(v.imag) < 1e-9 for v in chi.values())
            if real and fD > 1:
                # mu_psi PO definition
                mupsi = sum(cc * chiD[[m for m in unitsD if m % d == b % d][0]].real / phi(d)
                            for d, b, cc in cells if d % fD == 0)
                assert abs(mupsi - c * phi(Q)) < 1e-9
        if all(abs(v - 1) < 1e-9 for v in chi.values()):
            assert abs(c - mu / phi(Q)) < 1e-9
    assert supp <= Z * Z
    return Q, ds, N, supp, Z * Z


if __name__ == "__main__":
    done = 0
    for s in range(400):
        r = run(s)
        if r:
            done += 1
            if done <= 8:
                print("Q=%d ds=%s N=%d |supp|=%d Z^2=%d" % r)
        if done >= 40:
            break
    print("all checks passed on", done, "random instances")
