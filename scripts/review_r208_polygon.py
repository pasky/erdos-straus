"""R208 from-scratch: Z_r(N) at odd squares (FRIEZE_ES §4), hexagon identity, Thm 4.1 small facts.

Interior word (b_1..b_r), b_i >= 2, N = K(b) (negative continuant). Polygon V_1=(0,-1), V_2=(1,0),
V_{j+1} = b_{j-1} V_j - V_{j-1}; V_{r+2} = (N, A). Quiddity at V_j = |det(V_{j-1}, V_{j+1})| (cyclic).
Z_r(N): some interior word of length r at N has a quiddity = 0 mod 4.
"""
import sys
from fractions import Fraction as F


def quid(b):
    V = [(0, -1), (1, 0)]
    for x in b:
        (a1, a2), (p1, p2) = V[-1], V[-2]
        V.append((x * a1 - p1, x * a2 - p2))
    L = len(V)
    det = lambda u, v: abs(u[0] * v[1] - u[1] * v[0])
    sides = [det(V[j], V[(j + 1) % L]) for j in range(L)]
    q = [det(V[j - 1], V[(j + 1) % L]) for j in range(L)]
    return V[-1][0], V[-1][1], sides, q


def words(r, N):
    """all interior words of length r with K = N (DFS with monotone continuant pruning)."""
    out = []
    def rec(pref, k1, k0):  # k1 = K(pref), k0 = K(pref minus last)
        if len(pref) == r:
            if k1 == N:
                out.append(tuple(pref))
            return
        x = 2
        while True:
            k2 = x * k1 - k0
            # remaining letters >= 2 keep continuant increasing: K_final >= k2 + (r-len-1)*(k2-k1)
            rem = r - len(pref) - 1
            if k2 + rem * (k2 - k1) > N:
                break
            rec(pref + [x], k2, k1)
            x += 1
    rec([], 1, 0)
    return out


def main():
    rmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    Mmax = int(sys.argv[2]) if len(sys.argv) > 2 else 25
    # hexagon identity
    for k in range(2, 3000):
        N = 4 * k - 3
        assert F(4, N) == F(1, k) + F(1, k * (2 * k - 1)) + F(1, (2 * k - 1) * (3 * k - 2)) + F(1, N * (3 * k - 2))
        Nn, A, sides, q = quid((2, 2, 2, k))
        assert Nn == N and sides == [1] * 5 + [N] and q[5] == 4
    print("hexagon identity + (2,2,2,k) quiddity 4 at V6: OK for k < 3000")
    # r = 0 mod 4 family
    for r in (4, 8, 12, 16, 20):
        for k in range(2, 200):
            Nn, A, sides, q = quid((2,) * (r - 1) + (k,))
            assert Nn == r * k - r + 1 and sides == [1] * (r + 1) + [Nn] and r in q
    print("(2^{r-1},k) family: K = rk-r+1, quiddity r present, r in {4..20}: OK")
    for r in range(2, rmax + 1):
        first = None
        for M in range(3, 2 * Mmax, 2):
            N = M * M
            for b in words(r, N):
                Nn, A, sides, q = quid(b)
                assert Nn == N and sides == [1] * (r + 1) + [N]
                if any(x % 4 == 0 for x in q):
                    first = (N, b, q)
                    break
            if first:
                break
        print("r", r, "first odd-square witness:", first)


if __name__ == "__main__":
    main()


def family_all_r(rmax=60):
    """R208: uniform odd-square witness for every r >= 5: word (2,2,2,4,2^l,k), l = r-5,
    Q = K(2,2,2,4,2^l) = 9l+13, K' = Q-9, N = (2Q+3)^2, k = (N+K')/Q. Letter 4 is a quiddity."""
    for r in range(5, rmax + 1):
        l = r - 5
        p = (2, 2, 2, 4) + (2,) * l
        Q = quid(p)[0]
        Kp = quid(p[:-1])[0]
        assert Q == 9 * l + 13 and Q - Kp == 9
        N = (2 * Q + 3) ** 2
        assert (N + Kp) % Q == 0
        k = (N + Kp) // Q
        w = p + (k,)
        Nn, A, sides, q = quid(w)
        assert k >= 2 and Nn == N and sides == [1] * (r + 1) + [N] and 4 in q and len(w) == r
    print("family (2,2,2,4,2^{r-5},k) at N=(2Q+3)^2: odd-square Z_r witness OK for 5 <= r <=", rmax)


family_all_r()
