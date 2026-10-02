#!/usr/bin/env python3
"""POINTWISE_OMEGA3 (EVIDENCE): pair codegrees of the Pi_0-system at y=T^theta.

For a pair of free primes (l1,l2) (q=l1*l2) and every class c mod q, compute
  Delta(c) = sum over distinct hyperedges e = (l3, class mod l1 l2 l3) through
  the vertices (l1, c mod l1), (l2, c mod l2) of 1/(l3-1),
where hyperedges come from atoms (M,D): M = m*l1*l2*l3 <= T, M = 3 (4), m y-smooth,
l3 > y prime (distinct from l1,l2), D | A_M^2, m | 4D+1, class -4D mod M.
Each heavy class is reduced to its shortest lattice vector (u,v): u + c v = 0 (mod q),
i.e. c = -u/v (mod q); "height" = |u*v|.

usage: omega3_codeg.py T theta l1 l2 [top]
"""
import sys
from math import gcd
from sympy import factorint, isprime


def divisors_sq(fa):
    ds = [1]
    for p, e in fa.items():
        ds = [d * p ** k for d in ds for k in range(2 * e + 1)]
    return ds


def shortest(c, q):
    """Gauss-reduce the lattice {(u,v): u + c v = 0 mod q}; return shortest vector."""
    b1, b2 = (q, 0), ((-c) % q, 1)
    def n2(v):
        return v[0] * v[0] + v[1] * v[1]
    if n2(b1) < n2(b2):
        b1, b2 = b2, b1
    while True:
        # make b2 the shorter
        mu = round((b1[0] * b2[0] + b1[1] * b2[1]) / n2(b2))
        b1 = (b1[0] - mu * b2[0], b1[1] - mu * b2[1])
        if n2(b1) >= n2(b2):
            return b2, b1
        b1, b2 = b2, b1


def codegrees(T, theta, l1, l2):
    y = T ** theta
    q = l1 * l2
    edges = {}  # (l3, class mod q*l3) -> c mod q
    M = q
    while M <= T:
        if M % 4 == 3:
            f = factorint(M)
            if f.get(l1) == 1 and f.get(l2) == 1:
                rough = [p for p in f if p > y and p not in (l1, l2)]
                if len(rough) == 1 and f[rough[0]] == 1:
                    l3 = rough[0]
                    m = M // (q * l3)
                    A = (M + 1) // 4
                    r = q * l3
                    for D in divisors_sq(factorint(A)):
                        if (4 * D + 1) % m == 0:
                            edges[(l3, (-4 * D) % r)] = 1
        M += q
    Delta = {}
    for (l3, cl) in edges:
        c = cl % q
        Delta[c] = Delta.get(c, 0.0) + 1.0 / (l3 - 1)
    return Delta


def main():
    T = int(float(sys.argv[1])); theta = float(sys.argv[2])
    l1, l2 = int(sys.argv[3]), int(sys.argv[4])
    top = int(sys.argv[5]) if len(sys.argv) > 5 else 25
    assert isprime(l1) and isprime(l2) and l1 > T ** theta and l2 > T ** theta
    q = l1 * l2
    Delta = codegrees(T, theta, l1, l2)
    tot = sum(Delta.values())
    print(f"T={T:.3g} theta={theta} y={T**theta:.1f} q={q} classes={len(Delta)} sumDelta={tot:.4f} avg/q={tot/q:.3g}")
    ht = {}
    for c in Delta:
        (u, v), _ = shortest(c, q)
        ht[c] = (abs(u * v), u * v > 0)
    for X in (1, 4, 16, 64, 256, 1024, 4096):
        rest = [Delta[c] for c in Delta if not (ht[c][1] and ht[c][0] <= X)]
        mixed = [Delta[c] for c in Delta if not ht[c][1]]
        print(f"  X={X:5d}: max Delta over classes not -u/v with 0<uv<=X: {max(rest):.5f};"
              f"  (mixed-sign classes max {max(mixed) if mixed else 0:.5f})")
    print("  top classes outside {-u/v: 0<uv<=1024}:")
    nonhub = [(c, Delta[c]) for c in Delta if not (ht[c][1] and ht[c][0] <= 1024)]
    for c, d in sorted(nonhub, key=lambda kv: -kv[1])[:8]:
        (u, v), (u2, v2) = shortest(c, q)
        print(f"    c={c:>10d} Delta={d:.5f} short=({u},{v}) next=({u2},{v2})")
    for c, d in sorted(Delta.items(), key=lambda kv: -kv[1])[:top]:
        (u, v), _ = shortest(c, q)
        if v < 0:
            u, v = -u, -v
        print(f"  c={c:>10d}  Delta={d:.5f}  c=-u/v: u={u:>6d} v={v:>6d} |uv|={abs(u*v)}")


if __name__ == "__main__":
    main()
