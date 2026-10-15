"""z1 (O224): (A) is S_8 / S_4 membership a function of the isometry class of L_w?
(B) norm-one split classes <1> + M in G^-_p: are they path classes?"""
import sys
from sympy import primerange
from cf_lib import words, jacobi
from ce_classes import canon, classes, gram_of, aniso_at

def penta(w):
    t, u, v = w
    return (t, u, v, t*u-1, t*v-1)

def inS(w, m):
    return any(x % m == 0 for x in penta(w))

P0, P1 = int(sys.argv[1]), int(sys.argv[2])
mixed8 = 0; mixed4 = 0; tot = 0
for p in primerange(P0, P1):
    cls = {}
    for w in words(p):
        t, u, v = w
        k = canon([[v, -1, 0], [-1, t, -1], [0, -1, u]])
        cls.setdefault(k, []).append(w)
    for k, ws in cls.items():
        tot += 1
        s8 = {inS(w, 8) for w in ws}; s4 = {inS(w, 4) for w in ws}
        if len(s8) > 1:
            mixed8 += 1
            if mixed8 <= 5: print('mixed S8 class p=%d' % p, k, ws)
        if len(s4) > 1:
            mixed4 += 1
print('path classes', tot, 'S8-mixed', mixed8, 'S4-mixed', mixed4)
