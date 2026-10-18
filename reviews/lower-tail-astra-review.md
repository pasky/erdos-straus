# R285 — hostile review of O275 (LOWER_TAIL_ASTRA.md, GPT-Astra lower-tail attack)

Reviewer: R285 side agent, branch `side-agent/review-tail-astra` (merged `side-agent/lower-tail-astra` at dbb88f9b-era head).
Scope: LOWER_TAIL_ASTRA.md §§1–6, BRAINSTORM/z43_astra_word_forest.md, AGENT_REPORT_O275.md, the author's self-review.
Every lemma was re-derived by hand; all numerics were recomputed with reviewer-written code that does not reuse
`z43_astra_*`:

* `scripts/review_lta_forest.c` (C, `gcc -O2 … -lm`; run `review_lta_forest 1000000 200000`, ≈11 s, one core,
  `ulimit -v 8000000`; output `logs/review_lta_forest_1e6.txt`). Edges by divisor enumeration of n+u for u with
  (u−1)u ≤ n+1; checks (per edge) unique parent, parent = (−n mod v), acyclicity by union–find, word identity,
  unit endpoints at primes, (A/n) = χ(u)χ(v), (A*/n) = (A/n), and (A/n) = −1 ⟺ five 2-adic conditions; and, for every
  odd prime/odd square ≤ 2·10⁵ (18 206 inputs), an **edge-by-edge** comparison with the O(n) residue-parent scan
  v = 2..n+2, r = −n mod v.
* `scripts/review_lta_counts.py` (sympy): O(n) scan vs divisor scan for all odd n ≤ 2000; edge totals.
* `scripts/review_lta_fixtures.py` (sympy): exhaustive component BFS (neighbours of x = divisors v of n+x with
  xv | n+x+v) for the Thm 3.1, 3.2, 5.1 and Prop 4.2 families.

## Summary verdicts

| Claim | Verdict |
|---|---|
| Lemma 2.1 (forest, unique parent −n mod v, vertex bound, diagonal words) | **SOUND** |
| Lemma 2.2 (sign = χ(u)χ(v); bichromatic ⟺ five-slice for n ≡ 1 (4), unit endpoints) | **SOUND** (sign identity and five-slice equivalence imported, correctly cited) |
| Thm 3.1 (four forms ⇒ closed 8-vertex all-residue component of 1) | **SOUND** (one MINOR wording point, D1) |
| Thm 3.2 (fixed finite roots fail; CONDITIONAL on Dickson) | **SOUND** |
| Lemma 4.1 (continued-fraction recurrence, Fibonacci growth) | **SOUND** |
| Prop 4.2 (arbitrarily long all-residue paths, Dirichlet) | **SOUND** (MINOR wording, D2) |
| Thm 5.1 (p = 2521+9240a, q = 211+770a: ℓ(p) = 11 isolated) | **SOUND** |
| §6 census figures | **SOUND** — every figure reproduced exactly |
| Novelty / attribution | **SOUND-AFTER-REPAIRS** (D4, D5) |
| Labels | **SOUND** |

No FATAL or MAJOR defect. Details follow claim by claim.
