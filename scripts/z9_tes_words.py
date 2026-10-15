"""Order-3 analogue test (O233 goal 3).  TES-words of Type II shape at a prime pi of Z[w]:
(T, u, v) in O^3, T != 0, with  c_i pi + c_j v + c_k u = T u v  for an assignment (i, j, k) of c = (w, w^2, 2),
giving the point  T/pi = c_i/(uv) + c_j/(pi u) + c_k/(pi v).  chi3(w) := tame cubic symbol at pi of
alpha = (-U0/U2, -U1/U2), U_m = x_m / c_m (TWISTED_T1 Thm 3.2).  A word is a TES solution iff 9 | T and the
denominators s*x_m (s = T/9) are 2-primary.  Reports per prime: #words, chi3 histogram, chi3 of solutions,
#words with target chi3, and their v_lambda(T) distribution.
Usage: z9_tes_words.py a b [a b ...]   (pi = a + b w, 2-primary)."""
import sys
import math
from collections import Counter
from itertools import permutations
from tf_core import mul, add, norm, div, disk, factor, divisors, two_primary, W, W2, TWO
from tw_eis import tame_symbol

C = (W, W2, TWO)
LAM = (1, -1)


def vlam(x):
    k = 0
    while True:
        q = div(x, LAM)
        if q is None:
            return k
        x, k = q, k + 1


def words(pi):
    out = set()
    R = ((3 + math.sqrt(9 + 4 * math.sqrt(norm(pi)))) / 2) ** 2 + 1
    small = disk(R)
    for i, j, k in permutations(range(3)):
        ci, cj, ck = C[i], C[j], C[k]
        cp = mul(ci, pi)
        for s in small:
            # case u = s small: v | ci pi + ck u
            for (uu, role) in ((s, 'u'), (s, 'v')):
                base = add(cp, mul(ck, uu)) if role == 'u' else add(cp, mul(cj, uu))
                if base == (0, 0):
                    continue
                for d in divisors(factor(base)):
                    u, v = (uu, d) if role == 'u' else (d, uu)
                    num = add(add(cp, mul(cj, v)), mul(ck, u))
                    T = div(num, mul(u, v))
                    if T is None or T == (0, 0):
                        continue
                    out.add(((i, j, k), T, u, v))
    return out


def analyse(pi):
    ws = words(pi)
    hist, sol_chi, tgt = Counter(), Counter(), []
    for (ijk, T, u, v) in ws:
        i, j, k = ijk
        x = [None] * 3
        x[i], x[j], x[k] = mul(u, v), mul(pi, u), mul(pi, v)
        a = (mul(x[0], C[2]), mul(C[0], x[2]))   # U0/U2
        b = (mul(x[1], C[2]), mul(C[1], x[2]))   # U1/U2
        ch = tame_symbol(a, b, pi)
        hist[ch] += 1
        s = div(T, (9, 0))
        is_sol = s is not None and all(two_primary(mul(s, xm)) for xm in x)
        if is_sol:
            sol_chi[ch] += 1
        tgt.append((ch, vlam(T), is_sol))
    return len(ws), hist, sol_chi, tgt


if __name__ == "__main__":
    args = list(map(int, sys.argv[1:]))
    for a, b in zip(args[::2], args[1::2]):
        n, hist, sol, tgt = analyse((a, b))
        print((a, b), "N", norm((a, b)), "words", n, "chi3", dict(hist), "solutions chi3", dict(sol))
