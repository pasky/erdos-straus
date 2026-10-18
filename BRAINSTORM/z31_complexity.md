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
* **Hardness transfer (PROVED in the campaign, (J)35 Prop 4.1/4.2):** an ES-five certificate yields an explicit quadratic
  non-residue mod p (and maximal orders) without factoring. Consequently (Assessment, combining with the Graham–Ringrose
  unconditional Ω-bound n(p) = Ω(log p · log₃ p) i.o., POINTWISE_OMEGA §8): *certificates whose non-residue A is
  ≤ c log p log₃ p cannot exist for all p*, and a deterministic poly(log p) ES-five solver would derandomise QNR finding — a
  statement not known without GRH. So any *constructive* proof of B2 with polylog-height certificates is at least as hard as
  deterministic QNR finding. (This is the complexity face of the Mordell-hard primes, (J)26/(J)54.)

## (c) Transfer to B2
* Lenstra/CHN: blocked by F2/F3 in a precise sense — the slices where ES solutions live have small modulus s = 4d ≪ n^{1/4}
  (EVIDENCE: least certificates are small, B1_LINE / (J)90), exactly the regime where the lattice method has no bound and no
  algorithm; and the method certifies non-existence beyond a list, never existence (gon_lll memo (b1)).
* TFNP: a parity (PPA-style) proof of totality would be a windmill; INVOLUTION_ES/ES2 ((J)2) bar finite-menu affine
  involutions (conditionally) and T1 kills the odd set on square classes. Factoring-hardness is not an obstruction to
  *existence*: ES at p is decided by brute force in time O(p^{1+o(1)}) regardless of factoring.

## (d) Verdict: Lenstra/CHN — EQUIVALENT *per slice* (E2 at fixed d is exactly a divisors-in-residue-classes decision
problem) but in the wrong size regime and with no existence content: **NOT SHARP**. TFNP/QNR — ANALOGUE; it yields a
*hardness* statement (constructive polylog B2 ⟹ deterministic QNR finding), already in the campaign.
