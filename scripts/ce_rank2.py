import sys
from ce_classes import classes, aniso_at, gram_of, canon
from ce_rank import adj, minvec
from cf_lib import words, jacobi
for p in map(int, sys.argv[1:]):
    cl = classes(p)
    minus = [k for k in cl if aniso_at(gram_of(k), p)]
    allm = sorted((minvec(adj(gram_of(k))), k[0]) for k in minus)
    print(p, 'smallest (min E0, min L) over G-:', allm[:14])
    for (t, u, v) in words(p):
        if jacobi((-(t * u - 1)) % p, p) == -1:
            G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
            print('   cert', (t, u, v), 'A,A*,uv =', t*u-1, t*v-1, u*v, 'min E0', minvec(adj(G)), 'min L', canon(G)[0])
