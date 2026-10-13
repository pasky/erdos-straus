"""R180: check the stated 'iff' congruences of Thm 9.1 table and multiplicative orders."""
from sympy import n_order
claims = [(9,5,6,5),(9,2,6,1),(13,8,12,3),(27,17,18,15),(109,101,36,21),(37,31,36,9)]
for d,res,L,r in claims:
    S={m%n_order(2,d) for m in range(1,200) if pow(2,m,d)==res}
    print(d,"ord",n_order(2,d),"2^m=%d iff m mod ord in"%res,S,"claimed",r%L,"mod",L)
# residue conditions from n=2^m-2: n+c ≡0 mod d  <=> 2^m ≡ 2-c
for d,c in [(9,6),(9,18),(13,7),(27,12),(109,10),(37,82)]:
    print(d,c,"2^m ≡",(2-c)%d)
