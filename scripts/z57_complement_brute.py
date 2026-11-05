# z57 COMPLEMENT: brute-force validation of z57_complement_words.c (all columns except bands) for small odd n ≡ 1 (4).
# Enumerates all (t,u,v) >= 1 with t*u*v - u - v = n directly, and the c-lines 4abcd - a - b = c n.
import sys, math
from fractions import Fraction as Fr
def words(n):
    out = []
    for u in range(1, n + 3):
        for v in range(1, n + 3):
            s = n + u + v
            if s % (u * v) == 0:
                t = s // (u * v)
                if t >= 1: out.append((t, u, v))
            if u * v > n + u + v: break
    return out
def row(n, C2=3):
    W = words(n); L2 = math.log(n) ** 2; hc = math.floor(L2)
    S = B = I = Q = BND = G = K = H3 = HC = 0
    for (t, u, v) in W:
        bnd = (t == 1 or u == 1 or v == 1)
        s = t % 4 == 0; b1 = u % 4 == 0 or v % 4 == 0; i1 = (t * u) % 4 == 1 or (t * v) % 4 == 1
        if bnd: BND += 1
        if s:
            S += 1; P, Qq, C = min(u, v), max(u, v), t // 4
            if Qq ** 4 > P * n: G += 1
            else: K += 1
            if 64 * C ** 3 <= n: H3 += 1
            if C <= hc: HC += 1
            # certificate check (u,B,C) -> 4/n = 1/(uBC)+1/(nBC)+1/(nuC)
            assert Fr(1, u * v * C) + Fr(1, n * v * C) + Fr(1, n * u * C) == Fr(4, n)
        if b1:
            B += 1
            # López b = 1 certificate (DEDEKIND_ES Thm 4.5): 4 | u = 4w, f = tv - 1: 4/n = 1/(wf) + 1/(tnw) + 1/(tnwf)
            for (uu, vv) in ((u, v), (v, u)):
                if uu % 4 == 0:
                    w = uu // 4; f = t * vv - 1
                    assert f > 0 and Fr(1, w * f) + Fr(1, t * n * w) + Fr(1, t * n * w * f) == Fr(4, n)
        if i1:
            I += 1
            # Type I a = 1 certificate (CONDITIONAL_ES Lemma 1.1): orientation with 4 | t*f - 1 (f = v), c = u
            for (c, f) in ((u, v), (v, u)):
                g = t
                if (f * g) % 4 == 1 and f * g > 1:
                    d = (f * g - 1) // 4; b = (n + c) // f
                    assert (n + c) % f == 0
                    assert Fr(1, b * d * n) + Fr(1, c * d) + Fr(1, b * c * d) == Fr(4, n)
        if not bnd and not s and not b1 and not i1: Q += 1
    cl = []
    for c in range(2, C2 + 1):
        cnt = 0
        for (t, u, v) in words(c * n):
            if t % (4 * c) == 0:
                cnt += 1
                d = t // (4 * c); a, b = u, v
                x, y, z = a * b * d, a * c * d * n, b * c * d * n
                assert Fr(1, x) + Fr(1, y) + Fr(1, z) == Fr(4, n)
        cl.append(cnt)
    return [n, len(W), S, B, I, Q, BND, G, K, H3, HC] + cl
if __name__ == '__main__':
    for line in sys.stdin:
        n = int(line)
        print(' '.join(map(str, row(n))))
