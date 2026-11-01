# Z2880: is the ES sign (some cluster var ≡ 0 mod 4) a function of gamma_w mod 4 / mod 8, or of its conjugacy class?
import itertools
def mul(A,B,q): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%q for j in range(2)) for i in range(2))
def M(a,q): return ((a%q,(-1)%q),(1,0))
NMAX=20000
for q in (4,8,16):
    tab={}; conflicts=0; n=0
    for c in range(2,200):
        for m in range(2,200):
            for s in range(2,200):
                N=m*c*s-c-s
                if N>NMAX: break
                if N%4!=1: continue
                h=c*m-1; hp=m*s-1
                sign=any(x%4==0 for x in (c,m,s,h,hp))
                g=mul(mul(M(c,q),M(m,q),q),M(s,q),q)
                n+=1
                tab.setdefault(g,set()).add(sign)
    amb=sum(1 for v in tab.values() if len(v)>1)
    print(f"q={q}: words={n}, distinct gamma mod q={len(tab)}, ambiguous classes={amb}")
# conjugacy class test mod 8 and 16
for q in (8,16):
    G=[((a,b),(c,d)) for a in range(q) for b in range(q) for c in range(q) for d in range(q) if (a*d-b*c)%q==1]
    def inv(A): (a,b),(c,d)=A; return ((d,(-b)%q),((-c)%q,a))
    rep={}
    for g in G:
        if g in rep: continue
        for x in G:
            rep.setdefault(mul(mul(x,g,q),inv(x),q),g)
    tab={}
    for c in range(2,200):
        for m in range(2,200):
            for s in range(2,200):
                N=m*c*s-c-s
                if N>NMAX: break
                if N%4!=1: continue
                h=c*m-1; hp=m*s-1
                sign=any(x%4==0 for x in (c,m,s,h,hp))
                g=mul(mul(M(c,q),M(m,q),q),M(s,q),q)
                tab.setdefault(rep[g],set()).add(sign)
    print(f"q={q}: conj classes hit={len(tab)}, ambiguous={sum(1 for v in tab.values() if len(v)>1)}")
