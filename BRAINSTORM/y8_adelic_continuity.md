# y8_adelic_continuity — "continuity of T1" is adelic: clean levels and the √(log B / log tp) law (O217)

## Idea
O209 (§3.2) observed sign-dominance failures N₊(p) > N₋(p) "near squares". Correction (R214, and independently here):
the relevant proximity is **small-prime-adic**, not archimedean. Mechanism: for p prime, p ≡ 1 (4), and a word w ∈ X_p
with A = tu − 1, A* = tv − 1, AA* = tp + 1:
* (L1, PROVED) χ(w) = (−A/p) = (A/p) = (A*/p) = ∏_{ℓ^e ∥ A} (ℓ/p)^e (Legendre; AA* ≡ 1 mod p).
* (L2, PROVED) For an odd prime ℓ ∤ t with ℓ | tp + 1: (ℓ/p) = (p/ℓ) = (−t/ℓ) (since −tp ≡ 1 mod ℓ). So
  χ(w) = ∏_{ℓ | A} (−t/ℓ)^{v_ℓ(A)} × (2-adic factor (2/p)^{v₂(A)}).
* (L3, PROVED: clean levels) Call level t **clean** if every prime factor ℓ of tp + 1 has (ℓ/p) = +1. Then every word
  of level t has χ = +1. For odd ℓ ∤ t this is "ℓ splits in ℚ(√−t)"; for p = m² every level is clean (ℓ | tm² + 1 ⇒
  −t ≡ (1/m)² mod ℓ): **T1 is "all levels clean"** (tm² + 1 = 1² + t·m² is a norm from ℤ[√−t]).
* (L4, PROVED) Every prime ℓ < lnr(p) (least quadratic non-residue) is automatically clean. So only the
  lnr(p)-rough prime factors of tp + 1 can make a level unclean: near a profinite square (lnr large), tp + 1 has few
  "coins" (rough primes), each a ±1 that must be −1 somewhere in an admissible divisor A ≡ −1 (t).

## Literature
Sathe–Selberg (E[z^{ω(n)}] ~ F(z)(log x)^{z−1}); Tenenbaum, *Intro. to analytic and probabilistic NT*, II.6;
genus theory of ℚ(√−t) (Cox, *Primes of the form x² + ny²*, §3). Least non-residue: Burgess; GRH bound lnr ≤ 2 log² p
(Bach). (J)27 STERILE_STEER (non-square pattern N(x)).

## Barrier screen
B2: a level is unclean iff tp + 1 has a prime factor in the "wrong" genus class — divisor-in-class, moving modulus t.
B5/T1: at squares every level is clean, consistent. B6: the law below is an average over p with fixed pattern; it says
nothing at a single p. B3: clean-level probability is ≍ (log B/log p)^{1/2} per level, so the expected number of
unclean levels is still ≍ (#levels); no main-term certificate.

## Cheap numerics (`scripts/y8_census_features.py`, `scripts/y8_smooth.c`, `scripts/y8_levels.py`)
* All 39 174 primes p ≡ 1 (4), 5 < p < 10⁶ (si_census): mean N₋/N by decile of dist(p, ℤ²)/√p is 0.643–0.647 in
  every decile (archimedean distance irrelevant); by (p mod 8, lnr): (1,3) 0.645, (1,5) 0.604, (1,7) 0.565,
  (1,11) 0.516, (1,13) 0.481, (1,17) 0.452, (1,19) 0.442, (1,≥23) 0.430; p ≡ 5 (8): 0.685.
* Worst primes: 2521 (lnr 11), 9601 (13), 297 049 (19), 3361 (11), 1249 (7), 70 249 (17), 225 289 (17), …; the
  archimedean m² + 24 coincidences are the cheap way to get p ≡ □ mod 2, 3 (q | 24).
* 1 500 random primes p ≡ 1 (4) in (2·10⁵, 10⁶), levels t ≤ 30: fraction of clean levels vs mean of
  √(log B/log tp), B = lnr: (1,3) 0.314/0.265, (1,5) 0.431/0.320, (1,7) 0.498/0.352, (1,11) 0.570/0.393,
  (1,13) 0.575/0.405, (1,≥17) 0.606/0.433; (5, 2) 0.195/0.211. Ratio ≈ 1.2–1.4 for p ≡ 1 (8), stable: consistent
  with a Sathe–Selberg law P(level clean | lnr = B) ≍ (log B/log tp)^{1/2}.
* **Calibrated coin model (no free constant).** Exact Legendre signs for primes ℓ ≤ 100 of tp + 1, independent fair
  coins for the larger ℓ with odd exponent, **conditioned on the exact reciprocity constraint
  ∏_ℓ (ℓ/p)^{v_ℓ(tp+1)} = ((tp + 1)/p) = +1**: predicted vs observed clean fraction (600 primes, t ≤ 30):
  (1,3) 0.314/0.317, (1,5) 0.456/0.446, (1,7) 0.508/0.514, (1,11) 0.576/0.563, (1,13) 0.602/0.585,
  (1,≥17) 0.638/0.602, (5,2) 0.196/0.194. Without the constraint the model under-predicts by a factor ≈ 1.6; with
  unconditioned coins from lnr upward it is off in the other direction. Consequence (PROVED): if tp + 1 = s·ℓ^e (e odd)
  with s (lnr−1)-smooth and ℓ prime, level t is clean ("rank-one sterility").
* Removing words with A or A* (lnr−1)-smooth (forced +, 0 exceptions) flattens the ratio: N₋/(N − S) ≈ 0.66 for
  every lnr bucket 3…13 (p ≡ 1 mod 8) — but NOT at the extreme primes (2521: N − S = 27, N₋ = 4): there the whole
  level t = 1 (p + 1 = 2·13·97) and t = 2 (2p + 1 = 3·41²) are clean. The extremes are clean-level clusters.
* Example 2521: 19 words up to reversal; the two χ = −1 words are (15,2,87) (A = 29) and (44,2,29) (A = 3·29);
  29 is the only rough prime with (29/2521) = −1 that lands in an admissible divisor.

## Assessment
EVIDENCE (law) + PROVED (L1–L4, elementary). Answers goal (b): F is a function of the non-square pattern, through
the clean-level probability; T1 = all levels clean; continuity = Sathe–Selberg interpolation (log B/log p)^{1/2} → 1.
Steering: the hard primes are those where a few consecutive small levels are clean; any ES-five proof must show that
not all levels can be clean (a joint-factorisation statement on {tp + 1}_t: H-A).
