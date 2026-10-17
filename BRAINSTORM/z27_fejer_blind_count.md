# z27_fejer_blind_count — the class-blind count of pretentious primes, and the P-loss in exact form (O256)

**Idea.** Count primes q ∈ (x/2, x] having a large-order character ψ with 𝔻_S(ψ) < ε by Fejér-weighted collision pairs of
the S-unit box: a pretentious ψ squeezes g^{Box} into ≤ N(2B+1)ε elements, forcing ≥ (B+1)^{2k}/(N(2B+1)ε) collisions; each
relation h is charged with the ≤ 2B log P/log x primes dividing N_h.
**Result (PROVED, BALANCED_LATTICE Prop 3.1).** #Bad₁(ε) ∩ (x/2, x] ≤ 48(6xε)^{(k+1)/(k−1)} log P/log(x/2) — no 2^k/6^k factor
(the Fejér weight w(h) = ∏(B+1−|h_s|)₊ sums to (B+1)^{2k}). Excluding Bad₁ from ONE class mod 8P forces
ε ≍ x^{−2/(k+1)}(P log P)^{−(k−1)/(k+1)}, i.e. L ≳ P^{1−o(1)}: the P-loss, which reproduces CAP_INTERPOLATION Thm 4.2(b)
exp(O(√(log₂p log₃p))) in dual language (Cor 3.3). Not a GRH barrier — a limit of class-blind counting (cf. R264 D8).
**Literature.** PHASE_DIAGRAM Step 2 / CAP_INTERPOLATION Thm 4.2(iv) (same count, primal, with 6^k); Erdős–Murty type counts of
primes with small order (rank 1). Corvaja–Zannier gcd(u−1, v−1) bounds (subspace theorem) would save only a factor ε in a
rank-2 count — not the x^{−1} per extra rank the random model predicts.
**Barrier screen.** B6 in its sharpest form: the bound is an average over q with no class information.
**Cheap numerics.** n/a (identity-level; the bound is far from the truth: random model gives #Bad₁ ≈ x²(2ε)^k/(2k! log x)).
**Assessment.** PROVED (bound) + Assessment (the P-loss is intrinsic to any class-blind upper bound: it cannot see a set of
relative density 1/φ(8P)).
