from mordell_lib import cls_modulus_residues, solve
from fractions import Fraction as Fr
from sympy import isprime
for fam,P in [('I2',(125,88,11999)),('II3',(8,33,11999))]:
    M,res=cls_modulus_residues(fam,P)
    MT=1859; Mp=M//MT
    assert M%MT==0 and Mp%11 and Mp%13
    for r in res:
        if r%Mp==1 and r%MT==2:
            print(fam,P,'M=',M,'residue',r)
            # x* neighbourhood: n = r mod M; also n=2 mod 11^8 13^8 not needed (class only sees M)
            n=r
            while not isprime(n): n+=M
            x,y,z=solve(fam,P,n)
            assert all(int(v)==v and v>0 for v in (x,y,z))
            assert Fr(4,n)==Fr(1,x)+Fr(1,y)+Fr(1,z)
            print(' prime',n,'mod 11:',n%11,'mod 13:',n%13,'mod 840:',n%840,'sol',x,y,z)
