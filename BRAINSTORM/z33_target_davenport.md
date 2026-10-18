# z33_target_davenport — zero-sum with target −1: how many escaping factors would be needed (O263; §4)

**Idea.** In an abelian group, long sequences have zero-sum subsequences (Davenport). Want: enough forced factors outside
every subgroup H ∌ −1 ⟹ a subset product −1.
**Literature.** Davenport constant; Olson; Kneser (LONGSHOT_PIGEONHOLE Prop 1.4); ±-weighted Davenport (Adhikari et al.).
**Result (PROVED).** Target constant η(G) := sup over −1-free sequences of min_H #(escapers). Lemma 4.1: an element x of
order 2n (n odd) with x^n = −1 gives η ≥ n − 1 (n − 1 copies of x^{±1}); for t = 4q, q ≡ 3 (4) prime, η ≥ (q − 3)/2. Prop 4.2:
the forced supply of escaping LARGE factors in one N is ≤ 1 per subgroup (0 for ker χ₋₄ on the b = 1 line), and large primes
are private to one N (Lemma 2.3, SYNTHESIS_SPARKS8), so no pooling across levels. Hence zero-sum forcing only works where
η(G) = 0, i.e. exponent-2 levels t | 24.
**Barrier screen.** B2 (single integer), B4 (pigeonhole/covering by small primes), (J)64 cap: η is the multiplicity gap
between ⟨S⟩ (cap relaxation) and Σ(S) (ES).
**Assessment.** Davenport cannot convert parity forcing into class forcing; at best it reproduces the exponent-2 shadow.
