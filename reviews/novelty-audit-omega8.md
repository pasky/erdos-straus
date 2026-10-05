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
