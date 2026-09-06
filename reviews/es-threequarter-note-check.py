import resource
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024**2, 512 * 1024**2))
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
from math import gcd, lcm, comb, prod
from fractions import Fraction as Q

# Small exact class counts, not an asymptotic Shiu test.
def phi(n):
    return sum(gcd(a,n)==1 for a in range(n))
def rad(n):
    return prod(p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,int(p**.5)+1)))
profiles=0
for k in range(1,61):
    for g in range(1,k+1):
        if k%g: continue
        q0=lcm(g,rad(k))
        units=[a for a in range(q0) if gcd(a,q0)==1]
        counts=[0]*g
        for u in units:
            for v in units:
                a=(-u*pow(v,-1,g))%g if g>1 else 0
                counts[a]+=1
        for a,count in enumerate(counts):
            assert count == (phi(q0)**2//phi(g) if gcd(a,g)==1 else 0)
            profiles+=1
print('residue-profile unit/nonunit counts:',profiles,'PASS')

# Unequal prime powers, with/without selector: exact conditional probabilities.
local=0
for p in (3,5,7):
    for e in range(1,5):
        for f in range(5):
            for selected in (False,True):
                modulus=p**max(e,f)
                den=num=0
                for n in range(modulus):
                    if selected and n%p==0: continue
                    if f and n%(p**f)!=1: continue
                    den+=1
                    num += n%(p**e)==1
                qy=Q(p,p-1) if selected else Q(1)
                h=min(e,f)
                by=(p**(h-1)*(p-1) if selected and h else p**h)
                assert Q(num,den)==qy*by/(p**e)
                local+=1
print('prime-power relative probabilities:',local,'PASS')

atoms=[(1,29,3),(5,29,1),(25,29,2),(1,31,4),(9,31,5),(25,31,7)]
L=lcm(*(k for k,ell,a in atoms)); M=lcm(L,6)*29*31
hist={c:[0]*3 for c in range(L) if gcd(c,3)==1}
for n in range(M):
    if gcd(n,6)!=1: continue
    H=sum(n%(k*ell)==a%(k*ell) for k,ell,a in atoms)
    assert H<=2
    hist[n%L][H]+=1
for c,counts in hist.items():
    means=[Q(sum(c%k==a%k for k,ell,a in atoms if ell==p),p) for p in (29,31)]
    a,b=means
    law=[(1-a)*(1-b), a*(1-b)+(1-a)*b, a*b]
    den=sum(counts)
    assert [Q(v,den) for v in counts]==law
    for j in range(1,8):
        moment=sum(Q(counts[h],den)*prod(range(h-j+1,h+1)) for h in range(j,3))
        assert moment <= sum(means)**j
print('CRT residues enumerated:',M,'fibres:',len(hist),'moments through order 7: PASS')

checks=0
for r in range(0,41,2):
    for h in range(201):
        poly=sum((-1)**j*comb(h,j) for j in range(min(r,h)+1))
        assert poly==(1 if h==0 else (comb(h-1,r) if h-1>=r else 0))
        assert int(h==0)<=poly<=int(h==0)+(comb(h,r+1) if h>=r+1 else 0)
        checks+=1
print('even Bonferroni inequalities:',checks,'PASS')
rounding=0
for N in (0,1,2,17,100):
    for q in (1,2,3,17,101,1000):
        counts=[0]*q
        for n in range(1,N+1): counts[n%q]+=1
        assert all(abs(Q(count)-Q(N,q))<=1 for count in counts)
        if q>N: assert all(count<=1 for count in counts)
        rounding+=q
print('integer class rounding, including q>N:',rounding,'PASS')
print('These are finite algebra/CRT checks; no toy is asserted to instantiate H=K^10, z>=H^2.')
