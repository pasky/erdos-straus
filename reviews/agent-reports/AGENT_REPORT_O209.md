# AGENT_REPORT_O209 — spark relay Y1: the two bad fibres of X₀(2p), words as hyperbolic SL₂(ℤ) matrices (checkpoint 1)

Branch side-agent/two-fibres (merged side-agent/sign-identity first). Deep file TWO_FIBRES.md; memos BRAINSTORM/y1_*.md
(6, indexed in BRAINSTORM/README.md); scripts `scripts/y1_*`. **ES is not solved, nor any infinite case of it.**

## SHARP:
1. **The χ = +1 fibre is the cubic lattice ℤ³ (TWO_FIBRES Thm A, PROVED from class number one of B_{2,∞} and of the
   genus of I₃).** For every odd n and word w: Diff(T_w) = {2} ⟺ **n·G_w is a Gram matrix of three integer vectors** ⟺
   ∃ x, y ∈ ℤ³ with |x|² = tv − 1, |y|² = tu − 1, x·y = 1 (and x × y ≡ x + y mod t). For p prime the χ = +1 lattices
   are L_ℓ = {x ≡ λℓ mod p} on the conic x² + y² + z² ≡ 0, i.e. 𝔊⁺_p is the image of P¹(𝔽_p)/S₄ (onto, not always injective:
   p = 109) — Cerednik–Drinfeld's char-2 tree made explicit. Hence **ES-five(p) ⟺ some p·G_w is NOT a Gram matrix in ℤ³** (equivalently some path binary [[tv−1,1],[1,tu−1]]
   of det tp is not represented by x² + y² + z²). **T1 becomes an embedding (Thm B): every path lattice of odd square
   determinant m² is an index-m sublattice of ℤ³** (for m = q prime: ker(f mod q) with f off the conic). Checked: all
   81 857 words of odd n ≤ 3001, all 121 815 words of primes ≤ 12 000 and all 12 053 words of primes in (99 000, 10⁵] (Thm A is PROVED; these are consistency checks — the per-word lift search is
   too slow for primes near 10⁶), all 8 073 words of odd squares ≤ 10⁵, 0 mismatches.
   Why it matters: it is the first explicit *asymmetry* between the two signs (exact class-number-one world on one side).
   Honest limit: at the level of single words it gives only the 2-adic cell law (TWO_FIBRES §3.1), and the sign-dominance
   injection it suggested is false (§3.2).
2. **No Eisenstein + cuspidal identity — by size at primes, not T1 (Prop G″, PROVED relative to the PNT for cuspidal
   GL(m) L-functions; memo y1_gl3_cuspidal; (R214 repair) of D6/D7).** No finite combination of exponent-zero twisted
   divisor convolutions d_k(n; ψ…) and coefficients λ_π(n)ψ(n) of unitary cuspidal π on GL(m) (any m ≥ 2, any characters)
   equals N₋ — **unconditionally**, all self-dual orthogonal (Sym²/Ad) π included. Proof in five lines: on primes ℓ ≡ 1 (L)
   every d_k(ℓ; ψ…) = k, so the Eisenstein part is constant; the cusp part has mean o(1); N₋(p) ≥ ω₃(p + 1) has divergent
   mean. The earlier Prop G′ (T1 at ℓ₀^{2a} + a one-prime genericity hypothesis) mis-attributed the mechanism, and its
   hypothesis fails at every admissible prime for Ad of a tetrahedral weight-one form (R214 D7); it survives only as the
   conditional Remark G (T1 ⇒ E constant on S_L). Steering: an exact identity for N₋ needs a non-constant main term on
   primes; T1 is not what kills finite automorphic combinations (the same applies to O205 Prop 2.3's "E ≠ N₋").

## Results (labels)
* PROVED: Thm A (H1–H4), Cor A1, Prop A2, Thm B (TWO_FIBRES §1–2); Prop G″ (rel. PNT for cuspidal GL(m) L-functions; R214 repair), Remark G (conditional);
  G1 (χ is a function of M_w mod 8 — finite cell check), G2 (not an SL₂(ℤ)-class function), G3 (genus-character reformulation, content-free);
  K1 (congruence/index identity: root-2 level-t forms with x = 4 index 4n; the Heegner/GKZ reading is Assessment —
  imprimitive forms occur); R1 (only reversal-fixed word (p+2,1,1) for p ≥ 5; it is parabolic, trace −2), R3 (n-preserving rotations on X_p are the
  reversal; R214 repair D12).
* CERTIFIED (finite): 𝔊⁺_p = image of the conic orbits, onto for all primes 5 ≤ p ≤ 127, non-injective exactly at
  p = 71, 79, 107, 109, 113, 127 ((R214 repair) D5; my original list had only p ≡ 1 (4)). Sign dominance N₋ ≥ N₊ fails at exactly
  2 402 of the 39 174 primes p ≡ 1 (4), 5 < p < 10⁶ (exact computation, reproduced by R214).
* EVIDENCE: N₋(p) mod 8 equidistributed for p ≡ 1 (4) < 10⁶; fibre split not mass-equidistributed per class mod 8.
* Assessment: Cerednik–Drinfeld/Ribet dictionary (y1_cerednik_swap); GKZ local-height reading (y1_heegner_level_t).

## Barrier hypotheses violated, and outcome
* "Genus data only" → integral class-number-one structure (Thm A/B): positive form of T1, but at primes only local (B2).
* "Bounded multiplicity / main-term" → fibre-swapping injection: refuted by exact computation (worst primes: p ≡ 1 (24), (p/5) = +1).
* "Finite fixed-level Eisenstein" → GL(m) cuspidal additions: dead (G″), by size at primes — T1 not needed.
* "Class function" → mod-8 twisted (correspondence) trace formula: carries the sign, cannot select three-letter
  presentations (≤ T^{−2/3+ε} of the classes of trace T; B3).
* "Fixed level" → level-t Heegner pairs (K1): B2 restated.

## Sparks (not pursued)
* Conic distribution: for χ = +1 words, a map w ↦ ℓ(w) ∈ P¹(𝔽_p)/S₄ (needs a choice of embedding/overlattice); for χ = −1, w ↦ edge of the 2-isogeny graph. Which
  conic points/edges carry path bases (small-height ℓ? LPS/Ramanujan equidistribution of Hurwitz orbits)? A
  "path bases concentrate on few conic orbits" statement plus an edge-count would be a structural size statement.
* Sign-dominance failures (§3.2): quantify N₊(p) − N₋(p) as a function of the quadratic-residue pattern of p modulo small
  moduli (24, 5, 7, …) — a "p looks like a square to small moduli" law, cf. (J)27.
* Composite n: Thm A splits χ = +1 words into Diff = {2} (ℤ³-embeddable) and Diff ⊋ {2} (χ = +1 but ramified at odd
  primes; 7 824 words ≤ 3001). Is there a composite analogue of SQ₅ using the three classes {2 ∉ Diff}, {Diff = {2}}, {2 ∈ Diff ⊋ {2}}?

## Self-review (R209-self: deep reviewer via `review`, since side-agent/sign-identity)
Verdict "request changes"; core proofs confirmed (Thm A incl. nM^# ⊂ ℤ³, Thm B and A2 via maximal lattices + cyclic
discriminant group, G/G′ exponential-polynomial step, E ≡ C₀ + C₁ on S_L, the ω₃ mean). Reviewer reproduced y1_z3_gram 151,
y1_matrix_mod, y1_three_squares 1001. Findings and repairs (all accepted):
* N₊ ≠ Σ r(T_w, I₃)/48 (p = 5: 5 vs 6) → corrected (y1_hurwitz_lift, TWO_FIBRES §3.3).
* "𝔊⁺_p = P¹/S₄" → "image of" everywhere; H4 proof routed through A2 (general lattices).
* Hyperbolic overstatements: boundary words reduce (S_aS_1S_b = S_{a−1}S_{b−1}), (p+2,1,1) is parabolic (trace −2);
  unproved T^{o(1)} bound → O(T^{1/3+ε}), fraction T^{−2/3+ε}; "reciprocal geodesic" → "reversal-fixed word"; p = 3 exception.
* G3 sign wording clarified; false "full genus-character class sums are positive L-value products" → they vanish.
* K1 downgraded to the congruence/index identity; imprimitive example (2,2,3); converse narrowed.
* §3.1 "exactly cells mod 8" false → sufficient condition only, with counterexamples (29,1,3), (5,1,3), (1,4,7).
* G/G′: ℓ₀ odd; α⁴ ≠ 1 ⟺ a² ∉ {0, 4}; common-prime quantifier; scope narrowed from "every automorphic identity";
  tempered caveat for the illustrative κ formula; BV not needed for divergence.
* Cerednik–Drinfeld: Mumford only after unramified quadratic extension; conventions flagged.
* Minor: dead assert removed; numerics section filled; novelty wording ("three squares" occurs elsewhere in the repo).

## R214 repairs (hostile review reviews/two-fibres-review.md: no FATAL; Thm A, Thm B, A1, A2, K1 SOUND)
All defects applied, marked "(R214 repair)" / "R214 repair Dx" in the files:
* D6/D7 (MAJOR): Props G/G′ replaced by the unconditional Prop G″ (size at primes); ℓ₀/T1 analysis demoted to Remark G
  with the tetrahedral/dihedral counterexamples to its hypothesis; memo title, TWO_FIBRES Summary/§0/§4, README, SHARP 2 updated.
* **D9 — explicit note for O217 (three-squares relay): the "near squares" story is WRONG and is withdrawn.** The worst
  sign-dominance failures (13 primes < 10⁶ with N₊ ≥ 4N₋) are not archimedeanly near m² (29 401 = 171² + 160,
  225 289 = 474² + 613, 871 249 = 933² + 760); what they share is **p ≡ 1 (24) and (p/5) = +1** (11/13 also (p/7) = +1), i.e.
  p is a quadratic residue to the small moduli seen by short words ((J)27 in its arithmetic, not archimedean, reading).
  Re-checked here from the 10⁶ census. Thm A itself is unaffected.
* D5 (non-injectivity at 71, 79, 107, 109, 113, 127), D1 (orientation of the congruence lift), D2 (classical local–global
  attribution), D3 (norm-maximal lattices; ℤ³ norm-maximal), D4 (citation for ES-five ⟺ N₋ ≥ 1), D8 (PNT input, BV dropped),
  D10 (hyperbolic example pair (3,5,3)/(5,3,3), T = 34; G3 called a reformulation), D11 (stale T^{−1+o(1)}), D12 (R3 restated),
  D13 ((p+1)/12 edges vs (p+1)/24 lattice classes explained).
