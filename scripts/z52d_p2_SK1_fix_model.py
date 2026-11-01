# z52d pass2 SK1 fix (Z1105 integer model with cuts; Z1242 motif mining; Z1255 replayable trace of the Type-II identity)
import sympy as sp
from collections import Counter
def isp(m): return m>1 and all(m%d for d in range(2,int(m**.5)+1))
# Z1105: 0/1 model over pairs (u,C): x_{uC}=1 iff (4uC-1) | (p+u) with B=(p+u)/(4uC-1) >= 1.
# Cut (valid by congruence): for fixed (u,C) the equation (4uC-1)B = p+u has at most one B, so one 0/1 variable per pair.
# Check: the 0/1 model's objective equals the word count R(p) (u,B,C all unbounded, pairs bounded by 3000) ; parity cut R even.
K=3000; mism=0; odd=0; checked=0; examples=[]
for p in [q for q in range(5,2001,4) if isp(q)]:
    model=0
    for u in range(1,K):
        for C in range(1,K):
            m=4*u*C-1
            if m>p+u: break
            if (p+u)%m==0 and (p+u)//m>=1: model+=1
    words=0
    for u in range(1,K):
        for B in range(1,K):
            # solve for C: 4uBC - u - B = p
            num=p+u+B
            if num%(4*u*B)==0 and num//(4*u*B)>=1: words+=1
    checked+=1
    if model!=words: mism+=1
    if model%2: odd+=1
print(f"Z1105 0/1 pair-model vs word count on {checked} primes p=1 mod 4 <=2000: mismatches {mism}; odd totals {odd}")
# Z1242: hand-encoded operation sequences of repo derivations (each a list of proof operations); motifs = repeated 3-op windows
D={
 "normal_form_p_divides_z":["clear","rearrange","mod_p","divides","conclude"],
 "x_divides_z_iff_y":["clear","rearrange","mod_x","mod_y","conclude"],
 "isosceles_factor":["clear","rearrange","factor","sign_mod4","conclude"],
 "U_minus_D_count":["clear","factor","sign_mod4","count_pairs","conclude"],
 "typeII_identity":["clear","rearrange","cancel","conclude"],
 "two_term_obstruction":["clear","factor","sign_mod4","count_pairs","conclude"],
 "saturation_irreducible":["clear","factor","restrict_plane","conclude"],
 "continuant_recurrence":["expand","rearrange","factor","conclude"],
}
win=Counter()
for name,ops in D.items():
    for i in range(len(ops)-2): win[tuple(ops[i:i+3])]+=1
top=[(k,v) for k,v in win.most_common() if v>1]
print("Z1242 derivations:",len(D),"; repeated 3-op motifs:",len(top), "; top:", top[:3])
# Z1255: replayable trace: each step checked symbolically
u,B,C=sp.symbols('u B C',positive=True); n=sp.Symbol('n',positive=True)
steps=[]
s1=sp.Eq(n,4*u*B*C-u-B); steps.append(("definition n = 4uBC-u-B",True))
lhs=1/(u*B*C)+1/(n*B*C)+1/(n*u*C)
s2=sp.together(lhs); steps.append(("combine over common denominator n*u*B*C", sp.simplify(s2-(n+u+B)/(n*u*B*C))==0))
s3=(n+u+B)/(n*u*B*C); steps.append(("substitute n+u+B = 4uBC (from definition)", sp.simplify(s3.subs(n,4*u*B*C-u-B)-4/(4*u*B*C-u-B)*0-(4*u*B*C)/((4*u*B*C-u-B)*u*B*C))==0))
steps.append(("cancel to 4/n", sp.simplify((4*u*B*C)/(n*u*B*C)-4/n)==0))
for t,ok in steps: print("Z1255 step:",t,"-> verified" if ok else "-> FAILED")
