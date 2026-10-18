"""R285 from-scratch fixture checks for LOWER_TAIL_ASTRA Thm 3.1, Thm 3.2, Thm 5.1, Prop 4.2.
Component exploration: neighbours of x in F_n are the v != x, 1<=v<=n+2, with x*v | n+x+v (necessarily v | n+x).
"""
import sys
from math import lcm
from sympy import isprime, divisors, legendre_symbol, nextprime
from sympy.ntheory.modular import crt


def nbrs(n, x):
    return [v for v in divisors(n + x) if v != x and v <= n + 2 and (n + x + v) % (x * v) == 0]


def component(n, roots):
    seen, edges, stack = set(roots), set(), list(roots)
    while stack:
        x = stack.pop()
        for v in nbrs(n, x):
            edges.add((min(x, v), max(x, v)))
            if v not in seen:
                seen.add(v); stack.append(v)
    return seen, edges


def thm31(K):
    found = []
    for k in range(1, K + 1):
        p, r, s, w = 24 * k + 1, 12 * k + 1, 8 * k + 1, 6 * k + 1
        if not (isprime(p) and isprime(r) and isprime(s) and isprime(w)):
            continue
        V, E = component(p, [1])
        want = {(1, 2), (1, r), (1, 2 * r), (2, 3), (2, s), (2, 3 * s), (3, 2 * w)}
        assert E == want, (p, E)
        assert len(V) == 8 and all(legendre_symbol(v % p, p) == 1 for v in V), p
        found.append(p)
    return found


def thm32(H, K, want_n):
    M = lcm(24, *[i * (i + 1) for i in range(1, H + 1)])
    out = []
    for k in range(1, K + 1):
        p = 1 + M * k
        if not isprime(p) or not all(isprime(1 + M // (i + 1) * k) for i in range(1, H + 1)):
            continue
        for i in range(4, H + 1):
            assert nbrs(p, i) == [], (p, i)
        V, E = component(p, [1, 2, 3])
        kk = M * k // 24
        assert len(V) == 8 and len(E) == 7, (p, E)
        assert {(1, 2), (1, 12 * kk + 1), (2, 3), (3, 12 * kk + 2)} <= E
        assert all(legendre_symbol(v % p, p) == 1 for v in V)
        out.append(p)
        if len(out) >= want_n:
            break
    return M, out


def least_nr(p):
    l = 2
    while legendre_symbol(l, p) != -1:
        l += 1
    return l


def thm51(A):
    out = []
    for a in range(A + 1):
        p, q = 2521 + 9240 * a, 211 + 770 * a
        assert 12 * q == p + 11
        if isprime(p) and isprime(q):
            assert least_nr(p) == 11 and nbrs(p, 11) == [], p
            out.append(p)
    return out


def prop42(h):
    # v0=1, v1=2, v2 prime = 1 mod 8; v_{i+1} prime = v_{i-1} mod v_i, = 1 mod 8, > v_i
    vs = [1, 2, 17]
    while len(vs) < h + 1:
        a, b = vs[-2], vs[-1]
        x, m = crt([b, 8], [a, 1])
        x = int(x)
        while x <= b or not isprime(x):
            x += int(m)
        vs.append(x)
    mods, res = [8], [1]
    for i in range(2, len(vs)):
        mods.append(vs[i]); res.append((-vs[i - 1]) % vs[i])
    x, m = crt(mods, res)
    x, m = int(x), int(m)
    while not isprime(x) or x + 2 < vs[-1]:
        x += m
    p = x
    for i in range(len(vs) - 1):
        u, v = vs[i], vs[i + 1]
        assert (p + u + v) % (u * v) == 0, (p, u, v)
    assert all(legendre_symbol(v % p, p) == 1 for v in vs)
    return vs, p


if __name__ == "__main__":
    f31 = thm31(int(sys.argv[1]) if len(sys.argv) > 1 else 20000)
    print("Thm3.1 fixtures:", len(f31), "first 8:", f31[:8])
    for H, K, nwant in [(6, 400000, 3), (8, 3000000, 1)]:
        M, out = thm32(H, K, nwant)
        print(f"Thm3.2 H={H} M={M}:", out)
    f51 = thm51(3000)
    print("Thm5.1 fixtures:", len(f51), f51[:8])
    vs, p = prop42(6)
    print("Prop4.2 path", vs, "p =", p)
