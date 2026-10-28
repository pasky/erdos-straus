"""z49_i3fable_cells.py — enumerate all interior words of n = k*m^2 (k in {1,2}) and tabulate the
(t mod 8, u mod 8) cells (ordered words, u = the endpoint attached to A = tu-1), separately for odd and even m.
Also checks the predicted empty-cell table of I3_DEEP_FABLE Thm 2.1 (squares) and prints the k=2 table.
Usage: uv run python scripts/z49_i3fable_cells.py [MMAX=240]
"""
import sys
from collections import defaultdict
from math import isqrt

def words(n):
    """ordered interior words (t,u,v) of n, t,u,v >= 3"""
    out = []
    u = 3
    while 3 * u * u - 2 * u <= n:
        # v | n+u, v >= u, (n+u)/v = tu-1 with t >= 3  <=>  v <= (n+u)/(3u-1); and v ≡ -n (mod u)
        N = n + u
        d = 1
        while d * d <= N:
            if N % d == 0:
                for v in {d, N // d}:
                    if v >= u and (v + n) % u == 0:
                        A = N // v
                        if (A + 1) % u == 0 and (A + 1) // u >= 3:
                            t = (A + 1) // u
                            out.append((t, u, v))
                            if v != u: out.append((t, v, u))
            d += 1
        u += 1
    return out

def predicted_allowed_square(t, u, modd):
    """Thm 2.1 table: is the cell (t mod 8, u mod 8) allowed at n = m^2 (modd: m odd)?"""
    t8, u8 = t % 8, u % 8
    if t % 4 == 0 or t8 == 7: return False
    if t8 in (1, 5):
        if u % 4 == 2: return True
        if u % 4 == 0: return False
        return modd and u8 == 3          # odd u: A even, needs m odd and u ≡ 3 (8)
    if t8 == 3:
        return modd and u % 4 == 1
    # t ≡ 2, 6 (mod 8)
    return u % 4 in (1, 2)

def main():
    MMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 240
    for k in (1, 2):
        for parity in (1, 0):
            cells = defaultdict(int); tot = 0
            viol = 0
            for m in range(3, MMAX + 1):
                if m % 2 != parity: continue
                n = k * m * m
                for (t, u, v) in words(n):
                    cells[(t % 8, u % 8)] += 1; tot += 1
                    if k == 1 and not predicted_allowed_square(t, u, parity == 1):
                        viol += 1
                        if viol <= 5: print("VIOLATION", n, (t, u, v))
            print(f"\n# n = {k}*m^2, m {'odd' if parity else 'even'}, m <= {MMAX}: {tot} ordered interior words; rows t mod 8, cols u mod 8")
            print("t\\u " + " ".join(f"{c:>6d}" for c in range(8)))
            for r in range(8):
                print(f"{r:>3d} " + " ".join(f"{cells[(r, c)]:>6d}" for c in range(8)))
            if k == 1:
                pred_empty = [(r, c) for r in range(8) for c in range(8) if not predicted_allowed_square(r, c, parity == 1)]
                nonempty_pred = [rc for rc in pred_empty if cells[rc] > 0]
                allowed_empty = [(r, c) for r in range(8) for c in range(8) if predicted_allowed_square(r, c, parity == 1) and cells[(r, c)] == 0]
                print(f"predicted-empty cells: {len(pred_empty)}; violations: {viol}; predicted-allowed cells that are empty in data: {allowed_empty}")

if __name__ == "__main__":
    main()
