"""R121B from-scratch checks of EXCEPTIONAL_TYPEI_LOGLOG3 §1 (Lemmas 1.1, 1.3) and §2 constants."""
import math, numpy as np
from fractions import Fraction
import sympy as sp

# Lemma 1.3(a): h(x)=exp(-1/x); h^(p)(x)=e^{-u}Q_p(u), u=1/x, Q_{p+1}=u^2(Q_p-Q_p')
u=sp.symbols('u',positive=True)
Q=sp.Integer(1); worst=0
for p in range(0,25):
    if p>0:
        Q=sp.expand(u**2*(Q-sp.diff(Q,u)))
    f=sp.lambdify(u,Q,'mpmath')
    import mpmath as mp
    mp.mp.dps=40
    us=[mp.mpf(10)**(k/50) for k in range(-200,400)]
    m=max(abs(f(x))*mp.e**(-x) for x in us)
    bound=mp.mpf(9)**p*mp.factorial(p)**2
    worst=max(worst,float(m/bound))
print("Lemma1.3(a) max ratio |h^(p)|/(9^p p!^2), p<=24:",worst)

# Lemma 1.3 full eta: numeric derivatives on grid using exact polynomial structure would be heavy;
# check rho's I lower bound
import scipy.integrate as si
h=lambda x: math.exp(-1/x) if x>0 else 0.0
I=si.quad(lambda x:h(0.25+x)*h(0.25-x),-0.25,0.25,limit=200)[0]
print("I=",I," (1/4)e^-16=",0.25*math.exp(-16), I>=0.25*math.exp(-16))

# Lemma 1.1: f=tau^B; check f(n)/n^delta <= (2B/delta)^(B 2^(B/delta)) by computing exact sup over prime-power products
def sup_ratio(B,delta):
    # sup_n f(n)/n^delta = prod_p max_a ((a+1)^B p^{-a delta})
    tot=0.0
    p=2
    import sympy
    for p in sympy.primerange(2,10**6):
        best=max(B*math.log(a+1)-a*delta*math.log(p) for a in range(0,400))
        if best<=0: break
        tot+=best
    return tot
for B,d in [(1,0.5),(1,0.25),(2,0.5),(3,1.0),(1,0.1)]:
    lhs=sup_ratio(B,d); rhs=B*2**(B/d)*math.log(2*B/d)
    print(f"Lemma1.1 B={B} d={d}: log sup={lhs:.3f} <= log bound={rhs:.3f}", lhs<=rhs)

# §2 Prop 2.1 case (C) constant: 2*sqrt2*pi*pi^(1+4d) < 45 for d<=1/10
print("2√2π·π^1.4 =",2*math.sqrt(2)*math.pi*math.pi**1.4)
print("∫(1+t^2)/(1+t^4) =",si.quad(lambda t:(1+t*t)/(1+t**4),-np.inf,np.inf)[0], math.sqrt(2)*math.pi)
# exponent identity
d=sp.symbols('d'); print("exp:",sp.expand(2*d*(1-d)+(1-2*d)*(1+4*d)))
