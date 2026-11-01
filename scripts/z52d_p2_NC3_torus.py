# Z2812 premise check: monodromy gamma_w = [[p,-A*],[A,-t]] (word matrix); H1(T_gamma) torsion = coker(gamma - I), order |tr-2|.
# Item claims |tr gamma_w - 2| = tu + tv - 4. Check directly on words, and also the other common convention.
import sys
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
from sympy import Matrix, eye
bad = 0; n = 0; ex = []
for p in L.primes_upto(200):
    if p < 5: continue
    for (t, u, v) in L.words(p):
        A, As = t*u-1, t*v-1
        g = Matrix([[p, -As], [A, -t]])
        assert g.det() == 1
        tr = g.trace()
        n += 1
        if abs(tr-2) != t*u + t*v - 4: bad += 1; ex.append((p,(t,u,v),int(tr)))
        # alternative: the item's claimed order
        
print("words checked:", n, " words where |tr-2| != tu+tv-4:", bad, " examples:", ex[:4])
print("|det(g-I)| = |2-tr| equals |p-t-2| identically:", all(abs((Matrix([[p,-(t*v-1)],[t*u-1,-t]])-eye(2)).det()) == abs(p-t-2) for p in [13,17,29] for (t,u,v) in L.words(p)))
