# s7_certified_caps — congruence-certified caps on the least-non-residue lines (O247, mandatory (ii))

## Idea
(J)64/(J)66 give the forced cap e ≤ (q − 3)/4 at a window q with (q/p) = −1 (one non-residue prime s | K with odd
exponent; CAP_DOWN Prop 1.3). Combine it with the *forced small primes* of K_q = (p + q)/4: ℓ | K_q ⟺ p ≡ −q (mod ℓ),
which a congruence class of p fixes. Question (ii): does this give cap ≤ 1 or 2 on an explicit positive-density set
of primes that matters (i.e. inside the undecided least-non-residue lines, not where ES is already known)?

**Lemma 1 (certified cap of a class; PROVED, elementary from CAP_DOWN Lemma 1.1).** Let p ≡ 1 (8), q ≡ 3 (4) prime with
(q/p) = −1, F the set of primes ℓ ≤ L with ℓ | K_q (for ℓ = 2: q ≡ 7 (8)). Put G_e = {−1, 0, 1, 3, 5, …, 2e + 1}. If for
every non-residue class a mod q, −1 ∈ a^{G_e}·Π_F, and for every non-residue ℓ₀ ∈ F, −1 ∈ ℓ₀^{G_e}·Π_{F∖{ℓ₀}} (all mod q),
where Π_F := {∏_{ℓ∈F} ℓ^{j_ℓ} : j_ℓ ∈ {−1, 0, 1}} is the bounded product set (not the generated subgroup), then e*(p) ≤ e.
*Proof.* K has a prime s, (s/q) = −1, b_s odd (reciprocity, CAP_DOWN Thm 1.2); either s ∉ F (first condition with
a = s mod q) or s ∈ F (second). Take d = K·s^g·∏ℓ^{j_ℓ} realising −1. For ℓ ∈ F, c_ℓ = b_ℓ + j_ℓ ∈ [0, 2b_ℓ];
for s, g ∈ {−1, 0, 1} gives c_s ≤ 2b_s, and g = 2e' + 1 gives c_s = b_s + g even with c_s/2 − b_s ≤ e'. Lemma 1.1. ∎
The hypothesis depends only on p mod 8·q·∏_{ℓ ≤ L} ℓ: each certified class is a congruence class (B1-type object),
but the existence of s is reciprocity, not a congruence (the (J)64 mechanism). For windows with (q/p) = +1 only the
F-part is available and certifies cap 0 iff −1 ∈ Π_F (an ET Type II class).

## Literature
CAP_POINTWISE Thm 1.1, CAP_DOWN Thm 1.2 / Prop 1.3 / Cor 2.2; STERILE_LOWER Comp 4.1 (lines r ≤ 13 are finitely
ET-covered at level 1, so cap statements there are superseded by ES).

## Barrier screen
* Statements on {(q/p) = −1} for q ∈ {3, 7, 11} are superseded: (p/3) = −1 or (p/7) = −1 is outside the Mordell-hard
  classes (ES, s7_window_lottery Prop 1), and every line lnr(p) = r ≤ 13 is ET-covered (STERILE_LOWER Comp 4.1).
  E.g. Lemma 1 at q = 11 gives e*(p) ≤ 1 for p ≡ 1 (24), (p/11) = −1 (3 | K₁₁ forced), but ES is already known there.
* So the first meaningful line is lnr(p) = 17 (undecided, (J)70/(J)77). There q₁(p) ≥ 19 and every forced bound is
  ≥ 1 unless F helps.
* B1: for every fixed e the points of the line with (q/p) = +1 for all primes q ≡ 3 (4), q ≤ 4e + 3, have positive Haar
  measure and receive no forced witness ≤ e; certification there is F-only (= ET classes). So no fixed-cap uniform
  statement on a whole line comes from forced windows: "almost ES for a positive proportion" is a congruence statement,
  and positive proportions with ES itself are classical.
* T1: no window exists at odd squares (checked to 10⁷, s7_window_lottery).

## Cheap numerics (scripts/s7_certified_cap.py, s7_rgeneric_windows.py)
* Actual primes on the line lnr = 17 below 2·10⁷ (4 945 primes), forced windows only, q, L ≤ 200: certified cap 0 for
  79.4 %, ≤ 1 for 93.8 %, ≤ 2 for 95.2 %, max 21.
* Haar measure on the line (random residues mod every prime ≤ Q; QR below 17, QNR at 17; 3–4·10³ samples):
  forced windows only: cap 0 / ≤ 1 = 0.770 / 0.928 (Q = 200), 0.875 / 0.959 (Q = 400);
  forced + F-only unforced windows: cap 0 = 0.982 (Q = 200), 0.997 (Q = 400), 1.000 (Q = 800, 3 000 samples).
  So Haar-generic points of the r = 17 line are ET-covered quickly; any sterility lives on a null set (as known).
* r-generic line (p ≡ 1 at every prime ≠ r): x-windows at level 1 leave the cells r = 19: {2, 3, 10, 13} and
  r = 23: {5, 14} — exactly STERILE_LOWER Comp 4.1's survivor sets (an independent consistency check of the
  window ↔ P-datum dictionary); at r = 17 windows leave {3, 5, 6, 7} (Comp 4.1, all ET types: {5, 7}), at r = 13
  {2, 5, 7, 8} (Comp 4.1: none), so Type I / Q-data matter at r ≤ 17.

## Assessment
PROVED (Lemma 1, per class) + EVIDENCE (densities). Answer to (ii): yes, explicit positive-density classes of the first
undecided line r = 17 get e*(p) ≤ 1 (Haar measure ≈ 0.93–0.96 with windows ≤ 400) — but these are congruence classes, and
the same window data at cap 0 already cover Haar-almost all of the line. The forced witness adds nothing at the
points that matter (the r-generic / sterile points, where (q/p) = +1 for every window prime q ≠ r, so no window is
forced at all). Value: a clean statement of *where* (J)64 lives — it is a Haar-generic mechanism, blind on the
sterile null set.
