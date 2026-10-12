# Brainstorm O149(c): Igusa zeta functions, Berkovich spaces, and the char-p (function-field / perfectoid) transfer

ES is not solved; nothing here proves any case of it. No new script. The local claims rest on Prop A of
`padic_adelic_scaling.md`.

## 1. Idea

Three exotic local-to-global or characteristic-transfer devices:
* **(c1) Igusa / p-adic integration.** Count N_k(n) = #𝒰_n(ℤ/ℓ^k) through Igusa's local zeta function (its
  poles, monodromy-conjecture data), or through motivic integration uniformly in ℓ. Hope: an arithmetic
  invariant of n that is positive exactly when ES(n) holds.
* **(c2) Berkovich analytification** of U_n over ℚ_ℓ, with its skeleton (= tropicalisation; memo (b)), or over
  ℤ "hybrid" spaces that mix archimedean and non-archimedean data.
* **(c3) Char-p transfer.** Perfectoid tilting ℚ_p(p^{1/p^∞})^♭ ≅ 𝔽_p((t^{1/p^∞})), or simply the function-field
  analogue over A = 𝔽_q[T]. There, large-q equidistribution (Deligne/Katz, Sawin-type) sometimes yields
  theorems that are open over ℤ. Hope: prove an A-analogue of ES, and read off what the ℤ-proof would need.

## 2. Literature anchor

* Igusa, *An introduction to the theory of local zeta functions* (AMS/IP 2000), from memory. Denef–Loeser
  motivic integration, from memory.
* Berkovich, *Spectral theory and analytic geometry over non-archimedean fields* (1990), from memory.
  Skeleton = tropicalisation: Payne, Baker–Payne–Rabinoff, from memory.
* Scholze, *Perfectoid spaces* (2012), from memory. Tilting identifies Galois groups and étale sites. It does not
  identify integer points of varieties over ℤ, and it does not see the archimedean place.
* Function-field Erdős problems in the large-q limit: L. Xie, *On a conjecture of Erdős over function fields*,
  arXiv:2510.17612. This concerns a *different* Erdős conjecture; checked by web search, abstract only.
* No campaign file or web hit treats ES over 𝔽_q[T] (git grep of the repo; one web search, negative).
  Novelty of §3.3 is unverified.

## 3. Results

**3.1 Igusa and Berkovich data are local (PROVED, from Prop A).** N_k(n), the Igusa zeta function Z_ℓ(s; n),
its poles, and the Berkovich space U_n^{an} over ℚ_ℓ are invariants of 𝒰_n ⊗ ℤ_ℓ. So they depend only on
v_ℓ(n) (Cor A1). For prime p, they do not distinguish p mod q. They take identical values at primes and at
odd-square-adjacent primes, while the counts differ by a factor > 3 between classes. Hybrid/adelic Berkovich
spaces add the archimedean place, but the archimedean data are also n-independent up to scaling (Prop A). The
integrality interplay is the global ℚ-structure, i.e. the denominator problem of Prop C.

**3.2 Tilting does not transfer the problem (Assessment, near-trivial).**
* ES(p) is a statement about ℤ-points with a positivity condition.
* Tilting changes the base field ℚ_p (a single place) and has no effect on ℤ or on ℝ.
* At the place p, the local problem is already solvable. Local data are all "yes" (Prop 8.3 of
  POINTWISE_TYPEII_SPECTRAL, BL), so there is nothing to transfer.

**3.3 The function-field analogue is ill-posed in two instructive ways (PROVED, elementary).** Let
A = 𝔽_q[T] with q odd.
* (i) *A constant numerator trivialises the problem.* For c ∈ 𝔽_q^×, c/P = 1/X + 1/Y + 1/Z always has the
  solution X = 2c⁻¹P, Y = Z = 4c⁻¹P. The numerator "4" is a unit, so the analogue must use a numerator
  M ∈ A of positive degree. ET's square obstruction needs M to be a square (POINTWISE_MN dichotomy), so the
  natural choice is M = Q² with Q irreducible.
* (ii) *There is no positivity.* "Monic" is the analogue of "positive", but it does not forbid cancellation
  at ∞. Suppose all X_i are monic and exactly k of them have the minimal degree e. Then the leading term of
  Σ1/X_i is k·T^{−e}. So either k ≠ 0 in 𝔽_q, and then k = 1 and e = deg P − deg M (one dominant term), or
  k ≡ 0 (mod char) and cancellation occurs. The true archimedean condition (every 1/x_i < 4/n strictly, and no
  cancellation) has as its tropical analogue "|1/X_i|_∞ ≤ |M/P|_∞ for all i". This is an ultrametric condition
  and much weaker than an order.

**3.4 What large-q equidistribution could give (Assessment; the mechanism is the point).**
* Fix d = deg P and let q → ∞. The relevant parameters (ET's a, c, d, e analogues) have degree ≤ d, so they
  form finitely many algebraic families. "Some N_θ(P) has a divisor in a class" becomes a condition on the
  Frobenius of P in a fixed monodromy group G.
* Chebotarev with error O(q^{−1/2}) then gives: either the bad set C ⊂ G is empty, and the analogue holds for
  *every* P of degree d once q is large; or C ≠ ∅, and a positive proportion of P fail.
* So in this regime pointwise truth is the statement "C = ∅", which is a *finite covering of a group*. Over ℤ,
  the corresponding statement is a covering by finitely many families of fixed degree. That is exactly what
  Theorem C / Mordell (B1) and redteam-2 Thm 2.2(iii) (B2) exclude: the square classes are never covered.
* Over A the analogue of the square obstruction (ET Prop 1.6 via reciprocity in A) puts the "square" Frobenius
  classes into C, unless the degrees of the moduli reach d. The bounded-q, d → ∞ regime is the true analogue of
  ES, and there the large-q tools give nothing.

## 4. Barrier screen

* **B1.** (c1), (c2): local invariants are congruence/Haar data (Cor A1). (c3) in the large-q limit: a finite
  group covering, i.e. a Frobenius-congruence covering, exactly Theorem C in disguise.
* **B2.** Bounded-degree families = a fixed finite set of slices, which fail on the square classes.
* **B3.** In the large-q limit the expected count is bounded in q (a product of probabilities over finitely
  many families). Pointwise truth must therefore come from C = ∅, not from a main term.
* **B5 / T1.** At odd squares the local and tilted data are all "yes". The failing step is "local
  everywhere ⇒ global", as for BM.
* **B6.** Chebotarev in G is a statement about proportions of P. It becomes pointwise only through C = ∅.

## 5. Viability Assessment

**COLLAPSES.**
* (c1) and (c2) collapse to B1 at the very first step, since they are local invariants (Prop A).
* (c3) collapses to B1/B2: in the only regime where function-field tools are strong (q → ∞, d fixed), pointwise
  truth means a finite group covering, which is the function-field image of the excluded polynomial-covering
  route.

Sub-question left **UNCLEAR**, as a possible small side theorem rather than an ES route: for M = T² and fixed
small d, is C = ∅ in the monodromy group? That is, does the A-analogue (with the tropical no-cancellation
condition) hold for all irreducible P of degree d and all large q?
* If yes, the reason must be that the moduli reach degree d, the analogue of "Type II moduli must exceed
  exp(c(log p)^{1/4})".
* Deciding it needs a brute-force search over 𝔽_q[T] for small q and d ≤ 4. This was not done (budget).
