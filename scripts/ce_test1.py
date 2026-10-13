import sys
from ce_lib import *
from cf_lib import words, jacobi
p = int(sys.argv[1])
for (t,u,v) in words(p):
    A = t*u-1
    chi = jacobi(-A % p, p)
    T = c0_table(path_gram(t,u,v)); al = Alg(T); B0 = ident_basis()
    d0 = discrd(al, B0)
    ov = maximal_overorders_2(al, B0)
    stats = {}
    for k,(B,d) in ov.items(): stats[d] = stats.get(d,0)+1
    print((t,u,v), 'chi',chi, 'discrd C0', d0, 'overorders by discrd', sorted(stats.items()))
