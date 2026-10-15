# AGENT_REPORT_O218 — Synthesis IV: "ES must imitate the archimedean place" (checkpoint 1)

Branch `side-agent/synthesis-four` (merged main incl. (J)50 and three-squares). Deliverables: `SYNTHESIS_SPARKS4.md`
(deep file), 8 memos `BRAINSTORM/s4_*.md` (indexed in BRAINSTORM/README.md), scripts `scripts/s4_*`.
**ES is not solved; no infinite case of ES is claimed.**

## SHARP:
1. **Positivity is T1's anchor, not the bottleneck (SYNTHESIS_SPARKS4 §2).** The signed n-adic relaxation
   (R_n): "some integral point of X_n with tuv ≠ 0, not necessarily positive, has χ = (−(tu−1)/n) = −1" keeps T1
   automatically (PROVED), is a finite search |t| ≤ n + 3 (PROVED), has no forcing (χ(A)χ(B) = 1 for every
   factorisation, PROVED), has an explicit genus slot table at |t| ∈ {1,2,3,4,6} (PROVED; CERTIFIED 4 900 n), and no
   finite t-set suffices (CONDITIONAL on Schinzel H, sketch). **CONJECTURE SQ_± (EVIDENCE: every odd non-square
   n ≤ 10⁷, least |t| ≤ 18): some signed point has χ = −1 ⟺ n is not a square** — the SQ₅ exception 105
   disappears. Steering rule: test any lottery-breaking idea on SQ_± first (same T1, same box, twice the tickets);
   if it fails there, positivity will not rescue it.
2. **Precise meta-statement (s4_three_bits_meta).** Positive ⟺ path form definite (L1, PROVED); the positive locus is
   a single connected component D of X_n(ℝ) (L2, PROVED); ES-five(n) ⟺ X_n(ℤ) ∩ (D × Ω₂) ≠ ∅, and the CHI_FLIP
   class has inv_∞ = ½ exactly on D. Three-bit law certificate ⟺ χ·s_∞ = −1 for *all* words, signed included
   (CERTIFIED n ≤ 1001). Positivity-blind = "conclusion lands outside D"; tool classes listed.
3. **Selling/Voronoi dictionary (s4_selling_voronoi_wall, Lemma S PROVED).** Path forms are exactly the obtuse
   superbases with a face of conorms (1, 1, 0): ES-five certificates are χ = −1-genus lattices on a Voronoi wall
   (two zero conorms) with two unit conorms. The positivity-using reduction-theory form of the certificate set.

## Other results (all modest)
* s4_kudla_green_infinity: ∞ ∈ Diff(T_w) ⟺ w signed; at odd squares all certificate-shaped T have Diff = {∞}
  (PROVED given the three-bit law).
* s4_maslov_inertia: (J)45's Maslov count = ind_−(path form)/2 (PROVED, CERTIFIED 75 097 words); at length 3 the
  ∞-factor is all-or-nothing, so no partially-signed T1-bearing variant exists on the five slices.
* s4_minkowski_sail: Lemma M (word ⟺ positive vector (c,s) ∈ Λ_A with cs | p + c + s); Minkowski/Thue are sign-blind
  (50.0 % quadrant); one-quadrant geometry of numbers is HJ itself; no volume theorem.
* s4_two_and_infinity: numerator data is purely 2-adic, positivity purely ∞; their unique coupling over ℚ is
  Hamilton's B_{2,∞} — i.e. TWO_FIBRES Thm A. (For 4 | M, full T1 is inherited from 4 because Ω₂^{(M)} ⊆ Ω₂^{(4)}.)
* s4_mute_infinity: steering table of all relaxations; every PROVED one has a fixed c_∞-modulus *and* infinitely
  many shots.
* s4_real_analytic_tools: θ > 0 on iℝ, IVT/degree, SOS, Hodge-index/Hasse — all on the real/genus layer (COLLAPSES).

## Iteration (construction-first) summary
First attempted a "rotation number of continuant vectors" reading of the Maslov count — false (consecutive
continuants do not have det 1; caught numerically, script deleted); replaced by the correct inertia-index lemma.
Initially attributed SQ_±'s ease to "the c_∞ condition moving to modulus 4"; on checking the slot table this was
wrong — the gain is just the extra numbers sn − 1 (memo corrected).

## Points for the reviewer
* P3(d)/§2.4 (no finite t-set under H) is a sketch: admissibility of the prime tuple and the sign of the bounded
  exceptional factorisations need a per-T check.
* K2 (Kudla) relies on the three-bit law for signed words, which is CERTIFIED, not proved; a proof should follow
  from TRANSPORT Thm 3.1 plus the 2-adic cell law.
* "Conorm multiset is a lattice invariant" and the Voronoi-type names are quoted from memory of Conway–Sloane VI;
  only the multiset invariance was checked numerically.
* Novelty: L1/L2 and the inertia lemma are elementary/classical; new are the SQ_± conjecture and the steering
  conclusion, and the Selling-wall reading.

## Sparks (not pursued)
1. Prove SQ_± for n in a positive-density set via the slot table + a sieve on the ten numbers |t|n ± 1 (lower-bound
   sieve for "some slot has a prime in the non-principal genus" — this is a statement over *many* n; at a single n it
   is again a lottery).
2. Selling wall × ℓ-neighbour graph: is the set of wall lattices in the χ = −1 genus hit by a canonical walk (e.g.
   Voronoi-flip descent) from a canonical start (the spine word (p + 2, 1, 1) lives in χ = +1)?
3. SQ_± vs SQ₅ at composite n: classify n where signed words are needed (105 and the |t| ≤ 6 failures 34 489,
   97 185, …): are they all "locally square" for small primes as in (J)27?
4. Higher-rank archimedean: the Klein polyhedra (3D sails) of the lattice {x ≡ A y ≡ B z} and length-3 words as sail
   faces (Arnold's programme) — untested.
