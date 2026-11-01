# z52d pass2 SK1 fix round: Z1254 (parametric Type-II identity + integrality), Z1257 (property-based generation),
# Z1151 (continuant = tridiagonal determinant), Z1119 (single-valuedness of the completion rewrite),
# Z1111 (series/parallel splits of ES triples), Z1205 (straight-line size vs expanded digits).
import random, sympy as sp
from fractions import Fraction
from math import gcd
random.seed(7)
out = {}
# Z1254: symbolic identity 1/(uBC)+1/(nBC)+1/(nuC) = 4/n with n = 4uBC-u-B
u,B,C=sp.symbols('u B C',positive=True)
n=4*u*B*C-u-B
expr=sp.together(1/(u*B*C)+1/(n*B*C)+1/(n*u*C)-4/n)
out['Z1254_symbolic_residual'] = sp.simplify(expr)
# integrality: denominators uBC, nBC, nuC are integers whenever u,B,C integers and n integer -> trivially
# numeric check over all words with n prime
def isp(m): return m>1 and all(m%d for d in range(2,int(m**.5)+1))
ok=0; tot=0; words=0; primes_words=0
for uu in range(1,60):
  for BB in range(1,60):
    for CC in range(1,60):
      nn=4*uu*BB*CC-uu-BB
      if nn<1: continue
      words+=1
      if isp(nn):
          primes_words+=1
          tot+=1
          if Fraction(1,uu*BB*CC)+Fraction(1,nn*BB*CC)+Fraction(1,nn*uu*CC)==Fraction(4,nn): ok+=1
out['Z1254_numeric'] = f"words with n prime (u,B,C<60): {tot}; identity exact in {ok}; total words {words}"
# Z1257: random structured generation (hypothesis-respecting words), identity + positivity checks
fails=0; posfail=0; N=100000
for _ in range(N):
    uu=random.randint(1,500); BB=random.randint(1,500); CC=random.randint(1,500)
    nn=4*uu*BB*CC-uu-BB
    if nn<1: posfail+=1; continue
    if Fraction(1,uu*BB*CC)+Fraction(1,nn*BB*CC)+Fraction(1,nn*uu*CC)!=Fraction(4,nn): fails+=1
out['Z1257'] = f"{N} random words (u,B,C<=500): identity failures {fails}, nonpositive n skipped {posfail}"
# Z1151: continuant K(a1..ak) = det of tridiagonal matrix with a_i on diagonal and 1 off-diagonal
def continuant(a):
    p0,p1=1,a[0]
    for x in a[1:]: p0,p1=p1,x*p1+p0
    return p1
def tri_det(a):
    M=sp.zeros(len(a),len(a))
    for i,x in enumerate(a):
        M[i,i]=x
        if i+1<len(a): M[i,i+1]=1; M[i+1,i]=-1  # product -1 => recurrence K_n = a_n K_{n-1} + K_{n-2}
    return M.det()
bad=0
for _ in range(300):
    k=random.randint(1,6); a=[random.randint(1,9) for _ in range(k)]
    if continuant(a)!=tri_det(a): bad+=1
out['Z1151'] = f"300 random tridiagonal (size 1-6): continuant != determinant in {bad}"
# Z1119: completion rewrite z = p x y/(a y - p x), a=4x-p: single-valued (a function of (x,y)).
# Rule set: the only exact rewrite in the problem is the completion of a 2-term tail; check that every
# (x,y) yields at most one z and that distinct paths (x then y, y then x) give the same triple.
def isp2(m): return isp(m)
cnt_pairs=0; conflicts=0
for p in [p for p in range(3,501,2) if isp(p)]:
    for x in range(p//4+1,3*p//4+1):
        a=4*x-p
        if a<=0: continue
        for y in range(x,2*p*x//a+1):
            d=a*y-p*x
            if d<=0 or (p*x*y)%d: continue
            z=p*x*y//d
            cnt_pairs+=1
            if z<y: continue
            # critical overlap: from the pair (x,z) the completion of the tail must return y (and be unique)
            e=4*x-p; num=p*x*z; den=e*z-p*x
            if den<=0 or num%den: conflicts+=1; continue
            if num//den!=y: conflicts+=1
out['Z1119'] = f"completion pairs (x,y) at primes<=500: {cnt_pairs}; single-valuedness conflicts {conflicts}"
# Z1111: series/parallel 2-term splits 1/x = 1/(x+1)+1/(x(x+1)) applied to ES triples (p<=300): count 3-term outputs
splits_total=0; triples=0; merged_ok={}
for p in [p for p in range(3,301,2) if isp(p)]:
    for x in range(p//4+1,3*p//4+1):
        a=4*x-p
        if a<=0: continue
        for y in range(x,2*p*x//a+1):
            d=a*y-p*x
            if d<=0 or (p*x*y)%d: continue
            z=p*x*y//d
            if z<y: continue
            triples+=1
            for (i,j,k) in [(0,1,2),(0,2,1),(1,2,0)]:
                T=[x,y,z]; s_=T[i]+T[j]
                splits_total+=1
                if (T[i]*T[j])%s_==0:   # parallel merge 1/T_i+1/T_j = 1/c with c = T_i T_j/(T_i+T_j) integer
                    merged_ok[p%4]=merged_ok.get(p%4,0)+1
out['Z1111'] = f"ES triples p<=300: {triples}; pair-merges tested: {splits_total}; integral merges (1/x+1/y=1/c, c in Z) by p mod 4: {merged_ok}"
two={1:0,3:0}
for p in [p for p in range(3,301,2) if isp(p)]:
    for c in range(p//4+1, 3*p+1):
        a=4*c-p
        if a>0 and (p*c)%a==0: two[p%4]+=1
out['Z1111_two_term'] = f"2-term reps 4/p=1/c+1/z (c<=3p) by p mod 4: {two}"
for k,v in out.items(): print(k,':',v)
