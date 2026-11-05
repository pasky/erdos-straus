# z58 TRYF2: verify (i) for n = 1 (4), C>=1, d | 4nC+1, gcd(d,n)=1: jacobi(d,n) == jacobi(-C,d);
# (ii) h_C <= m_C, with h_C = #{d|4nC+1: d = -1 mod 4C}, m_C = #{d | 4nC+1 : jacobi(d,n) = -1};
# (iii) the identity phi(4C) h_C = 2 m_C + E_C, E_C := sum_{psi mod 4C, psi not in {1, chi_{-C}}} psi(-1) S_psi, i.e.
#       equivalently E_C := phi(4C) h_C - tau(N) + r_chi(N), r_chi(N) = sum_{d|N} jacobi(d,n). We check tau - r_chi = 2 m_C.
from sympy import divisors, jacobi_symbol, totient, isprime, gcd
import sys
def check(n, Cmax):
    bad=0; tot=0; hits=0
    for C in range(1,Cmax+1):
        N=4*n*C+1; D=divisors(N); h=0; m=0
        for d in D:
            if gcd(d,n)!=1: continue
            tot+=1
            if jacobi_symbol(d,n)!=jacobi_symbol(-C,d): bad+=1
            if d%(4*C)==4*C-1: h+=1
            if jacobi_symbol(d,n)==-1: m+=1
        rchi=sum(jacobi_symbol(d,n) for d in D)
        assert len(D)-rchi==2*m, (n,C)
        assert h<=m, (n,C)
        hits+=h
    return bad,tot,hits
for n in [5,13,409,577,841,1225,25*49,57,105,2305,10009,9601,12841]:
    bad,tot,hits=check(n,400)
    print(n, "prime" if isprime(n) else ("square" if int(n**0.5)**2==n else "comp"), "pairs",tot,"identity failures",bad,"hits C<=400:",hits)
