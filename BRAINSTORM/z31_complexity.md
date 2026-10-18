# z31 — Computational complexity: divisors in residue classes, TFNP, QNR-finding (O261 field memo 8)

Labels as in DISCOVERIES.md. Read (agent E, verbatim abstracts): Lenstra 1984 (`lenstra_divisors.txt`), Coppersmith–Howgrave-
Graham–Nagaraj 2008 (`chn2008.txt`), Jeřábek 2016 abstract. Builds on gon_lll_relation_lattice.md, s3_lll_lenstra (README),
CONSTRUCTIVE_ES Prop 4.1/4.2 ((J)35), POINTWISE_OMEGA §8 (Graham–Ringrose Ω-bounds).

## (a) Counterparts
1. **Divisors in residue classes.** Lenstra, Math. Comp. 42 (1984): for s > n^{1/3}, gcd(r, s) = 1, "there exist at most 11
   positive divisors of n that are congruent to r modulo s, and there is a polynomial algorithm for determining all these
   divisors". CHN, Math. Comp. 77 (2008): for s ≥ n^α, α > 1/4, O((α − 1/4)^{−3/2}) such divisors, found constructively (LLL /
   Coppersmith). This is literally the *decision* version of one B2 slice: E2 at slice d is "does n = p + 4d have a divisor
   ≡ −1 (mod s = 4d)?".
2. **Total search (TFNP).** If ES is true, "given n, output (x, y, z)" is a total NP-search problem. Papadimitriou 1994 (PPA,
   PPP: parity and pigeonhole classes); Jeřábek, JCSS 82 (2016), abstract: factoring is randomized-poly-time reducible to PPA
   and to WEAKPIGEON (PPP). Zagier's involution places "write p ≡ 1 (4) as a² + b²" in the parity world, though agent E found
   no paper stating a TFNP-class membership for it (no claim).
3. **Deterministic QNR finding** (open unconditionally; poly-time under GRH via Ankeny/Bach).

## (b) What is proved
* (1) is pointwise and *unconditional*, but only in the large-modulus regime s > n^{1/4+ε}; it is an **upper bound +
  algorithm**, never an existence statement.
* **Hardness transfer (input PROVED in the campaign, (J)35 Prop 4.1/4.2; PARITY_AUDIT event (a)):** an ES-five certificate
  w = (t, u, v) carries A = tu − 1, B = tv − 1 with ψ(A) = ψ(B) = −1, i.e. an explicit quadratic non-residue, without factoring.
  Consequences (R-O261 repair M7: two different statements, kept apart):
  (i) *existence of small certificates* — if every prime p ≡ 1 (4) had an ES-five certificate with min(A, B) ≤ X(p), then
  n(p) ≤ X(p); by the unconditional Graham–Ringrose bound n(p) = Ω(log p · log₃ p) infinitely often, made available for hard primes
  p ≡ 1 (24) via Lau–Wu Prop 5.1 (POINTWISE_OMEGA Thm 8.5; secondary source there), this fails for X(p) = c log p · log₃ p
  with c small (PROVED relative to those cited results).
  (ii) *a solver* — a deterministic algorithm that outputs an ES-five certificate in time poly(log p) would output a QNR in
  poly(log p) time, i.e. derandomise QNR finding (not known without GRH). A mere existence proof of polylog-height certificates
  does not supply such a solver (enumerating candidate certificates needs factoring or a search; CONSTRUCTIVE_ES's repaired
  statement is p^{o(1)} search relative to factoring, (J)35).
  (This is the complexity face of the Mordell-hard primes, (J)26/(J)54.)

## (c) Transfer to B2
* Lenstra/CHN: the decisive objection is that the method has no existence content — it certifies the complete list of
  divisors in a class (possibly empty), never non-emptiness (gon_lll memo (b1)). It decides individual slices with
  s = 4d > (p + 4d)^{1/4+ε} in polynomial time; some certificates live there (e.g. p ≡ 5 (8): d = (p + 3)/8, w = 4d − 1 = (p+4d)/3,
  R-O261 repair M7), others at small d where the method gives nothing.
* TFNP: a parity (PPA-style) proof of totality would be a windmill; INVOLUTION_ES/ES2 ((J)2) bar finite-menu affine
  involutions (conditionally) and T1 kills the odd set on square classes. Factoring-hardness is not an obstruction to
  *existence*: ES at p is decided by brute force in time p^{O(1)} regardless of factoring.

## (d) Verdict: Lenstra/CHN — EQUIVALENT *per slice* (E2 at fixed d is exactly a divisors-in-residue-classes decision
problem) but in the wrong size regime and with no existence content: **NOT SHARP**. TFNP/QNR — ANALOGUE; it yields a
*hardness* statement (a poly(log p) ES-five solver ⟹ deterministic QNR finding; small-A certificates fail i.o.), already in
substance in the campaign ((J)35, POINTWISE_OMEGA §8).
