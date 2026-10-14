"""R205 from-scratch checks of LENGTH_THREE Prop 1.1, Cor 1.2, Thm 2.1, Thm 3.1 (generic words).

Usage: PYTHONPATH=scripts uv run python scripts/review_l3_words.py NMAX NSET
  NMAX: enumerate all words (c,m,s) >= 1 with 0 < N = mcs - c - s <= NMAX
  NSET: compare interior words with an independent HJ-expansion census of L3(N) for N <= NSET
Independent of scripts/l3_*.py.
"""
import sys
from fractions import Fraction as F
from math import gcd


def jacobi(a, n):
    assert n > 0 and n % 2 == 1
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def det(u, v):
    return u[0] * v[1] - u[1] * v[0]


def hj(N, A):
    """Hirzebruch-Jung expansion N/A = b1 - 1/(b2 - ...), all b >= 2 for 0 < A < N."""
    out = []
    while A:
        b = -(-N // A)
        out.append(b)
        N, A = A, b * A - N
    return out


def words(NMAX):
    # N = s*h - c is increasing in s (h >= 1); min over s>=1 of the positive values is >= max(h - c, 1)
    # and for fixed m it is increasing in c: N(s=2) = 2h - c = c(2m-1) - 2.
    for m in range(1, NMAX + 3):
        if m - 2 > NMAX:  # c = 1, s = 1 gives N = m - 2, the minimum over c, s
            break
        for c in range(1, 2 * NMAX + 5):
            h = c * m - 1
            if h <= 0:
                continue
            if c * (2 * m - 1) - 2 > NMAX and h - c > NMAX:
                break
            s = 1
            while True:
                N = s * h - c
                if N > NMAX:
                    break
                if N > 0:
                    yield c, m, s, N
                s += 1


def main():
    NMAX = int(sys.argv[1]); NSET = int(sys.argv[2])
    nw = ninterior = nslice = 0
    fails = []
    interior_by_N = {}
    has_word = set(); has_slice = set()
    for c, m, s, N in words(NMAX):
        nw += 1
        h, hp = c * m - 1, m * s - 1
        V = [(0, -1), (1, 0), (c, 1), (h, m), (N, hp)]
        lam = {(i, k): abs(det(V[i], V[k])) for i in range(5) for k in range(5)}
        L = lambda i, k: lam[(i - 1, k - 1)]
        exp = {(1, 2): 1, (2, 3): 1, (3, 4): 1, (4, 5): 1, (1, 5): N, (1, 3): c, (2, 4): m, (3, 5): s,
               (1, 4): h, (2, 5): hp}
        for (i, k), v in exp.items():
            if L(i, k) != v:
                fails.append(("lam", c, m, s, i, k))
        # cyclic order on the boundary: inf > c > h/m > N/h' > 0
        if not (F(c) > F(h, m) > F(N, hp) > 0):
            fails.append(("order", c, m, s))
        # all five Ptolemy relations from the generic formula on the 5 quadrilaterals
        for drop in range(1, 6):
            a, b, cc, d = [x for x in range(1, 6) if x != drop]
            if L(a, cc) * L(b, d) != L(a, b) * L(cc, d) + L(a, d) * L(b, cc):
                fails.append(("ptolemy", c, m, s, drop))
        # Penner fan identity at each vertex, generic: sum of triangle arcs = total arc
        for v in range(1, 6):
            others = [((v - 1 + t) % 5) + 1 for t in range(1, 5)]  # v+1, v+2, v+3, v+4
            arcs = [F(L(x, y), L(v, x) * L(v, y)) for x, y in zip(others, others[1:])]
            total = F(L(others[0], others[-1]), L(v, others[0]) * L(v, others[-1]))
            if sum(arcs) != total:
                fails.append(("fan", c, m, s, v))
        # table of Thm 2.1, literally as printed
        tab = [
            (F(hp, N), F(1, c) + F(1, c * h) + F(1, h * N)),
            (F(c, N), F(1, hp) + F(1, m * hp * N) + F(1, m * N)),
            (F(m, N), F(1, c * s) + F(1, c * N) + F(1, s * N)),
            (F(s, N), F(1, h) + F(1, m * h * N) + F(1, m * N)),
            (F(h, N), F(1, s) + F(1, s * hp) + F(1, hp * N)),
        ]
        for i, (l, r) in enumerate(tab):
            if l != r:
                fails.append(("table", c, m, s, i + 1))
        # Thm 3.1: K_c(s) = 1/m with r^2 = N/m ; product identity
        r2 = F(N, m)
        if F(c * s) - r2 != F(c + s, m):
            fails.append(("machin", c, m, s))
        has_word.add(N)
        if min(c, m, s) >= 2:
            ninterior += 1
            interior_by_N.setdefault(N, []).append(hp)
            if N % 4 == 1:
                some = any(x % 4 == 0 for x in (c, m, s, h, hp))
                nslice += some
                if some:
                    has_slice.add(N)
                if (jacobi(hp, N) == -1) != some:
                    fails.append(("cor1.2", c, m, s))
            # Lemma: h' < N, gcd(h',N)=1, HJ expansion = [c,m,s]
            if not (0 < hp < N and gcd(hp, N) == 1 and hj(N, hp) == [c, m, s]):
                fails.append(("hj", c, m, s))
    # set identity with independent census
    setfail = 0
    for N in range(2, NSET + 1):
        L3 = sorted(A for A in range(1, N) if gcd(A, N) == 1 and len(hj(N, A)) == 3)
        if L3 != sorted(interior_by_N.get(N, [])):
            setfail += 1
    sq = [k * k for k in range(3, int(NMAX ** 0.5) + 1, 2)]
    print(f"words={nw} interior={ninterior} slice(N=1 mod 4)={nslice} fails={len(fails)} {fails[:5]}")
    print(f"L3 set identity N<= {NSET}: mismatches={setfail}")
    print(f"odd squares 9..{NMAX}: {len(sq)}, with interior word: {sum(1 for q in sq if q in interior_by_N)},"
          f" with slice word: {sum(1 for q in sq if q in has_slice)}")
    print("105: interior words", interior_by_N.get(105), " any word", 105 in has_word)
    print("5: interior", interior_by_N.get(5), "; (1,4,2) N =", 4 * 2 - 1 - 2)
    E_W = [n for n in range(2, NMAX + 1) if n not in interior_by_N]
    print("N without interior word:", E_W)


if __name__ == "__main__":
    main()
