# Level-t words via divisors (exact identity): for t>=2, word (t,u,v) with tuv-u-v=p  <=>  A=tu-1 divides N=tp+1 with
# A ≡ -1 (mod t), A* = N/A ≡ -1 (mod t), A >= 2t-1, A* >= 2t-1; then u=(A+1)/t, v=(A*+1)/t  (since AA* = tp+1 and
# tuv-u-v = (AA*-1)/t = p).  Used for Z3147 (reachability with 4|t), Z3090/Z3121/Z3005 (least level).
import sys
from sympy import factorint, divisors
def level_words(p, t):
    N = t*p + 1
    out = []
    for A in divisors(N):
        if A % t != t - 1 or A < 2*t - 1: continue
        B = N // A
        if B % t != t - 1 or B < 2*t - 1: continue
        out.append(((A+1)//t, (B+1)//t))   # (u, v)
    return out
if __name__ == "__main__":
    import z52d_p2_NC3_lib as L
    # check the identity against the brute-force word list for small p, all t
    bad = 0; n = 0
    for p in L.primes_upto(400):
        if p < 5: continue
        W = set(L.words(p))
        for t in range(2, 13):
            S1 = {(t, u, v) for (u, v) in level_words(p, t)}
            S2 = {w for w in W if w[0] == t}
            n += 1
            if S1 != S2: bad += 1
    print("identity check (p<400, t<=12):", n, "cases, mismatches:", bad)
