#!/usr/bin/env python3
"""z51 forcing: joint failure of forced windows vs the independence model (EXSET_CHAR_FORCING §4).
Reads data/z51_forcing/win_1eK_perp.txt (pattern strings from z51_forcing_windows.c).
For R in a list: observed fraction of p whose forced windows q <= R all fail (Type II: 'F' or 'f'; full: 'F'),
vs the model  mean_p prod_{q forced, q<=R} f_q  with f_q the empirical per-q forced failure rate (same file).
Usage: z51_forcing_joint.py K [K ...]"""
import sys, math

def qlist(Q=400):
    out = []
    for q in range(3, Q + 1, 4):
        if all(q % d for d in range(2, int(q ** 0.5) + 1)):
            out.append(q)
    return out

def main():
    qs = qlist()
    for K in sys.argv[1:]:
        rows = []
        for line in open(f"data/z51_forcing/win_1e{K}_perp.txt"):
            if line.startswith("#"): continue
            parts = line.split()
            rows.append(parts[4])
        n = len(rows)
        nf2 = [0] * len(qs); nfF = [0] * len(qs); nfor = [0] * len(qs)
        for pat in rows:
            for i, c in enumerate(pat):
                if c in "SfF":
                    nfor[i] += 1
                    if c in "fF": nf2[i] += 1
                    if c == "F": nfF[i] += 1
        f2 = [nf2[i] / nfor[i] for i in range(len(qs))]
        fF = [nfF[i] / nfor[i] for i in range(len(qs))]
        print(f"== p ~ 1e{K}: {n} primes")
        print(" R   #q  obs_all_fail2  model2        obs_all_failF  modelF       mean#forced")
        for R in (12, 20, 32, 50, 80, 128, 200, 400):
            idx = [i for i, q in enumerate(qs) if q <= R]
            o2 = oF = 0; m2 = mF = 0.0; mf = 0
            for pat in rows:
                forced = [i for i in idx if pat[i] in "SfF"]
                mf += len(forced)
                if all(pat[i] in "fF" for i in forced): o2 += 1
                if all(pat[i] == "F" for i in forced): oF += 1
                m2 += math.prod(f2[i] for i in forced)
                mF += math.prod(fF[i] for i in forced)
            print(f"{R:4d} {len(idx):3d}  {o2/n:.3e} ({o2:5d})  {m2/n:.3e}   {oF/n:.3e} ({oF:5d})  {mF/n:.3e}   {mf/n:.2f}")

if __name__ == "__main__":
    main()
