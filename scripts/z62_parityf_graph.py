"""Gamma_p (coprime version = S_p): vertices = positive integers, edge {a,c} (a != c) iff a | p+c and c | p+a. S_p = ordered edges + loop (1,1).
Check: is Gamma_p a tree? Does each vertex c>1 have exactly one smaller neighbour (= -p mod c)?
Mark edges with 4 | g, g = (p+a+c)/(ac)."""
import sys
from sympy import isprime, divisors
from math import gcd
from collections import defaultdict

def gamma(p):
    adj = defaultdict(set)
    for a in range(1, 2*p+3):
        for c in divisors(p + a):
            if c != a and (p + c) % a == 0 and gcd(a, c) == 1:
                adj[a].add(c); adj[c].add(a)
    return adj

def analyse(p):
    adj = gamma(p)
    V = sorted(adj)
    E = sum(len(adj[v]) for v in V)//2
    # components
    seen = set(); comps = 0
    for v in V:
        if v in seen: continue
        comps += 1; stack = [v]; seen.add(v)
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen: seen.add(y); stack.append(y)
    smaller = {v: sorted(c for c in adj[v] if c < v) for v in V}
    bad = [(v, smaller[v]) for v in V if v > 1 and len(smaller[v]) != 1]
    bad2 = [(v, smaller[v]) for v in V if v > 1 and smaller[v] and smaller[v][0] != (-p) % v]
    es_edges = sorted((a, c) for a in V for c in adj[a] if a < c and (p + a + c) % (4*a*c) == 0)
    roots = [v for v in V if v == 1 or not smaller[v]]
    return V, E, comps, bad, bad2, es_edges, adj, roots

if __name__ == "__main__":
    for p in map(int, sys.argv[1:]):
        V, E, comps, bad, bad2, es, adj, roots = analyse(p)
        print(p, "P" if isprime(p) else "C", "|V|=%d |E|=%d comps=%d tree=%s" % (len(V), E, comps, (E == len(V)-1 and comps == 1)),
              "bad(#smaller!=1)=%s bad2=%s" % (bad[:5], bad2[:5]), "roots=%s ES-edges=%s |S_p|=%d" % (roots, es, 1+2*E))
        if p <= 60:
            print("   adj:", {v: sorted(adj[v]) for v in V})
