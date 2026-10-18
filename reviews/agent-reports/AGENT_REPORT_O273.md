# AGENT REPORT — O273 (board #2 slate)

Branch `side-agent/board-two-slate`. Main file `BOARD2_SLATE.md`; edits to `ZAREMBA_TRANSFER.md` (§2 attribution note) and
`FORCED_WINDOW.md` (new §8). Scripts `scripts/z42_*`, logs `logs/z42_*`, new source `sources/henriot-erratum-2014.pdf`.
ES is not solved; none of the four items is single-prime lower-tail progress (the board's verdict stands).

## (1) ABH attribution — DONE (KNOWN)
* Read arXiv:2210.14095v2 directly: Thm 1, Thm 6 and identity (5) are as the board quoted them, at a single fixed
  denominator. The transfer, re-derived: λ(p) ≤ (6/π²) log p log log p + O(log p). It is recorded as KNOWN in
  ZAREMBA_TRANSFER right after Theorem A; the existing text is kept.
* Checks (`z42_abh_check.py`):
  * the HJ formula is r = 1 + Σ_even − δ with δ ∈ {0, 1};
  * |S_alt + 12D| ≤ 3.
* Argon's "convergent Legendre invariant" is a one-line consequence of a q_i ≡ (−1)^i ρ_i (mod p). It is the same
  genus-character fact as DEDEKIND_ES Thm 4.5. Recorded as **not new**.

## (2) Moving-window cap-0 witnesses — DONE (FORCED_WINDOW §8)
* **Theorem 8.5 (PROVED modulo Henriot 2014 New Thm 5, Siegel–Walfisz, Mertens; ineffective).** Let 0 < α < 1/6. All
  but O(X/L^{4/3−2α−ε}) primes p ≡ 1 (8) in (X, 2X] satisfy the L¹ Fourier certificate, and hence have a Type II
  solution with window q, at **every** prime q ≡ 3 (8) in [L^α, 2L^α].
* Forcedness is not needed, since the certificate is target-free. This is a small strengthening of the board's phrasing.
* Henriot's statement was taken from the **2014 erratum itself** (downloaded). New Thm 5 was applied with
  Q₁ = t, Q₂ = 4t − q and F = f(n₁)·1[P⁻(n₂) > √x] ∈ M₂(1, 1, ε). The local factors were computed exactly. The erratum's
  changes (ρ̂ → ρ̆ ≤ ρ̂; D* → a*D*) do not affect the use.
* Value: dominated. Fixed q = 3 alone gives ≪ X/L^{3/2} exceptions; Vaughan and the 3/4 chain are far stronger. New only
  in shape.
* Priority: a limited search found nothing. The fixed-window analogue is Elsholtz–Tao Thm 1.8.
* EVIDENCE: certificate ⇒ explicit solution, 0 violations over 990 windows. One note: Σ = 1 exactly occurs, so the
  certificate's inequality must be strict.

## (3) Five-slice union R_III^int — DONE, with a correction to the board
* **Lemma 3.2 (PROVED): the sign at a hit is forced.**
  * Odd–odd: a pair can be active iff it is not ≡ (1, 1) mod 4.
  * k = 1: activation is a mod-8 condition.
  * **k ≥ 2 (4 | u or 4 | v): every 2-adically compatible pair is automatically active.**
* **T1-exact main term** M(n), with all three sustained repairs built in: the gcd(n, uv) = 1 restriction, principal only
  for square odd part, and activation recomputed. PROVED: M ≥ 0, M(m²) = 0, mean-preserving.
* **Principal constant is 45/(8π²) ≈ 0.570 L², not 33/(8π²).** The opposite-parity sector is 3 × 3/(2π²), not 2 ×.
  Sector fits over 10⁴…10⁸ reproduce 9/(8π²) (odd–odd) and 3/(2π²) (k = 1, k = 2) to 4 digits. This confirms the ruling's
  suspicion (c) and resolves it.
* **Burgess lower bound I can prove: M(p) ≥ (45/(32π²) − o(1)) L² ≈ 0.142 L²** (Pólya–Vinogradov: 15/(64π²)). The proof
  is BM_CORRECTED Thm 2.2's method plus one device: put the class restriction inside the trivial initial segment.
  * This is the main-term bound only; R(p) > 0 does not follow.
  * The board's 33/(64π²) is superseded.
* Numerics (EVIDENCE):
  * Mean R/L² = 0.47 at 10⁶ (491 primes). **The board's "≈ 0.39 L²" is not reproduced**: it was a decomposition built on
    the wrong 2·M_BM identification.
  * R = M = 0 at the test squares.
  * 8/131 and 8/241 have no solutions at all, while R(241) = 6.
  * Thm 4.5's five conditions ⟺ (uv/n) = −1 at every hit: 0 violations.

## (4) 8/n zero law to 10⁹ — DONE (EVIDENCE)
* AP-marking with the three patches:
  * cutoff muB − u − B ≤ N;
  * exact φ(muB) and, for m = 12, the 3 | uB split (target unit iff m′ ≢ 2 (3));
  * m = 12, 16 sub-sampled at 10⁷.
* Brute-force self-test passes. The code agrees with `z38_mbm.c` for m = 8.
* Zeros: 2.75·10⁶ among odd non-squares ≤ 10⁹. **1 423 zeros have exact M ≥ 26 → drop-condition (a) passes.**
* Fit on M ∈ [10, 30]: **β = 0.89 ± 0.03**; local β in the top bins is 0.84 and 1.05. The excess over swap-Poisson grows
  from 2 to 15. The tail is fatter than Poisson but still decays like e^{−0.59 M^{0.89}} on the range. Under fable's rule
  (b), β ∈ [0.8, 1] means record and stop.
* Main caveat: M_BM is not 2-adically refined. Mixing n mod 2^j classes can produce the excess. The 2-adically refined main
  term is the next control; it was not run because of the CPU budget, which was ≈ 2 CPU-h used.

## For the parent
* Suggested DISCOVERIES/STATUS entries (not edited by me, to avoid merge conflicts):
  * ABH attribution (KNOWN);
  * FORCED_WINDOW Thm 8.5 (PROVED mod cited);
  * five-slice principal 45/(8π²) and Burgess bound 45/(32π²) (PROVED);
  * zero law β ≈ 0.89 (EVIDENCE).
* Points most worth a hostile check:
  * Thm 3.5's template, i.e. the "error scales with density" step and the family disjointness;
  * Lemma 3.2(iii) for odd k ≥ 3;
  * Lemma 8.3's local-factor computation at ℓ = q.
