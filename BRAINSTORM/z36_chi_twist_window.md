# z36 — Can the Zaremba method be twisted by the quadratic character? (O266 memo 4)

## Idea
Every rung of the ES ladder needs a non-residue. Ask what it takes to get "Zaremba with a non-residue" (Hypothesis ZQ_M)
from the 2026 machinery, and where T1 must enter. Details: ZAREMBA_TRANSFER.md §4.

## Literature
Shk (151) ε < 1/18 (gluing intervals of length < q^{1/9}); Burgess (character sums nontrivial on intervals ≥ q^{1/4+δ},
from memory); Zhang Thm 1.2 (all q, squares included); Shk Lemma 10 (x|y| characterisation of bounded digits).

## Content
1. **Window conflict (Assessment).** χ-information enters only through the gluing intervals of length N = q^{2ε}, ε < 1/18;
   Burgess needs ε > 1/8 — incompatible for a per-interval input; averaged character-sum inputs over the intervals
   (moments, large sieve) are not excluded by this argument (R276 repair D7). A uniform "non-residue in every interval of length q^{1/9}" would beat Burgess for n_p.
2. **T1 location (PROVED as a logical remark).** Zaremba holds at q = m² (Zhang), ZQ fails at q = m²; hence no argument
   using only growth in SL₂(ℤ/q) proves ZQ. The extra input must fail at squares (Jacobi-symbol cancellation), and it must
   act on the glued set A ∩ B^{−1}: the χ-value of a glued numerator depends on the middle window, not on half-set data.
3. **Multiplier reduction (PROVED, conditional on the preprints for Zaremba(M)).** c·Z_M(q) ⊆ Z_{4cM}(q) (Lemma 10), so
   Zaremba(M) ⟹ ZQ_{4Mn_p}. Pointwise useless (n_p ≪ p^{0.152}); under GRH λ ≪ M log³ p, worse than Theorem A.
4. **What ZQ would buy (Theorem B).** λ(p) ≪ M log p versus λ(p) ≪ log p log log p unconditionally (Theorem A): a log log
   factor.

## Barrier screen
T1: correctly located (step 2). B3: ZQ is a density-1/2-type rung only after the log log saving; ES needs L = 3.
B6: not involved.

## Cheap numerics (`scripts/z36_zq.py`)
ZQ₄ for all primes 7 ≤ p < 2·10⁴ (ZQ₃ except p = 277); ZQ₃ in windows at 10⁵ and 10⁶. The non-residue restriction never pushes the minimum above 3 except at 277
(2 → 4), but raises it 2 → 3 at 357 of the 2259 primes < 2·10⁴, e.g. p = 43 (R276 repair D5: earlier "costs nothing" was false).

## Assessment
CONJECTURE (ZQ, EVIDENCE as above) + Assessment. Open sub-question worth a line in the ledger: *is there a non-residue
with bounded partial quotients for every large prime?* — the χ-twisted Zaremba problem; neither 2026 preprint addresses it.
