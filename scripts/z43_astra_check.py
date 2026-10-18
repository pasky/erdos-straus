"""Independent O275 checks: direct residues, divisor enumeration, rational certificates.

Run with PYTHONPATH=scripts uv run python scripts/z43_astra_check.py.
Small complete comparisons supplement the all-prime C census through 10^6.
"""
from fractions import Fraction
from math import gcd, isqrt
from sympy import divisors, isprime, jacobi_symbol


def residue_edges(n):
    out = set()
    for v in range(2, n + 3):
        u = (-n) % v
        if u and (n + u + v) % (u * v) == 0:
            out.add((u, v))
    return out


def divisor_edges(n):
    out = set()
    for u in range(1, isqrt(n + 1) + 2):
        for v in divisors(n + u):
            v = int(v)
            if v > u and (n + u + v) % (u * v) == 0:
                out.add((u, v))
    return out


def certificates(n, u, v, k=4):
    t = (n + u + v) // (u * v)
    if t % k == 0:
        d = t // k
        yield (u*v*d, n*v*d, n*u*d)
    for a, b in ((u, v), (v, u)):
        if a % k == 0:
            d, c, h = a // k, t, t*b - 1
            yield (h*d, h*c*d*n, c*d*n)
        if (t*a - 1) % k == 0:
            d, h = (t*a - 1) // k, t*b - 1
            yield (h*d*n, b*d, h*b*d)


def components(n, edges):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)
    comps = []
    seen = set()
    for v in sorted(adj):
        if v in seen:
            continue
        todo, comp = [v], set()
        while todo:
            w = todo.pop()
            if w in comp:
                continue
            comp.add(w)
            todo.extend(adj[w])
        seen |= comp
        comps.append(comp)
    return comps


def main():
    counts = [0, 0, 0]
    for n in range(3, 2001, 2):
        E = residue_edges(n)
        assert E == divisor_edges(n), n
        C = components(n, E)
        assert len(E) == sum(len(c)-1 for c in C)
        for u, v in E:
            t = (n+u+v)//(u*v)
            A = t*u-1
            if gcd(n, u*v) == 1:
                assert jacobi_symbol(A,n) == jacobi_symbol(u*v,n)
            certs = list(certificates(n,u,v))
            if n % 4 == 1:
                assert bool(certs) == (jacobi_symbol(A,n) == -1)
            for xyz in certs:
                assert min(xyz) > 0
                assert sum((Fraction(1,x) for x in xyz), Fraction()) == Fraction(4,n)
                counts[2] += 1
            if n in (131,241):
                assert not list(certificates(n,u,v,8))
        counts[0] += 1
        counts[1] += len(E)
    print('independent small complete checks: n,edges,rational_certificates =', counts)
    # Direct graph/rational checks at all 499 odd squares <= 10^6.
    sqedges = 0
    for m in range(3,1000,2):
        n=m*m
        for u,v in divisor_edges(n):
            assert not list(certificates(n,u,v))
            sqedges += 1
    print('square control: 499 squares, edges =',sqedges)
    # Exact prime fixtures for the four-form construction, no probable-prime claims.
    fixtures=[]
    for k in range(1,100000):
        p=24*k+1
        if all(isprime(a*k+1) for a in (24,12,8,6)):
            r,s,w=12*k+1,8*k+1,6*k+1
            expected={(1,2),(1,r),(1,2*r),(2,3),(2,s),(2,3*s),(3,2*w)}
            E=divisor_edges(p)
            comp=next(c for c in components(p,E) if 1 in c)
            assert {e for e in E if e[0] in comp} == expected
            assert all(jacobi_symbol(v,p)==1 for v in comp)
            mixed=[min(c) for c in components(p,E)
                   if len({int(jacobi_symbol(v,p)) for v in c})>1]
            fixtures.append((k,p,len(E),min(mixed) if mixed else None))
            if len(fixtures)==8:
                break
    assert len(fixtures)==8
    print('four-form fixtures (k,p,edges,least_mixed_root):',fixtures)
    isolated=[]
    for a in range(2000):
        p,q=2521+9240*a,211+770*a
        if isprime(p) and isprime(q):
            assert all(jacobi_symbol(v,p)==1 for v in range(1,11))
            assert jacobi_symbol(11,p)==-1
            assert all(v%11!=9 for v in divisors(p+11))
            isolated.append(p)
            if len(isolated)==8:
                break
    assert len(isolated)==8
    assert all(11 not in e for e in divisor_edges(2521))
    print('two-form least-QNR isolated fixtures:',isolated)


if __name__ == '__main__':
    main()
