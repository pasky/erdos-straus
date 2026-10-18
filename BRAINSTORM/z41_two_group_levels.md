# z41_two_group_levels — levels t = 2^k·F with (ℤ/t)^× a 2-group (O272; §5)

**Idea.** If the 2-power ladder were free, the ES event at 2-group levels would be forced. Independently of reciprocity: do the
O(log n) 2-group levels suffice for every non-square n?
**Literature.** Fermat primes (only 3, 5, 17, 257, 65537 known); Yamamoto-type quadratic obstructions (twisted squares).
**Result.** Lemma 1.1: at a fixed level the event is ⋃_a {n ≡ −a (ta − 1)} (B1). Lemma 5.1 (PROVED): n = D m² has no word at
any level 4D | t (χ_{−t/D} is trivial on all divisors). EVIDENCE: 169 T2 levels ≤ 10⁶; 20 325 odd non-squares and 1 298 primes
≤ 10⁶ (largest 999 979) have no T2 word, of which 1 180 primes have (★) words elsewhere; failure rate per decade
0.217 → 0.069 → 0.029 → 0.0136.
**Barrier screen.** B1 (fixed level sets), B2. T1: 0 squares with a T2 word. Numerator 8: 131, 241 have no 8 | t word.
**Cheap numerics.** `scripts/z41_two_group.py` (exact certificates), `scripts/z41_twisted_levels.py`.
**Assessment.** EVIDENCE (negative): 2-group levels do not suffice; the decreasing failure rate matches ≍ log n expected T2
hits (Assessment), still infinitely many failures expected.
