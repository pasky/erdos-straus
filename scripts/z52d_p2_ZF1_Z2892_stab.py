"""Z2892: which pairs (g,h) in SL2(Z) (entries |.|<=R) map the length-3 word set
W3 = {γ_w = [[A, n],[t, A*]] : t,u,v>=2}  (QUESTION_R Prop 1.1) into itself by γ -> g γ h ?
A Zariski-dense (thin) group/semigroup acting on W3 would be needed for an Apollonian/RS-type orbit model.
Test set: all words with t,u,v <= K; (g,h) kept if g γ_w h ∈ W3 for every test word."""
import itertools, sys
R = int(sys.argv[1]) if len(sys.argv) > 1 else 3
K = int(sys.argv[2]) if len(sys.argv) > 2 else 9
def inW3(m):
    (a, b), (c, d) = m
    return c >= 2 and (a + 1) % c == 0 and (d + 1) % c == 0 and a >= 2 * c - 1 and d >= 2 * c - 1 and a * d - b * c == 1
def mul(x, y):
    return ((x[0][0]*y[0][0]+x[0][1]*y[1][0], x[0][0]*y[0][1]+x[0][1]*y[1][1]),
            (x[1][0]*y[0][0]+x[1][1]*y[1][0], x[1][0]*y[0][1]+x[1][1]*y[1][1]))
words = [((t*u-1, t*u*v-u-v), (t, t*v-1)) for t in range(2, K+1) for u in range(2, K+1) for v in range(2, K+1)]
assert all(inW3(w) for w in words)
G = [((a, b), (c, d)) for a, b, c, d in itertools.product(range(-R, R+1), repeat=4) if a*d - b*c == 1]
print("SL2 elements with entries <=", R, ":", len(G), "; test words:", len(words))
good = []
for g in G:
    gw = [mul(g, w) for w in words]
    for h in G:
        if all(inW3(mul(x, h)) for x in gw):
            good.append((g, h))
print("pairs (g,h) preserving W3:", len(good))
for g, h in good:
    print("  g =", g, " h =", h)
