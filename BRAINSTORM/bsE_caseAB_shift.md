# bsE_caseAB_shift — #Case A(α) = #Case B(α + 1) at slice points? (O178)

## Idea
Exhaustive counts over the c-slices (q = 3): Case B tuples per s = 4, 5, 6, 7 are 2, 4, 10, 8. Case A tuples per α = 3, 4, 5, 6 are
2, 4, 10, 8. For q = 5 both vanish for s ≤ 5 / α ≤ 4. This suggests a bijection Case A(α) ↔ Case B(α + 1), presumably a type swap
a ↔ X/a. Both are representations of a power of T by a "cfg − c − f" cubic (DEPTH_ASPECT Lemmas 2.1, 2.3).
## Literature
FUNCTIONFIELD_ES §6.2 (types), ET §2 (the involutions between Σ^I and Σ^II charts).
## Barrier screen
Structural only. It would halve the counting work and explain why both exponents are ≤ 1/2.
## Cheap numerics
`scripts/bsE_caseA.py` vs `scripts/bsE_famcount.c` (data in DEPTH_ASPECT §4). α = 7, 8 (q = 3) and q = 5, α ≥ 5 were still running at
checkpoint.
## Assessment
CONJECTURE (EVIDENCE on 4 + 2 data points). Cheap to test further.
