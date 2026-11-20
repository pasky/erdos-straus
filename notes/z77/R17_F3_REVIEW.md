Result: Independent Opus review found no fatal or major issue with the sufficient threshold r ≥ 7219. Label: Assessment (internal hostile review; full replay and independent checks)
Scope: SE/ZL input dependencies, libm assumption and un-rechecked high rows as in the author note; not an external review or an integer ES result.
Review: cross-model (this record of `functions.review`, smart mode, `anthropic/claude-opus-5-5`, range `7e39f7e70..c6abb8e7c`)
Triage: DATA
STATUS delta: none beyond the author note

## Review record (summarised by the lane)

**Verdict.** “I found no fatal or major error. The integer theorem in `notes/z77/R17_F3.md` (sterile r-generic points for every prime r ≥ 7219) holds up under full replay, an independent re-implementation of the combiner and independent brute-force checks.” The reviewer also accepted the orientation-A necessary condition in `F3_TARGET.md`.

The reviewer replayed every certificate step with byte-identical tables. A separate rational combiner reading the same tables gave no failures on the claimed prime range, worst ≈0.4965176 at 7219, and failure ≈0.500905 at 7213. The r³ sieve was the winning P₃ bound throughout its range on the theorem interval; the fine bound won for 753 primes at K=5. The SE Q table always won. The reviewer checked the inversion and unit tests, cube compression, small-side lemma, τ interval estimates, row divisibility in the determinant, reversed progression step length and lower cofactor bound, truncations and tail cutoffs.

Separate code counted all level-1 cells at 17, 7213, 7219, 50021 and 177839. A separate cube sieve matched at 17,19,23,101,1009,2003; a brute enumeration at primes 17 through 37 checked the per-shift and integer-centre lemmas. A random cap test against true divisor lists had zero violations in 44,215 tests. The large-shift bound was compared to brute enumeration at 1021³. See `scripts/z77_review_{combine,level1,brute,large}.py`. This does not amount to independent exhaustive regeneration of the underlying SE/ZL tables or a second independent exact level-1 implementation run on the entire interval above 20000.

**Repairs applied.** Reported the narrow margin, gain from the pooled τ bound versus the cofactor determinant, dependence on Q₃, and level-1 cross-check coverage. Added complete proposed master deltas (not master edits) and an old-budget replay. Restated the F₃[T] lemma with its full lower endpoint and derived empty case-2 windows, corrected citations, kept the function-field item out of STATUS. These edits do not change the certificate or the threshold.
