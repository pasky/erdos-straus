# Z2746 check: for every word (t,u,v) of primes p = 1 (8), p <= P: (A*/p) == (A/p) with A = tu-1, A* = tv-1, and AA* = tp+1.
import sys
sys.path.insert(0, 'scripts')
import z52d_p2_NC3_lib as L
P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
n = bad = inv = 0
for p in L.primes_upto(P):
    if p < 17 or p % 8 != 1: continue
    for (t, u, v) in L.words(p):
        A, As = t*u-1, t*v-1
        n += 1
        bad += (L.legendre(As, p) != L.legendre(A, p))
        inv += (A*As == t*p+1)
print("words", n, "sign(A*) != sign(A):", bad, "  AA* = tp+1 holds:", inv)
