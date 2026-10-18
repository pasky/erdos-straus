# B2_ACROSS_FIELDS — is B2 equivalent to a solved / deeply studied problem in another field? (task O261, wide net)

Status: checkpoint 0 (skeleton). **ES is not solved here or anywhere.** Labels as in DISCOVERIES.md (PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment). External theorems are "Cited" only if their statement was read in the source
(abstract or excerpt in `sources/lit2026g/`); "(memory)" marks anything recalled but not re-read. Field memos:
`BRAINSTORM/z31_*.md`. Builds on (and does not repeat) LITERATURE_2026.md, LITERATURE_AUTOMORPHIC.md, PARITY_AUDIT.md ((J)87),
SYNTHESIS_SPARKS8.md ((J)89), BRAINSTORM/thin_group_orbits.md, farey_ford_cf.md, logic_divisibility_lgp.md,
gon_lll_relation_lattice.md, s6_divisor_pigeonhole.md, MARKOFF_ES.md.

## 0. Iteration log
* cp0: B2 forms checked against the source files (§1); feature list (§2); field plan.

## 1. B2 in its precise forms (checked against the files named)

Fix a prime p ≡ 1 (mod 4).
* **(E1) c = 1 line (★)** (PARITY_AUDIT §0, (J)6): ∃ C, u, B ≥ 1 with 4uBC − u − B = p; equivalently ∃ C: 4Cp + 1 has a
  divisor ≡ −1 (mod 4C). Heuristic count R(p) ≈ (log p)²/8 (EVIDENCE: 44, 52, 68 at p ≈ 10⁸, 10⁹, 10¹⁰). Fails at exactly 14
  primes ≤ 10¹⁰ ((J)90).
* **(E2) b = 1 line** (SYNTHESIS_SPARKS8 Prop 1.3, B1_LINE.md; López 2404.01508 Thm 7 "Type A"): ∃ d ≥ 1: p + 4d has a divisor
  w ≡ −1 (mod 4d), w ≠ p + 4d. Fails at 193, 2521, 66529 and at no other prime ≤ 10¹¹ ((J)90).
* **(E3) window form** (CAP_POINTWISE §1, FORCED_WINDOW Prop 2.1, PARITY_AUDIT event (b)): for a prime q ≡ 3 (4), q ≡ 4 − p (8),
  (q/p) = −1, K := (p + q)/4: ES holds at window q (cap 0) iff Rat_q(K) ∩ {−1, −p} ≠ ∅, where Rat_q(K) = {u/v mod q : uv | K,
  gcd(u, v) = 1} (the brief's "Σ_q(K)"). Least-residue form (FORCED_WINDOW Prop 2.1): ES-Type-II(p) ⟺ ∃ coprime (u, v) with
  (−p mod 4uv) | u + v (prime to p).
* **(E4) lattice form** (ASTRA_BRIDGE Thm 3.4(c), (J)81): for g ≡ 3 (4), gcd(g, p) = 1, h = (g + 1)/4, ρ² ≡ −p (mod g),
  L_ρ(g) = {(M, Y) : Y ≡ ρM (mod g)}; ES shots with modulus g ⟷ points (2k, 1) ∈ L_ρ(g) with k | h, i.e. g | 4k²p + 1 with
  4k | g + 1.
* **(E5) twisted hyperbola** (SYNTHESIS_SPARKS8 Prop 1.5): ES-Type-II(p) ⟺ ∃ u ≥ 1 and (X, ε) with Xε ≡ u (mod p), height
  c = (Xε − u)/p ≥ 1, X ≡ −1 (mod 4cu). Kloosterman-fraction form: X̄/(4p) within ≍ 1/(uX) of 1/(4u) (§1.7 there).
* **(E6) integral points** on the affine cubic surface U_n : 4xyz = n(xy + yz + zx) in the positive octant (Bright–Loughran,
  arXiv:1908.02526, `sources/bright-loughran-1908.02526.pdf`); Br U_n/Br ℚ ≅ ℤ/2 (BL Thm 1.6), no BM obstruction to existence
  of positive points (BL Thm 1.8), BM does not control strong approximation (BL Thm 1.9).

## 2. Structural features a counterpart must match (the "fingerprint")
F1 single fixed integer p (pointwise, not almost-all);
F2 polylogarithmic expected count ≍ (log p)²–(log p)³ (no power-size main term);
F3 tied modulus: the residue-class modulus is part of the solution (height-dependent target);
F4 no local obstruction at primes (T1: odd squares kill only the Type I/II *shapes*);
F5 4-specific: the numerator-8 analogue of the event fails (131, 241);
F6 class-group / genus data see only the quadratic-character shadow (WINDMILL_REDUCTION Prop 10.3).

## 3. Field-by-field verdicts (table filled in as memos are completed)

| # | field | counterpart | pointwise proved? mechanism | blocked by | verdict | memo |
|---|---|---|---|---|---|---|

## 4. Deep items (Zaremba; Markoff/Chen; Duke; Bloom)

## 5. Synthesis and verdict
