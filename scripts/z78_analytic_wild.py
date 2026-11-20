"""Exact local checks; no numerical test of GRH or prime asymptotics."""
from collections import Counter, deque
from fractions import Fraction as F
from itertools import combinations
from math import gcd, prod, isqrt
import cmath


def fac(n):
    d = 2
    ans = {}
    while d*d <= n:
        while n % d == 0:
            n //= d
            ans[d] = ans.get(d, 0) + 1
        d = 3 if d == 2 else d+2
    if n > 1:
        ans[n] = 1
    return ans


def packet(n, R, q, K, E, S):
    V = prod(v for v in S if E[v] % 2)
    g = V
    if pow(V, (q-1)//2, q) == 1:
        g *= next(v for v, b in E.items() if v != 2 and v not in S and b % 2 and pow(v,(q-1)//2,q)==q-1)
    # Enumerate H and nonnegative exponent witnesses, independently of lattice estimates.
    H = {1: (0,)*len(S)}
    queue = deque([1])
    while queue:
        h = queue.popleft()
        for i,v in enumerate(S):
            t = h*v*v % q
            if t not in H:
                a = list(H[h]); a[i] += 1; H[t] = tuple(a); queue.append(t)
    j, rem = divmod((q-1)//2, len(H)); assert rem==0 and j%2==1
    a = H[pow(-g, -j, q)]
    d = K * g**j * prod(v**(2*w) for v,w in zip(S,a))
    A, rem = divmod(K+d, q); assert rem == 0
    x, y, z = n//R*K, n*A, F(n*K*A,d)
    assert F(1,x)+F(1,y)+1/z == F(4,n)
    root = isqrt(z.denominator); assert root**2 == z.denominator and gcd(root,2*n)==1
    left = root
    for v in E:
        w = 0
        while left % v == 0:
            left //= v; w += 1
        assert w<=j+max(a) and (w==0 or y%v==0)
    assert left == 1
    return (g==V, j>1, root>1, any(E[v]%2 for v in S))


zeros = [5569,9601,83449,102001,712321,1724209,1726201,5212561,8813281]
# The 17,401,609 zero is composite, not one of the nine primes in Mordell's classes.
panel = zeros + [17401609, 4545, 17**2, 17**2*41, 17*41**2, 131, 241, 1590284203561]
small = [p for p in range(17,1000,8) if fac(p)=={p:1}]
qs = [q for q in range(3,256,4) if fac(q)=={q:1}]
counts = Counter(); no = []
for n in panel + small:
    pf = fac(n); R = prod(pf)
    if any(p%8!=1 for p in pf):
        no.append((n,pf)); continue
    tests = 0
    for q in qs:
        if pow(R, (q-1)//2, q)!=q-1:
            continue
        K=(R+q)//4; E=fac(K); odd=[v for v in E if v!=2]
        for s in (1,2,3):
            for S in combinations(odd,s):
                counts[packet(n,R,q,K,E,S)] += 1; tests+=1
    assert tests
print('cap arithmetic: #exact rational checks',sum(counts.values()), 'packet inside S',sum(v for k,v in counts.items() if k[0]), 'proper H',sum(v for k,v in counts.items() if k[1]), 'actual overflow',sum(v for k,v in counts.items() if k[2]), 'odd planted valuation',sum(v for k,v in counts.items() if k[3]))
print('classical branch on panel',no)
assert all(any(k[i] for k in counts) for i in range(4))

# Signed patch in physical coordinates: exact test with box cutoff 1 <= (4Ck-n)/V <= 4.
# Compare one centered pair against the primitive-frequency projector by local DFT inversion.
P,W,D=257,3000,12
pr=[q for q in range(P+1,2*P+1) if fac(q)=={q:1}]; n=4*W**3+73
sg=lambda x: 1-2*((x & (x>>1)).bit_count()%2)
for C in range(W+1,W+1+P//2):
    k0=n//(4*C); V=D*W
    ks=range((n+V+4*C-1)//(4*C),(n+4*V)//(4*C)+1)
    def row(q,k):
        if C%q==0 or (4*C*n+1)%q==0:
            l=pow(((4*C*k-n)**2-4*k)%q,(q-1)//2,q)
            return -1 if l==q-1 else l
        i=(k-k0)%q; m=q//2
        return sg(i) if i<m else (-sg(i-m) if i<2*m else -1)
    for k in ks:
        vals=[]
        for q in pr:
            dc=0 if C%q==0 else (q-1 if (4*C*n+1)%q==0 else -1)
            vals.append(F(row(q,k)*q-dc,q))
        assert (sum(vals)**2-sum(t*t for t in vals))/(len(vals)*(len(vals)-1)) > F(1,2)
    if C==W+1:
        for q in pr[:2]:
            e=cmath.exp(2j*cmath.pi/q); tab=[row(q,j) for j in range(q)]
            G=[sum(t*e**((h*j)%q) for j,t in enumerate(tab)) for h in range(1,q)]
            assert max(map(abs,G)) <= 9*q**.5
            for k in ks:
                assert abs(sum(t*e**((-h*k)%q) for h,t in enumerate(G,1))/q - (row(q,k)-sum(tab)/q)) < 1.e-8
print('coherent patch: verified positive signed pair average on',P//2,'rows;',len(pr),'shared prime tables')

# Affine dispersion exponent over a block: r=beta-target, b-gamma+ (gamma+r)/2.
for target in (F(29,100),F(3,10),F(4,13),F(7955,24966)):
    vertices=[(target,1-2*target,target),(target,target,1-2*target),((1-target)/2,(1-target)/2,target)]
    # Evaluate throughout the b>=g half (D>=1); include the additional intersection b=g.
    vertices=[v for v in vertices if v[1]>=v[2]]+[(target,(1-target)/2,(1-target)/2),(F(1,3),)*3]
    gap=lambda v: v[1]-v[2]+(v[2]+v[1]-target)/2-target
    assert max(map(gap,vertices))==F(3,2)-5*target
    print('patch exponent excess at worst vertex:',target,max(map(gap,vertices)))
# log cost normalized to sqrt(u log u): 2/b+m*b/2, equality b^2=4/m.
for m in (1,2):
    bsq=F(4,m)
    assert (2+F(m,2)*bsq)**2/bsq==4*m
    print('planting multiplicity',m,'optimal b^2',bsq,'squared leading constant in u-units',4*m)
