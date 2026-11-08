# z65 LOGIC2 — literature verification (done by the lane itself; the research subagents failed with an expired
# auth token, so every check below was made directly by the lane, 2026-11-08)

Verdicts: VERIFIED (primary text or the publisher/indexer abstract read by the lane, quoted) / PARTLY / NOT FOUND.
Tools: author PDF (curl + pdftotext), OpenAlex API abstracts (`api.openalex.org/works?search=…`), Jina web search
snippets. Semantic Scholar and ScienceDirect pages were captcha/rate-limited.

## 1. Jeřábek, *Abelian groups and quadratic residues in weak arithmetic*, MLQ 56 (2010) 262–278 — VERIFIED
Author PDF `users.math.cas.cz/~jerabek/papers/flt.pdf` (archived: `jerabek_2010_abelian_qr.pdf`), read.
* Abstract: "We prove the quadratic reciprocity theorem (including the supplementary laws) in the arithmetic theories
  T⁰₂ + Count₂(PV) and IΔ₀ + Count₂(Δ₀) with modulo-2 counting principles."
* **Theorem 5.7**: "T⁰₂ + Count₂(PV) and IΔ₀ + Count₂(Δ₀) prove the law of quadratic reciprocity (p/q)(q/p) =
  (−1)^{(p−1)(q−1)/4}, the supplementary laws (−1/p) = (−1)^{(p−1)/2}, (2/p) = (−1)^{(p²−1)/8}, and multiplicativity
  of the Legendre symbol … where p, q are distinct odd primes". The Legendre symbol is *defined* by squareness
  (Def. 5.2: [a|p] = 0 iff a ≡ □ (mod p)), so (a|p) = 1 means "a is a square mod p" — no counting is hidden in the
  definition. p, q range over all (also nonstandard) primes of the model.
* **Theorem 5.8**: the Jacobi symbol has a Δ₀-definition in IΔ₀, and S¹₂ + Count₂(PV), IΔ₀ + Count₂(Δ₀) prove its
  laws (congruence invariance, multiplicativity in both arguments, gcd(a, n) ≠ 1 ↔ (a/n) = 0, reciprocity for odd
  positive m, n, supplementary laws).
* **Theorem 4.2**: S²₂ + iWPHP(PV) + PHP(PV) proves Fermat's little theorem. **Theorem 4.6** (in S¹₂): Euler's
  criterion ⟺ FLT ∧ ∃a a^{(p−1)/2} ≡ −1 (mod p). **Theorem 4.7**: S²₂ + iWPHP(PV) + PHP(PV) proves Euler's criterion.
* Directly after Thm 5.7 (p. 20; re-checked in the Astra retro review): "Lagrange's four-square theorem is also
  provable in IΔ₀ + Count₂(Δ₀)." So Lag in IΔ₀ + Count₂(Δ₀) is Jeřábek's explicit statement (VERIFIED as a statement;
  the underlying Berarducci–Intrigila proof was **not** independently read).
* Introduction (a primary source *reporting* other results; not re-read in the originals): "the proof of infinitude of
  prime numbers in IΔ₀ + WPHP(Δ₀) by Paris et al. [22], the proof of Lagrange's four-square theorem in IΔ₀ + WPHP(Δ₀)
  by Berarducci and Intrigila [2], the proof of the prime number theorem in IΔ₀ + exp by Cornaros and Dimitracopoulos
  [8]"; "The supplementary laws were proved by Berarducci and Intrigila [2] in IΔ₀ extended with modular counting
  principles"; "Mod-2 counting by involutions was used to prove Fermat's theorem on sums of two squares by Heath-Brown
  [12] and Zagier [24]" (no formalisation claimed). Status of these four: PARTLY (via Jeřábek).

## 2. Otero, *Quadratic forms in normal open induction*, JSL 58 (1993) 456–476 — VERIFIED (abstract, OpenAlex)
> "Here we study the problem of representability of an element a of a model M of NOI (in some extension of M) by a
> quadratic form of the type X² + bY² where b is a nonzero integer. Using either a trigonometric or a hyperbolic
> parametrization we prove that except in some trivial cases, M[x, y] with x² + by² = a can be embedded in a model of
> NOI. We also study quadratic extensions of a model M of NOI; we first prove some properties of the ring of Gaussian
> integers of M. Then we study the group of solutions of a Pell equation in NOI …"
No theorem numbers accessed. Relevance: prior art for making a given element a sum of two squares inside NOI (our
Thm T does it by design for one prime; Otero's embedding does it for an arbitrary element, without control of ES).

## 3. Mohsenipour, *A Bezout computable nonstandard model of open induction* (2006, talk abstract) — VERIFIED (abstract)
OpenAlex record (no venue/DOI). Quotes:
> "Attempts in the first direction were culminated in the work of Wilmers [10] where it is shown that IE1 does not have a
> computable nonstandard model"; "We mention that GCD is stronger than normality, Bezout is stronger than GCD and Bezout
> is weaker than IE1"; "In [4] we succeeded to strengthen Berarducci-Otero's construction by combining their method
> with that of Smith [7] (which is itself a generalization of Macintyre-Marker's work to the GCD and Bezout case) and
> obtained a nonstandard computable model of Iopen+GCD+cof(prime). In this talk, we go one step further by bringing all
> of these materials together (Smith's chains, Berarducci-Otero's computable construction and Moniri's transseries) to
> produce a computable nonstandard model of Open Induction which is Bezout and has cofinal primes."
Status of the Bezout model itself: PARTLY (talk abstract only; no paper with proofs located).

## 4. Smith, *Building discretely ordered Bezout domains and GCD domains*, J. Algebra 159 (1993) 191–239 — PARTLY
Abstract text visible only as a search-engine snippet (ScienceDirect/ResearchGate): "Using constructions due to
A. Macintyre and D. Marker, we build GCD domains and Bezout domains with the open induction property. In fact we show
that an open induction domain can be a principal ideal domain different from Z. The rings we construct are all
countable or of cardinality ℵ₁; we show that the order type of the infinite primes is arbitrary for GCD domains …"
Theorem numbers: NOT FOUND.

## 5. Wilmers, *Bounded existential induction*, JSL 50 (1985) 72–90 — PARTLY
OpenAlex abstract (first part) read: it recalls Tennenbaum (no nonstandard recursive model of PA), Shepherdson
(recursive nonstandard IOpen models) and McAloon ("even for the weaker system of arithmetic with only bounded
induction, neither the addition nor the multiplication of a nonstandard model could be recursive"). The IE₁
non-computability result is attributed to Wilmers by Mohsenipour (item 3). Theorem number: NOT FOUND.

## 6. Smith, *Fermat's last theorem and Bezout's theorem in GCD domains*, JPAA 79 (1992) — via U64 `lit_models.md` §6
"We show that IE1 ⊢ IOpen + Bez" (publisher abstract, VERIFIED there). Not re-checked here.

## 7. Macintyre–Marker, *Primes and their residue rings in models of open induction*, APAL 43 (1989) 57–77
Bibliographic record VERIFIED (OpenAlex, DOI 10.1016/0168-0072(89)90025-0); no abstract available; contents NOT FOUND.
D'Aquino–Macintyre arXiv:2102.00295 abstract (VERIFIED, arXiv): Macintyre's earlier paper "gave a systematic analysis
of definability and decidability for rings M/pM, where M is a model of Peano Arithmetic and p is a prime in M".

## 8. D'Aquino–Macintyre, *Non-standard finite fields over IΔ₀ + Ω₁*, Israel J. Math. 117 (2000) 311–333 — NOT FOUND
Only the indexer snippet "This paper begins to develop a theory of binary quadratic forms over weak fragments of Peano
Arithmetic" was visible. No theorem used.

## 9. Not found (searched, nothing usable)
* Dirichlet's theorem for nonstandard moduli in IΔ₀ + exp (or genus theory of binary quadratic forms in weak
  arithmetic): NOT FOUND. Hence "IΔ₀ + exp ⊢ NR" is left OPEN in the memo.
* Any paper on ES / Egyptian fractions in weak arithmetic: NOT FOUND.

## Summary
1. QR (with supplementary laws, all moduli) is provable in IΔ₀ + Count₂(Δ₀) (Jeřábek Thm 5.7); Jacobi symbols are
   Δ₀-definable in IΔ₀ with their laws provable in IΔ₀ + Count₂(Δ₀) (Thm 5.8).
2. FLT / Euler's criterion: S²₂ + iWPHP(PV) + PHP(PV) (Jeřábek Thms 4.2, 4.7).
3. Lagrange in IΔ₀ + WPHP(Δ₀) (Berarducci–Intrigila), infinitely many primes in IΔ₀ + WPHP(Δ₀) (PWW), PNT in
   IΔ₀ + exp (Cornaros–Dimitracopoulos): all as reported in Jeřábek's introduction.
4. NOI models: x² + by² = a can be solved in an NOI extension (Otero 1993 abstract).
5. OI + Bez models with infinite primes exist: Smith 1993 (even a PID ≠ ℤ, abstract snippet); a computable Bezout
   model with cofinal primes is announced by Mohsenipour 2006 (talk abstract).
6. IE₁ has no computable nonstandard model (Wilmers; via Mohsenipour's abstract).

## Access limits (added after the Astra retro review)
* **Shepherdson 1964** (integer-part criterion): the original was **not** read; the memo relies on BO Thm 1.1's
  statement of it (BO p. 2, checked). The RCIN archive copy is restricted to Institute terminals. Original-source
  verification incomplete.
* **Smith 1993**: only an abstract snippet; the full construction was not read.
* **Berarducci–Intrigila**: only as reported by Jeřábek; the proof was not read.
