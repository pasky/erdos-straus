# z59 MSPF: numerical checks of Lemmas 1.3, 1.6 and the §3 families/classes.  uv run --with sympy python scripts/z59_mspf_lemmacheck.py
import sympy
def hit(n,d):
    k=(-n)%d
    return d%4==3 and k>0 and ((d+1)//4)%k==0
bad=tot=0
for d in range(3,4000,4):
    for k in range(1,(d+1)//4+1):
        if ((d+1)//4)%k==0:
            tot+=1
            if sympy.jacobi_symbol(-k,d)!=-1: bad+=1
print("Lemma 1.3 pairs:",tot,"bad:",bad)
bad=tot=0
for n in sympy.primerange(5,3000):
    if n%4!=1: continue
    for k in range(1,n):
        for B in range(1,n//(2*k)+2):
            if (n+k+B)%(4*k*B)==0:
                tot+=1
                if sympy.jacobi_symbol(B,n)!=-sympy.jacobi_symbol(k,n): bad+=1
print("Lemma 1.6 pairs:",tot,"bad:",bad)
bad=0
for a in range(3,400,4):
    for k in range(1,(a+1)//4+1):
        if ((a+1)//4)%k==0 and not hit(a*(a+1)-k,a): bad+=1
print("family n=a(a+1)-k bad:",bad)
bad=0
for s in range(1,40):
    for t in range(1,40):
        d=4*s*t-1; n=d*d-s
        if n<=0 or not hit(n,d) or (-n)%d!=s: bad+=1
print("family n=(4st-1)^2-s bad:",bad)
print("d=11 classes:",sorted({(-k)%11 for k in [1,3]})," d=55 classes:",sorted({(-k)%55 for k in [1,2,7,14]}))
