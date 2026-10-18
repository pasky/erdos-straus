# z36 — T1 is a Rickards–Stange reciprocity obstruction (truncated to length 3) (O266 memo 7) — SHARP candidate (R276 repair D3: one row exact, the rest analogy)

## Idea
Find the published thin-orbit object whose obstruction has the same source as T1 and whose positive side is a theorem.
Details and dictionary table: ZAREMBA_TRANSFER.md §5.

## Literature
Rickards–Stange, arXiv:2401.01860v3, Duke Math. J. 2025 (read: Def 2.1, Prop 2.2, Def 2.4, Thms 2.5, 2.6, 2.8, 2.10,
2.18, 2.20, Conj 2.14, 2.15, 2.22, §4 Lemmas 4.1, 4.3; excerpts in sources/lit2026g/rickards_stange.txt). Background:
HKRS (Apollonian, campaign memo apollonian_reciprocity); DEDEKIND_ES Cor 4.1, Prop 3.1, Thm 4.5, §4.4.

## Content
* **Exact (PROVED, R276):** the ES slice numerator sets exhibit a reciprocity obstruction in the sense of RS Def 2.4:
  X_T = {n ≡ 1 (4) : n = tuv − u − v, 4 | t} has no square (Prop 3.1) yet meets 1 mod m for every m
  ((t, u, v) = (4, 4m − 1, 4m) gives n ≡ 1 (mod 8m)); same for the 4 | A slice with (3, 8m − 1, 8m). Caveat: Def 2.4 is
  stated for semigroup orbits; the length-3 slice set is not known to be one. Closest RS analogue: Thm 2.18 / Cor 2.19.
* Analogy (Assessment): same mechanism — Jacobi reciprocity along Euclid/CF moves (RS Prop 3.2 ↔ DEDEKIND Cor 4.1);
  neither statement implies the other.
* Analogy (Assessment): conjectural shape "every non-square beyond an explicit bound" — RS Conj 2.14/2.15 (n > 10569),
  Conj 2.22 (v > 7.97·10¹²) ↔ DEDEKIND 4.4 CONJECTURE (n > 28225). (RS Thm 2.8 is the PROVED fat-orbit case, not the
  label-matched counterpart.)
* Exponent: RS orbits have δ ∈ (1/2, 1]; the length-3 words number ≍ X log² X up to X, i.e. δ = 1/2 exactly (the BK
  threshold) in BK normalisation. RS's *proved* case (Ψ, δ = 1) uses a fat linear family + Pólya–Vinogradov (M1⁺ + long character sum).
* RS Thm 2.20 refutes BK's alphabet local–global conjecture. 4ℤ⁺ alphabets have δ bounded away from 1, so the growth
  method's counting step cannot apply to them at all (R276 D9); beyond that it could not handle congruence-restricted
  alphabets without controlling the middle window (where the Kronecker information lives) and without a main term that
  vanishes at squares. Question R (ZAREMBA_TRANSFER §5.3).

## Barrier screen
T1: this *is* the T1 mechanism, recognised in the literature as a new obstruction class (not BM, not congruence; RS
Prop 2.7: not inherited from Γ₁(4)). B2/B3: the positive side needs a line (fat family) where ES has a hyperbola.
B6: RS's results are pointwise (effective), so the analogy is pointwise-to-pointwise.

## Cheap numerics
None new (ES side: DEDEKIND scripts dk_vanish.py, dk_thm45_check.py; RS side: their PARI code [Ric23]).

## Assessment
Row "Def 2.4" PROVED (R276); the remaining correspondence is an Assessment. Value for the campaign's map: it places T1
in a published 2024–25 obstruction class for continued-fraction semigroups (in the exact Def-2.4 sense), gives a proved
fat-orbit model (RS Thm 2.8: "all but squares and 15 sporadic values") of ES's conjectured shape, and identifies the minimal
open problem (Question R) where growth methods would have to learn reciprocity.
