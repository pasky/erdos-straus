"""Independent finite checks for Z69_TWIST; uv run --with sympy python this_file [archive].
No campaign enumerator is imported. Memory is bounded by small divisor lists.
"""
import sys
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt
from pathlib import Path
from sympy import divisors, isprime, jacobi_symbol, primerange

BASE = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('/tmp/xrev_TWIST')

def ds(n):
    return [int(d) for d in divisors(n)]

def words(n):
    # Unordered outer letters: (xy-1)z=n+x and (x-1)^2<=n+1.
    out = []
    for x in range(1, isqrt(n+1)+2):
        for f in ds(n+x):
            if (f+1) % x:
                continue
            y, z = (f+1)//x, (n+x)//f
            if z < x:
                continue
            out.append((x,y,z))
            if z != x:
                out.append((z,y,x))
    return out

def certificate(w):
    x,y,z = w
    return y%4 == 0 or x%4 == 0 or z%4 == 0 or (y%4 == 3 and (x%4 == 3 or z%4 == 3))

pairs = 0
for M in range(1,1002,2):
    for a in ds(M*M):
        for b in ds(M*M//a):
            pairs += 1
            assert (a+b) % (2*M+1)
    # Directly test the original question about M^4, not only the pair reformulation.
    assert all((v+M*M) % (2*M+1) for v in ds(M**4))
print('V: unrestricted pairs and M^4 divisor question PASS;', pairs, 'pairs, odd M<=1001', flush=True)

points = 0
for a in range(1,401):
    for d in range(1,400//a+1):
        N, mod = 4*a*a*d+1, 4*a*d
        for f in ds(N):
            for p in range((-f)%mod,3000,mod):
                if p < 5 or p%4 != 1 or not isprime(p):
                    continue
                points += 1
                assert jacobi_symbol(d,p) == -1 and N%p
assert points == 6718
print('T10: 6718 points independently regenerated PASS', flush=True)

roots = {}
for j in range(1,302,2):
    roots[j] = []
    for eps in range(3,2*j,4):
        nu = 2*j-eps
        if nu < 3:
            continue
        K = (nu*eps-1)//4
        for alpha in ds(K):
            for b in ds(K//alpha):
                if b > alpha and (b-alpha)%eps == 0:
                    c,d = (b-alpha)//eps, K//(alpha*b)
                    n,e = 4*b*c*d-eps, 4*b*c*d+nu
                    a = c*e-b
                    assert n > 0 and a > 0 and 4*a*b*d == n*e+1
                    roots[j].append((n,nu,eps,alpha,b,c,d))
sterile = [j for j,r in roots.items() if not r]
expected = [1,3,5,9,13,17,21,29,33,37,41,49,57,61,69,73,77,89,93,113,117,121,129,133,153,157,169,173,189,197,209,213,233,241,257,261,281,297]
assert sterile == expected
solutions = 0
for n in range(1,1002,4):
    for j in range(1,102,2):
        e = n+2*j
        N = (n*e+1)//4
        for b in ds(N):
            for a in ds(N//b):
                if a <= b or (a+b)%e:
                    continue
                solutions += 1
                c,d = (a+b)//e, N//(a*b)
                assert roots[j]
                # Walk the whole descent, not just the first image.
                nn,ee,aa,bb = n,e,a,b
                while nn > 0:
                    aa,bb = max(aa,bb),min(aa,bb)
                    n2,e2 = 4*bb*c*d-ee,4*bb*c*d-nn
                    a2 = c*e2-bb
                    assert n2 < nn and e2 > 0 and e2-n2 == 2*j
                    assert n2*e2+1 == 4*a2*bb*d
                    assert (4*bb*c*d-e2,4*bb*c*d-n2,c*ee-bb) == (nn,ee,aa)
                    nn,ee,aa = n2,e2,a2
                assert -nn >= 3 and -aa > 0 and bb+aa == c*ee
print('Vieta: exact 38 sterile gaps; complete descents of', solutions, 'solutions (n<=1001,j<=101) PASS', flush=True)

for n in range(3,2001):
    ws = words(n)
    if isprime(n) and n >= 5:
        assert len(ws)%2
    if n in (9,105):
        assert len(ws) == 11 and not any(certificate(w) for w in ws)
    if n%8 != 1:
        continue
    odd = [w for w in ws if all(t%2 for t in w)]
    A = [w for w in odd if w[0]%4 == w[2]%4 == 1]
    B = [w for w in odd if w not in A]
    assert all(y%4 == 3 for x,y,z in odd)
    assert all(y%8 == 3 for x,y,z in A) and all(y%8 == 7 for x,y,z in B)
    if isprime(n):
        assert len(A)%2 and len(B)%2 == 0
    for x,y,z in B:
        if x%4 != 3:
            x,z = z,x
        a,b,c,d,e = 1,y*z-1,z,(x*y-1)//4,y
        assert 4*a*b*d == n*e+1 and c*e == a+b
assert words(73) and len([w for w in words(73) if all(t%2 for t in w)]) == 3
print('P, P-prime, certificate predicates: all n<=2000 PASS', flush=True)

# Check the short algebraic reductions without calling the target's routines.
for n in range(1,1002,4):
    for x,y,z in words(n):
        if y%4 == 0:
            t = x*z
            assert (x+z+n)%(4*t) == 0
            assert (x+z+n)//(4*t) == y//4
            if y*y > n:  # Lenstra regime 4d=y>sqrt(n)
                assert t == (n+y-1)//y
for D in range(3,404,4):
    for k in ds((D+1)//4):
        u = (D+1)//(4*k)
        assert gcd(4*k,D) == 1
        for p in range(D):
            assert ((p+u)%D == 0) == ((4*k*p+1)%D == 0)
for b,c,d,e in product(range(1,13),range(1,13),range(1,13),range(1,25)):
    a = c*e-b
    if a <= 0:
        continue
    n = 4*a*b*d-e
    assert n > 0 and n == e*(4*b*c*d-1)-4*b*b*d
    assert (n%4 == 1) == (e%4 == 3)
    if d == 1:
        s = b-a
        A,B,C = 4*a*c-1,4*a,e
        assert B*B-4*A*C == -4*n
        # Swap then shear by c: [e,-4a,A] -> [e,2s,c^2 e-1].
        assert -4*a+2*c*e == 2*s and c*c*e-4*a*c+A == c*c*e-1
print('I24, I12, Type-II free parameters and I17 form dictionary: finite algebra checks PASS', flush=True)

def triples(p):
    # Factor identity for 1/y+1/z=A/B: (Ay-B)(Az-B)=B^2.
    out = []
    for x in range(p//4+1,3*p//4+1):
        A,B = 4*x-p,p*x
        g = gcd(A,B); A//=g; B//=g
        for u in ds(B*B):
            v = B*B//u
            if u > v or (u+B)%A or (v+B)%A:
                continue
            y,z = (u+B)//A,(v+B)//A
            if y >= x:
                out.append((x,y,z))
    return out

def lifts(p,n,H):
    out = set()
    # Enumerate signed divisors m of n, then solve g^2=p*h^2-m.
    for h in range(1,H+1):
        for m0 in ds(n):
            for m in (m0,-m0):
                v = p*h*h-m
                if v < 0:
                    continue
                g = isqrt(v)
                if g*g == v and gcd(g,h) == 1:
                    out.update((F(g,h),F(-g,h)))
    return out

def positive_quadratic(r,s,p):
    # Decide r+s*sqrt(p)>=0, independently of Decimal approximations.
    if not s:
        return r >= 0
    if not r:
        return s > 0
    if r > 0 and s > 0:
        return True
    if r < 0 and s < 0:
        return False
    return r*r >= s*s*p if r > 0 else s*s*p >= r*r

H = 40
nt, no_lift = 0, []
for p in primerange(5,400):
    if p%4 != 1:
        continue
    hit = False
    for ns in triples(p):
        nt += 1
        assert sum((F(1,n) for n in ns),F(0)) == F(4,p)
        mu = min(abs(sum((F(s,n) for s,n in zip(signs,ns)),F(0))) for signs in product((-1,1),repeat=3))
        assert mu >= F(3,H*H*p)
        ls = [lifts(p,n,H) for n in ns]
        for i in range(3):
            j,k = [v for v in range(3) if v != i]
            for w in ls[i]:
                A = w/ns[i]
                for sj,sk in product((-1,1),repeat=2):
                    B = F(sj,ns[j])+F(sk,ns[k])
                    assert positive_quadratic(A*A+p*B*B-F(4,H**4*p),2*A*B,p)
        for i,j,k in ((0,1,2),(0,2,1),(1,2,0)):
            for u in ls[i]:
                for v in ls[j]:
                    w = -ns[k]*(u/ns[i]+v/ns[j])
                    m = p*w.denominator**2-w.numerator**2
                    if m and ns[k]%m == 0:
                        hit = True
    if not hit:
        no_lift.append(p)
assert nt == 647 and len(no_lift) == 36 and 5 not in no_lift
print('I23: independent factor enumeration, all 647 triples, exact truncation and two-small-lift search PASS;',len(no_lift),'no-lift primes', flush=True)

# Late tail data: independent exact counts at every published block minimiser.
all_min = [(1465,4),(5481,2),(25305,4),(111969,2),(978145,6),(2646105,8),(4808265,6),(17158185,14),(88601865,19),(320411025,18)]
prime_min = [(2521,4),(9601,8),(21841,14),(76441,14),(351289,18),(4149601,18),(5516281,24),(17287201,30),(111664081,36),(278893729,46)]
for n,c in all_min+prime_min:
    assert sum(map(certificate,words(n))) == c,(n,c)
print('Tail: exact counts at all 20 published minimisers PASS (not a full 1e9 recount)', flush=True)

# Screen compatibility: positivity for C is permitted where narrower lines vanish.
def load(name):
    return [int(line.split()[0]) for line in (BASE/'data/z58/screens'/name).read_text().splitlines() if line.strip() and not line.startswith('#')]
for name in ('star_prime_zeros.txt','gstar_zeros.txt','composite_zeros_le8e6.txt'):
    values = load(name)
    zero = []
    for n in values:
        ws = words(n)
        if name != 'gstar_zeros.txt':
            assert not any(y%4 == 0 for x,y,z in ws)
        if not any(certificate(w) for w in ws):
            zero.append(n)
    assert zero == ([105] if name.startswith('composite') else [])
    print('Screen',name,len(values),'C-zeros',zero,flush=True)
# F2: certify an odd-C star witness at every archived R8 zero, without pretending
# that this finite witness search re-certifies absence of all even-C witnesses.
for p in load('r8_zeros_1e10.txt'):
    found = False
    for d in range(1,2001,2):
        N = 4*d*p+1
        for f in ds(N):
            if f%(4*d) == 4*d-1:
                a,b = (f+1)//(4*d),(N//f+1)//(4*d)
                assert 4*a*b*d-a-b == p
                found = True
                break
        if found:
            break
    assert found,p
print('F2: all 12 archived R8 zeros have independently checked odd-C star witnesses', flush=True)
print('ALL CHECKS PASS')
