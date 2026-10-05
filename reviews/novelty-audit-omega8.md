# Novelty audit: POINTWISE_OMEGA8 (sub-exponential witness-modulus bound)

Task O33, Step A. Object audited: POINTWISE_OMEGA8.md §§1–5, i.e.
Thm 4.3 (`W(p) ≥ exp(c(log p)^{1/14})` i.o. over Mordell-hard p, mod
Thorner–Zaman + Elsholtz–Tao Prop 1.4) and Thm 4.4
(`log W ≥ (1/(2log2)−o(1))log₂p·log₃p`, mod TZ only). §6 (in progress) is
out of scope.

## Search limits (read first)

* **No internet in this pass** (brief: rely on `sources/` and
  `LITERATURE_2026.md`). Everything marked *[memory]* below is from the
  auditor's background knowledge of the literature, **not** checked
  against a primary text; bibliographic details (years, venues, exact
  theorem statements) may be off. Items marked *[archived]* were read in
  `sources/`.
* Archived and read for this audit: Benjamini–Gurel-Gurevich–Peled
  arXiv:1201.3261 (`sources/lit2026/audit-arxiv-1201.3261v1.txt`),
  Peled–Yadin–Yehudayoff arXiv:0801.0059, Berend–Ernst–Kontorovich–Kumar
  arXiv:2407.18688, Ford–Green–Konyagin–Maynard–Tao arXiv:1412.5029 and
  Ford–Konyagin–Maynard–Pomerance–Tao "Long gaps in sieved sets"
  (`sources/jacobsthal-literature/`), the earlier campaign audits
  `reviews/novelty-audit-2026-10.md`, `reviews/lit-audit-B-pointwise.md`.
* **Not accessed at all:** Bazzi (FOCS 2007 / SICOMP 2009), Razborov
  (ACM TOCT 2009), Braverman (CCC 2009 / JACM 2010), Linial–Mansour–Nisan
  (JACM 1993), Håstad (STOC 1986), Green's Möbius/AC0 paper, Bourgain's
  Möbius–Walsh papers, Hough (Annals 2015), Balister–Bollobás–Morris–
  Sahasrabudhe–Tiba (Inventiones 2022 and later), Graham–Ringrose 1990.
* "New" below means: **no prior source known to the auditor or found in
  the archive**. It is not a priority certificate; a real literature
  search (MathSciNet citations of Bazzi/Razborov/Braverman; arXiv
  full-text "switching lemma" ∧ "primes") is the first item for an
  external reviewer.

## (i) Bazzi / Razborov / Braverman ("bounded independence fools DNF/AC0") in sieve theory or analytic number theory

**What the TCS literature contains** *[memory]*:
* Bazzi (FOCS 2007; SICOMP 2009): `O(log²(m/ε))`-wise independence
  ε-fools every m-clause DNF. Razborov (TOCT 2009) gave the short proof
  whose one-sided ℓ² scheme `B = 1 − Σ_i A_i(1−v_i)²` is OMEGA8 Lemma 3.1;
  the deterministic choice of `u_j` as a low-degree ℓ² approximation of the
  "conditional survival" function is usually credited to Wigderson in
  Razborov's write-up. Braverman (CCC 2009; JACM 2010) extended this to
  AC0; Tal (CCC 2017) and Harsha–Srinivasan sharpened the parameters.
* Even–Goldreich–Luby–Nisan–Velicković (1992/98; cited as [16] in BGP
  *[archived]*): k-wise independence fools combinatorial rectangles over
  large alphabets. That is the single-coordinate-event (prime-local) case.
* Linial–Nisan (1990) and Kahn–Linial–Samorodnitsky (1996) on approximate
  inclusion–exclusion, plus BGP and PYY *[archived]*. These are the
  Bonferroni / alternating-sum side, which the earlier campaign audit
  (`reviews/novelty-audit-2026-10.md`) already matched against the
  sieve-limit note. BGP §4.3 *[archived, lines 352, 509]* discusses the
  Linial–Nisan conjecture and LMN–Håstad concentration, but not Bazzi.

**Number theory.** The auditor knows **no** use of Bazzi's theorem,
Razborov's sandwich or Braverman's theorem inside sieve theory or
analytic number theory. Nothing in the archive contradicts this.

**Closest classical analogues** (conceptual; nobody claims these as the
same result):
* *Selberg's lower-bound sieve* *[memory; Opera de Cribro ch. 7 not
  accessed]* uses minorants of the shape `(1 − Σ_{p|n,p∈𝒫}1)(Σ_{d|n}λ_d)²`.
  Like B, this is a "1 minus a non-negative quadratic correction" with
  optimised weights. The differences: Selberg's quadratic form ranges
  over divisor-supported weights at level `D` (modulus size), while BRW's
  ranges over juntas, with level = **number of primes**. Also BRW's
  correction is local (`A_i·square`, using the first occurring event).
* *Brun's pure sieve* truncates `Σμ(d)` at `ω(d)≤r`, i.e. by the number of
  primes, as OMEGA8 does. It is alternating, though, and §2.3 of OMEGA8
  explains why alternating truncations fail here.
* *Beurling–Selberg extremal functions*: one-sided band-limited
  approximation. This is the classical ANT counterpart of TCS
  "sandwiching polynomials".

**Assessment.** As far as the auditor knows, OMEGA8 is the first place
where a Bazzi–Razborov sandwich serves as a sieve minorant transferred to
primes. The step that carries the novelty: in the Linnik range, primes
`≡1 (Q)` behave like a t-wise independent law on residue cells with
**multiplicative** error. Thorner–Zaman's relative error term (PO Thm 4.1)
supplies that. Consequently the "level" that costs anything is the number
of primes per cell, and the modulus size is nearly free (log p ≈ K·log Z).
This should be stated in the paper as a transfer of a known TCS tool. It
should **not** be called a new minorant: Lemma 3.1 is Razborov's
identity, verbatim.

## (ii) Switching-lemma Fourier tails in number theory

**Known** *[memory]*: the switching lemma and LMN show up in number
theory in the *opposite* direction. There the arithmetic function is the
object and the AC0 function is the test:
* Green, *On (not) computing the Möbius function using bounded depth
  circuits* (CPC 2012): μ(n), with n in binary, has o(1) correlation with
  AC0. The proof uses AC0 structure (random restrictions / Fourier
  concentration) together with distribution of μ in residue classes. The
  details are from memory only.
* Bourgain (2013, J. Anal. Math. and Israel J. Math.): Möbius–Walsh
  correlation bounds, motivated by the same question (Kalai). From these
  and LMN-type concentration one gets Möbius vs AC0 in sharper ranges.
* Allender–Saks–Shparlinski (2001) and Bernasconi–Damm–Shparlinski:
  circuit lower bounds and Fourier spectra for primality, quadratic
  residuosity and similar predicates.

**OMEGA8's direction is different.** The *sieve indicator itself* (a CNF
of width `kb` in the bits of the residues) is the AC0 object. Håstad + LMN
bound its Efron–Stein tail, and that tail is the error term of a sieve
minorant (Lemma 4.1 → Cor 4.2). The auditor knows no prior use of a
switching lemma to bound a sieve error term or a covering-avoidance
density. Status: **apparently new, low confidence** (no search possible).

**Routine parts** (no novelty claimed): the bit encoding of `ℤ/q` by
`⌊q·int(u)/2^b⌋`, with fibres as unions of `≤2b` subcubes and density ratio
`≤e^{1/2}`; LMN with the binomial-median variant; Jensen to go back from
bits to coordinates.

## (iii) Prior Ω-results: the ES witness modulus and covering-avoidance analogues

**ES witness modulus.** The earlier audit (`novelty-audit-2026-10.md`
row 2a; `lit-audit-B-pointwise.md`) found **no** Ω-result in the
literature for any least ES witness parameter (ET, PW, Dahan, Salez,
Bright–Loughran all inspected *[archived]*). The only prior Ω-results
for W are the campaign's own: the class of one + Linnik
(`W ≫ log p`), es-omega-note v3 (`(log p)^k` for every k), and OMEGA3/4
(`log W ≥ (1+o(1))log₂p log₃p/log₄p`). Thm 4.3 supersedes all of these.
Relative to the literature, **the statement is new**, with the caveat
the earlier audit already made: W is a campaign-defined parameter.

**Analogues** (each is a "the object avoids every small modulus"
statement, i.e. a prime that lies in the uncovered set of a congruence
system):
* *Least quadratic non-residue / least primitive root.*
  Fridlender–Salié `Ω(log p)`, Graham–Ringrose `Ω(log p·log₃p)`, and
  Montgomery (GRH) `Ω(log p·log₂p)` *[secondary: Lau–Wu (1.7), archived]*.
  These are prime-local: single-coordinate events, one CRT class,
  avoider density `≈2^{−π(T)}`. Here the truth is ≈ log p, and the method
  is a single CRT class plus least-prime bounds. In OMEGA8 the Haar
  density is `e^{−𝓛^{O(1)}}` (OMEGA2 Thm 11.3), and the point is to reach
  it on primes **without** a single CRT class. A single class would cost
  `log p ≍ T`. That is exactly the gap between the v3 note's
  prime-local exponent-2 ceiling and the present rate.
* *Jacobsthal / long prime gaps.* Erdős–Rankin, Maier–Pomerance, FGKMT
  *[archived: arXiv:1412.5029 abstract and §4, a Pippenger–Spencer-type
  hypergraph covering theorem]* and FKMPT "sieved sets" *[archived: random
  CRT residue choice + covering lemma, Appendix A]*. These run the
  probabilistic method on the **covering** side (make an interval
  composite); they do not transfer a covering-*avoidance* density to
  primes in a union of classes.
* *Erdős covering systems.* Hough (Annals 2015; minimum modulus
  `≤10^{16}`) and Balister–Bollobás–Morris–Sahasrabudhe–Tiba (Inventiones
  2022, "the density of the uncovered set"; also the square-free
  Erdős–Selfridge paper). The "distortion method" gives lower bounds of
  the type `∏(1−O(1/d))` on the uncovered density, by an iterative
  reweighting that is LLL-like *[memory: BBMST relate it to Hough's
  method; whether they explicitly call it an LLL variant is not
  checked]*. This is the closest analogue of OMEGA8's **Haar input**
  (OMEGA2 Thm 11.3: local lemma, `δ ≥ e^{−2.2S}`). It is not an analogue
  of the new step, the transfer to primes. The auditor knows no result
  bounding the least **prime** in the uncovered set of a congruence
  system with lcm far beyond the Linnik range via a bounded-junta
  minorant.
* *Least prime in a union of progressions / Chebotarev with many
  conditions* (Linnik-type, Thorner–Zaman's own Chebotarev work)
  *[memory]*: these give upper bounds for the least prime in a given set
  of classes. OMEGA8's PO Thm 4.1 is such a bound for a union presented
  as a signed combination of cells with controlled ℓ¹ mass and twists.
  The idea of feeding a sieve minorant into Linnik is standard
  (Chang/Iwaniec-type least-prime-in-sieved-sets results). The
  *junta-size* bookkeeping is the specific feature.
