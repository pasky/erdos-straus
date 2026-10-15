"""dump Case B tuples (q=3) for s in [3, S] to a file: s m g w1 C1 (coeff strings low->high)"""
import sys, time
import review_r249_caseb as cb
S = int(sys.argv[1]); out = open(sys.argv[2], "w"); S0 = int(sys.argv[3]) if len(sys.argv) > 3 else 3
for s in range(S0, S + 1):
    t = time.time(); A = cb.tuples_T0(s)
    for (m, g, w1, C1) in A:
        out.write("%d %s %s %s %s\n" % (s, *("".join(map(str, p)) for p in (m, g, w1, C1))))
    out.flush(); print(s, len(A), "%.1fs" % (time.time() - t), flush=True)
