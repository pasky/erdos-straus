"""z43 (FABLE): the mutual-shift graph G_p.

Vertices: integers e >= 1 that occur in some coprime pair (t,e) with t e | p + t + e
(equivalently t | p+e and e | p+t).  Edges: such pairs.  Colour: Legendre (e/p).
Fact (DEDEKIND_ES Thm 4.5 in these coordinates): ES(p) <=> some edge is bichromatic.
Here we look at the component structure: number of components, whether the component of
vertex 1 contains a QNR, whether every component is monochromatic for squares (control).
Edges enumerated via: for each e, divisors t of p+e with t ≡ -p (mod e).
"""
import sys
from collections import defaultdict
from sympy import primerange, divisors, jacobi_symbol, isprime
from math import gcd

def edges(n, E):
    """all coprime (t,e), 1<=e<=E, t>=1, with te | n+t+e; returns set of frozensets"""
    es = set()
    for e in range(1, E + 1):
        tgt = (-n) % e
        for t in divisors(n + e):
            if t % e == tgt and t != e and gcd(t, e) == 1:
                es.add(frozenset((t, e)))
    return es

def components(es):
    adj = defaultdict(set)
    for ed in es:
        a, b = tuple(ed)
        adj[a].add(b); adj[b].add(a)
    seen = {}; comps = []
    for v in adj:
        if v in seen: continue
        stack = [v]; comp = set()
        while stack:
            x = stack.pop()
            if x in seen: continue
            seen[x] = len(comps); comp.add(x); stack.extend(adj[x] - set(seen))
        comps.append(comp)
    return comps

def chi(a, n):
    a %= n
    if a == 0: return 0
    return jacobi_symbol(a, n)

if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    which = sys.argv[2] if len(sys.argv) > 2 else "primes"
    ns = [p for p in primerange(5, P) if p % 4 == 1] if which == "primes" else [m * m for m in range(3, int(P ** 0.5) + 1, 2)]
    stats = defaultdict(int)
    for n in ns:
        E = n + 1
        es = edges(n, E)
        comps = components(es)
        bich = any(chi(a, n) * chi(b, n) == -1 for ed in es for a, b in [tuple(ed)])
        c1 = next((c for c in comps if 1 in c), set())
        nverts = sum(len(c) for c in comps)
        stats["n"] += 1
        stats["connected"] += (len(comps) == 1)
        stats["bichromatic"] += bich
        stats["QNR in comp(1)"] += any(chi(v, n) == -1 for v in c1)
        stats["QNR vertex exists"] += any(chi(v, n) == -1 for c in comps for v in c)
        stats["comp(1) is everything"] += (len(c1) == nverts)
        if which == "primes" and not bich:
            print("NO BICHROMATIC EDGE at", n)
        if len(comps) > 1:
            stats["multi"] += 1
            others = [sorted(c) for c in comps if 1 not in c]
            if stats["multi"] <= 15 or n > P - 60:
                print(n, "comp(1) size", len(c1), "| other comps:", others[:3], "total", len(comps),
                      "| other comps bichromatic:", [any(chi(a,n)*chi(b,n)==-1 for ed in es for a,b in [tuple(ed)] if a in c and b in c) for c in comps if 1 not in c][:3])
    print(dict(stats))
