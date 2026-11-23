"""Small two-auxiliary reconstruction; equality of the entire residue is tested."""
from math import gcd,lcm,isqrt,prod

def fac(k):
    a={}; t=2
    while t*t<=k:
        while k%t==0: a[t]=1+a.get(t,0); k//=t
        t+=1
    if k>1: a[k]=1
    return a

def primes(x): return [r for r in range(2,x) if not any(r%d==0 for d in range(2,isqrt(r)+1))]
def oddpart(k): return k//(k&-k)

if __name__=='__main__':
    # Constructible signs at one K, not a claim to have reached the proof's large-q regime.
    P=primes(6000); Q=[q for q in P if q<100 and q%4==1]; count=0; nonzero=0
    for p in P:
        if p%8!=1: continue
        for q in Q:
            if pow(p,(q-1)//2,q)!=q-1: continue
            for s in P[:160]:
                k=q*s
                if k%8!=3 or pow(p,(s-1)//2,s)!=1: continue
                x=(p+k)//4; f=fac(x); bs=[b for b in f if pow(b,(q-1)//2,q)==q-1 and pow(b,(s-1)//2,s)==s-1]
                if len(bs)<2: continue
                b1=next((b for b in bs if f[b]==1),None)
                if not b1: continue
                b2=next(b for b in bs if b!=b1); h=oddpart(lcm(q-1,s-1)); lam=lcm(q-1,s-1)
                j=next(j for j in range((q-1)//2) if pow(x//b1*pow(b2,2*j,q),h,q)==q-1)
                ds={b:((h*(v+2*j*(b==b2)))%lam if b!=b1 else 0) for b,v in f.items()}
                assert prod(pow(b,i,k) for b,i in ds.items())%k==k-1
                assert all(i<=f[b] or i%2==f[b]%2 and (i-f[b])//2<lam/2 for b,i in ds.items())
                count+=1; nonzero+=bool(j)
                if count>=200 and nonzero: break
            else: continue
            break
        else: continue
        break
    assert count>0 and nonzero
    print('two-auxiliary complete residue and legal overflow checks',count,'nonzero square adjustments',nonzero)
