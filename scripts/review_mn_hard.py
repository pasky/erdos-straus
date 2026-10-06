# From-scratch: Type-II-hard sets H_m(Q) and the m=7 small-prime death claim (review R63).
from math import gcd
from sympy import divisors, factorint
def atoms_dividing(m,Q):
    out=[]
    for M in divisors(Q):
        if M>=3 and M%m==m-1:
            A=(M+1)//m
            out.append((M,{(-m*D)%M for D in divisors(A*A)}))
    return out
def hard(m,Q):
    at=atoms_dividing(m,Q)
    return [r for r in range(Q) if gcd(r,Q)==1 and all(r%M not in C for M,C in at)]
for m,Q in [(4,840),(5,840),(8,840),(6,840),(7,840)]:
    H=hard(m,Q); print("m",m,"Q",Q,"|H|",len(H), "1 in H",1 in H)
H5=hard(5,840); print("H_5(840) mod 7:",sorted({r%7 for r in H5}), "mod 8:",sorted({r%8 for r in H5}),"mod 3",sorted({r%3 for r in H5}),"mod 5",sorted({r%5 for r in H5}))
print("H_5(840) == {r: r%7 in {1,3,5}}:", set(H5)=={r for r in range(840) if gcd(r,840)==1 and r%7 in (1,3,5)})
H4=hard(4,840); sq={r for r in range(840) if gcd(r,840)==1 and all(pow(r,(p-1)//2,p)==1 for p in (3,5,7))}
print("m=4: squares-at-odd-primes subset of H_4(840):", sq<=set(H4), len(sq))
# m=7 death at l=3: atoms M=2^a 3^b <= T, M = 6 mod 7
T=20000; m=7
def e_max(l): 
    return max((factorint(M).get(l,0) for M in range(3,T+1) if M%m==m-1), default=0)
e2,e3=e_max(2),e_max(3); Q2,Q3=2**e2,3**e3
at2=[(M,{(-m*D)%M for D in divisors(((M+1)//m)**2)}) for M in range(3,T+1) if M%m==m-1 and Q2%M==0]
at23=[(M,{(-m*D)%M for D in divisors(((M+1)//m)**2)}) for M in range(3,T+1) if M%m==m-1 and (Q2*Q3)%M==0 and M%3==0]
allowed2=[r for r in range(1,Q2,2) if all(r%M not in C for M,C in at2)]
dead=0
for r2 in allowed2:
    ok=0
    for r3 in range(Q3):
        if r3%3==0: continue
        # CRT residue mod Q2*Q3
        r=(r2*Q3*pow(Q3,-1,Q2)+r3*Q2*pow(Q2,-1,Q3))%(Q2*Q3)
        if all(r%M not in C for M,C in at23): ok+=1
    if ok==0: dead+=1
print("m=7 T=2e4: e2,e3",e2,e3,"allowed 2-adic units",len(allowed2),"of",Q2//2,"dead at 3:",dead, "frac",dead/len(allowed2))
cand={r for r in range(840) if gcd(r,840)==1 and r%4==1 and r%7 in (1,3,5)}
print("H_5(840) == {r=1 (4), r%7 in {1,3,5}}:", set(H5)==cand)
print("joint (mod 8, mod 7) pairs:", sorted({(r%8,r%7) for r in H5}))
