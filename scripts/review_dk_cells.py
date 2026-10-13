"""R169 from-scratch checks of Thm 4.5, §8.1 (mod-4 sign), §8.2 (rotation), §8.3 (scaling).
Brute force over all length-3 words [[v,t,u]] with n = tuv-u-v <= N, n = 1 mod 4: direct Jacobi symbol.
Usage: PYTHONPATH=scripts uv run python scripts/review_dk_cells.py N
"""
import sys
from collections import defaultdict
from review_dk_core import jacobi


def five(t, u, v):
    return (t * u - 1) % 4 == 0 or (t * v - 1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0


PLUS = {(1, 2, 3), (1, 3, 2), (2, 1, 2), (2, 2, 1), (3, 1, 1)}


def poly_cells():
    """Proof step of Thm 4.5: 2(A/n) = n+1-n(t+u+v-9)-A-A* (mod 8) from (R)+(D2); check all 512 cells."""
    bad = 0; cnt = 0
    for t in range(8):
        for u in range(8):
            for v in range(8):
                n = t * u * v - u - v
                if n % 4 != 1:
                    continue
                cnt += 1
                V = (n + 1 - n * (t + u + v - 9) - (t * u - 1) - (t * v - 1)) % 8
                if V not in (2, 6):
                    bad += 1; continue
                sign = 1 if V == 2 else -1
                if (sign == -1) != five(t, u, v):
                    bad += 1
                if (sign == 1) != ((t % 4, u % 4, v % 4) in PLUS):
                    bad += 1
    print("polynomial cell check: admissible cells=%d bad=%d" % (cnt, bad))


def main():
    poly_cells()
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    bad = 0; words = 0; rot = 0; rotbad = 0
    cell8 = defaultdict(set)
    sq = set(k * k for k in range(1, int(N ** 0.5) + 2))
    slice_at_sq = 0
    for t in range(2, N):
        if 4 * t - 4 > N:
            break
        for u in range(2, N):
            if 2 * t * u - u - 2 > N:
                break
            for v in range(2, N):
                n = t * u * v - u - v
                if n > N:
                    break
                if n % 4 != 1:
                    continue
                words += 1
                A = t * u - 1
                j = jacobi(A, n)
                cell8[(t % 8, u % 8, v % 8)].add(j)
                if (j == -1) != five(t, u, v):
                    bad += 1
                    if bad < 10: print("Thm4.5 fail", t, u, v, n, j)
                if (j == 1) != ((t % 4, u % 4, v % 4) in PLUS):
                    bad += 1
                    if bad < 10: print("8.1 fail", t, u, v, n, j)
                if n in sq and five(t, u, v):
                    slice_at_sq += 1
                # rotation (v,t,u) -> (t,u,v): new middle u, n' = tuv - t - v
                n2 = t * u * v - t - v
                if n2 % 4 == 1:
                    rot += 1
                    if jacobi(u * v - 1, n2) != j:
                        rotbad += 1
    # mod-8 cell census
    adm = [c for c in cell8]
    nm = sum(1 for c in adm if cell8[c] == {-1}); npl = sum(1 for c in adm if cell8[c] == {1})
    mixed = sum(1 for c in adm if len(cell8[c]) > 1)
    # admissible mod-8 cells in theory
    th = sum(1 for t in range(8) for u in range(8) for v in range(8) if (t * u * v - u - v) % 4 == 1)
    th4 = sorted((t, u, v) for t in range(4) for u in range(4) for v in range(4) if (t * u * v - u - v) % 4 == 1)
    print("N=%d words(n=1 mod 4)=%d bad=%d slice-words-at-squares=%d" % (N, words, bad, slice_at_sq))
    print("mod-8 cells: theory admissible=%d observed=%d  all -1:%d  all +1:%d mixed:%d" % (th, len(adm), nm, npl, mixed))
    print("mod-4 admissible classes:", len(th4), " +1 classes subset:", PLUS <= set(th4),
          " five-cond false exactly on PLUS:", {c for c in th4 if not five(*c)} == PLUS)
    print("rotation pairs with n,n'=1 mod 4: %d  sign changes: %d" % (rot, rotbad))


if __name__ == "__main__":
    main()
