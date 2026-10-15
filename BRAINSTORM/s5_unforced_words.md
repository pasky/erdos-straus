# s5_unforced_words — hard primes are the primes where almost every word is forced by a clean side (own idea, O230)

## Idea
By s5_three_sides Lemma S, a word on a clean side is *forced* to χ = +1. Let U(n) be the number of *unforced* words,
those with all three sides unclean. Lemma S gives N₋ ≤ U (PROVED). The questions: how much of the sign lottery is
explained by U, and is there a structural inequality N₋ ≥ c·U?

## Definitions
* n ≡ 1 (mod 4) odd, ψ = (·/n) (Jacobi).
* A side is clean if no prime factor r has ψ(r) = −1. Zeros are allowed, so at odd squares every side is clean and
  U(m²) = 0 (T1 form).
* For n ≡ 3 (mod 4), χ = −ψ(A) and the question is trivial (Mordell), so these n are excluded.

## Results
* **Hard primes = forced primes (EVIDENCE).** For all 13 primes < 10⁶ with N₊ ≥ 4N₋ ((J)48's hardest list), N₊ − N_forced
  ∈ {0, 2}: every χ = +1 word but at most 2 is forced by a clean side. Their forced fraction (0.78–0.89) is in the top
  0.1 % of all primes (median 0.11).
* Over the 39 095 primes p ≡ 1 (mod 4), p < 10⁶:
  * corr(N₋, U) = 0.966, versus corr(N₋, N) = 0.903.
  * N₋/U has mean 0.768 and sd 0.077.
  * At the 16 primes with U < 16, N₋ = U in 15 cases: every unforced word is a certificate.
  * So **ES-five hardness is, to first order, the smallness of U(p)**. A certificate fails to exist essentially only
    when (almost) every word sits on a clean side.
* **CONJECTURE U (EVIDENCE).** For odd non-square n ≡ 1 (mod 4), U(n) = 0 ⟺ n = 105.
  * `scripts/s5_U.c`: the only n ≤ 2·10⁵ with U = 0 is 105, the SQ₅ exception. There, every word of X₁₀₅ lies on a
    clean side.
  * Since N₋ ≤ U, CONJECTURE U is implied by SQ₅ (plus 105) and is weaker than it. The exception sets agree up to
    2·10⁵.
* **"Unforced sign dominance" N₋ ≥ U/2 (REFUTED).**
  * It holds at every prime ≡ 1 (mod 4) below 5·10⁶ (minimum 122/241 = 0.506 at p = 3 103 073), which suggested an
    injection.
  * It fails for the composite 110 897 = 43·2579 (44/97).
  * It fails at the primes **5 270 849 (192/389), 17 188 937 (164/345) and 21 387 257 (126/259)**, from a census of all
    754 586 primes p ≡ 1 (mod 4) in (5·10⁶, 3·10⁷).
  * So there is no exact pairing of unforced χ = +1 words with certificates.
  * Steering note: the near-miss at 1/2 is a distributional coincidence, not a symmetry. Anyone who sees the 0.506 should
    not chase an involution.

## Catalogue: the least-N₋ prime in each dyadic block (EVIDENCE; s5_sides, p < 3·10⁷)
| p | N | N₋ | U | forced | K0 | lnr | p mod 840 |
|---|---|---|---|---|---|---|---|
| 2 521 | 37 | 4 | 4 | 0.89 | 21 | 11 | 1 |
| 9 601 | 53 | 8 | 8 | 0.85 | 192 | 13 | 361 |
| 21 841 | 43 | 14 | 15 | 0.65 | 232 | 11 | 1 |
| 174 241 | 65 | 14 | 14 | 0.78 | 352 | 13 | 361 |
| 944 329 | 73 | 20 | 20 | 0.73 | 1488 | 19 | 169 |
| 5 516 281 | 53 | 24 | 24 | 0.55 | 3177 | 23 | 1 |
| 9 768 361 | 105 | 24 | 24 | 0.77 | 2736 | 13 | 1 |
| 17 287 201 | 119 | 30 | 34 | 0.71 | 6552 | 11 | 1 |

Every block minimum has a forced fraction of 0.55–0.89 (median about 0.12) and N₋ = U or nearly. Most are p ≡ 1
(mod 840), i.e. squares modulo all small primes. K0 is generic, so these primes are not archimedeanly near squares,
consistent with (J)48 D9.

## Why the unforced words are mostly certificates (Assessment)
* An unforced word with χ = +1 needs A to contain an even number (≥ 2) of ψ-odd primes, and both other sides unclean.
* A certificate needs one.
* When p is a square modulo all small primes (the hard primes), every ψ-odd prime is ≥ lnr(p), so two of them in A
  cost a lot. Hence N₋/U → 1 exactly where U is small. This is the (J)27/(J)48 "p looks like a square to small moduli"
  reading, now made quantitative through the forced/unforced split.

## Literature
None specific. The forced/unforced split is a refinement of THREE_SQUARES' clean levels to all three sides.

## Barrier screen
* T1: U(m²) = 0 (all sides clean).
* B2: U ≥ 1 still requires a word with three unclean sides, which is a divisor event in moving moduli.
* B6: the correlations are statistics over p.
* No forcing.

## Cheap numerics
* `scripts/s5_sides.c` (primes 5 to 3·10⁷): 0 Lemma S violations in every run.
* `scripts/s5_U.c` (all n ≡ 1 (mod 4) to 2·10⁵): 0 Lemma S violations; U = 0 only at 105.
* Tiny summaries are in SYNTHESIS_SPARKS5 §3.

## Assessment
* PROVED: N₋ ≤ U.
* EVIDENCE: hardness ≈ small U, the 13 hard primes are fully forced, and CONJECTURE U.
* REFUTED (with explicit counterexamples): N₋ ≥ U/2.
* A sharp descriptive law, not an existence mechanism.
