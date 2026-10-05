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
