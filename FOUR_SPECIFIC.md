# FOUR_SPECIFIC — hunting 4-specific inputs after the numerator-blindness barrier (task O212, spark relay Y4)

Builds on SYNTHESIS_SPARKS3 (O208; R207 repair: the "must be 4-specific" reading is an Assessment, since thresholds
n > n₀(M) are not excluded by finitely many failures; threshold-robust form via Pomerance–Weingartner Thm 1.2),
MODEL_SPECIFIC (J)32, CHI_FLIP (J)33. Memos: `BRAINSTORM/y4_*.md`; scripts `scripts/y4_*`.
**ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.

## 0. Iteration log (construction → kill → hypothesis → modification)
(Y1) *Which numerators are blind?* O208 Thm 1.1 used (−M/g) = −1 for g ≡ −1 (M). This holds exactly for M ≡ 0, 3 (mod 4)
(−M a discriminant), §1. Result: T1 is not 4-specific; 7 is a T1-bearing, failure-free sibling. It becomes the control
for every candidate (§5).
(Y2) *One-odd SQ₅.* ES = 8/n ⊔ one-odd. On the five slices the parity is v₂ of the slot (§2). "S₄^{odd}(p) ≠ ∅" holds at
every prime ≤ 10⁷, while S₈ fails 27 times. Kill: it is false at composites (321, 4545, …), where SQ₅ holds, and it has
no 2-adic lattice meaning (§2.3). Hypothesis violated: none; it is strictly harder than SQ₅. Modification: none worth it.
(Y3) *Genus of path forms as a deterministic mechanism* (certificate ⟺ Q_w ℚ₂-isotropic ⟺ Q_w in the "B_{p,∞}" genus).
Kill: already bsA_selling_sandpile D3. The genus has ≍ p classes, only ≍ log²p of which are path forms (B3).
(Y4) *Universal witnesses.* Can a single slot value A serve all of its χ = −1 classes? Exactly for
A ∈ {2, 3, 5, 7, 8, 15, 20}, and their reach is exactly Mordell's 840 (§4, PROVED). Hypothesis of B1 (a finite menu)
satisfied, hence the ceiling. Modification: let A grow. This gives the τ(A+1)/φ(A) lottery (B2).
(Y5) *First lottery.* 4 is the unique M ≥ 3 with a {±1}-unit-group slice (e ∈ {1, 3}) at every prime (§3, PROVED).
For p ≡ 1 (mod 12) both e = 3 slices are empty 9.1% of the time (p < 10⁶): not deterministic. Modification: combine
with the χ-fibre. The e = 3 slices are a sub-union of the χ = −1 words at t = 3 and t = 1 (§3.2), so nothing new.
(Y6) *Harness on the hatches* (§6). All are uniform skeletons with a lottery content. Only the χ-fibre passes as a
stated 4-specific input.

## 1. T1-bearing numerators (PROVED; BRAINSTORM/y4_t1_numerators, `scripts/y4_t1_numerators.py`)
**Prop 1.1.** For M ≥ 3, (−M/g) = −1 for all odd g ≡ −1 (mod M) ⟺ M ≡ 0, 3 (mod 4). Hence (Cor 1.2): the
M-shot relaxation M^□ is a theorem at every odd non-square prime to M for every M ≥ 3 (Dirichlet); its odd-g shot family
has T1 exactly when M ≡ 0, 3 (mod 4) (even g sneak in iff M ≡ 3 mod 8); for M ≡ 1, 2 (mod 4) the relaxation holds at
squares too. Checked for M = 3..24 (odd squares k ≤ 99, Q ≤ 40) and at every census failure (exact certificates).
New harness entry: **11/37** (non-trivial: 11/37 < 3), `11/37 = 1/8 + 1/148 + 49/296`.
T1-bearing and failure-free to 10⁸: **3 (trivial), 4, 7**.
