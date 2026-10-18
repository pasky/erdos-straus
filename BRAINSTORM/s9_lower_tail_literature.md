# s9_lower_tail_literature — which theorems prove r(n) ≥ 1 for EVERY n when the main term is only polylog? (O271, mandatory (i))

## Idea
ES at p is now (O268 Thm 2.2, merged as (J)100) a lower-tail statement R(p) ≥ ε·M_BM(p) with M_BM ≍ (log p)². Map the literature
for every-n existence theorems whose expected representation count is polylogarithmic, and classify their mechanism with the
(J)94 input list (M1a power final count, M1b power auxiliary set + pigeonhole, M2 fixed-modulus group event, M3 homogeneity /
group action, M4 free choice of objects, M5 count congruence).

## Literature (precise refs; ✓ = statement checked by web search in this task; unmarked = from memory / repo citations, not re-checked)
| statement | typical r(n) | every n? | mechanism |
|---|---|---|---|
| Erdős–Tetali, *Representations of integers as the sum of k terms*, Random Struct. Alg. 1 (1990) 245–261 ✓: ∃ basis of order k with r(n) ≍ log n | log n | yes (for the constructed set) | M4: the SET is chosen (probabilistic method, Chernoff + union bound over n ≤ x; the union bound needs exponent > log n, available because the designer picks the set) |
| Kolountzakis, *An effective additive basis for the integers*, Discrete Math. 145 (1995) | log n | yes | M4, derandomised |
| binary / Zeckendorf / complete sequences (Brown's criterion) | 1 | yes | M3 (greedy / induction) |
| Graham 1963: every n > 77 is a sum of distinct integers with reciprocal sum 1 | — | yes | M3/M4 (induction with free choice) |
| Romanov n = p + 2^k | ≍ 1 | **no**: Erdős 1950 covering congruences, an AP of odd exceptions | structured (covering) exceptions |
| n = p + 2^a + 2^b | ≍ log n | **no**: Crocker, Pacific J. Math. 36 (1971) 103–107 ✓ (infinitely many odd exceptions); Pan, Acta Arith. 148 (2011) 55–61 ✓: ≫ x^{1−ε} odd exceptions ≤ x | structured exceptions of almost full power count |
| Linnik's problem n = p₁ + p₂ + 2^{a₁} + … + 2^{a_K} (Pintz–Ruzsa, K = 8) | n/log²n·(log n)^K | yes | M1a (two primes: power main term) |
| n = p + x² + y² (Linnik 1960, dispersion; Hooley under GRH) | ≍ n/… (power) | yes | M1a |
| n = p + (k-free) (Estermann 1931) | power | yes | M1a |
| ternary forms, Duke–Schulze-Pillot, Invent. Math. 99 (1990) | n^{1/2} | yes (large n, spinor-genus admissible) | M1a + spinor (genus) layer |
| Markoff-type x² + y² + z² − xyz = k (Ghosh–Sarnak, Invent. Math. 229 (2022)) ✓ (R282) | (log k)² on average = number of ORBITS of the Markoff group (GS §7; each orbit infinite; R282 repair) | **no**: infinitely many integral Hasse failures; many explained by reciprocity (Loughran–Mitankin; Colliot-Thélène–Wei–Xu) | structured exceptions at ES's own scale |
| Erdős–Turán conjecture (r(n) ≥ 1 ∀ n ⇒ r unbounded) | — | open | (shows the theory of thin bases is about designed sets) |
| Bloom 2021 (positive-density sets contain unit-fraction sums = 1), Croot 2003 | — | density statements, not every n | M1a-type density |

## Barrier screen
B6/Lemma 3.2 of SYNTHESIS_SPARKS9: a counting proof at polylog scale must have a large-deviation exponent > log n. Erdős–Tetali
gets it only because M4 lets the designer discard bad sets. Every natural polylog problem in the table that is not designed has
structured exception sets (covering congruences, reciprocity). T1 is ES's analogue; BL Thm 1.8 says ES has no BM-type
obstruction at n ≥ 2, and SYNTHESIS_SPARKS9 Prop 2.2 says the level-BM layer is free at every non-square, so ES is NOT a
reciprocity-obstructed problem beyond squares; but no theorem proves the lower tail for any natural fixed set at this scale.

## Cheap numerics
None needed (literature). The p + 2^a + 2^b analogy is quantitative: there the main term is ≍ log n and exceptions have count
≫ x^{1−ε} (Pan) because covering congruences act on a FIXED set {2^a}; ES's sets move with n (B2), so covering arguments only
give the T1/shadow obstructions ((J)97 Prop 3.1).

## Assessment
**No theorem known to us proves r(n) ≥ 1 for every n (of a natural, non-designed problem) when the main term is polylog.**
Positive every-n theorems at polylog scale are designed (M4) or structural (M3); natural problems at that scale (Romanov,
p + 2^a + 2^b, Markoff) have infinitely many structured exceptions. Goldbach-type and Linnik-type every-n theorems all have
power main terms (M1a). Label: literature map (Assessment). Steering: an ES proof must be structural (M2/M3/M5-type) at the
class layer, or a new kind of lower-tail theorem with exponent > log p.
