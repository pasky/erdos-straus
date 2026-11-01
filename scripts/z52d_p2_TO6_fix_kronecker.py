"""z52d pass2 TO6 fix (Z2346): numerical check of Kronecker's double-series identity, the building block of the
theta-quotient / Appell-Lerch form used in METAPLECTIC_ES.md (K1'):
  sum_{n in Z} x^n/(1 - y q^n) = (q;q)^2 (xy;q)(q/(xy);q) / [ (x;q)(q/x;q)(y;q)(q/y;q) ],  |q| < |x| < 1, y not in q^Z.
Also checks the coefficient claim in (K1') at the level of the boundary series's first terms is NOT attempted (see not_done)."""
import mpmath as mp
mp.mp.dps=30
def poch(a,q,N=400):
    r=mp.mpf(1)
    for k in range(N): r*= (1-a*q**k)
    return r
def lhs(x,y,q,N=200):
    s=mp.mpf(0)
    for n in range(-N,N+1):
        s+= x**n/(1-y*q**n)
    return s
def rhs(x,y,q):
    return poch(q,q)**2*poch(x*y,q)*poch(q/(x*y),q)/(poch(x,q)*poch(q/x,q)*poch(y,q)*poch(q/y,q))
for (q,x,y) in [(mp.mpf('0.3'),mp.mpf('0.5'),mp.mpf('0.7')),(mp.mpf('0.2'),mp.mpf('0.45'),mp.mpf('0.31')),(mp.mpf('0.1'),mp.mpf('-0.4'),mp.mpf('0.6'))]:
    L=lhs(x,y,q); R=rhs(x,y,q)
    print('q=%s x=%s y=%s  LHS=%s RHS=%s  |diff|=%s' % (q,x,y,mp.nstr(L,12),mp.nstr(R,12),mp.nstr(abs(L-R),3)))
