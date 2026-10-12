# AGENT REPORT O144 — brainstorm: Farey / Ford circles / continued fractions / Apollonian & thin groups

Branch `side-agent/bs-farey-apollonian`. Four memos under `BRAINSTORM/`, scripts `scripts/bs_farey_*`.
ES is not solved, and no infinite case of it is.

**(a) `farey_ford_cf.md` — COLLAPSES to B2 (B1 for finitely many N).** Lemma A.1 (PROVED, elementary;
reproduces f_I exactly for all 1005 primes ≤ 8000) gives the exact dictionary: Type I ⟺ (N = 4ad, a | N/4,
e | aN + 1, N | pe + 1), i.e. e/N < b/p are Farey neighbours (tangent Ford circles). In the range N < p, b < p
this is "the left F_p-parent of some C(b/p)". That range misses exactly {5, 17, 41, 241} below 8000. The
strongest reason for collapse: for fixed N the minimal e is −p⁻¹ mod N, the penultimate-convergent denominator
of p/N, which is congruence data. The residual condition "e | aN + 1" is the one-integer divisor lottery.
Zaremba/Bourgain–Kontorovich are almost-all (B6). Pointwise, they control partial-quotient *sizes*, which the
divisor event ignores, and bounded type only thins the family (B3).

**(b) `apollonian_reciprocity.md` — COLLAPSES as an existence route; PARTIAL as structure.**
* Prop B.2 (PROVED, from BL Cor 2.7): Br U_n/Br ℚ = ℤ/2, so over ℚ no quartic or higher Brauer–Manin
  obstruction exists for ES (a quartic class needs μ₄ ⊂ k).
* Prop B.1 (PROVED relative to BL; the Type I half is implicit in BL's proof): the BM set of the Type I locus,
  and separately of the Type II locus, is non-empty at every prime.
* HKRS obstructions come from thin-orbit constancy (HKRS: "not its Zariski closure"). ES at fixed n has no
  infinite group action (BL Lemma 3.10). HKRS families u·m^k contain ≤ 1 prime.
* EVIDENCE to 2·10⁷:
  * odd n with no Type I/II point in ET coordinates are exactly the odd squares, plus 105 (an artefact of the
    gcd(abd, n) = 1 convention);
  * (2/p)₄ and (3/p)₄, which are non-congruence invariants, show no bias in f_I + f_II, in mean or lower tail
    (158 581 primes p ≡ 1 (24)).
* HKRS's own "no further obstructions" (Conj 1.5) is open, so no proof strategy transfers.

**(c) `thin_group_orbits.md` — COLLAPSES to B3.** Strongest reason: thin-orbit circle methods need
power-size representation counts per target, and even then give only density one. ES has polylog mass per
prime. Its natural orbit group (SO(Q_d)(ℤ) on X_d: ef − 4da² = 1) is arithmetic, not thin, and thinning only
lowers the main term below 1. The affine sieve runs the wrong direction (almost-prime values, not prescribed
values).

**(by-product) `farey_chain_frieze.md` — PARTIAL (sharp reformulation).**
* Prop C.1 (PROVED, elementary): for prime p ≥ 5, ES(p) ⟺ some monotone 3-step Farey path (a positive
  width-2 frieze q₀, q₁, q₂, q₃ with q_{i−1} + q_{i+1} = k_i q_i) spans a positive integer multiple 4d/p,
  with (x, y, z) = d·(q₀q₁, q₁q₂, q₂q₃). The chain is (a, c, b, ap) with turning numbers (e, f) for Type I, and
  (cp, a, b, cp) for Type II.
* The unscaled form (span exactly 4/p) is the ET-"d is a square" sub-family. "⇐" is PROVED; "⇒" is EVIDENCE
  on 11 800 solutions. Its mass is L², and it misses 17 primes ≤ 6000, all ≡ 1 (12).
* It is still B2 once (q₀, q₁) is fixed. Novelty unverified.

No memo is LIVE.
