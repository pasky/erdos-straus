"""Independent checks: exact rectangular fraction search; exact word moduli at
small controls; verify panel certificates and fit two (non-identified) tails.
Run with -B; build z80_extreme_words.c into data/z80/extreme/words.bin first.
"""
import csv,math,subprocess,sys
from pathlib import Path
from collections import Counter
from z80_extreme_et import count,P
D=Path('data/z80/extreme')
def brute(n,k):
    ans=[]
    for x in range(n//k+1,3*n//k+1):
        g=k*x-n;s=n*x
        for h in P.divisors(s*s).python():
            if h>s:break
            if (s+h)%g or (s+s*s//h)%g:continue
            y=(s+h)//g;z=(s+s*s//h)//g
            if x<=y:ans.append((x,y,z))
    return ans

def word(n):
    # enumerate f=tu-1; v>=1, u<=f+1. For t=1, (u-1)(v-1)=n+1
    # implies f<=n+1; for t>=2, u<=(f+1)/2 gives f<=2n+1.
    R=C=U=S=W=0;H=0
    for f in range(1,2*n+2):
        for u in range(f-n%f,f+2,f):
            if (f+1)%u:continue
            t=(f+1)//u;v=(n+u)//f;W+=1;R+=t%4==0;C+=t%8==0;U+=t*u%8==0
            S+=min(x%4 for x in (u,t,v,f,t*v-1))==0
            if not H and min(u,t,v)>=2 and P.kronecker(f,n)==-1:H=f
    return R,C,U,S,H,W

def check():
    for n in range(3,251,2):
        if not P.isprime(n) and math.isqrt(n)**2!=n:continue
        s=count(n);direct=brute(n,4); expected=[0,0]
        for triple in direct:
            m=sum(x%n==0 for x in triple)
            if m in (1,2) and all(x%n==0 or math.gcd(x,n)==1 for x in triple):expected[m-1]+=1
        assert expected==list(map(len,s)),(n,expected,s)
        if n<=25 and P.isprime(n):
            # OEIS A073101, n=2 onward, stored in repo cache.
            A=[0,1,1,2,5,5,6,4,9,7,15,4,14,33,22,4,21,9,30,25,22,19,45,10]
            assert sum(x<y<z for x,y,z in direct)==A[n-2]
        if not P.isprime(n):print('odd square',n,'strict',expected,'all sorted',len(direct))
    assert not brute(131,8) and not brute(241,8)
    print('full 8/131 and 8/241: zero; odd primes <=250: ET = direct')
    z7=[105,1465,3865,4545,10305,12145,39361,67425]
    z4=[int(s) for s in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if not s.startswith('#')]+[17401609]
    ns=sorted(set([9,25,49,81,121,169,225,241,409]+z7+z4))
    rr=list(csv.DictReader(subprocess.check_output([D/'words.bin',*map(str,ns)],text=True).splitlines()))
    for row in rr:
        n,*r=map(int,row.values());R,C,U,S,H,W=r
        if n in z4 or n in z7 or math.isqrt(n)**2==n:assert R==0
        if n in z7:assert U==0
        if n<100000:assert tuple(r)==word(n)
    assert not count(4545)[1];print('R: 14 prime controls plus composite 17401609; U7 eight zeros; Type II at 4545 empty')
    # Cross-verify nontrivial full-count/AP computeds against literal identities
    for name in ('ap361','ap9240'):
        h=0;miss=[]
        for line in (D/(name+'.txt')).read_text().splitlines():
            if line.startswith('H '):
                n,u,b,c=map(int,line.split()[1:]);assert 8*u*b*c-u-b==n;h+=1
            elif line.startswith('MISS'):miss.append(int(line.split()[1]))
            else:assert line.startswith('# k=8') and f'hard_primes={h+len(miss)} ' in line
        print(name,h,'positive fallback identities;',miss)
    for row in csv.DictReader((D/'panel.csv').open()):
        n=int(row['n']);assert int(P.isprime(n))==int(row['prime']) and math.prod(map(int,row['factorization'].split('*')))==n
        if row['prime']=='0':continue
        x,y,z=map(int,row['first_xyz'].split(':'));assert x<=y<=z and 4*x*y*z==n*(x*y+x*z+y*z)
        for mode,key in enumerate(('R_first','R8_first','U7_first','HJ_first')):
            f=int(row[key]);
            if not f:continue
            # verify at least one appropriate tuple for each reported hit
            ok=False
            for u in P.divisors(f+1).python():
                if (n+u)%f:continue
                t=(f+1)//u;v=(n+u)//f
                ok|=(not t%4,not t%8,not t*u%8,min(u,t,v)>=2 and int(P.kronecker(f,n))==-1)[mode]
            assert ok
    print('All panel certificates: positive checked; completeness of windows from divisor enumeration.')

def fit():
    # screen-wide minima vs record-panel (not global above 30000).
    data=[]
    for line in Path('data/z52b/raw/f4_all_30000.txt').read_text().splitlines():
        n,f,*_=map(int,line.split());
        if P.isprime(n):data.append((n,f))
    for d in range(1,5):
        bins=[(n,f) for n,f in data if 10**(d-1)<=n<10**d];low=min(f for n,f in bins);r,n=min((f/math.log(n)**3,n) for n,f in bins)
        print('all-prime decade',d-1,len(bins),low,next(n for n,f in bins if f==low),r,n)
    rows=[(int(r['p']),int(r['I'])+int(r['II'])) for r in csv.DictReader((D/'et.csv').open())]
    for d in sorted(set(len(str(n))-1 for n,f in rows)):
        b=[(n,f) for n,f in rows if len(str(n))==d+1];print('record-list decade',d,len(b),min((f,n) for n,f in b),min((f/math.log(n)**3,n) for n,f in b))
    # Conditional working model: all primes with p=1 (8) and QR at 3,5,7,11.
    # Estimate central mean outside the SELECTED record list on this same fixed fibre.
    train=[(n,f) for n,f in data if n>=1000 and n%8==1 and all(P.kronecker(n,q)==1 for q in (3,5,7,11))]
    c=sum(f for n,f in train)/sum(math.log(n)**3 for n,f in train)
    phi=sum((f-c*math.log(n)**3)**2/(c*math.log(n)**3) for n,f in train)/(len(train)-1)
    # Compound Poisson with geometric clump size on {1,2,...}, Fano=2m-1.
    m=max(1,(1+phi)/2);print('fixed fibre',len(train),'c',c,'phi',phi,'m',m,'log10Pr0 at 1e18',-c*math.log(1e18)**3/m/math.log(10))
    pred=[(n,f/(c*math.log(n)**3)) for n,f in rows if n>=30000];print('record-list held out observed/predicted',min(v for n,v in pred),max(v for n,v in pred))
if __name__=='__main__':check();fit()
