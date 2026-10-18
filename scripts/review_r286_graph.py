"""R286 from-scratch census of the mutual-shift graph G_n (LOWER_TAIL_FABLE §2.9).
Edges: unordered coprime pairs {t, e}, t != e, with t e | n + t + e. Complete enumeration: if min(t,e) = 1 the
other end divides n + 1; otherwise (t-1)(e-1) <= n + 1, so for s = min <= sqrt(n+1)+1 the other end divides n + s.
(Every edge is found from its smaller endpoint s; s <= 1 + sqrt(n + 1).)
Reports: #components (non-isolated vertices), component of 1, QNR in comp(1), bichromatic edge, shape of other comps.
"""
import sys
from math import gcd, isqrt
from collections import Counter, defaultdict
from review_r286_canon import isprime, divisors, jacobi


def edges(n):
    E = set()
    for s in range(1, isqrt(n + 1) + 3):
        for t in divisors(n + s):
            if t > s and gcd(t, s) == 1 and (n + t + s) % (t * s) == 0:
                E.add((s, t))
    return E


def comps(E):
    adj = defaultdict(set)
    for a, b in E:
        adj[a].add(b); adj[b].add(a)
    seen, out = set(), []
    for v in adj:
        if v in seen:
            continue
        st, c = [v], set()
        while st:
            x = st.pop()
            if x not in seen:
                seen.add(x); c.add(x); st.extend(adj[x])
        out.append(c)
    return out, adj


if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    st = Counter()
    shapes = Counter()
    ex = []
    for n in [p for p in range(5, P, 4) if isprime(p)]:
        E = edges(n)
        cs, adj = comps(E)
        c1 = next(c for c in cs if 1 in c)
        st["primes"] += 1
        st["connected"] += len(cs) == 1
        st["QNR in comp(1)"] += any(jacobi(v, n) == -1 for v in c1)
        st["bichromatic edge"] += any(jacobi(a * b, n) == -1 for a, b in E)
        st["bichromatic edge inside comp(1)"] += any(jacobi(a * b, n) == -1 for a, b in E if a in c1)
        st["sum |comp(1)|"] += len(c1)
        for c in cs:
            if 1 in c:
                continue
            ne = sum(1 for a, b in E if a in c)
            k = len(c)
            shapes["%d vertices, %d edges%s" % (k, ne, " (clique)" if ne == k * (k - 1) // 2 else "")] += 1
            if n in (73, 229):
                ex.append((n, sorted(c), sorted((a, b) for a, b in E if a in c)))
        if not any(jacobi(v, n) == -1 for v in c1):
            print("comp(1) all QR at", n, "size", len(c1), "other comps", [sorted(c) for c in cs if 1 not in c])
    for m in range(3, 80, 2):
        n = m * m
        st["squares: bichromatic edge"] += any(jacobi(a * b, n) == -1 for a, b in edges(n))
    print(dict(st)); print(dict(shapes)); print(ex)
