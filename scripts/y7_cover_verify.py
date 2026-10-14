# y7 (O215): turn the level-L covering into explicit certificates and verify them exactly on all primes <= X.
# usage: y7_cover_verify.py M L X   (prints primes p<=X, p∤L, NOT certified, and their residues)
import sys
from math import gcd
from fractions import Fraction
from y7_mordell_cover import divisors
def families(M,L):
    F=[]  # (modulus q, class r, kind, params)
    D=divisors(L)
    for q in D:
        if q%M==0:
            ab=q//M
            for a in divisors(ab):
                b=ab//a
                for e in divisors(a+b):
                    F.append((q,(-e)%q,'IId',(a,b,e)))
                    if gcd(e,q)==1: F.append((q,(-pow(e,-1,q))%q,'Id',(a,b,e)))
            r=q//M
            for a in divisors(r):
                for d in divisors(r//a):
                    e=r//(a*d); F.append((q,(-M*a*a*d-e)%q,'IIc',(a,d,e)))
            for a in divisors(r):
                d=r//a; t=M*a*a*d+1
                for e in divisors(t): F.append((q,(-(t//e))%q,'Ic',(a,d,e)))
    for g in D:
        if (g+1)%M==0:
            acd=(g+1)//M
            for a in divisors(acd):
                for d in divisors(acd//a):
                    c=acd//(a*d); F.append((g,(-M*a*a*d)%g,'IIe',(a,c,d)))
    return F
def cert(M,n,fam):
    q,r,k,P=fam
    if k=='IId':
        a,b,e=P; d=(n+e)//(M*a*b); c=(a+b)//e
        return (a*b*d, a*c*d*n, b*c*d*n)
    if k=='Id':
        a,b,e=P; d=(n*e+1)//(M*a*b); c=(a+b)//e
        return (a*b*d*n, a*c*d, b*c*d)
    if k=='IIc':
        a,d,e=P; c=(n+e+M*a*a*d)//(M*a*d*e); b=c*e-a
        return (a*b*d, a*c*d*n, b*c*d*n)
    if k=='Ic':
        a,d,e=P; c=(n+(M*a*a*d+1)//e)//(M*a*d); b=c*e-a
        return (a*b*d*n, a*c*d, b*c*d)
    if k=='IIe':
        a,c,d=P; g=q; e=(n+M*a*a*d)//g; b=c*e-a
        return (a*b*d, a*c*d*n, b*c*d*n)
def primes(X):
    s=bytearray([1])*(X+1); s[0]=s[1]=0
    for i in range(2,int(X**.5)+1):
        if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
    return [i for i in range(X+1) if s[i]]
if __name__=="__main__":
    M,L,X=map(int,sys.argv[1:4])
    F=families(M,L)
    byclass={}
    for fam in F:
        q,r=fam[0],fam[1]
        for R in range(r,L,q): byclass.setdefault(R,[]).append(fam)
    bad=[];ok=0
    for p in primes(X):
        if L%p==0 or M%p==0: continue
        got=False
        for fam in byclass.get(p%L,[]):
            den=cert(M,p,fam)
            if den and min(den)>0 and Fraction(1,den[0])+Fraction(1,den[1])+Fraction(1,den[2])==Fraction(M,p):
                got=True;break
        if got: ok+=1
        else: bad.append(p)
    res=sorted(set(p%L for p in bad))
    print(f"M={M} L={L} X={X}: certified {ok}, not certified {len(bad)}; residues of uncertified mod L: {res[:20]}{'...' if len(res)>20 else ''}")
