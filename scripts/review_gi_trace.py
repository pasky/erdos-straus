"""R170 from-scratch implementation of the Eichler-Selberg trace formula (Cohen's form, (n,N) = 1, k >= 2)
and independent tests: dimension formulas, eta products (11a, the weight-3 form of level 7), Delta.
No author code reused.  Usage: PYTHONPATH=scripts uv run python scripts/review_gi_trace.py
"""
import cmath
from fractions import Fraction
from math import gcd, isqrt
from functools import lru_cache


def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def phi(n):
    r = n
    for p in factor(n):
        r = r // p * (p - 1)
    return r


def psi(n):
    r = Fraction(n)
    for p in factor(n):
        r *= Fraction(p + 1, p)
    return int(r)


@lru_cache(None)
def h_w(D):
    """Weighted class number of primitive pos.-def. forms of discriminant D<0 (h/ (w/2))."""
    assert D < 0 and D % 4 in (0, 1)
    h = 0
    a = 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (c == a and b < 0):
                continue
            if gcd(gcd(a, abs(b)), c) != 1:
                continue
            h += 1
        a += 1
    if D == -3:
        return Fraction(h, 3)
    if D == -4:
        return Fraction(h, 2)
    return Fraction(h)


# ---------- Dirichlet characters mod q (complex-valued) ----------
def characters(q):
    """List of characters mod q as dicts x -> value (0 off units)."""
    units = [x for x in range(q) if gcd(x, q) == 1]
    # generators of the group via brute force: build group as product of cyclic pieces greedily
    gens, orders = [], []
    sub = {1 % q}
    while len(sub) < len(units):
        # pick element maximizing new subgroup size
        best = None
        for g in units:
            if g in sub:
                continue
            o, y = 1, g
            while y not in sub:
                y = y * g % q
                o += 1
            if best is None or o > best[1]:
                best = (g, o)
        g, o = best
        gens.append(g)
        orders.append(o)
        new = set()
        for s in sub:
            y = s
            for _ in range(o):
                new.add(y)
                y = y * g % q
        sub = new
    # discrete log table: each unit = prod g_i^{e_i}, but o_i is order relative to previous subgroup, so
    # g_i^{o_i} lies in earlier subgroup: characters must respect relations -> solve by enumerating values.
    rep = {1 % q: ()}
    elems = [(1 % q, ())]
    for i, (g, o) in enumerate(zip(gens, orders)):
        nxt = []
        for (s, e) in elems:
            y = s
            for j in range(o):
                nxt.append((y, e + (j,)))
                y = y * g % q
        elems = nxt
    rep = dict(elems)
    # relation: g_i^{o_i} = element of earlier subgroup with exponents r_i
    rels = []
    for i, (g, o) in enumerate(zip(gens, orders)):
        rels.append(rep[pow(g, o, q)])
    # enumerate characters: value z_i = chi(g_i) must satisfy z_i^{o_i} = prod_{j<i} z_j^{r_ij}
    chars = [()]
    for i, o in enumerate(orders):
        new = []
        for zs in chars:
            target = 1
            for j, e in enumerate(rels[i][:i]):
                target *= zs[j] ** e
            arg = cmath.phase(target)
            for k in range(o):
                new.append(zs + (cmath.exp(1j * (arg + 2 * cmath.pi * k) / o),))
        chars = new
    out = []
    for zs in chars:
        d = {x: 0 for x in range(q)}
        for x, e in rep.items():
            v = 1
            for z, ee in zip(zs, e):
                v *= z ** ee
            d[x] = v
        out.append(d)
    return out


def conductor(chi, q):
    for d in divisors(q):
        if all(abs(chi[x] - 1) < 1e-9 for x in range(q) if gcd(x, q) == 1 and x % d == 1 % d):
            return d
    return q


def trace(n, k, N, chi=None):
    """Tr T_n on S_k(Gamma_0(N), chi), gcd(n,N)=1, k>=2."""
    assert gcd(n, N) == 1 and k >= 2
    if chi is None:
        chi = {x: (1 if gcd(x, N) == 1 else 0) for x in range(N)}
        trivial = True
    else:
        trivial = all(abs(chi[x] - 1) < 1e-9 for x in range(N) if gcd(x, N) == 1)
    fchi = conductor(chi, N)
    A1 = 0
    r = isqrt(n)
    if r * r == n:
        A1 = n ** (k / 2 - 1) * chi[r % N] * (k - 1) / 12 * psi(N)
    A2 = 0
    t = 0
    while t * t < 4 * n:
        for tt in ({t, -t} if t else {0}):
            D = tt * tt - 4 * n
            # (rho^{k-1}-rhob^{k-1})/(rho-rhob) = polynomial P_k(t,n) via recursion
            p0, p1 = 0, 1  # P_1 = 1, P_2 = t, P_{j+1} = t P_j - n P_{j-1}
            for _ in range(k - 2):
                p0, p1 = p1, tt * p1 - n * p0
            P = p1
            s = 0
            for f in range(1, isqrt(-D) + 1):
                if D % (f * f) or (D // (f * f)) % 4 not in (0, 1):
                    continue
                Nf = gcd(N, f)
                mu = 0
                for x in range(N):
                    if (x * x - tt * x + n) % (Nf * N) == 0:
                        mu += chi[x]
                mu *= Fraction(psi(N), psi(N // Nf))
                s += float(h_w(D // (f * f))) * mu
            A2 += -0.5 * P * s
        t += 1
    A3 = 0
    for d in divisors(n):
        dp = n // d
        inner = 0
        for tau in divisors(N):
            g = gcd(tau, N // tau)
            if (dp - d) % g != 0 or (N // fchi) % g != 0:
                continue
            # y = d mod tau, d' mod N/tau  (mod lcm = N/g)
            L = N // g
            y = next(y for y in range(L) if (y - d) % tau == 0 and (y - dp) % (N // tau) == 0)
            inner += phi(g) * chi[y % N]
        A3 += -0.5 * min(d, dp) ** (k - 1) * inner
    A4 = 0
    if k == 2 and trivial:
        A4 = sum(tt for tt in divisors(n) if gcd(N, n // tt) == 1)
    return A1 + A2 + A3 + A4, (A1, A2, A3, A4)


# ---------- independent references ----------
def dim_S_gamma0(k, N):
    """Classical dimension formula (k even >= 2), trivial character."""
    mu = psi(N)
    fa = factor(N)
    nu2 = 0 if N % 4 == 0 else 1
    nu3 = 0 if N % 9 == 0 else 1
    for p in fa:
        nu2 *= (1 + (0 if p == 2 else (1 if p % 4 == 1 else -1)))
        nu3 *= (1 + (0 if p == 3 else (1 if p % 3 == 1 else -1)))
    c = sum(phi(gcd(d, N // d)) for d in divisors(N))
    if k == 2:
        return 1 + Fraction(mu, 12) - Fraction(nu2, 4) - Fraction(nu3, 3) - Fraction(c, 2)
    return (Fraction((k - 1) * mu, 12) + (k // 4 - Fraction(k - 1, 4)) * nu2
            + (k // 3 - Fraction(k - 1, 3)) * nu3 - Fraction(c, 2))


def genus_X1(N):
    if N <= 4:
        return 0
    s = Fraction(N * N, 24)
    for p in factor(N):
        s *= 1 - Fraction(1, p * p)
    return 1 + s - Fraction(sum(phi(d) * phi(N // d) for d in divisors(N)), 4)


def eta_product(terms, M):
    """q-expansion of prod eta(a z)^e, returned with the q^{sum a e/24} shift removed, up to q^M."""
    c = [0] * (M + 1)
    c[0] = 1
    for a, e in terms:
        for _ in range(e):
            for j in range(1, M // a + 1):  # multiply by (1 - q^{a j})
                for i in range(M, a * j - 1, -1):
                    c[i] -= c[i - a * j]
    return c


def main():
    bad = 0
    # (a) dimensions S_k(Gamma_0(N)), k = 2,4,6, N <= 40
    for N in range(1, 41):
        for k in (2, 4, 6):
            tr = trace(1, k, N)[0]
            if abs(tr - float(dim_S_gamma0(k, N))) > 1e-6:
                bad += 1
                print("dim fail", N, k, tr, dim_S_gamma0(k, N))
    print("(a) dim S_k(Gamma0(N)), k in {2,4,6}, N<=40 vs classical formula: failures so far", bad)
    # (b) genus X1(q) = sum over even chi of dim S_2(q,chi)
    for q in range(3, 26):
        s = sum(trace(1, 2, q, chi)[0] for chi in characters(q) if abs(chi[q - 1] - 1) < 1e-9)
        if abs(s - float(genus_X1(q))) > 1e-6:
            bad += 1
            print("X1 fail", q, s, genus_X1(q))
    # dim S_3(Gamma1(q)) = sum over odd chi of dim S_3(q, chi)
    d3 = {q: round(sum(trace(1, 3, q, chi)[0] for chi in characters(q) if abs(chi[q - 1] + 1) < 1e-9).real)
          for q in range(3, 13)}
    print("(b) genus X1(q), q<=25: failures so far", bad, "; dim S_3(Gamma1(q)) q=3..12:", d3)
    # (c) 11a: eta(z)^2 eta(11z)^2 = q prod ...
    c = eta_product([(1, 2), (11, 2)], 60)
    a = {m: c[m - 1] for m in range(1, 61)}
    for n in [2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 17, 23, 29, 31]:
        tr = trace(n, 2, 11)[0]
        if abs(tr - a[n]) > 1e-6:
            bad += 1
            print("11a fail", n, tr, a[n])
    # (d) weight 3, level 7, chi = (-7/.) : eta(z)^3 eta(7z)^3, q-shift 1
    chi7 = {x: 0 for x in range(7)}
    for x in range(1, 7):
        chi7[x] = 1 if x in (1, 2, 4) else -1
    c = eta_product([(1, 3), (7, 3)], 60)
    b = {m: c[m - 1] for m in range(1, 61)}
    for n in [1, 2, 3, 4, 5, 6, 8, 9, 11, 13, 15, 23, 25, 29]:
        tr = trace(n, 3, 7, chi7)[0]
        if abs(tr - b[n]) > 1e-6:
            bad += 1
            print("level-7 weight-3 fail", n, tr, b[n])
    # (e) Delta
    c = eta_product([(1, 24)], 20)
    for n in [2, 3, 5, 7, 11]:
        tr = trace(n, 12, 1)[0]
        if abs(tr - c[n - 1]) > 1e-3:
            bad += 1
            print("Delta fail", n, tr, c[n - 1])
    print("TOTAL trace-formula test failures:", bad)


if __name__ == "__main__":
    main()
