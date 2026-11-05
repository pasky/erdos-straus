# Literature verification

## 1. Shimura’s half-integral-weight Hecke formula

**Exact statement/formula.** In Shimura’s notation, for an odd integer `k=2λ+1`, a Fourier expansion `f(z)=Σ a(n)q^n`, and an odd prime `p` prime to the level, the `T(p²)` coefficient formula is

> `b(n)=a(p²n)+ψ(p) ((−1)^λ n/p) p^{λ−1}a(n)+ψ(p²)p^{k−2}a(n/p²)`.

Here `(·/p)` is the Legendre symbol, `a(x)=0` unless `x` is a nonnegative integer, and `ψ` is the Dirichlet character in the half-integral-weight transformation law; thus the middle symbol is `( ((−1)^λ n)/p )`. Some sources write the middle character term as `ψ(p)( ((−1)^λ n)/p )` and the last as `ψ(p²)p^{k−2}`. Be careful: formulations of the operator normalized by a factor `p^{−(k−2)}` or with different character conventions redistribute powers/characters.

**Source.** G. Shimura, “On modular forms of half integral weight,” *Annals of Mathematics* 97 (1973), 440–481, Theorem 1.7. JSTOR record: https://www.jstor.org/stable/1970831. Textbook cross-reference: N. Koblitz, *Introduction to Elliptic Curves and Modular Forms*, GTM 97, Springer, 1984/1993, Chapter IV, §3, Proposition 13; Google Books: https://books.google.com/books?id=99v9XcOjhO4C.

**How verified.** Shimura paper record and theorem heading/snippet verified; theorem text itself was not available for full page-by-page collation here. Koblitz location verified by bibliographic/search record, not full text. The displayed conventional formula is provided with the normalization caveat; confidence: **medium** (verify character convention against an owned scan before quoting as a verbatim transcription).

## 2. Duke–Schulze-Pillot ternary representation theorem

**Source.** W. Duke and R. Schulze-Pillot, "Representation of integers by positive ternary quadratic forms and
equidistribution of lattice points on ellipsoids", Invent. Math. 99 (1990) 49–57. Primary scan
https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0099/LOG_0011.pdf (pp. 54–56 read by the z58 cross-model
reviewer; this file's earlier paraphrase from metadata is replaced).

**Statements used.** Theorem 2(i): the genus representation number is the product of local densities (Siegel).
Theorem 2(ii): spinor-genus and genus averages differ only on finitely many square classes t·m². Lemma 4(i): θ_L − θ_{gen L}
is a cusp form. Lemma 4(ii) and the paragraph after it: the orthogonal complement U^⊥ of the unary theta series consists of
the forms whose Shimura lifts are cuspidal (general level). Theorem 3 and its Corollary (p. 56): an asymptotic for
representations with error n^{1/2−1/28+ε}, whose main term is the **spinor-genus** average, under square-part /
congruence restrictions; the Corollary requires primitive representation by the spinor genus. It is *not* "every
sufficiently large locally represented integer" without these qualifications. Large good primes avoid the finitely
many exceptional square classes. Confidence: high (primary scan, via reviewer).

## 3. Iwaniec's coefficient bound and Duke's weight-3/2 extension

**Iwaniec.** H. Iwaniec, "Fourier coefficients of modular forms of half-integral weight", Invent. Math. 87 (1987)
385–401, Theorem 1, p. 386 (primary scan https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0087/LOG_0022.pdf,
read by the cross-model reviewer): for a cusp form of actual weight κ ≥ 5/2 and squarefree n,
|a(n)| ≪ n^{κ/2 − 2/7} τ(n)(log 2n)², i.e. exponent κ/2 − 1/4 − 1/28.

**Duke.** W. Duke, "Hyperbolic distribution problems and half-integral weight Maass forms", Invent. Math. 92 (1988)
73–90 (https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf): eq. (1.2) recalls Iwaniec's bound; p. 76 states
that Theorem 5 includes holomorphic weight 3/2, giving exponent 13/28 = 3/4 − 2/7 for weight 3/2 (squarefree n, forms
orthogonal to unary thetas; DSP Lemma 2 gives the general-character version). Duke's Theorem 1 concerns fundamental
discriminants and a fixed region, not exact hypercycle incidences. Confidence: high (primary, via reviewer).

## 4. Waldspurger and Kohnen–Zagier central-value formula

**Waldspurger.** J.-L. Waldspurger, "Sur les coefficients de Fourier des formes modulaires de poids demi-entier",
J. Math. Pures Appl. 60 (1981) 375–484; primary PDF https://mate.dm.uba.ar/~nsirolli/files/waldspurger.pdf (I §§1–4,
Corollary 2 p. 379, proof pp. 483–484, read by the cross-model reviewer). His level N is the memo's 4N, his weight
numerator k is 3; weight 3/2 is restricted to U^⊥. With χ₀ = ψχ_{−1} the relevant twist is φ ⊗ χ₀^{−1}χ_t = φ ⊗ ψ̄χ_{−t}
(= χ_{−4p} for ψ = 1, p ≡ 1 (4)). **Corollary 2:** if n₁/n₂ ∈ ℚ_q^{×2} for every q dividing the level, then
a(n₁)²·L(½, φ ⊗ ψ̄χ_{−n₂})·ψ(n₂/n₁)·n₂^{1/2} = a(n₂)²·L(½, φ ⊗ ψ̄χ_{−n₁})·n₁^{1/2}. It requires neither odd N/4 nor complete
bad-prime eigenvectors; the proof's last paragraph removes (H2) in the same 2-adic square class, and (H1) is automatic if
the half-integral eigenspace exists (Prop. 2). A 0 = 0 ratio (all L-values vanishing) gives nothing. The general
factorisation "a(t)² = C(class of t)·t^{1/2}·L(½, …)" used as (W-loc) in the memo is not asserted by this corollary and
stays a hypothesis; for non-quadratic ψ the factor ψ(n₂/n₁) must be kept.

**Kohnen–Zagier.** W. Kohnen and D. Zagier, Invent. Math. 64 (1981) 175–198, Theorem 1 (full PDF read:
https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01389166/fulltext.pdf): for level one and g in the plus space,
c(|D|)²/⟨g,g⟩ = ((k−1)!/π^k)·|D|^{k−1/2}·L(f, D, k)/⟨f,f⟩. The plus space vanishes at n ≡ 1 (mod 4) in weight 3/2, so it is
not the relevant statement for p ∈ 𝔐. Confidence: high.

**Secondary.** C. Darreye, arXiv:2007.06224 §2 (read): Shimura/Niwa lift and a Waldspurger statement for N odd and
complete eigenforms, twist ((−1)^k t/·)χ.

## 5. Cohen Eisenstein series and Hurwitz class numbers

**Cohen series.** H. Cohen, “Sums involving the values at negative integers of L-functions of quadratic characters,” *Mathematische Annalen* 217 (1975), 271–285 (bibliographies sometimes give 277–285; use journal record pagination), DOI/search record: https://link.springer.com/article/10.1007/BF01436232. The coefficient construction is commonly denoted `H(r,n)`; Cohen proves that `Σ_{n≥0} H(r,n)q^n` is a modular form of weight `r+1/2` on `Γ₀(4)` (for positive integer `r`, with the appropriate parity condition). Kohnen–Zagier explicitly recall this: their full text says “The space `M_{k+1/2}` is generated by … an Eisenstein series `G_{k+1/2}` (found by Cohen [1]) whose constant term is `ζ(1−2k)` and whose `[|D|]`th Fourier coefficient for `(-1)^kD>0` is `L_D(1−k)`.”

**Hurwitz class number identity.** For negative fundamental discriminant `D`, the standard imprimitive-discriminant relation, in the usual Hurwitz convention, is

> `H(|D|f²)=H(|D|) Σ_{d|f} μ(d)χ_D(d) σ₁(f/d)`.

Here `χ_D=(D/·)`, `σ₁(m)=Σ_{e|m}e`, and `H(|D|)=h(D)/(w(D)/2)` with `w(D)` the number of units of the quadratic order (so the exceptional unit factors for `D=−3,−4` are included). Check the convention for `H` when applying to nonfundamental discriminants; references sometimes use a rescaled class-number function.

**Zagier series.** D. Zagier, “Nombres de classes et formes modulaires de poids 3/2,” *Comptes Rendus de l’Académie des Sciences de Paris* 281 (1975), 883–886. The result is that the generating series of Hurwitz class numbers occurs as the holomorphic part of a non-holomorphic modular form of weight `3/2` (the completed series, not the holomorphic series alone, is modular). Scan/record: https://people.mpim-bonn.mpg.de/zagier/ (publication list); Cohen paper above.

**How verified.** Cohen-series description corroborated by KZ’s full PDF (read); stated Zagier/Cohen bibliographic sources and standard class-number identity not independently collated against the original pages. The formula and Zagier wording are standard-convention paraphrases, not verbatim quotations. Confidence: **medium**.

## 6. Quadratic-twist nonvanishing and Goldfeld

**Conjecture / proved proportion.** Goldfeld’s conjecture predicts that, in a quadratic-twist family of an elliptic curve over `Q`, 50% of twists have analytic rank 0 and 50% rank 1 (with root-number signs determining the parity). A positive proportion, rather than the conjectural 50%, is proved in important settings. The abstract of D. Kriz and C. Li, “Goldfeld’s conjecture and congruences between Heegner points,” *Forum of Mathematics, Sigma* 7 (2019), e15, says:

> “Given an elliptic curve E over Q, a celebrated conjecture of Goldfeld asserts that a positive proportion of its quadratic twists should have analytic rank 0 (respectively 1).”

Their work establishes Goldfeld-type positive-proportion results under specified hypotheses; it is not a theorem of nonvanishing for every sufficiently large prime twist in a progression. Ono–Skinner, “Non-vanishing of quadratic twists of modular L-functions,” *Inventiones Mathematicae* 134 (1998), 651–660, proves quantitative positive-proportion results for twists, with hypotheses and twist families stated in their paper; do not summarize this as universal nonvanishing at all primes.

**Prime twists / arithmetic progressions.** No general theorem is known asserting `L(1/2,f⊗χ_p)≠0` for **all sufficiently large primes** `p` in an arithmetic progression. Functional-equation sign `−1` forces central vanishing on the corresponding classes; even in sign `+1` classes current positive-proportion results do not imply every sufficiently large prime works. This “no general theorem” statement is a literature-status conclusion, not a quoted theorem.

**Sources.** Kriz–Li paper and abstract: https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/goldfelds-conjecture-and-congruences-between-heegner-points/05E581EF286E02A8B4D681096E24E709 ; preprint https://arxiv.org/abs/1609.06687. Ono–Skinner record/search: https://www.researchgate.net/publication/226227590_Non-vanishing_of_quadratic_twists_of_modular_L-functions.

**How verified.** Kriz–Li abstract read via search result/record; primary Ono–Skinner abstract not directly accessed. Confidence: **high** on positive-proportion versus universal distinction; **medium** on precise hypotheses of the cited older theorems (not transcribed here).

## 7. Siegel’s lower bound

**Statement.** For every `ε>0` there is a positive constant `c(ε)` such that for every fundamental discriminant `D<0`,

> `L(1,χ_D) ≥ c(ε)|D|^{−ε}`.

The constant is ineffective: Siegel’s theorem does not provide an effective value of `c(ε)`.

**Source.** H. Davenport, *Multiplicative Number Theory*, 3rd ed., revised by H. L. Montgomery, Graduate Texts in Mathematics 74, Springer, 2000, Chapter 21 (Siegel’s theorem). Google Books: https://books.google.com/books?id=0Q8ZBQ9C9lAC. Equivalent standard formulations state `L(1,χ) ≫_ε q^{−ε}` for real primitive characters of conductor `q`.

**How verified.** Standard textbook theorem citation and statement; book page not directly read here. Confidence: **high** on theorem and ineffectivity; edition/page-number details should be checked against the chosen copy.

## 8. (added by lane) Shimura lift in weight 3/2 — cuspidality on the complement of unary thetas
Secondary source read (PDF text): C. Darreye, "Sign of Fourier coefficients of half-integral weight modular forms in
arithmetic progressions", arXiv:2007.06224, §2: "Shimura [S1] and Niwa [N] showed that the function Sh f … is a complete
Hecke eigenform in S_{2ℓ}(2N, χ²) whenever ℓ ≥ 2. For ℓ = 1, this holds if one assumes that f is in the orthogonal
complement of the subspace spanned by single variable theta-functions", followed by (2.1)
a(tn²)n^{ℓ−1/2} = a(t) Σ_{d|n} μ(d)(((−1)^ℓ t)/d) χ(d) d^{ℓ−1} λ(n/d) (normalized coefficients) and Deligne's bound.
Primary (Shimura 1973; Niwa, Nagoya Math. J. 56 (1975)) not re-read. Confidence: medium-high (standard statement).

## 9. Corrections after internal review (lane; §§2–4 above were rewritten in place after the cross-model review)
* §2 (Duke–Schulze-Pillot): the theorem concerns primitive representations with bounded divisibility at anisotropic
  primes and has spinor-exception qualifications (finitely many square classes t·m²); genus and spinor-genus averages
  are not interchangeable for all integers. The memo only uses it for large primes outside those classes.
* §3 (Iwaniec): the stated "equivalent" exponent k/2 − 1/2 − 1/28 is a typo; for weight k/2 (k odd) the bound is
  a(n) ≪ n^{k/4 − 1/4 − 1/28 + ε}; at weight 3/2 (via Duke 1988) this is n^{13/28+ε}.
* §5 (Cohen): the holomorphic Cohen–Eisenstein statement is for r ≥ 2; r = 1 (weight 3/2) is Zagier's non-holomorphic
  case and must not be treated as holomorphic.
* §6: positive-proportion results hold under their stated hypotheses; no blanket attribution to every twist family.
* §8 (Waldspurger in general level): Darreye's §2 statement assumes N odd and complete eigenforms and twists by
  ((−1)^k t/·)χ; the even-level (N = 210) local-class form used in the memo is hypothesis (W-loc), not verified here.
