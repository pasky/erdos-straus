# Run: uv run --no-project --with sympy python scripts/literature_bl_character_check.py
# Check: for every signed solution of 4/p = 1/x+1/y+1/z (nonzero integers),
# positive  <=>  Legendre(-A*B, p) == -1, A,B = same-valuation pair with p removed
# (Bright-Loughran Thm 1.2 + Thm 1.5 + Lemma 3.4; = campaign (2a) when p = 1 mod 4).
from fractions import Fraction
from sympy import primerange, divisors
def leg(a,p):
    a%=p; r=pow(a,(p-1)//2,p); return -1 if r==p-1 else r
def vp(n,p):
    k=0
    while n%p==0: n//=p; k+=1
    return k
tot=0; bad=0
for p in primerange(3,400):
    sols=set()
    for x in range(1, 3*p//4+1):
        R=Fraction(4,p)-Fraction(1,x)
        if R==0: continue
        r,s=R.numerator,R.denominator  # r may be negative, s>0
        for d in divisors(s*s):
            for D in (d,-d):
                y,ry=divmod(D+s,r)
                if ry: continue
                z,rz=divmod(s*s//D+s,r)
                if rz or y==0 or z==0: continue
                t=tuple(sorted((x,y,z)))
                sols.add(t)
    for t in sols:
        assert Fraction(1,t[0])+Fraction(1,t[1])+Fraction(1,t[2])==Fraction(4,p)
        v=[vp(abs(u),p) for u in t]
        pair=[i for i in range(3) if v.count(v[i])==2]
        assert len(pair)==2, (p,t)
        A=t[pair[0]]//p**v[pair[0]]; B=t[pair[1]]//p**v[pair[1]]
        pos=all(u>0 for u in t)
        ok = (leg(-A*B,p)==-1)==pos
        tot+=1; bad+= (not ok)
        if not ok: print("VIOLATION", p, t)
print("signed solutions checked:",tot,"violations:",bad)
raise SystemExit(1 if bad else 0)
