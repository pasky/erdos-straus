# z52b pass 1 — batch H00 (PILOT: first 8 of 25 items)

- Outcomes (8 items): nothing 6 (Z0042, Z0067, Z0069, Z0100, Z0110, Z0121), covered 2 (Z0109, Z0120), interesting 0, needs-compute 0, skipped 0.
- No interesting items. Note 1 (Z0067): the Bradford–Ionascu cone Q1 ∪ Q3 contains −ℕ, so it is trivial on the real axis; the closed-Q1 cone restricts to exactly ES and has 12 exceptions in total (6 up to symmetry), all of norm ≤ 293 (searched to norm 4000).
- Note 2 (Z0042): the BM main term M_BM does not reproduce the fitted (q/p) weights β_q; it misses the q ≡ 2 (3) pattern.
- Note 3 (Z0109, Z0110): Pomerance–Weingartner Table 1 (8/n exceptions to 10¹³) plus a trivial 2-adic lemma explain why the failure sets of "all denominators even" and "some 4 | denominator" coincide.
- Records: data/z52b/pass1/outcome_H00.jsonl; scripts scripts/z52b_p1_H00_*; data data/z52b/pass1/H00/.

## Notes (not "interesting"; recorded for reproducibility)

**Z0067: Gaussian ES cones.** `scripts/z52b_p1_H00_gauss.py NORMMAX A` runs an exhaustive search, complete for A ≥ 1.
The smallest denominator satisfies |a| ≤ 3|n|/4, and the two-term remainder is solved through all Gaussian divisors of N².
* Bradford–Ionascu cone K = Q1 ∪ Q3 (closed): every first-quadrant n ∉ {0, 1, i, 1+i} with N(n) ≤ 2000 has a
  solution (1614 values; CERTIFIED by the search). For real n it is trivial, since −ℕ ⊂ K. So
  BRAINSTORM/other_rings.md §4, which says the Gaussian cone is "discrete, a lottery again", overstates the case for rational inputs.
* Closed Q1 cone only: for real n, Im(1/a) ≤ 0 for every a ∈ Q1, so all denominators are real and the problem is exactly ES
  (PROVED). Exceptions with N(n) ≤ 4000 (3205 values) number 12, i.e. 6 up to the symmetry n ↦ i·n̄:
  2+5i (29), 3+4i = (2+i)² (25), 4+5i (41), 5+6i (61), 10+13i (269), 2+17i (293). There are none in 293 < N ≤ 4000.
  Reproduce: `uv run --with sympy python scripts/z52b_p1_H00_gauss.py 4000 2 q1` (≈ 2 min) → `data/z52b/pass1/H00/gauss_Q1_4000_2.json`.
