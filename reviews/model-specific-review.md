# R197 — hostile review of MODEL_SPECIFIC.md (O197)

Reviewer: R197 (side-agent/review-model-specific). Author branch merged: side-agent/model-specific.
From-scratch scripts: `scripts/review_ms_*`. ES is not solved; nothing below changes that.

## Summary verdicts
(filled in progressively)

### Lemma 3.0 (five m-slices give m/n solutions) — **SOUND**
Re-derived by hand: (I) 1/(vd)+1/(A*vd) = t/(A*d), plus 1/(A*dn) gives (tn+1)/(A*dn) = AA*/(A*dn) = m/n;
(T) (n+u+v)/(uvcn) with n+u+v = tuv = mcuv; (U) 1/(wf)+1/(tnw)+1/(tnwf) = (tn+f+1)/(tnwf) = (n+v)/(nwf), and
n+v = u(tv−1) = mwf; (I′),(V) by u↔v. `review_ms_words.py 1500`: every slice solution of every word of every odd
n ≤ 1500, all m = 4..24, checked in exact `Fraction` arithmetic, all denominators > 0: 0 failures.
Remark: gcd(A, n) = 1 is automatic (AA* = tn + 1), so the gcd clause in the word definition is redundant (harmless).

### Lemma 3.0′ (cell formula on all words incl. boundary) — **SOUND** (relative to DEDEKIND Cor 4.1)
Re-derived the reductions: t = 1: (u−1)(v−1) = n+1, n/(u−1) = [[v−1, u−1]] (b₁b₂ − 1 = n), K(b₁) = v−1 = A*,
Σ(b_i−3) = u+v−8 ✓. u = 1, t ≥ 2: n = (t−1)v − 1, n/(t−1) = [[v, t−1]]; the r = 2 right side
n+1−n(t+v−7)−A−v equals the length-3 one n+1−n(t+v−8)−A−(n+v) identically ✓. Corners ((t,1,1), (1,2,v), (1,u,2),
(2,1,v); (2,u,1) by symmetry): RHS = 4n−2 ≡ 2 (mod 8) and (A/n) = 1 ✓. u↔v symmetry ✓ ((A/n)(A*/n) = (1/n)).
Independent numeric check (own Jacobi, not sympy): all 35 179 words of odd n ≤ 1500: 0 mismatches.
The only non-elementary input remains (D2)+(R) behind Cor 4.1 (DEDEKIND: "cited from memory, verified numerically");
the label "relative to Cor 4.1" is honest.

### Theorem 3.1 — **SOUND** (as narrowed: "determined by χ = (−A/n)")
* Cells (`review_ms_cells.py`, own enumeration over (ℤ/L)³, L = lcm(8, m)): every odd-n cell has RHS ∈ {2, 6} (asserted);
  m = 4: χ=−1 cells 240/240 in S_4, χ=+1 cells 0/80 ✓ (a). m = 8: 140/240, m = 12: 2304/6480, m = 16: 600/1920, and
  χ = +1 cells 0 for every 4 | m ≤ 24 ✓ (b). For 4 ∤ m the slice fraction is *identical* on both χ-halves for every
  m = 5..23 (0.712, 0.489, 0.563, 0.421, 0.333, 0.391, 0.339, 0.251, 0.251 for m = 5..15 match the document; also
  17: 0.267, 18: 0.183, 19: 0.242, 21: 0.187, 22: 0.167, 23: 0.203). For odd m this is automatic by CRT
  (cells mod 8m = cells mod 8 × cells mod m, χ depends on the first factor, S_m on the second).
* Example words: (4,1,2) (n=5, A=3, χ=−1) ∈ S_4, ∉ S_m for m ≥ 8 ✓ (note it IS in S_7 via A* = 7 — irrelevant, claim is for
  4 | m ≥ 8); (m,1,2) ∈ S_m with χ = −1 for 4 | m; for 4 ∤ m the t = m members with (u,v) = (2,3)/(1,2)/(1,1) have χ = +1,
  n odd ≥ 3, and the non-members (3,1,2) (m ≥ 6), (3,1,6) (m = 5) have χ = +1 — all verified for every 5 ≤ m < 2000.
* Word level, odd n ≤ 1500 (`review_ms_words.py`): 35 179 words, 23 825 χ = −1 (all in S_4), 11 354 χ = +1 (none in S_4);
  S_8: 12 026 / 0; S_12: 6 573 / 0; S_5: 14 775 / 6 752 — **all of the document's §5 word numbers reproduced exactly**.
  For every 4 | m ≤ 24, no χ = +1 word lies in S_m (as the inclusion predicts).
* Proof logic: χ = (−1/n)(A/n), n mod 4 is a cell function, so χ is a cell function mod 8; S_m a cell function mod m. ✓
  Quantifiers: (a) is for every odd n, every word; (b) properness is per m with one fixed word; (c) per m. No hidden
  uniformity issue.

### Corollary 3.2 and the 131 / 241 statement — **SOUND**
Own enumeration: n = 131: 43 words, 29 with χ = −1 (all in S_4), 0 in S_8; n = 241: 31 words, 12 with χ = −1, 0 in S_8.
(The repaired 29/12 are correct; the original 22/7 was indeed an undercount.)

## Defects
(numbered; FATAL / MAJOR / MINOR)

## Work log
