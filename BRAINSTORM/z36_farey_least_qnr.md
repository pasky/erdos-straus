# z36 — The Farey-metric least non-residue: the ES ladder λ(p) ≤ L (O266 memo 2)

## Idea
ES-five(p) ⟺ λ(p) ≤ 3 (DEDEKIND_ES Cor 4.6), λ(p) = least HJ length r(p/A) over non-residues A. Relax 3 → L and ask for
the least L that is a theorem. Details: ZAREMBA_TRANSFER.md §2, §4.

## Literature
* G. Larcher (1986), quoted in M.-C. Chang, "Partial quotients and equidistribution" (math.ucr.edu/~mcc/paper/141,
  read): some b mod N has Σ a_i(b/N) < c log N log log N; Chang Thm 5: *most primitive roots* x mod p have
  Σ a_i(x/p) ≪ log p log log p; Chang p. 2: removing the log log factor "is still open and would follow from … Zaremba".
* Chang Prop 1 / Thm 2: for subgroups G ≤ F_p^*, |G| > p^{7/8+ε}, most x ∈ G have max a_i ≪ log p.
* Aistleitner–Borda–Hauke, TAMS 377 (2024), arXiv:2210.14095 (distribution of partial quotients at fixed denominator;
  not read beyond the abstract).

## Results
* **Theorem A (PROVED, elementary; KNOWN in substance via Chang Thm 5, since primitive roots are non-residues).**
  λ(p) ≤ 1 + 10(1 + log p)(1 + log⌈10(1 + log p)⌉) for all primes p > 5. Self-contained pigeonhole proof in §2.
* **Theorem B (CONDITIONAL on Hypothesis ZQ_M: a non-residue with all digits ≤ M).** λ(p) ≤ 1.04 M log p + O(M).
* So the ladder: L = 3 (ES-five; ≍ log²p certificates) … L fixed (polylog) … L = c log p (p^{θ(c)}, density p^{−β(c)})
  … L ≍ log p log log p (density ≥ 1/2: theorem by pigeonhole).

## Barrier screen
B3: the theorem rung is exactly where the certificate set has positive density; B5/T1: every rung is void at m² (no
non-residues), and the proof's false-at-m² step is "#non-residues = (p − 1)/2"; B6 not involved (pointwise).

## Cheap numerics (`scripts/z36_ladder.py`, `scripts/z36_thmA_check.py`)
At p ≈ 10⁶ (true HJ lengths; R276 repair D2 — the first version used the false formula r = 1 + Σ_{i odd} a_i, which is only an upper bound): |S₃| = 143, |S₈| = 21761, |S_{13}| = p^{0.86}, median r = 25 ≈ 1.8 log p; the inequality
#{(a, i) : c_i ≥ k} ≤ 2(p/k)(1 + log p) holds with ratio ≤ 0.51 at p = 11 … 10⁶; at 997² the same set sizes but no −1.

## Assessment
PROVED (known in substance) + CONDITIONAL. Quantifies the ES gap in one metric: log p log log p (theorem) vs 3 (ES).
The 2026 Zaremba theorems would at best remove the log log factor (Thm B), and only after a χ-twist they do not contain.
