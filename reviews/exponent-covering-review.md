# R185 — hostile review of O185 EXPONENT_COVERING.md (reviewer 1 of 2, full document)

Reviewer branch `side-agent/review-expcover-1`. From-scratch scripts `scripts/review_ec_*.py`.
Status: IN PROGRESS.

## Summary verdicts
(filled in below as each claim is checked)

## Defects

### Thm 4.1 (ES for all k·2^m + 1, k ∈ {1, 9, 21, 27, 57, 171, 231, 315, 393, 495, 15015}) — **SOUND** (minor wording defects)
Independent checker `scripts/review_ec_cert.py` (sympy, exact; uses only (M, r, x(n), y(n), z(n)) from each certificate, ignores the
author's `exps`/`fam` fields and does not import any author code). For each of the 11 certificates and every class it verifies:
(i) 4xyz − n(xy+yz+zx) = 0 in Q[n] (this also confirms the coefficient lists are ascending); (ii) integer-valuedness of x, y, z on
n = r + Mt by the Pólya criterion (values at t = 0..deg) AND, as a cross-check, by reducing the cleared numerator modulo its
denominator D for all t mod D (all D ≤ 10⁶, so the cross-check was exhaustive for every class); (iii) positivity: positive leading
coefficient and exact largest real root (all bounds are ≤ 1, so positivity holds for every n ≥ 2); (iv) M = 2^s M′ with
M′ | 2^L − 1, and coverage of every m in [m₁, m₁ + 2L) with m₁ = max s (so n_m mod M is L-periodic for m ≥ m₁ for *every* class
simultaneously), plus exact evaluation of the solution at each such n_m; (v) all m < m₁ (at most 5 values per k) by an independent
ES search with exact verification. **Result: all 11 certificates PASS** (runtime ~2 s). The logic "cover at L consecutive
representatives m ≥ max s ⟹ cover all m ≥ max s" is correct (Lemma 1.1 for each class separately, all representatives ≥ every s).
Side facts re-checked (`scripts/review_ec_facts.py`): 315·8 = 2520, 15015·8 = 120120; 27·2^m+1 is prime for m ∈ {2, 4, 7, 16, 19,
20, 22, 26, 40, 44, 46, 47, 50, 56, 59, 64} (m < 80), so 27·2²⁶+1 and 27·2⁵⁰+1 are indeed prime and ≡ 529 (mod 840); the k = 27
character table of §2 is correct entry by entry, and the listed cases exhaust Z/12.
The ES-solvability of each class is fully contained in the certificate's explicit polynomial identity — the Thm 1.2 "ET classes
avoid odd squares" input (T1) is NOT used by Thm 4.1, nor is the ET/mordell_lib provenance of the classes. Label PROVED
(computer-assisted) is appropriate. Defects: D1, D2 (minor).
