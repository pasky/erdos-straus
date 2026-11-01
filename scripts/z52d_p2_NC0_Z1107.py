# z52d Pass 2 NC0 — Z1107 toric ideals of monomial substitutions.
# Cleared ES equation 4xyz = p(xy+yz+zx) has monomials m1=xyz, m2=xy, m3=yz, m4=zx. (i) toric kernel of the exponent map
# (x,y,z)->(m1..m4); (ii) same after gcd substitution x=g a, y=g b, z=g c (monomials in g,a,b,c); (iii) check the
# ES relation is NOT binomial (it is linear in the monomials), and the toric relation holds identically.
import sympy as sp
def kernel(A):
    M=sp.Matrix(A)           # rows = monomials, cols = variables
    return M.T.nullspace()   # integer relation vectors c with sum c_i * row_i = 0
A=[[1,1,1],[1,1,0],[0,1,1],[1,0,1]]
Ker=kernel(A); print('(i) kernel of exponent map (x,y,z):', [list(v) for v in Ker])
B=[[3,1,1,1],[2,1,1,0],[2,0,1,1],[2,1,0,1]]   # exponents in (g,a,b,c)
KerB=kernel(B); print('(ii) kernel after gcd substitution:', [list(v) for v in KerB], 'rank', sp.Matrix(B).rank())
# (iii) toric relation m2*m3*m4 - m1^2 vanishes identically; ES relation 4 m1 - p(m2+m3+m4) is linear
x,y,z,p=sp.symbols('x y z p')
m1,m2,m3,m4=x*y*z,x*y,y*z,z*x
print('(iii) m2*m3*m4 - m1^2 =', sp.expand(m2*m3*m4-m1**2))
print('      ES relation 4*m1 - p*(m2+m3+m4) =', sp.expand(4*m1-p*(m2+m3+m4)), '(not a binomial; in the toric ideal iff it vanishes identically -> no)')
