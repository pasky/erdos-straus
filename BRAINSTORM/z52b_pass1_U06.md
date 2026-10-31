# z52b pass1 U06 — status (batch complete; not merged)

Counts (207 mids, one line each in data/z52b/pass1/outcome_U06.jsonl): nothing 125, covered 22, interesting 2, needs-compute 46, skipped 12.

Interesting:
1. Z3132 — PROVED + verified (1754/1754 certificate divisors, p ≡ 1 (4) ≤ 3000, C ≤ 60): every d | 4Cp+1 with d ≡ -1 (mod 4C) is a QNR mod p (Jacobi: (d/p) = (p/d) = -(C/d) = -1). Next: compare with the genus-character Lemma S (DISCOVERIES.md).
2. Z1007 — five-slice A/p (CF length ≤ 3): 47% all-even CF quotients vs 0.9% of all A/p (150 primes). Next: split by p mod 8 and by 4 | t over p ≤ 10^4.

Caveats: Z0794 U(p) (unordered) gives corr(log U, CF period) = +0.36, opposite sign to classical_corr.txt (-0.275) — unreconciled. Z2184 lookup failed (nothing, not checked). Z2820 OEIS term searches: no hits. Z2001/Z1998 are scaled-down (200-digit primes; 5-slice cap u ≤ 400 at k=5 only).
Needs-compute items (45) carry an explicit estimate: most are >1 h of design/coding (Lean, PARI, Hecke/Hirzebruch theory, transfer operators), not compute-bound.

Scripts: scripts/z52b_p1_U06_{a..p}.py; data: data/z52b/pass1/U06/.
