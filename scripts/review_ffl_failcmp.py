"""R161: recompute exhaustive failure lists with the from-scratch S2 solver and diff against data/ffl/fail_*."""
import sys, os, time
from review_ffl_solve import failures

cases = [tuple(c.split(":")) for c in sys.argv[1:]]
for q, A, n in cases:
    t = time.time()
    R, irr, fails = failures(int(q), A, int(n))
    mine = sorted(R.show(P) for P in fails)
    fn = f"../data/ffl/fail_q{q}_A{A}_n{n}.txt"
    theirs = sorted(l.strip() for l in open(fn)) if os.path.exists(fn) else None
    status = "no author list" if theirs is None else ("MATCH" if theirs == mine else f"MISMATCH author={theirs}")
    print(f"q={q} A={A} n={n}: FAIL {len(fails)}/{len(irr)} [{status}] ({time.time()-t:.0f}s) mine={mine[:6]}", flush=True)
