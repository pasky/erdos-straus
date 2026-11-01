"""Z2688: realise every length-3 ES word (c,m,s) of N (N = cms-c-s) as a pentagon cut out of a classic
Conway-Coxeter frieze (Cuntz-Holm-Jørgensen arXiv:1909.02332 §4), and test where the sign is visible.
Construction: fan at V3 with m triangles, then c-1 ears glued at V2 and s-1 ears at V4 (quiddity insertions
(x,y) -> (x+1,1,y+1)).  Checks: (i) the sequence is a CC quiddity (product of [[a,-1],[1,0]] = -I, positive
frieze); (ii) the cut-out pentagon V1..V5 has sides (1,1,1,1,N) and diagonals (h',c,m,s,h);
(iii) sign: Jacobi (h'/N) = -1  <=>  some triangle count at V2,V3,V4 lies in C_N = 4Z ∪ (8Z-N)
(LOWERTAIL_ROUND2_FABLE Thm 1)  <=>  4 | one of the five diagonals (FRIEZE_ES Cor 1.3);
(iv) CHJ Thm 1.1/5.12 triangle conditions on all 10 sub-triangles of the pentagon."""
import sys
from math import gcd
from sympy import jacobi_symbol, isprime

def build(c, m, s):
    # cyclic list of [label, count]; fan polygon: V3 hub, order V3, V4, Y_{m-1..1}, V2
    if m >= 2:
        poly = [["V3", m], ["V4", 1]] + [["Y", 2] for _ in range(m - 1)] + [["V2", 1]]
        poly[2][1] = 2 if m > 2 else 2
        # ends of the Y chain adjacent to V4/V2 have count 2 already (fan); fix: Y's all 2
    else:
        poly = [["V3", 1], ["V4", 1], ["V2", 1]]
    def insert_after(i):  # ear between poly[i] and poly[i+1]
        j = (i + 1) % len(poly)
        poly[i][1] += 1; poly[j][1] += 1
        poly.insert(i + 1, ["Z", 1])
    if m == 1:
        insert_after(1)  # ear on edge V4-V2: both become 2
        # now V2=2, V4=2; more ears on V2's outer edge and V4's outer edge
        for _ in range(c - 2):
            i = [k for k, x in enumerate(poly) if x[0] == "V2"][0]
            insert_after(i - 1 if i > 0 else len(poly) - 1)
        for _ in range(s - 2):
            i = [k for k, x in enumerate(poly) if x[0] == "V4"][0]
            insert_after(i)
    else:
        for _ in range(c - 1):  # ear on the outer edge of V2 (edge between V2's predecessor and V2)
            i = [k for k, x in enumerate(poly) if x[0] == "V2"][0]
            insert_after(i - 1)
        for _ in range(s - 1):
            i = [k for k, x in enumerate(poly) if x[0] == "V4"][0]
            insert_after(i)
    # rotate so that order is V1, V2, V3, V4, V5, ...  (the list runs V3, V4, ..., V2 cyclically)
    i3 = [k for k, x in enumerate(poly) if x[0] == "V3"][0]
    poly = poly[i3 - 2:] + poly[:i3 - 2]  # now poly[0]=V1, [1]=V2, [2]=V3, [3]=V4, [4]=V5
    return [x[1] for x in poly], [x[0] for x in poly]

def is_quiddity(a):
    M = [[1, 0], [0, 1]]
    for x in a:
        M = [[M[0][0] * x + M[0][1], -M[0][0]], [M[1][0] * x + M[1][1], -M[1][0]]]
    return M == [[-1, 0], [0, -1]]

def frieze_entry(a, i, j):
    """c_{i,j} for i<j (positions in quiddity list) = continuant of a[i+1..j-1]"""
    p0, p1 = 1, 0  # K() = 1, K_{-1} = 0
    for x in a[i + 1:j]:
        p0, p1 = x * p0 - p1, p0
    return p0

def main(P):
    nwords = nfail = 0; tri_bad = 0; signchk = 0
    for N in range(5, P, 4):
        if not isprime(N):
            continue
        for t in range(1, N + 3):
            for u in range(1, N + 3):
                if t * u - 1 <= 0: continue
                if (N + u) % (t * u - 1): continue
                v = (N + u) // (t * u - 1)
                if v < 1: continue
                c, m, s = u, t, v   # FRIEZE_ES notation: word (c, m, s), N = mcs - c - s
                if m * c * s - c - s != N: continue
                if (c == 1 and m == 1) or (m == 1 and s == 1): continue
                a, lab = build(c, m, s)
                M = len(a)
                ok = is_quiddity(a) and all(x >= 1 for x in a) and lab[1:4] == ["V2", "V3", "V4"] and M >= 6
                ent = lambda i, j: frieze_entry(a, i, j) if i < j else frieze_entry(a[i:] + a[:i], 0, j + M - i)
                vals = {"sides": [ent(0, 1), ent(1, 2), ent(2, 3), ent(3, 4), ent(4, 0)],
                        "diag": [ent(4, 1), ent(0, 2), ent(1, 3), ent(2, 4), ent(3, 0)]}
                h, hp = c * m - 1, m * s - 1
                ok = ok and vals["sides"] == [1, 1, 1, 1, N] and vals["diag"] == [hp, c, m, s, h]
                nwords += 1; nfail += (not ok)
                # sign checks
                CN = lambda x: x % 4 == 0 or x % 8 == (-N) % 8
                j = jacobi_symbol(hp, N)
                s1 = (j == -1); s2 = any(CN(x) for x in (c, m, s)); s3 = any(x % 4 == 0 for x in (hp, c, m, s, h))
                if gcd(c * s, N) == 1 and not (s1 == s2 == s3): signchk += 1
                # CHJ Thm 1.1 on the 10 sub-triangles of the pentagon
                V = range(5)
                for (x, y, z) in [(x, y, z) for x in V for y in V for z in V if x < y < z]:
                    A, B, C = ent(x, y), ent(y, z), ent(x, z)
                    g = {gcd(A, B), gcd(B, C), gcd(A, C)}
                    nu = lambda n: (n & -n).bit_length() - 1
                    vs = {nu(A), nu(B), nu(C)}
                    if len(g) != 1 or not (vs == {0} or len(vs) > 1): tri_bad += 1
    print(f"primes N≡1 (4) < {P}: {nwords} words (incl. boundary words with a letter 1); cut-out realisation failures: {nfail}")
    print(f"sign equivalence failures (Jacobi vs triangle-count-in-C_N vs 4|diagonal), coprime words: {signchk}")
    print(f"CHJ Thm 1.1 violations on pentagon sub-triangles: {tri_bad}  (expected 0: every sub-triangle contains a side 1 or N)")

if __name__ == "__main__":
    main(int(sys.argv[1]))
