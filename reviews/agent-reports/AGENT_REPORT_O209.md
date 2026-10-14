# AGENT_REPORT_O209 — spark relay Y1: the two bad fibres of X₀(2p), words as hyperbolic SL₂(ℤ) matrices (checkpoint 1)

Branch side-agent/two-fibres (merged side-agent/sign-identity first). Deep file TWO_FIBRES.md; memos BRAINSTORM/y1_*.md
(6, indexed in BRAINSTORM/README.md); scripts `scripts/y1_*`. **ES is not solved, nor any infinite case of it.**

## SHARP:
1. **The χ = +1 fibre is the cubic lattice ℤ³ (TWO_FIBRES Thm A, PROVED from class number one of B_{2,∞} and of the
   genus of I₃).** For every odd n and word w: Diff(T_w) = {2} ⟺ **n·G_w is a Gram matrix of three integer vectors** ⟺
   ∃ x, y ∈ ℤ³ with |x|² = tv − 1, |y|² = tu − 1, x·y = 1 (and x × y ≡ x + y mod t). For p prime the χ = +1 lattices
   are L_ℓ = {x ≡ λℓ mod p} on the conic x² + y² + z² ≡ 0, i.e. 𝔊⁺_p = P¹(𝔽_p)/S₄ — Cerednik–Drinfeld's char-2 tree made
   explicit. Hence **ES-five(p) ⟺ some p·G_w is NOT a Gram matrix in ℤ³** (equivalently some path binary [[tv−1,1],[1,tu−1]]
   of det tp is not represented by x² + y² + z²). **T1 becomes an embedding (Thm B): every path lattice of odd square
   determinant m² is an index-m sublattice of ℤ³** (for m = q prime: ker(f mod q) with f off the conic). Checked: all
   81 857 words of odd n ≤ 3001, primes to 40 000 (see numerics), odd squares, 0 mismatches.
   Why it matters: it is the first explicit *asymmetry* between the two signs (exact class-number-one world on one side).
   Honest limit: at the level of single words it gives only the 2-adic cell law (TWO_FIBRES §3.1), and the sign-dominance
   injection it suggested is false (§3.2).
2. **No finite automorphic identity at all (Prop G′, PROVED relative to Jacquet–Shalika + Bombieri–Vinogradov; memo
   y1_gl3_cuspidal).** No finite combination of GL(k)-Eisenstein and GL(m)-cuspidal coefficients (any m, Dirichlet twists)
   equals N₋, given one prime ℓ₀ ≡ 1 (L) where 1 is at most a simple squared Satake parameter of each cusp form. This
   closes O205's GL(3) spark **including the self-dual orthogonal (Sym²/Ad) class**: SO(3) parameters contain 1, so the
   cusp side can absorb a constant at the square shapes, but then N₋ = const + cuspidal on primes ≡ 1 (L), whose mean is
   bounded, while N₋(p) ≥ ω₃(p + 1) has unbounded mean (BV).

## Results (labels)
* PROVED: Thm A (H1–H4), Cor A1, Prop A2, Thm B (TWO_FIBRES §1–2); Props G, G′ (rel. Jacquet–Shalika, BV);
  G1 (χ is a function of M_w mod 8 — finite cell check), G2 (not an SL₂(ℤ)-class function), G3 (genus-character form);
  K1 (words = x = 4 GKZ terms of two root-2 Heegner points on X₀(t), index 4n); R1, R3 (only reciprocal word (p+2,1,1)).
* CERTIFIED (finite): #𝔊⁺_p = #(conic/S₄) for 9 primes ≤ 101 (p = 109: 6 orbits → 5 classes, onto).
* EVIDENCE: N₋(p) mod 8 equidistributed for p ≡ 1 (4) < 10⁶; sign dominance N₋ ≥ N₊ fails at 2 402 primes (near squares);
  fibre split not mass-equidistributed per class mod 8.
* Assessment: Cerednik–Drinfeld/Ribet dictionary (y1_cerednik_swap); GKZ local-height reading (y1_heegner_level_t).

## Barrier hypotheses violated, and outcome
* "Genus data only" → integral class-number-one structure (Thm A/B): positive form of T1, but at primes only local (B2).
* "Bounded multiplicity / main-term" → fibre-swapping injection: refuted numerically (near-square primes).
* "Finite fixed-level Eisenstein" → GL(m) cuspidal additions: dead (G′).
* "Class function" → Γ(8)-twisted trace formula: carries the sign, cannot select three-letter cycles (B3).
* "Fixed level" → level-t Heegner pairs (K1): B2 restated.

## Sparks (not pursued)
* Conic distribution: for χ = +1 words, the map w ↦ ℓ(w) ∈ P¹(𝔽_p)/S₄; for χ = −1, w ↦ edge of the 2-isogeny graph. Which
  conic points/edges carry path bases (small-height ℓ? LPS/Ramanujan equidistribution of Hurwitz orbits)? A
  "path bases concentrate on few conic orbits" statement plus an edge-count would be a structural size statement.
* Near-square primes (§3.2): quantify N₊(p) − N₋(p) ≈ F(p − m²) — a "continuity of T1" law; might connect to (J)27.
* Prop G′'s leftover: cuspidal π with 1 a repeated squared parameter at every prime ≡ 1 (L) — do any exist?
* Composite n: Thm A splits χ = +1 words into Diff = {2} (ℤ³-embeddable) and Diff ⊋ {2} (χ = +1 but ramified at odd
  primes; 7 824 words ≤ 3001). Is there a composite analogue of SQ₅ using the three classes {2 ∉ Diff}, {Diff = {2}}, {2 ∈ Diff ⊋ {2}}?

## Self-review
(pending — see below)
