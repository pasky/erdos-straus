"""EXCEPTIONAL_TYPEI_LOGLOG Lemma 2.2 (separation of level-d Heegner points), numerical check.
For fixed d, enumerate (a,e,f) with e*f = 4a^2 d + 1, form Q = [f, 4ad, de] (disc -4d),
root z_Q = (-2ad + i sqrt(d))/f.  Check: cosh dist(z_Q, z_Q') = 1 + disc(Q-Q')/(8d),
disc(Q - Q') == 0 (mod 4d), hence cosh dist in 1 + Z/2, >= 3/2 for Q != Q'.
Exact integer check of the identity, float check of the distance formula."""
import math, itertools, sys

def forms(d, amax):
    out = []
    for a in range(0, amax + 1):
        m = 4 * a * a * d + 1
        for f in range(1, int(math.isqrt(m)) + 1):
            if m % f == 0:
                for ff in {f, m // f}:
                    out.append((ff, 4 * a * d, d * (m // ff)))
    return out

def disc(Q):
    A, B, C = Q
    return B * B - 4 * A * C

worst = {}
for d in [1, 2, 3, 5, 6, 12, 30, 97, 210]:
    F = forms(d, 60 if d < 50 else 25)
    mn = None
    for Q, R in itertools.combinations(F, 2):
        D = tuple(x - y for x, y in zip(Q, R))
        dd = disc(D)
        assert dd % (4 * d) == 0 and dd >= 0, (d, Q, R, dd)
        # float distance check
        z1 = complex(-Q[1] / (2 * Q[0]), math.sqrt(4 * d) / (2 * Q[0]))
        z2 = complex(-R[1] / (2 * R[0]), math.sqrt(4 * d) / (2 * R[0]))
        ch = 1 + abs(z1 - z2) ** 2 / (2 * z1.imag * z2.imag)
        assert abs(ch - (1 + dd / (8 * d))) < 1e-6 * ch, (Q, R, ch, dd)
        assert dd > 0
        mn = ch if mn is None else min(mn, ch)
    worst[d] = (len(F), mn)
for d, (n, mn) in worst.items():
    print(f"d={d:4d}  #forms={n:5d}  min cosh dist over distinct pairs = {mn:.6f}")
print("identity cosh = 1 + disc(Q-Q')/(8d), 4d | disc(Q-Q') > 0: all pairs OK")
