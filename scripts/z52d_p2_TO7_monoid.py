# Z2847: level-t monoid transport n3 = t n1 n2 + n1 + n2 (identity (t n1+1)(t n2+1) = t n3 + 1), words at level t.
# Z2818: gcd(4Cp+1, 4C'p+1) divides C-C' (proof: d | C'(4Cp+1) - C(4C'p+1) = C'-C), numeric check.
import math, sys
sys.path.insert(0,'scripts')
from z52d_p2_TO7_words import words, leg
def wt(n,t):
    return [w for w in words(n) if w[0]==t]
res={}
for t in [2,3,4,5,6,8]:
    W={n:wt(n,t) for n in range(2,80)}
    ok=[n for n in W if W[n]]
    both=0; n3ok=0; signok=0; signtot=0
    for n1 in ok:
        for n2 in ok:
            if n1>n2: continue
            n3=t*n1*n2+n1+n2
            both+=1
            if n3<200 and n3%2==1 and n1%2==1 and n2%2==1:
                if n3 in W and W[n3]:  pass
            if n3 in W and W[n3]:
                n3ok+=1
    # sign: for n odd (prime-like), does some pair of words give sign product at n3?
    for n1 in ok:
        for n2 in ok:
            n3=t*n1*n2+n1+n2
            if n1%2==0 or n2%2==0 or n3%2==0 or n3>=400 or n3 not in W or not W[n3]: continue
            signtot+=1
            s1=set(leg(u*v,n1) for (_,u,v) in W[n1]); s2=set(leg(u*v,n2) for (_,u,v) in W[n2]); s3=set(leg(u*v,n3) for (_,u,v) in W[n3])
            if any(a*b in s3 for a in s1 for b in s2): signok+=1
    res[t]=dict(n_with_words=len(ok), pairs=both, n3_has_level_t_word=n3ok, odd_pairs_sign_tested=signtot, sign_product_realised=signok)
    print("t",t,res[t], flush=True)
# Z2818
bad=0; tot=0
for p in [q for q in range(5,3000) if all(q%d for d in range(2,int(q**0.5)+1))]:
    for C in range(1,13):
        for C2 in range(1,13):
            if C>=C2: continue
            tot+=1
            g=math.gcd(4*C*p+1,4*C2*p+1)
            if (C2-C)%g!=0: bad+=1
print("Z2818 gcd(4Cp+1,4C'p+1) | (C'-C) checked:",tot,"violations:",bad)
