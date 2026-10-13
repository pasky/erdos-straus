# check: C0(L) = Z + 2-radical of E(L): i.e. 2E ⊂ C0 and C0/2E has F2-dim 3 with (C0/2E) = F2 + J(E/2E)
import sys
from ce_lib import *
from ce_lib import _solve
from cf_lib import words, jacobi
from fractions import Fraction as Fr
def contains(alg,Bbig,x):
    c=_solve(Bbig,x); return all(ci.denominator==1 for ci in c)
for p in [41,73,89,97,113]:
  for (t,u,v) in words(p):
    chi=jacobi(-(t*u-1)%p,p)
    al=Alg(c0_table(path_gram(t,u,v))); B0=ident_basis()
    ov=maximal_overorders_2(al,B0)
    E=[B for k,(B,d) in ov.items() if d==2*p]; assert len(E)==1; E=E[0]
    # 2E subset C0 ?
    ok=all(contains(al,B0,[2*c for c in e]) for e in E)
    # Jacobson radical test: elements x of E with x in C0... check C0 = Z + {x in E: x^2 in 2E ... } skip; check index
    nmax=sum(1 for k,(B,d) in ov.items() if d==p)
    print(p,(t,u,v),chi,'2E<C0',ok,'#max',nmax)
