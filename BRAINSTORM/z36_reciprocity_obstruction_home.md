# z36 — T1 is a Rickards–Stange reciprocity obstruction (truncated to length 3) (O266 memo 7) — SHARP candidate

## Idea
Find the published thin-orbit object whose obstruction has the same source as T1 and whose positive side is a theorem.
Details and dictionary table: ZAREMBA_TRANSFER.md §5.

## Literature
Rickards–Stange, arXiv:2401.01860v3, Duke Math. J. 2025 (read: Def 2.1, Prop 2.2, Def 2.4, Thms 2.5, 2.6, 2.8, 2.10,
2.18, 2.20, Conj 2.14, 2.15, 2.22, §4 Lemmas 4.1, 4.3; excerpts in sources/lit2026g/rickards_stange.txt). Background:
HKRS (Apollonian, campaign memo apollonian_reciprocity); DEDEKIND_ES Cor 4.1, Prop 3.1, Thm 4.5, §4.4.

## Content
* Same source: Kronecker/Jacobi symbol invariant under Euclid/CF moves (RS Prop 3.2 ↔ DEDEKIND Cor 4.1).
* Same obstruction: "symbol −1 ⇒ never a square" (RS Thm 2.5 ↔ DEDEKIND Prop 3.1/Thm 4.5 = T1 on the five slices).
* Same conjectural shape: "every non-square beyond an explicit bound" (RS Conj 2.15: n > 10569; Conj 2.22:
  v > 7.97·10¹²; ES slices DEDEKIND 4.4: n > 28225).
* Different dimension: RS orbits have δ ∈ (1/2, 1]; ES-five is length 3 (δ = 1/2 critical in counting terms, dimension 0 as a
  set). RS's *proved* case (Ψ, δ = 1) uses a fat linear family + Pólya–Vinogradov (M1⁺ + long character sum).
* RS Thm 2.20 refutes BK's alphabet local–global conjecture ⇒ the growth/gluing method cannot extend to congruence-restricted
  alphabets without controlling the middle window (where the Kronecker information lives) and without a main term that
  vanishes at squares. Question R (ZAREMBA_TRANSFER §5.3).

## Barrier screen
T1: this *is* the T1 mechanism, recognised in the literature as a new obstruction class (not BM, not congruence; RS
Prop 2.7: not inherited from Γ₁(4)). B2/B3: the positive side needs a line (fat family) where ES has a hyperbola.
B6: RS's results are pointwise (effective), so the analogy is pointwise-to-pointwise.

## Cheap numerics
None new (ES side: DEDEKIND scripts dk_vanish.py, dk_thm45_check.py; RS side: their PARI code [Ric23]).

## Assessment
Dictionary (PROVED on each side; the correspondence is an Assessment, no new theorem). SHARP for the campaign's map: it
places T1 in a published 2024–25 obstruction class for continued-fraction semigroups, gives a proved model case
(RS Thm 2.8: "all but squares and 15 sporadic values") of exactly ES's conjectured shape, and identifies the minimal
open problem (Question R) where growth methods would have to learn reciprocity.
