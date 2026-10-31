# z52b pass1 U06 — status (INCOMPLETE batch; not merged)

Status: 69 of 207 items have an outcome line; the remaining 138 are NOT yet processed. Counts from data/z52b/pass1/outcome_U06.jsonl are
in the file; the fix pass (pass1_U_fix.md) is applied only to the first 70 items.

Interesting (2):
1. Z3132 — PROVED + verified (1754/1754 certificate divisors, p ≡ 1 (4) ≤ 3000, C ≤ 60): every d | 4Cp+1 with d ≡ -1 (mod 4C) is a QNR mod p. Proof: (p/d) = (-1/d)(C/d) = -(C/d) and (C/d) = +1 by reciprocity; (d/p) = (p/d). Next: check overlap with DISCOVERIES.md Lemma S (genus character).
2. Z1007 — five-slice A/p (CF length ≤ 3, 150 primes): 47% have all-even CF quotients vs 0.9% of all A/p. Next: split by p mod 8 and level 4 | t over p ≤ 10^4.

Reproduce: scripts/z52b_p1_U06_e.py (Z0794, Z0838, Z1007, Z0152, Z1264, Z0854, Z0977, Z1003, Z1005, Z2237, Z2239, Z2862, Z3108, Z3085, Z2973, Z3177, Z3024, Z3132, Z3124, Z2571, Z1762, Z3146-old), scripts/z52b_p1_U06_f.py (Z3132 divisor table), scripts/z52b_p1_U06_g.py (Z3146), scripts/z52b_p1_U06_h.py (Z2001 cap sweep), scripts/z52b_p1_U06_a.py..d.py (earlier steps).

Caveat: Z0794 U(p) here (unordered solutions) gives corr(logU, logCF period) = +0.36 on 116 primes, opposite to the repo's classical_corr.txt (-0.275); unreconciled.
