# AGENT REPORT O176 — spark relay brainstorm C (building on O172's "T1 = Diff-parity"), checkpoint 1

Branch `side-agent/spark-diff-parity` (merged side-agent/kudla-incoherent and main incl. R172 repairs). Deep file
`DIFF_DEEP.md`; 8 memos `BRAINSTORM/bsC_*.md` (indexed in BRAINSTORM/README.md); scripts `scripts/bsC_*` (each ≤ 1 min).
**ES is not solved; no infinite case of ES is claimed.** Nothing below is a positive ES claim, so no 10⁶ triple-check
of a positive statement was needed; all equivalences were checked against the tuple enumerator, with odd squares as the
T1 control (0 solutions throughout).

## SHARP:
* **(LD_p): Type II is a "level-vs-determinant" condition on a pair of special endomorphisms (DIFF_DEEP Thm 2.1,
  PROVED, elementary; brute-force checked for all primes and odd squares n ≤ 300).** For odd n: Type II tuples ↔ (f, f', c)
  with n | ff' − 1, 4c² | h, h | cG, where h = (ff' − 1)/n and G = gcd(f + 1, f' + 1); a c exists iff
  **4h | gcd(h, G)²**. Geometrically: ES Type II(p) ⟺ some supersingular E/𝔽̄_p has trace-zero x, y ∈ End E with
  ⟨x, y⟩ = 1 whose Gram "level" G is ≥ 2√h, h = det/p. Kaneko gives h ≥ 1; the slice parameters (c, d) disappear
  (they are recovered from h and G). Caveat: an exact restatement of (I)4, not new arithmetic.
* **The ray condition is free on one endomorphism (DIFF_DEEP Prop 2.3, PROVED).** For every maximal order O of B_{p,∞},
  every M (p ∤ M) and every involution x₀ mod M there is x ∈ O⁰ with x ≡ x₀ (mod MO), so nrd x ≡ −1 (mod M), with
  nrd x ≪ M²p. The B2 core moves into an *exactness* condition on the second endomorphism, with a gap factor ≍ f^{3/2} ≥
  M^{3/2} in the determinant (Prop 2.4, Assessment) — B3 in geometry-of-numbers form.
* **Diff-parity over ANY base field sees a rational prime only through one quadratic Dirichlet character
  (bsC_parity_quadratic_only Prop 1, PROVED).** Hence unitary / big-CM incoherence (O172 spark 4) cannot carry order-≥3
  characters; parity can certify the ES ray condition only on slices with 4cd | 24 (Cor 2). EVIDENCE: those 9+9
  quadratic slices cover all but 71 of the 9732 primes p ≡ 1 (24) below 10⁶ (first misses 3361, 31081, 34897, …).

## Results
* §1 (DIFF_DEEP; bsC_supersingular_transfer): **supersingular transfer** — a configuration of Gram T exists on some
  supersingular curve iff Diff(T) = {p}; so "∃ curve" is genus-vacuous (answers the orchestrator's main question:
  no). "∀ curve" is false: Λ_{d,ab} is an Eichler order of level e, lies in exactly τ(e) maximal orders, e ≤ (p+1)²+1,
  so Type I certificates sit on ≪ p^{o(1)} curves (PROVED rel. ET; asymptotic only — at p ≈ 10⁴ f_I(p) still ≥ p/12).
* §2.5 canonical curve (EVIDENCE): Ibukiyama's curve O(q, r) carries a Type II configuration (f' ≤ 4p) for 144/267 primes
  p ≡ 1 (24) < 2·10⁴, slowly decaying by block (47/76 → 33/67) while certificates per p grow; no privileged-curve effect.
* §3: Type I via Eichler orientation (the orientation runs over all roots of −m, so it is free); unlike Type II, Type I
  needs a factorisation m = ab, which is not a Gram-matrix condition — Type II is the better test bed.
* bsC_valence_borcherds: Type II certificate = Heegner point of Z(−4Mcp, 0) on X₀(M) with representative shape
  C + 1 = B/2; Galois-orbit obstruction (orbits ≫ p^{1/2−ε} vs p^{o(1)} certificates; PROVED rel. Siegel + ET).
* bsC_typeII_commutative: Type II ⟺ (2ad + k)(2bd + k) = de(1 + 2ck) in ℤ[√−dn] (checked on 336357 tuples) — the
  "non-commutative" label of QUATERNION_ES §3 is presentational.
* bsC_fourier_jacobi (B1/B6/B2), bsC_isogeny_ramanujan (B3/B2), bsC_arithmetic_topology (dictionary only).

## Verdict (Assessment)
The supersingular/Deuring route collapses exactly where O172 predicted (genus), and when the ray condition is put on
the curve as level structure it becomes free, with the cost reappearing as an exactness/size condition (B3). The one
new object worth keeping is the lattice statement (LD_p) (DIFF_DEEP §4): "a pair of special endomorphisms with level
≥ 2√(covolume/p)". It is a faithful restatement of the H-A core, not an escape. No route to ES.

## Sparks (not pursued)
1. (LD_p) as a *successive-minima* problem: is there a reduction-theory statement for the genus of Gross lattices of the
   form "some O has a pair with level ≥ c·√h" for h in a range — with a proof that must use |Diff| = 1 (so fail at squares)?
2. Type II at fixed h (i.e. fixed c²d): Thm 2.1 says the level G must be ≥ 2√h; study the distribution of G over the
   τ(1 + ph) pairs (f, f') — is there any p-uniform lower bound on max G beyond the trivial one?
3. ∀E at small p: is every supersingular curve mod p carrying *some* ES configuration for p ≤ 10⁴ (where f(p) ≥ p/12)?
   Needs all maximal orders (ideal-class enumeration); a phase transition in p would be a curiosity.
4. Hermitian/unitary version of Thm 2.1 over ℚ(√−dp) via the commutative factorisation (bsC_typeII_commutative):
   the pair (2ad + k, 2bd + k) as a hermitian lattice, level ↔ the ideal 𝔡𝔢.
5. Canonical-curve statistics against the *full* spine (all ≈ h(−4p)/2 curves over 𝔽_p): is the per-curve share uniform?
