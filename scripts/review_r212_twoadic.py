"""R212 from-scratch test of FOUR_SPECIFIC Thm 2.3.

For every word (t,u,v) (t u v - u - v = n) of every odd n <= NMAX:
  * chi = (-A/n) Jacobi, A = tu - 1;
  * Q_w ⊗ Q_2 isotropy via the Hasse-Witt invariant (rational LDL^T + 2-adic Hilbert symbols);
  * Z_2-Jordan splitting of G_w = [[v,-1,0],[-1,t,-1],[0,-1,u]] over Z_(2) (exact Fractions with odd
    denominators): blocks <a> (a unit) or even unimodular planes H / A; invariants (det mod 8, type, oddity).
Compares with <1,-1,-n> (det n, odd, oddity -n mod 8). Also checks chi=+1 words are NOT of that symbol.
Also checks, for each chi=-1 word, the Thm 2.3 proof step: a primitive isotropic vector mod 2^K exists (sanity).
"""
from fractions import Fraction as Fr
import sys
from collections import Counter


def jacobi(a, n):
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


def v2i(m):
    m = abs(m)
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1
    return k


def v2(f):
    f = Fr(f)
    return v2i(f.numerator) - v2i(f.denominator)


def unit_mod8(f):
    f = Fr(f)
    assert v2(f) == 0
    return (f.numerator * pow(f.denominator, -1, 8)) % 8


def hilbert2(a, b):
    a, b = Fr(a), Fr(b)
    a = a.numerator * a.denominator
    b = b.numerator * b.denominator
    al, be = v2i(a), v2i(b)
    u, w = a >> al, b >> be
    def e(x):
        return 0 if x % 4 == 1 else 1
    def om(x):
        return 0 if x % 8 in (1, 7) else 1
    s = e(u) * e(w) + al * om(w) + be * om(u)
    return -1 if s % 2 else 1


def diag_Q(G):
    """rational diagonalisation (with pivoting by basis change), returns diagonal entries"""
    G = [[Fr(x) for x in row] for row in G]
    n = len(G)
    d = []
    while n:
        i = next((k for k in range(n) if G[k][k] != 0), None)
        if i is None:
            # all diagonal entries zero: e0 -> e0 + ej with G[0][j] != 0
            j = next(k for k in range(1, n) if G[0][k] != 0)
            row = [G[0][k] + G[j][k] for k in range(n)]
            row[0] = 2 * G[0][j]  # Q(e0+ej) = 0 + 2B + 0
            for k in range(n):
                G[0][k] = row[k]
                G[k][0] = row[k]
            continue
        a = G[i][i]
        d.append(a)
        rest = [k for k in range(n) if k != i]
        G = [[G[r][c] - G[r][i] * G[i][c] / a for c in rest] for r in rest]
        n -= 1
    return d


def z2_symbol(G):
    """returns (det mod 8, type 'I'/'II', oddity mod 8, blocks)"""
    G = [[Fr(x) for x in row] for row in G]
    blocks = []
    det = Fr(1)
    while G:
        n = len(G)
        i = next((k for k in range(n) if G[k][k] != 0 and v2(G[k][k]) == 0), None)
        if i is not None:
            a = G[i][i]
            blocks.append(('d', unit_mod8(a)))
            det *= a
            rest = [k for k in range(n) if k != i]
            G = [[G[r][c] - G[r][i] * G[i][c] / a for c in rest] for r in rest]
            continue
        # even part: find unit off-diagonal
        found = None
        for p in range(n):
            for q in range(p + 1, n):
                if G[p][q] != 0 and v2(G[p][q]) == 0:
                    found = (p, q)
                    break
            if found:
                break
        assert found, "not unimodular"
        p, q = found
        a, b, c = G[p][p], G[p][q], G[q][q]
        dd = a * c - b * b
        assert v2(dd) == 0
        det *= dd
        blocks.append(('H' if unit_mod8(-dd) == 1 else 'A', 0))
        rest = [k for k in range(n) if k not in (p, q)]
        # project out plane: x -> x - (B(x,ep), B(x,eq)) P^{-1} (ep, eq)
        inv = [[c / dd, -b / dd], [-b / dd, a / dd]]
        def proj(r, s):
            vr = (G[r][p], G[r][q])
            vs = (G[s][p], G[s][q])
            corr = sum(vr[i] * inv[i][j] * vs[j] for i in range(2) for j in range(2))
            return G[r][s] - corr
        G = [[proj(r, s) for s in rest] for r in rest]
    odd = any(bk[0] == 'd' for bk in blocks)
    oddity = sum(bk[1] for bk in blocks if bk[0] == 'd') % 8
    return unit_mod8(det), ('I' if odd else 'II'), oddity, blocks


def words(n):
    out = []
    for t in range(1, n + 3):
        if t == 1:
            umax = n + 2
        else:
            umax = (n + 1) // (t - 1) + 1
        for u in range(1, umax + 1):
            A = t * u - 1
            if A < 1:
                continue
            if (n + u) % A:
                continue
            v = (n + u) // A
            if v >= 1:
                out.append((t, u, v))
    return out


def main(NMAX):
    stats = Counter()
    bad = []
    for n in range(3, NMAX + 1, 2):
        for (t, u, v) in words(n):
            A = t * u - 1
            G = [[v, -1, 0], [-1, t, -1], [0, -1, u]]
            assert v * (t * u - 1) - u == n
            chi = jacobi(-A, n)
            d = diag_Q(G)
            hw = hilbert2(d[0], d[1]) * hilbert2(d[0], d[2]) * hilbert2(d[1], d[2])
            iso = hw == hilbert2(-1, -n)
            dm8, typ, odt, blocks = z2_symbol(G)
            target = (n % 8, 'I', (-n) % 8)
            same = (dm8, typ, odt) == target
            stats[(chi, iso, same)] += 1
            if (chi == -1) != iso or (chi == -1) != same:
                bad.append((n, t, u, v, chi, iso, dm8, typ, odt))
            stats[('odd', chi, n % 8, odt)] += 1
    for k, val in sorted(stats.items(), key=str):
        print(k, val)
    print("violations:", len(bad), bad[:10])


if __name__ == "__main__":
    main(int(sys.argv[1]))
