"""z49_i3fable_survival.py — empirical survival P(minV(n) > X) (no interior word with larger endpoint <= X)
by class of n in a window, from the arrays written by z49_i3fable_count.c; for comparison with the CRT model.
Usage: uv run python scripts/z49_i3fable_survival.py PREFIX LO HI
"""
import sys, numpy as np
from math import isqrt

def main():
    prefix, LO, HI = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    MV = np.fromfile(prefix + "_minv.u32", dtype=np.uint32)
    N = len(MV) - 1
    n = np.arange(LO, HI + 1, dtype=np.int64); mv = MV[LO:HI + 1].astype(np.int64)
    sq = np.zeros(len(n), dtype=bool); r = np.arange(isqrt(LO), isqrt(HI) + 2); rr = r * r; rr = rr[(rr >= LO) & (rr <= HI)]; sq[rr - LO] = True
    sq2 = np.zeros(len(n), dtype=bool); r2 = np.arange(isqrt(LO // 2), isqrt(HI // 2) + 2); rr2 = 2 * r2 * r2; rr2 = rr2[(rr2 >= LO) & (rr2 <= HI)]; sq2[rr2 - LO] = True
    odd = n % 2 == 1
    classes = [("odd non-square", odd & ~sq), ("even non-square", ~odd & ~sq & ~sq2), ("n=5 mod 8", n % 8 == 5), ("n=7 mod 8", n % 8 == 7),
               ("n=0 mod 4 nonsq", (n % 4 == 0) & ~sq), ("n=0 mod 12 nonsq", (n % 12 == 0) & ~sq), ("n=0 mod 60 nonsq", (n % 60 == 0) & ~sq),
               ("odd square", odd & sq), ("even square", ~odd & sq), ("square, 4|m", sq & (n % 16 == 0)), ("square, 12|m", sq & (n % 144 == 0)),
               ("square, 60|m", sq & (n % 3600 == 0)), ("2*square", sq2)]
    Xs = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    print(f"# window [{LO},{HI}]: class, count, then P(minV > X) for X = {Xs}, then P(I3=0)")
    for name, mask in classes:
        c = int(mask.sum())
        if c == 0: continue
        m = mv[mask]
        row = " ".join(f"{np.mean(m > X):.4f}" for X in Xs if X * X <= HI)
        print(f"{name:20s} {c:9d}  {row}   zero={np.mean(m == 0xFFFFFFFF):.2e} ({int((m == 0xFFFFFFFF).sum())})")

if __name__ == "__main__":
    main()
