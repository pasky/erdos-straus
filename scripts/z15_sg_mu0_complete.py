# O240 Prop 4.3: COMPLETE decision of the Sophie-Germain window menu at mu = 0 of c*2^s + 1 (c + 1 = 4^i).
# Window m(t) = 4ct^4 - 1 (t odd), near mu = 0: X == 1/2, atoms q | c (exp <= 2 v_q(c)), f± = g±/2, g± = 2t^2 ± 2t + 1 (exp <= 2),
# K == 4^(i-1).  Fires iff m(t) | N(t) := prod q^a * g+^x g-^y + 4^(i-1) 2^(x+y)  (d == -K, cleared of the unit 2^(x+y)).
# Pseudo-division: (4c)^r N = Q m + R, deg R <= 3, gcd(m, 2c) = 1  =>  m | N iff m | R(t).  If R == 0 identically: a
# polynomial family of windows; else |R(t)| < m(t) beyond an explicit t0, and t < t0 are checked directly.
import sys, itertools, math
from sympy import symbols, Poly, prem, factorint, ZZ
c=int(sys.argv[1]); i=0
while 4**i<c+1: i+=1
assert 4**i==c+1
t=symbols('t'); m=Poly(4*c*t**4-1,t,domain=ZZ)
gp=Poly(2*t**2+2*t+1,t,domain=ZZ); gm=Poly(2*t**2-2*t+1,t,domain=ZZ)
CF=factorint(c); qs=list(CF.items())
identities=[]; sporadic=set()
for ea in itertools.product(*[range(2*v+1) for _,v in qs]):
    cq=math.prod(q**a for (q,_),a in zip(qs,ea))
    for x in range(3):
        for y in range(3):
            N=Poly(cq,t,domain=ZZ)*gp**x*gm**y+Poly(4**(i-1)*2**(x+y),t,domain=ZZ)
            R=Poly(prem(N.as_expr(),m.as_expr(),t),t,domain=ZZ) if N.degree()>=4 else N
            if R.is_zero: identities.append((ea,x,y)); continue
            # t0: for t >= t0, |R(t)| < m(t)
            B=sum(abs(int(co)) for co in R.all_coeffs())
            t0=1
            while 4*c*t0**4-1 <= B*t0**3: t0+=1
            for tt in range(1,t0+1,2):
                mv=4*c*tt**4-1
                if math.gcd(mv,2*c)==1 and int(N.eval(tt))%mv==0: sporadic.add((tt,ea,x,y))
print("c=%d: polynomial window identities (all t): %s"%(c,identities))
print("     sporadic (t, exps_c, x, y): %s"%sorted(sporadic)[:20])
