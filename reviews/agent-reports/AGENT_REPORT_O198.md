# AGENT_REPORT_O198 — χ-flipping moves on X_n (spark relay S), checkpoint 1

Main file: CHI_FLIP.md. Scripts: scripts/cf_* (cf_lib.py, cf_census.c, cf_groupoid.py, cf_check_*.py, cf_rotation_law.py,
cf_cell_groupoid.py, cf_mordell_check.py, cf_census_summary.py, cf_path.py). Branch side-agent/chi-flip (main merged in).
**ES is not solved, nor any infinite case.**

## SHARP:
1. **χ is minus the 2-adic isotropy sign of the path form (Thm 1.1, PROVED by Hilbert reciprocity alone).** For every
   positive word w of every odd n: (−A/n) = −ε₂(Q_w), Q_w = vx² + ty² + uz² − 2xy − 2yz (det n). Hence, for n = p prime,
   **five-slice certificate ⟺ Q_w is isotropic over ℚ₂ ⟺ C₀(Q_w) ≅ B_{p,∞}** (the supersingular quaternion algebra;
   explicitly B_{p,∞} ≅ (−A*, −vA*p)); non-certificates give the Hurwitz algebra B_{2,∞}. **T1 = "a positive ternary
   lattice with cyclic discriminant group of square order cannot ramify at an odd prime".** This gives a conceptual,
   citation-free reason for the mod-8 sign law (DK Cor 4.1 / MODEL_SPECIFIC Lemma 3.0′), and shows χ is a function of the
   word alone (n-free).
2. **Azumaya/BM reading (Prop 1.6).** det Q = n is constant on X_n, so C₀(Q) is an Azumaya algebra β on X_n[1/2n]; Thm 1.1
   is BM reciprocity for β at integral points, and T1 at squares is exactly a Brauer–Manin obstruction to positive integral
   points in the 2-adic certificate region Ω₂. SQ₅ (C1) ⟺ "BM from β is the only obstruction to positive integral points of
   X_n in Ω₂" (non-square n ≠ 105). (Assessment: an existence statement with a prescribed 2-adic congruence condition — not
   strong approximation, X_n(ℤ_{>0}) is finite; integral-Hasse-with-BM statements of this kind fail in general for Markoff-type
   log K3s, so this is a specific conjecture, not an instance of a known theorem.)
3. **Normalisation correction:** DK 8.3 / HJ_DEEP C3's "scaling is the only χ-flip" is an artefact of using (A/n) instead of
   (−A/n): scaling is a rational similarity of the path forms and **preserves χ** (Cor 1.4, certified on 43 200 cases).
   In the uniform normalisation, the classical moves that flip χ are only rotations with all letters odd and t ≢ u (mod 4)
   (Prop 1.5), which change n; no *fixed* chain of classical moves is an n-preserving flip on all of X_n (§2.3).

## Results (labels)
* PROVED: Thm 1.1; Cor 1.3 dictionary (certificate ⟺ ℚ₂-isotropic ⟺ B_{p,∞}); Cor 1.4 (χ n-free, scaling preserves χ);
  Prop 1.5 rotation law (flip ⟺ t, u, v odd and t ≢ u mod 4; finite cell check); Prop 1.6 (Azumaya class; T1 = BM);
  §2.3 fixed move chains are cell maps restricted to a cubic curve Z_Φ ∩ X_n (so only lottery-type flips); §3.1 for q ∈ {2,3,5,7}
  a non-residue (q = 2: p ≡ 5 mod 8), A = q is a certificate word (Mordell's 840; among odd primes exactly 3, 5, 7 work for every class); §4.2 parity facts.
* CERTIFIED: χ = −ε₂ on 39 921 words; χ = −1 ⟺ anisotropic at p on 9 924 prime-n words; B_{p,∞} presentation on 6 357 words;
  §3.1 for all primes p ≡ 1 (4) < 10⁶.
* EVIDENCE: groupoid of reversal/rotation/scaling — flips at fixed n exist inside components (n = 11, 79, 89, 93, 233, 419, 439
  in the box letters ≤ 60), in that box always through even numerators; odd-only chains: 2 flips (n = 125, 1119, composites) in the box
  letters ≤ 130, n ≤ 10⁶ (278 014 components). Census of all odd n ≤ 10⁶ (boundary words included): χ ≡ +1 only at n = 105 and at the 499 odd
  squares (χ ≡ −1 at 38 n ≡ 3 mod 4, e.g. 15, 311 — so 'χ non-constant' in C1/C3 must read 'χ not identically +1'); mean N₋/|X_p| = 0.606 at primes ≡ 1 (8), minimum 4/37 at p = 2521.
* NEGATIVE (Assessment): no χ-flipping move with a deterministic domain found (proved only for fixed classical chains); no closed formula for Σχ; Vinogradov's least-QNR
  trick does not transfer (A-set of X_p not closed under any Euclid/product step). Every construction again reduces to
  "a divisor of tp + 1 in the class −1 mod t with a prescribed character" (H-A/B2).

## Barrier steering (what each attempt violated)
* Fixed slice sets / congruence (B1): moves defined uniformly are cell maps; flips need arithmetic domains (§2.3).
* "Leave X_n through composites": χ is n-free (Cor 1.4a), so composites give nothing per se; flips occur only through even
  determinants or odd-letter rotations, closing up at the same n by coincidence (§2.1–2.2).
* Algebraic/lattice moves (Kneser neighbours, similarity, Clifford): preserve the rational class, hence β, hence χ (Cor 1.4c).
  To flip one must change the quaternion algebra B_{2,∞} ↔ B_{p,∞}, i.e. produce B_{2,p}-data = a non-residue mod p.

## Sparks (not pursued)
* **Supersingular parallel.** For p ≡ 1 (mod 12) no supersingular curve with small CM exists a priori; constructing one
  needs D with (−D/p) = −1 (Bröker, GRH). ES's hard classes p ≡ □ (mod 840) are exactly where all small CM fields split.
  A certificate word hands over an explicit order of reduced discriminant 4p in B_{p,∞}. Is there a Deuring-side object
  (a supersingular curve over F_p with a specific 2-power level structure) whose existence is *unconditional* and which
  yields a path-shaped Gorenstein order? (Would need a deterministic supersingular construction — likely as hard.)
* Even-determinant intermediates are where the 2-adic class is free: study X_{2n} words with even outer letters
  (scaling by 2) and rotations there as a controlled flip channel.
* The cell-level odd groupoid (29 components on 320 cells) — classify the invariant g; it might be a Hasse invariant of the
  binary form of γ (trace T² − 4).
* SQ₅ as integral SA with BM on a Markoff-type cubic: compare with Loughran–Mitankin / Colliot-Thélène–Wei–Xu for Markoff
  surfaces; is X_n's Br(X_n)/Br(ℚ) generated by β? (not computed).

## Self-review (R-O198, deep reviewer) — all accepted and applied in CHI_FLIP.md
Thm 1.1 proof gap at ℓ ∤ n fixed; census wording ("not identically +1"; χ ≡ −1 at 38 n ≡ 3 mod 4); SA → existence-with-
congruence; odd-groupoid seed bug (278 014 components, flips unchanged); §2.3 scope narrowed; blanket "no move flips" removed
(rotation flips, changing n); q = 2 and q = 17 added in §3.1; counts (9 924 prime-n words; Ω₂ = 60 cells per class mod 8).
**For the parent (files outside my remit, from the main merge):** the reviewer flagged MODEL_SPECIFIC.md:259 (an aside
inferring pointwise failure from a log²p average — should be deleted) and DISCOVERIES.md:848 ("first T1-bearing ES analogue
with non-BM failures" overclaims vs the known 8/n example), and the "χ non-constant" wording in (J)32/C1 (DISCOVERIES.md:861).
