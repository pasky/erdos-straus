"""z52d pass2 TO6 quick exact checks (Z2033, Z2366, Z2209/Z2210/Z2227/Z2229/Z2231, Z2028/Z2085, Z2417, Z2268, Z2215 cross-check).
Memory-bounded: sieves to <= 1e6 / 1e4 only."""
import sys, json
from sympy import primerange, factorint, divisors
out = {}

# Z2033: diagonal solutions 4/p = 2/x + 1/z, check existence by residue class of p mod 4 (exact, all p<=2e5)
diag_r1 = diag_r3 = 0; ex_r3 = []
for p in primerange(3, 200000):
    # x=y: a=4x-2p must divide-type: from a(4z-p)=2p^2 with a=4x-2p; enumerate all positive divisors a of 2p^2
    found = False
    for a in divisors(2*p*p):
        if (a + 2*p) % 4: continue
        x = (a + 2*p)//4
        num = 2*p*p//a + p
        if num % 4: continue
        z = num//4
        if x>0 and z>0 and 4*x-2*p==a:
            found = True; break
    if found:
        if p % 4 == 1: diag_r1 += 1
        else:
            diag_r3 += 1
            if len(ex_r3) < 5: ex_r3.append((p, (a+2*p)//4, z))
out['Z2033'] = dict(diag_p1mod4=diag_r1, diag_p3mod4=diag_r3, examples_p3mod4=ex_r3)

# Z2366: two-term reps 3/p = 1/x+1/y and 4/p = 1/x+1/y, by residue mod 3 / mod 4 (p<=3000)
def two_term(k,p):
    # (kx-p)(ky-p)=p^2 ; need a=kx-p a positive-or-negative divisor of p^2 with a ≡ -p (mod k)
    for a in [1,p,p*p]:
        if (a+p)%k==0:
            return True
    return False
r3 = {}; r4 = {}
for p in primerange(3,3000):
    r3.setdefault(p%3,[0,0])[two_term(3,p)] += 1
    r4.setdefault(p%4,[0,0])[two_term(4,p)] += 1
out['Z2366'] = dict(three_over_p_two_terms_by_p_mod3={k:{'no':v[0],'yes':v[1]} for k,v in r3.items()},
                    four_over_p_two_terms_by_p_mod4={k:{'no':v[0],'yes':v[1]} for k,v in r4.items()})

# Z2209/Z2210/Z2227/Z2229/Z2231: representability by xy+yz+zx with x,y,z>=1 up to NMAX
NMAX = 10000
rep = bytearray(NMAX+1)
for x in range(1, NMAX):
    for y in range(x, NMAX):
        if x*y + y*(x+y) > NMAX: break
        for z in range(y, NMAX):
            v = x*y + z*(x+y)
            if v > NMAX: break
            rep[v] = 1
def squarefree(n):
    f = factorint(n); return all(e==1 for e in f.values())
def has_sq(n):
    f = factorint(n); return any(e>=2 for e in f.values())
nonrep = [n for n in range(1,NMAX+1) if not rep[n]]
sf_nonrep = [n for n in nonrep if squarefree(n)]
sq_nonrep = [n for n in nonrep if has_sq(n)]
out['xy+yz+zx'] = dict(NMAX=NMAX, nonrep_count=len(nonrep), nonrep_all=nonrep[:80],
    squarefull_nonrep=sq_nonrep, squarefree_nonrep=sf_nonrep,
    count_sqfree_nonrep=len(sf_nonrep))

# Z2028/Z2085: odd n <= X not of form p + 2^a + 2^b (a,b >= 0, a<=b), with p prime (p=2 included)
X = 200000
pow2 = sorted({2**a for a in range(0, 19)})
reach = bytearray(X+1)
isp = bytearray([1])*(X+1); isp[0]=isp[1]=0
for i in range(2, int(X**0.5)+1):
    if isp[i]: isp[i*i::i] = bytearray(len(isp[i*i::i]))
pr = [i for i in range(X+1) if isp[i]]
for p in pr:
    for i,a in enumerate(pow2):
        for b in pow2[i:]:
            v = p + a + b
            if v <= X: reach[v] = 1
            else: break
exc = [n for n in range(3, X+1, 2) if not reach[n]]
out['Crocker'] = dict(X=X, exceptions_count=len(exc), first_exceptions=exc[:60],
                      last_exceptions=exc[-20:])

# Z2417 / Z2023: least quadratic non-residue l(p) for primes p <= 10^6 (l(p) = least prime q with (q/p) = -1)
P = 1000000
isp2 = bytearray([1])*(P+1); isp2[0]=isp2[1]=0
for i in range(2,int(P**0.5)+1):
    if isp2[i]: isp2[i*i::i]=bytearray(len(isp2[i*i::i]))
small_primes = [q for q in range(2,2000) if isp2[q]]
def legendre(a,p):
    r = pow(a,(p-1)//2,p); return -1 if r==p-1 else (0 if r==0 else 1)
lmax = (0,0); cnt_ge = {13:0,17:0,19:0,23:0}; ex_ge17 = []
dist = {}
for p in range(3,P+1):
    if not isp2[p]: continue
    l = None
    for q in small_primes:
        if q == p: continue
        if legendre(q,p) == -1: l = q; break
    dist[l] = dist.get(l,0)+1
    if l > lmax[0]: lmax = (l,p)
    for t in cnt_ge:
        if l >= t: cnt_ge[t] += 1
    if l >= 17 and len(ex_ge17) < 10: ex_ge17.append((p,l))
out['leastQNR'] = dict(P=P, max_l=lmax[0], at_p=lmax[1], count_l_ge=cnt_ge, example_primes_l_ge17=ex_ge17,
                       dist_head={k:dist[k] for k in sorted(dist)[:12]})

# Z2268: greedy Egyptian expansion of 4/p: number of terms, primes p<=1e5
from fractions import Fraction
def greedy_len(p):
    r = Fraction(4,p); terms=[]
    while r > 0 and len(terms) < 200:
        x = -(-r.denominator // r.numerator)  # ceil(1/r)
        terms.append(x); r -= Fraction(1,x)
    return len(terms), terms[:3]
lens = {}
for p in primerange(5, 100000):
    if p % 4 != 1: continue
    L,_ = greedy_len(p); lens[L] = lens.get(L,0)+1
out['greedy_4_over_p_p1mod4'] = dict(length_hist=dict(sorted(lens.items())[:15]))
print(json.dumps(out, default=str, indent=None)[:20000])
json.dump(out, open('data/z52b/pass2/TO6/quick_checks.json','w'), default=str, indent=1)
