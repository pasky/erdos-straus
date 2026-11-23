"""Validate the bridge ranks' two valuation columns and full normalized rectangle.
Run in the repo root, alongside z83_jug_dyadic.py. Integer/Fraction only.
"""
from fractions import Fraction as F
from math import gcd,prod,lcm
from itertools import product
from sympy import primerange
from z83_jug_dyadic import factors,prime

def crt(x,m,y,n):
    return (x+m*((y-x)*pow(m,-1,n)%n))%(m*n)

def red(a,l):
    return a.numerator*pow(a.denominator,-1,l)%l

def val(a,l):
    def v(n):
        assert n
        e=0
        while n%l==0:n//=l;e+=1
        return e
    return v(a.numerator)-v(a.denominator)

def den(P):return lcm(*(q.denominator for q in P))

def bridge(p,W,E):
    h=F(p,4)
    X=[h/u for u in W];Y=[h/u for u in E]
    c,d=X[0],Y[0]; assert c!=d and c>0 and d>0
    v0=X[2]/X[1];v1=Y[2]/Y[1];assert v0!=1 and v1!=1
    exc=prod(z.numerator*z.denominator for z in [c,d,1-c,1-d,c-d,v0,v1])
    s,t=[l for l in primerange(5,1000) if exc%l][:2]
    N=crt((1+s)*pow(red(1-c,s*s),-1,s*s),s*s,(1+t)*pow(red(1-d,t*t),-1,t*t),t*t)
    bound=max(1/(1-c),1/(1-d)); stride=s*s*t*t
    N+=max(0,1+(bound-N)//stride)*stride
    assert N>bound
    b=F(1,N);W2=[c,b,1-c-b];W3=[d,b,1-d-b]
    print('bridge CRT',s,t,N)
    for P,Q,i in [(X,W2,0),(W2,W3,1),(W3,Y,0)]:
        assert sum(P)==sum(Q)==1 and all(a>0 for a in P+Q)
        j,k=sorted({0,1,2}-{i});A=P[k]/P[j];B=Q[k]/Q[j];w=A*B
        assert P[i]==Q[i] and A!=B and h/P[j]+w*h/P[k]==h/Q[j]+w*h/Q[k]
        assert ((val(A,s),val(A,t)),(val(B,s),val(B,t)))=={
            (0,0):((0,0),(1,0)),(1,0):((1,0),(0,1)),(0,1):((0,1),(0,0))
        }[val(A,s),val(A,t)]
        print(' s,t valuations of ratios',val(A,s),val(A,t),';',val(B,s),val(B,t))

def pick_split(n,k,full):
    eligible=[]
    for l,m in factors(n).items():
        if pow(l,15,31)==30 and (not full or l>31 and l%4==3):eligible.extend([l]*m)
    count=15 if full else 3
    assert len(eligible)>=count
    ls=eligible[:count]
    # Dynamic programming in the signed box with occurrence labels; stop when
    # a coefficient vector has the actual required residue. No 3^15 table.
    m=124 if full else 31;states={1:(1,1)}
    for l in ls:
        nxt=states.copy()
        for a,(u,v) in states.items():
            nxt.setdefault(a*l%m,(u*l,v));nxt.setdefault(a*pow(l,-1,m)%m,(u,v*l))
        states=nxt
    for j in ([0] if full else [-2,-1,0,1,2]):
        key=-pow(2,-j,31)%31 if not full else 123
        if key not in states:continue
        A,C=states[key];A*=2**max(0,j);C*=2**max(0,-j);g=gcd(A,C);A//=g;C//=g
        assert n%(A*C)==0 and (A+C)%m==0
        return max(A,C),min(A,C)
    raise AssertionError('missing promised quotient transfer')

def run(p,full):
    k=31;N=(p+k)//4;A,C=pick_split(N,k,full);g=(N//(A*C))*((A+C)//k)
    assert prime(p) and all(l%4==1 for l in factors((p+1)//2)) and p%1680==1
    print('p',p,'x31_factors',factors(N),'halfprime_factors',factors((p+1)//2),'A,C',A,C)
    W=[F(p,2),F(p+1,2),F(p*(p+1),2)]
    U=[F(p*N,k),F(g*k*A),F(g*k*C)]
    T=[F(N),F(g*p*A),F(g*p*C)]
    E=[F(p*(A+C),4*A),F(g*k*A),F(g*p*A)] if full else U
    for P in [W,E,U,T]:assert sum(F(1,u) for u in P)==F(4,p)
    # retained position zero at W has share 1/2; if A=C impossible by coprimality
    bridge(p,W,E)
    assert den(U)==31 and all(y%31==0 for y in U[1:]) and den(T)==1
    if full:
        assert A>31 and den(E)==A and all(y%A==0 for y in E[1:])
        assert E[1]==U[1] and sum(F(1,q) for q in [g*A*k,g*A*p,g*C*k,g*C*p])==F(4,p)
    u=F(p,4)/U[0];s=[F(p,4)/z for z in U];s=[1-u,u*s[1]/(1-u),u*s[2]/(1-u)]
    assert T==[F(p,4)/z for z in s]
    print('terminal denominator chain',([den(E)] if full else [])+[den(U),den(T)])

if __name__=='__main__':
    run(680401,False);run(31059039896040814550874265201,True)
    # 28 marked occurrences can miss every odd-C word at outer letter 31.
    L=39454073;r,s=43,571;N=4*(r*s)**14*L;p=4*N-31
    assert prime(L) and prime(p) and prime((p+1)//2) and p%1680==1
    assert L%248==1 and r%8==s%8==3 and r*s%31==1
    assert pow(r,15,31)==30 and all(pow(r,j,31)!=30 for j in range(-14,15))
    print('28-mark sharpness',p,'factors of odd K',r,s,'each x14, plus',L,'odd-C at outer 31: none')
    # At 8 the actual same k=31 box at 680401 has no hit even including p.
    for M in [4,8]:
        p=680401; N=(p+31)//M;R={1}
        for q,v in factors(p*N).items():R={r*pow(q,i,31)%31 for i in range(-v,v+1) for r in R}
        print('k=31 full box: M',M,'x',N,'hits',30 in R)
