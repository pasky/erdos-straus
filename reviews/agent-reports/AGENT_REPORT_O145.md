# AGENT_REPORT_O145 — brainstorm: machine-discovered identities / non-polynomial families / other numerators

Branch `side-agent/bs-identities`. Three memos under `BRAINSTORM/`, scripts `scripts/bs_ident_*`,
small outputs in `data/bs_ident/`. None of the memos is LIVE. ES is not solved.

**(a) `BRAINSTORM/ident_invariants.md` — COLLAPSES to B2 (B1 for class numbers).** I regressed e-slice
lottery data (successful e ≤ 200, e_min of Type I and II) for 2.4·10⁴ Mordell-hard primes ≤ 1.2·10⁷ on
h(−4p), the regulator / continued fraction of √p, and the non-abelian bits "2 is a quartic residue",
"2 is a cube", "3 is a cube", controlling for the QR pattern of p. Only h(−4p) shows a signal. That
signal fades as more of its own Euler factors enter the baseline (t falls from 8.5 to 2.5), so it is
congruence data. The quartic bit's marginal t flips sign between two independent samples (−1.94,
then +1.47). Strongest reason for the verdict: once any invariant is fixed, success still needs a
divisor of a specific integer in a moving class. Lemma 3.1 (PROVED, trivial) shows that units of
Q(√p) give no Type II solution at all for p ≡ 1 (4): f = f′ forces p ≡ 3 (4).

**(b) `BRAINSTORM/ident_form_families.md` — PARTIAL (no route to ES).** Topic: identities in a
quadratic parameter, p = t² + k. This is the gap in Thm C's Remark 2, which proves the theorem only
for linear P.
* Lemma 3.1: the character step becomes ray-class data in Q(√−k). For k = 1 the Gaussian class of
  one (t ≡ 0) is a universal trap (PROVED). Thm C therefore extends to p = t² + 1 (CONDITIONAL on H).
* Prop 3.2 (PROVED): every Type II family for a positive-definite quadratic P is old, i.e. all of its
  coordinates are polynomials in p.
* Lemma 3.3 / Prop 3.4 (PROVED algebra): constant-level Type I families exist exactly for
  4c²d = 4m²(m² + k).
  * For k = 1 they miss p ≡ 1 (8).
  * For k = 21 and k = 37 they solve every Mordell-hard prime t² + 21 (24 t-classes mod 9240), resp.
    t² + 37. These are non-congruence sets of hard primes; examples were verified as solutions of 4/p.
* Strongest reason it is not ES: the families cover only density-zero sets of primes, and their
  homogenisation forces v = 1, so there is no 2-variable version. Letting k grow with p brings back
  the B2 lottery.

**(c) `BRAINSTORM/ident_numerators.md` — COLLAPSES to B1 at the class of one, for every m ≥ 4.**
* Lemma 3.1 (PROVED, elementary; known in substance): the class of one lies in no ET-shaped Type I
  or II class iff m ≥ 4. So no numerator m ≥ 4 is provable by finitely many identities.
* What singles out 4 is two separate facts. It is the least m with a sterile class of one, and the
  least m with a sterile odd-square coset. The second needs 4 | m (Schinzel's theorem holds only
  for 4 | m, per Schuh).
* EVIDENCE: for m = 4, 8, 12 there are 0 Type I/II solutions at every odd square s² with s ≤ 45. For
  m = 5, 6, 7, 9, 10, 11, 13 there are many.
* The exceptions up to 3000 have the longest tails for m = 8 and m = 12. For m = 12, every exception
  above 25 is ≡ 1 (24).
* For m = 5 and 7, the class of one mod 840 has the fewest solutions (mean f/log²p). The other square
  classes fall between it and the non-squares. For m = 4, the class of one and the other square
  classes are about equal.

**Process note.** One run of `bs_ident_mn` used 4 cores for about 10 minutes, above the 2-core rule;
everything else ran on 1 core.
**Suggested next steps** (cheap; neither is promising for ES):
* Type I t-families with a non-constant level c(t), d(t).
* An explicit Thm C statement for p = t² + 1 in POINTWISE_SIZE.
