"""y2_even_edge: the even-edge theorem for pentagon friezes with frozen (1,1,1,1,N), N odd.

Claims checked on ALL positive (formal) words (c,m,s), letters >= 1, with N = mcs - c - s, 0 < N <= X, N odd:
 (E1) mod 2 the quiddity cycle (q1..q5) = (h', c, m, s, h) is a rotation of (1,0,0,1,1): exactly two even
      quiddities, and they are cyclically adjacent (the "even edge").
 (E2) for N = 1 (mod 4): Jacobi (h'/N) = -1  <=>  8 | e*e'  (e, e' the two even quiddities)
      <=> some quiddity = 0 (mod 4)   [DK Thm 4.5 / LENGTH_THREE Cor 1.2, extended to formal words]
 (E3) for N = 3 (mod 4): record the law empirically (no claim).
 Control: at odd squares N (all words), e*e' = 4 (mod 8) always.
usage: y2_even_edge.py X ; exits nonzero on any failure.
"""
import sys
from collections import Counter


def jacobi(a, n):
    a %= n
    res = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def main(X):
    fails = 0
    nwords = 0
    law3 = Counter()
    sq = {k * k for k in range(3, int(X ** 0.5) + 2, 2)}
    sq_words = 0
    pos = Counter()
    m = 1
    while True:
        # minimal N for this m with c=s=1: m-2 ; need >0 eventually
        if m * 1 * 1 - 2 > X:
            break
        c = 1
        while True:
            if m * c - c - 1 > X and m >= 2:
                break
            if m == 1 and c > X + 3:
                break
            s = 1
            while True:
                N = m * c * s - c - s
                if N > X:
                    break
                if N > 0 and N % 2 == 1:
                    h, hp = c * m - 1, m * s - 1
                    q = (hp, c, m, s, h)
                    ev = [i for i in range(5) if q[i] % 2 == 0]
                    nwords += 1
                    if len(ev) != 2 or (ev[1] - ev[0]) % 5 not in (1, 4):
                        fails += 1
                        print("E1 FAIL", c, m, s, N, q)
                        continue
                    pos[tuple(ev)] += 1
                    ee = q[ev[0]] * q[ev[1]]
                    J = jacobi(hp, N)
                    z = any(x % 4 == 0 for x in q)
                    if N % 4 == 1:
                        if (J == -1) != (ee % 8 == 0) or (J == -1) != z:
                            fails += 1
                            print("E2 FAIL", c, m, s, N, q, J)
                    else:
                        law3[(tuple(ev), ee % 8 == 0, J)] += 1
                    if N in sq:
                        sq_words += 1
                        if ee % 8 != 4:
                            fails += 1
                            print("SQ FAIL", c, m, s, N)
                if m == 1 and s > X + 3:
                    break
                s += 1
            c += 1
        m += 1
    print("odd-N words checked:", nwords, " even-edge positions:", dict(pos))
    print("odd-square words (control):", sq_words)
    print("N=3 mod 4 law (edge, 8|ee', J):", dict(law3))
    print("FAILURES:", fails)
    return fails


if __name__ == "__main__":
    sys.exit(1 if main(int(sys.argv[1])) else 0)
