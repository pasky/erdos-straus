"""Independent finite good-reduction checks of all claimed J slopes u=1/ell.
Use the plane group law itself (origin signed seed); bad reductions are skipped.
Only numeric literals and Fraction(.,.) from the replay are parsed.
"""
import ast
from fractions import Fraction as F
from pathlib import Path
from sympy import primerange

def literal(z):
    if isinstance(z,ast.Constant) and isinstance(z.value,(str,int)):return z.value
    if isinstance(z,ast.UnaryOp) and isinstance(z.op,ast.USub):return -literal(z.operand)
    if isinstance(z,ast.Tuple):return tuple(map(literal,z.elts))
    if isinstance(z,ast.Dict):return {literal(a):literal(b) for a,b in zip(z.keys,z.values)}
    if isinstance(z,ast.Call) and isinstance(z.func,ast.Name) and z.func.id=='Fraction':return F(*map(literal,z.args))
    raise ValueError('unexpected node')

def run(M,n,c,ell,k,P,W,q):
    u=F(1,ell);K=u*P[0]+P[1]-k*P[2];NN=F(M,n)*K
    def red(x):return F(x).numerator*pow(F(x).denominator,-1,q)%q
    if any(F(x).denominator%q==0 for x in (u,k,NN,*P,*W)):return None
    a,b,d=red(u),1,red(-k);N=red(NN)
    if not(a*d*N%q):return None
    # Eliminating square roots from N=(+-sqrt(a)+-sqrt(b)+-sqrt(d))^2
    # gives ( (N-a-b-d)^2-4(ab+ad+bd) )^2-64abdN.
    if (((N-a-b-d)**2-4*(a*b+a*d+b*d))**2-64*a*b*d*N)%q==0:return None
    def norm(T):
        T=tuple(v%q for v in T);m=next((i for i in T if i),0);assert m
        return tuple(x*pow(m,-1,q)%q for x in T)
    def calc(T):
        x,y,z=T; L=a*x+b*y+d*z; H=x*y+y*z+z*x
        return (L*H-N*x*y*z)%q, ((a*H+L*(y+z)-N*y*z)%q,(b*H+L*(x+z)-N*x*z)%q,(d*H+L*(x+y)-N*x*y)%q)
    def dot(L,R):return sum(x*y for x,y in zip(L,R))%q
    def chord(R,S):
        if R==S:
            G=calc(R)[1]
            for i,j in ((0,1),(0,2),(1,2)):
                V=[0]*3;V[i]=G[j];V[j]=-G[i]
                if any(v%q for v in V) and norm(V)!=R:break
            else:raise AssertionError('bad tangent')
            f,grad=calc(V);B=dot(grad,R);C=norm(f*x-B*y for x,y in zip(R,V))
        else:
            A=dot(calc(R)[1],S);B=dot(calc(S)[1],R);C=norm(B*x-A*y for x,y in zip(R,S))
        assert calc(C)[0]==0;return C
    O,T=norm(map(red,P)),norm(map(red,W));R=O
    assert calc(O)[0]==calc(T)[0]==0
    for _ in range(12):
        R=chord(O,chord(R,T))
        if R==O:return False
    return True

if __name__=='__main__':
    for line in Path('data/z81/duality/secants.txt').read_text().splitlines():
        M,n,rows=line.split(' ',2); rows=literal(ast.parse(rows,mode='eval').body)
        print(M,n,{tag:next(int(q) for q in primerange(17,2000) if run(int(M),int(n),*row,int(q))) for tag,row in rows.items()},flush=True)
