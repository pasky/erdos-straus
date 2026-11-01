# z52d Pass 2 NC0, item Z1088 — enumerate short SL2(Z) words over {L, R, L^-1, R^-1} plus ONE wildcard W = L^t (symbolic t),
# with the wildcard repeated exactly twice (same t); symbolic 2x2 matrix entries (sympy polynomials in t); count distinct entry polynomials
# and the words whose (1,2) entry is linear in t (the 'one repeated wildcard' form). Words of length <= LMAX.
import itertools, sympy as sp
t=sp.symbols('t')
L=sp.Matrix([[1,0],[1,1]]); R=sp.Matrix([[1,1],[0,1]]); W=sp.Matrix([[1,0],[t,1]])
letters={'L':L,'R':R,'l':L.inv(),'r':R.inv(),'W':W}
LMAX=int(__import__('sys').argv[1]) if len(__import__('sys').argv)>1 else 5
words=0; polys=set(); lin=set(); examples=[]
for k in range(2,LMAX+1):
    for w in itertools.product(list(letters),repeat=k):
        if w.count('W')!=2: continue
        M=sp.eye(2)
        for c in w: M=M*letters[c]
        M=M.applyfunc(sp.expand)
        words+=1
        key=tuple(M)
        polys.add(key)
        e12=M[0,1]
        if sp.degree(e12,t)==1 and sp.Poly(e12,t).LC()!=0: lin.add(sp.factor(e12))
        if len(examples)<4: examples.append((''.join(w),tuple(sp.factor(x) for x in M)))
print('LMAX',LMAX,'words with exactly two W:',words,' distinct matrices:',len(polys),' distinct linear (1,2)-entries:',len(lin))
print('linear (1,2) entries (first 12):',sorted(map(str,lin))[:12])
print('examples:',examples[:3])
