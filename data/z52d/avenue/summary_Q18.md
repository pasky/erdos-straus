# z52d avenue — batch Q18 (113 items) summary
ES is OPEN. Rows: `out_Q18.jsonl`. Per-row labels are Assessments unless they cite a PROVED/CERTIFIED source. This was a non-proof-attempt
batch, mostly the external-problem catalog (Z0408–Z0675): 86 rows are "calibration only", handled briefly.

**Status × plausibility** (rows: status; columns: plausibility 0/1/2/3)
| status | 0 | 1 | 2 | 3 | Σ |
|---|---|---|---|---|---|
| known-true (gap named / calibration fact) | 0 | 0 | 0 | 84 | 84 |
| circular | 10 | 0 | 0 | 0 | 10 |
| known-false | 10 | 0 | 0 | 0 | 10 |
| open-plausible | 0 | 3 | 1 | 0 | 4 |
| unclear | 0 | 3 | 0 | 0 | 3 |
| harder-than-open | 2 | 0 | 0 | 0 | 2 |
Novelty: 0 → 98, 1 → 15, 2 → 0. All plaus-3 rows are calibration facts or main-term statements (yield none), except Z0537 (thin families).

**Plausibility ≥ 2 AND novelty ≥ 1**: none with any ES yield. Z0500 (Ford divisor-range laws as a variance model for R) and
Z0513/Z0587/Z0588 are calibration facts. Nearest to a lane: **Z0669** (plaus 2, nov 0): *Haar survival of the residue model decays like
exp(−c log³X)*, which yields at most CRT exceptional-set bounds (capped at 3/4). **Z0537** (plaus 3, nov 0): Aurifeuillean identities for bases 3, 5, 6, 7
against the open thin families of FRONTIER §7.8.

**Recurring missing theorems**
1. *Forced-class divisors must still divide the tied integer* (circular; ℓ = 4Ck − 1 | 4Cp + 1 ⟺ ℓ | p + k, the trial form): Z0430, Z0431, Z0432,
   Z0498 (subset products = divisor condition), Z0408 (Stewart form; squares force exactly ker χ_{−4C}).
2. *Rational/Heegner/parity-forced points* (rational ≠ integral; B3): Z0423, Z0424, Z0425; norm/binary-form certificates Z0593 ((J)3).
3. *Pointwise lower tail* (H⁻_BM-type, circular): Z0670, Z0683, Z0773, Z0604 (singular series = M_BM, gap = H⁻_BM), Z0414 (ES₅).
4. *Bounded/congruence procedures* (B1, known-false): Z0440 (digit recursion), Z0561 (size forcing), Z0573 (Chebotarev ≠ divisor event),
   Z0631 (covering lemma), Z0649 (non-residue activation = parity layer only), Z1231 (identity families), Z0443 (pigeonhole, B4).
5. *Averages / density machinery* (B6): Z0418, Z0421, Z0499, Z0502, Z0572 (finite Dirichlet polynomial at fixed p), Z0588, Z0602.

**New in this pass** (script `scripts/z52d_avenue_Q18_sizes.py`, timeout 60–200 s, p < 2000)
* **Z0624 correction**: "all positive ES solutions are ≪ n²" is false. Max z reaches p^{3.6} (p = 1999), with z ≍ p⁴/16 at p ≡ 3 (4).
  The least achievable max denominator is ≤ 0.503 p² for every p < 2000, and is largest at 577, a (★)-zero. With Q03 Z0644's lower bound
  p^{3/2}/2, the size dividing line lies in k ∈ [3/2, 2], and the k = 2 form is ES-strength (Z0511).
* **Z0498** (PROVED, elementary): for 4C | 24, (ℤ/4C)^× is an elementary 2-group. So 4Cp + 1 has a divisor ≡ −1 (mod 4C) iff −1 lies in the
  span of its prime-factor classes. This corrects Pass 1's "not a constraint on prime factors". Davenport-type forcing would need
  ω(N_C) ≳ D((ℤ/4C)^×), which fails for large C, while fixed C is a finite menu (B2(iii)).
* **Z0512/Z0590** (Assessment): Crocker-type failures need *forced compositeness*, which covering congruences supply. ES failures need *forced
  confinement* of divisors, and congruences supply that only for finitely many slices (the Dickson "n = 1 shadow"). So the log vs log² minimal pair
  does not transfer as a failure mechanism.
* **Z0441**: the parity of R(p) is useless (R is always even). An M5 count-congruence route needs an involution on a p-dependent set
  whose fixed-point count sees (·/p).

**Corrections.** Z0624 premise (above). Z0498 Pass 1 (above). Z0573: "Type I at (a,d) ⟺ Frob_p in a subset" is not just a restatement but
incorrect: only a slice's congruence part is Chebotarev (CLASS_FORCING Thm 2.1). Z0582: the item's Burgess-range premise is refuted (Pass 1).

**Assessment.** Q18 is calibration. Every pointwise mechanism in the external catalog (Heegner points, parity, primitive divisors,
subset products, pigeonhole, coverings, singular series) uses an M1–M5 input that ES lacks, or reduces to the tied-divisor event.
