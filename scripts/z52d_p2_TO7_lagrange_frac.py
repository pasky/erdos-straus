# Z2833: forms Q(A,B)=nA^2-2mu AB+B^2, n=p prime, f=mu^2-n>0, theta=(mu+sqrt f)/n (root of n x^2-2mu x+1=0).
#   Test: every primitive (A,B) with 0<|Q|<sqrt(f) has B/A or A/B a convergent of theta? (Lagrange-type claim)
# Z2908: for n, the 'U+U' membership of 4/n - 1/d is exactly a two-term Egyptian representation: count d with 4/n-1/d = 1/e+1/f.
import math, sys
from fractions import Fraction
def convergents_of_quadratic(mu,n,f,K=60):
    # theta = (mu + sqrt f)/n : compute continued fraction via exact integer arithmetic on (P + sqrt D)/Q
    D=f
    # theta = (mu + sqrt(D))/n ; represent x=(P0+sqrt D)/Q0 with Q0 | D-P0^2
    P0,Q0=mu,n
    if (D-P0*P0)%Q0!=0:
        # scale: (mu+sqrt D)/n = (n mu + sqrt(n^2 D))/n^2 ; use general algorithm with Q dividing D - P^2 after scaling
        P0,Q0=mu*n, n*n; D=n*n*f
    a=[]; conv=[]
    h0,h1=1,None; k0,k1=0,1
    h_prev,h_cur=0,1; k_prev,k_cur=1,0
    cons=[]
    for _ in range(K):
        sq=math.isqrt(D)
        val=(P0+sq)//Q0 if Q0>0 else 0
        # floor((P0+sqrt D)/Q0)
        if Q0<0: val=(P0+sq)//Q0
        a_i=val
        cons.append(a_i)
        P0=a_i*Q0-P0
        Q0=(D-P0*P0)//Q0
        if Q0==0: break
    # convergents
    p_2,p_1=0,1; q_2,q_1=1,0
    res=[]
    for ai in cons:
        pn=ai*p_1+p_2; qn=ai*q_1+q_2
        res.append(Fraction(pn,qn)); p_2,p_1=p_1,pn; q_2,q_1=q_1,qn
    return res
from decimal import Decimal, getcontext
getcontext().prec=120
def cf_convergents(x, K=60):
    # convergents of a real x (Decimal), exact Fractions
    res=[]; p_2,p_1=0,1; q_2,q_1=1,0
    y=x
    for _ in range(K):
        a_i=int(y.to_integral_value(rounding='ROUND_FLOOR'))
        pn=a_i*p_1+p_2; qn=a_i*q_1+q_2
        res.append(Fraction(pn,qn)); p_2,p_1=p_1,pn; q_2,q_1=q_1,qn
        frac=y-a_i
        if frac==0: break
        y=1/frac
    return res
def is_prime(n): return n>1 and all(n%d for d in range(2,int(n**.5)+1))
tot=0; bad=0; examples=[]
for n in [q for q in range(3,160) if is_prime(q)]:
    rn=int(math.isqrt(n))
    for mu in range(rn+1, 3*rn+2):
        f=mu*mu-n
        if f<=0: continue
        sf=math.sqrt(f)
        sfD=Decimal(f).sqrt()
        conv=set(cf_convergents((mu+sfD)/n,K=40))|set(cf_convergents((mu-sfD)/n,K=40))
        # enumerate small primitive (A,B), 1<=|A|,|B|<=40
        for A in range(-40,41):
            for B in range(-40,41):
                if A==0 or B==0: continue
                if math.gcd(abs(A),abs(B))!=1: continue
                V=n*A*A-2*mu*A*B+B*B
                if V==0 or abs(V)>=sf: continue
                tot+=1
                ok = Fraction(A,B) in conv or Fraction(B,A) in conv or Fraction(-A,B) in conv or Fraction(-B,A) in conv
                # also allow sign conventions via absolute value
                ok = ok or any(abs(c.numerator)==abs(A) and abs(c.denominator)==abs(B) for c in conv) or any(abs(c.numerator)==abs(B) and abs(c.denominator)==abs(A) for c in conv)
                if not ok:
                    bad+=1
                    if len(examples)<5: examples.append((n,mu,A,B,V))
print(f"Z2833: primitive (A,B) with 0<|V|<sqrt f (|A|,|B|<=40, p<160): {tot}; not from a convergent of theta: {bad}; examples {examples}")
# Z2908
cnt=[]
for n in range(100,201):
    c=0; tot_d=0
    for d in range(n//4+1, 2*n+1):
        r=Fraction(4,n)-Fraction(1,d)
        if r<=0: continue
        tot_d+=1
        a,b=r.numerator,r.denominator
        # 1/e+1/f = a/b with e<=f : e in [b/a, 2b/a]
        ok=False
        for e in range(max(1,b//a+1 if b%a else b//a), 2*b//a+2):
            num=a*e-b
            if num>0 and (b*e)%num==0: ok=True; break
        c+=ok
    cnt.append((n,c,tot_d))
ES=[ (n,c) for n,c,_ in cnt if c==0]
print("Z2908: n in [100,200]: #d (n/4<d<=2n) with 4/n-1/d a 2-term sum: min over n",min(c for _,c,_ in cnt),"max",max(c for _,c,_ in cnt),"; n with zero two-term witnesses:",ES[:5])
print("Z2908: mean fraction of d with 2-term witness =", round(sum(c/t for _,c,t in cnt)/len(cnt),4))
