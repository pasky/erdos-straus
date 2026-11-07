#!/usr/bin/env python3
"""z62 PARITY — KT1: river (topograph) weights on certificate forms.

For n odd, words X(n) = {(t,u,v) >= 1 : t*u*v - u - v = n}, unordered u <= v.
gamma = [[t*u-1, n],[t, t*v-1]] in SL2(Z); form F = [t, t*(v-u), -n] (ambiguous), disc (t(u+v)-2)^2 - 4.
Families: STAR = (★) words (4 | t, u < v; = unordered (★) triples (u,B,C)=(u,v,t/4));
          U7   = words with 8 | t*u or 8 | t*v (A or A* = 7 mod 8);  ALLX = all words.
River weights per word (Gauss reduction cycle of F, proper equivalence):
  half  = (cycle length / 2) mod 2           (Gauss cycles have even length: a alternates sign)
  q4    = (cycle length / 2) mod 4 >= 2
  prin  = [cycle contains a = 1]             (F narrowly principal)
  neg   = [cycle of -F == cycle of F]
  amb   = #{forms in cycle with a | b} mod 2
  sym   = #{forms in cycle with c = -a} mod 2
  ambm1 = [some form in cycle with a | b has |a| = -1 mod t]
  hj    = HJ length of n/(A mod n) mod 2
  x*y   = pairwise products of the above (per word), then summed
Output: per n, the counts W_w(n) for each family, as TSV.
Usage: z62_parity_river.py N_MAX [extra n ...]
"""
import sys
from math import isqrt


def spf_sieve(N):
    s = list(range(N + 1))
    for i in range(2, isqrt(N) + 1):
        if s[i] == i:
            for j in range(i * i, N + 1, i):
                if s[j] == j:
                    s[j] = i
    return s


SPF = None


def factor(m):
    f = {}
    if SPF is not None and m < len(SPF):
        while m > 1:
            q = SPF[m]
            f[q] = f.get(q, 0) + 1
            m //= q
        return f
    d = 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1 if d == 2 else 2
    if m > 1:
        f[m] = f.get(m, 0) + 1
    return f


def divisors(m):
    ds = [1]
    for q, e in factor(m).items():
        ds = [d * q ** k for d in ds for k in range(e + 1)]
    return ds


def words(n):
    """unordered words (t,u,v), u <= v, t*u*v - u - v = n."""
    out = []
    u = 1
    while True:
        # f = t*u - 1 divides n + u, f = -1 mod u, v = (n+u)/f >= u  => f <= (n+u)/u
        if (u - 1) > (n + u) // u and u > 1:
            break
        lim = (n + u) // u
        for f in divisors(n + u):
            if f > lim or f < 1:
                continue
            if (f + 1) % u:
                continue
            t = (f + 1) // u
            if t < 1:
                continue
            v = (n + u) // f
            if v < u:
                continue
            out.append((t, u, v))
        u += 1
    return out


def rho(a, b, c, D, s):
    """one Gauss reduction step (proper equivalence)."""
    ac = abs(c)
    m = 2 * ac
    if s >= ac:
        # b' = -b mod 2|c|, largest <= s
        bp = s - ((s + b) % m)
    else:
        # b' in (-|c|, |c|]
        bp = (-b) % m
        if bp > ac:
            bp -= m
    cp = (bp * bp - D) // (4 * c)
    return c, bp, cp


def is_reduced(a, b, c, s):
    aa = 2 * abs(a)
    return 0 < b <= s and aa >= s - b + 1 and aa <= s + b


def cycle(a, b, c):
    D = b * b - 4 * a * c
    s = isqrt(D)
    assert s * s != D
    k = 0
    while not is_reduced(a, b, c, s):
        a, b, c = rho(a, b, c, D, s)
        k += 1
        assert k < 10000
    start = (a, b, c)
    cyc = [start]
    while True:
        a, b, c = rho(a, b, c, D, s)
        if (a, b, c) == start:
            break
        cyc.append((a, b, c))
        assert len(cyc) < 100000
    return cyc


def hj_len(n, A):
    A %= n
    if A == 0:
        return 0
    L = 0
    while A > 0:
        b = -(-n // A)
        n, A = A, b * A - n
        L += 1
    return L


BASE = ["one", "half", "q4", "prin", "neg", "amb", "sym", "ambm1", "hj"]
WEIGHTS = BASE + [f"{x}*{y}" for i, x in enumerate(BASE[1:], 1) for y in BASE[i + 1:]]


def river_weights(n, t, u, v):
    a, b, c = t, t * (v - u), -n
    cyc = cycle(a, b, c)
    L = len(cyc)
    st = set(cyc)
    ncyc = set(cycle(-a, b, -c))
    w = {}
    w["one"] = 1
    w["half"] = (L // 2) % 2
    w["q4"] = 1 if (L // 2) % 4 >= 2 else 0
    w["prin"] = 1 if any(x[0] == 1 for x in cyc) else 0
    w["neg"] = 1 if st == ncyc else 0
    ambs = [x for x in cyc if x[1] % x[0] == 0]
    w["amb"] = len(ambs) % 2
    w["sym"] = sum(1 for x in cyc if x[2] == -x[0]) % 2
    w["ambm1"] = 1 if any((abs(x[0]) + 1) % t == 0 for x in ambs) else 0
    w["hj"] = hj_len(n, t * u - 1) % 2
    return w


def fam_flags(n, t, u, v):
    star = (t % 4 == 0 and u < v)
    u7 = ((t * u) % 8 == 0) or ((t * v) % 8 == 0)
    return {"STAR": star, "U7": u7, "ALLX": True}


def is_prime(m):
    if m < 2:
        return False
    if SPF is not None and m < len(SPF):
        return SPF[m] == m
    return all(m % q for q in range(2, isqrt(m) + 1))


def row(n):
    W = {f: {w: 0 for w in WEIGHTS} for f in ("STAR", "U7", "ALLX")}
    for (t, u, v) in words(n):
        if t * (u + v) - 2 <= 2:
            continue  # degenerate disc
        fl = fam_flags(n, t, u, v)
        rw = river_weights(n, t, u, v)
        for i, x in enumerate(BASE[1:], 1):
            for y in BASE[i + 1:]:
                rw[f"{x}*{y}"] = rw[x] * rw[y]
        for f, on in fl.items():
            if on:
                for w in WEIGHTS:
                    W[f][w] += rw[w]
    return W


def main():
    global SPF
    N = int(sys.argv[1])
    extra = [int(x) for x in sys.argv[2:]]
    SPF = spf_sieve(N + isqrt(N) + 10)
    cols = [f"{f}_{w}" for f in ("STAR", "U7", "ALLX") for w in WEIGHTS]
    print("n\ttag\t" + "\t".join(cols))
    ns = [p for p in range(25, N + 1, 24) if is_prime(p)] + extra
    for n in ns:
        r = isqrt(n)
        tag = "SQ" if r * r == n else ("P" if is_prime(n) else "C")
        W = row(n)
        print(f"{n}\t{tag}\t" + "\t".join(str(W[f][w]) for f in ("STAR", "U7", "ALLX") for w in WEIGHTS), flush=True)


if __name__ == "__main__":
    main()


def word_patterns(N):
    """distinct per-word column patterns (bitmask over the table columns) for primes p = 1 (24) <= N."""
    cols = [(f, w) for f in ("STAR", "U7", "ALLX") for w in WEIGHTS]
    pats = set()
    for n in [p for p in range(25, N + 1, 24) if is_prime(p)]:
        for (t, u, v) in words(n):
            if t * (u + v) - 2 <= 2:
                continue
            fl = fam_flags(n, t, u, v)
            rw = river_weights(n, t, u, v)
            for i, x in enumerate(BASE[1:], 1):
                for y in BASE[i + 1:]:
                    rw[f"{x}*{y}"] = rw[x] * rw[y]
            m = 0
            for j, (f, w) in enumerate(cols):
                if fl[f] and rw[w] % 2:
                    m |= 1 << j
            pats.add(m)
    return pats
