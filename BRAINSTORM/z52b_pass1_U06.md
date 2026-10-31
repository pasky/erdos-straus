# z52b pass1 U06 — status (INCOMPLETE batch; not merged)

Status: 100 of 207 items have an outcome line; 107 are NOT yet processed (listed in outcome_U06 vs batch_U06).
Counts: {'covered': 17, 'needs-compute': 14, 'nothing': 51, 'skipped': 16, 'interesting': 2}.

Interesting:
1. Z3132 — PROVED + verified (1754/1754 certificate divisors, p ≡ 1 (4) ≤ 3000, C ≤ 60): every d | 4Cp+1 with d ≡ -1 (mod 4C) is a QNR mod p.
2. Z1007 — five-slice A/p (CF length ≤ 3, 150 primes): 47% all-even CF quotients vs 0.9% of all A/p. Next: split by p mod 8 and 4 | t.

Caveat: Z0794 U(p) (unordered solutions) gives corr(logU, CF period) = +0.36 on 116 primes, opposite sign to classical_corr.txt; unreconciled.

Scripts: scripts/z52b_p1_U06_{a..j}.py; data: data/z52b/pass1/U06/.
