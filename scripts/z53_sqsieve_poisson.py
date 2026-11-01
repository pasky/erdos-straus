"""Numerical check of the Poisson-dual identity (Lemma P) for the smoothed strip sum
  S^Phi_Q = sum_{C in [C1,C2]} sum_k Phi((4Ck-n)/S) chi_Q(f(C,k)),  f=(4Ck-n)^2-4k, chi_Q Jacobi symbol mod Q=q q'
  = sum_C sum_l (S/(4CQ)) Phihat(l S/(4CQ)) e(-l n/(4CQ)) G_C(l),  G_C(l)=sum_{k0 mod Q} chi_Q(f(C,k0)) e(l k0/Q)
with Phi(t)=exp(-t^2), Phihat(xi)=sqrt(pi) exp(-pi^2 xi^2).
Usage: python z53_sqsieve_poisson.py n q q' C1 C2 S
"""
import sys, math, cmath
from sympy import jacobi_symbol
n,q,qq,C1,C2,S = map(int, sys.argv[1:7]); Q=q*qq
def chi(a): return int(jacobi_symbol(a % Q, Q))
lhs=0.0
for C in range(C1,C2+1):
    k0=(n)/(4*C); w=10*S/(4*C)
    for k in range(max(1,int(k0-w)-1), int(k0+w)+2):
        t=(4*C*k-n)/S
        lhs+=math.exp(-t*t)*chi((4*C*k-n)**2-4*k)
rhs=0.0; main=0.0
for C in range(C1,C2+1):
    vals=[chi((4*C*k-n)**2-4*k) for k in range(Q)]
    a=S/(4*C*Q); L=int(8/(math.pi*a))+1
    for l in range(-L,L+1):
        G=sum(vals[k]*cmath.exp(2j*math.pi*l*k/Q) for k in range(Q))
        term=a*math.sqrt(math.pi)*math.exp(-(math.pi*l*a)**2)*cmath.exp(-2j*math.pi*l*n/(4*C*Q))*G
        rhs+=term.real
        if l==0: main+=term.real
print(f"n={n} Q={q}*{qq} C in [{C1},{C2}] S={S}: direct={lhs:.8f} dual={rhs:.8f} diff={lhs-rhs:.2e} (l=0 main term {main:.4f})")
