# Literature verification

## 1. Shimura’s half-integral-weight Hecke formula

**Exact statement/formula.** In Shimura’s notation, for an odd integer `k=2λ+1`, a Fourier expansion `f(z)=Σ a(n)q^n`, and an odd prime `p` prime to the level, the `T(p²)` coefficient formula is

> `b(n)=a(p²n)+ψ(p) ((−1)^λ n/p) p^{λ−1}a(n)+ψ(p²)p^{k−2}a(n/p²)`.

Here `(·/p)` is the Legendre symbol, `a(x)=0` unless `x` is a nonnegative integer, and `ψ` is the Dirichlet character in the half-integral-weight transformation law; thus the middle symbol is `( ((−1)^λ n)/p )`. Some sources write the middle character term as `ψ(p)( ((−1)^λ n)/p )` and the last as `ψ(p²)p^{k−2}`. Be careful: formulations of the operator normalized by a factor `p^{−(k−2)}` or with different character conventions redistribute powers/characters.

**Source.** G. Shimura, “On modular forms of half integral weight,” *Annals of Mathematics* 97 (1973), 440–481, Theorem 1.7. JSTOR record: https://www.jstor.org/stable/1970831. Textbook cross-reference: N. Koblitz, *Introduction to Elliptic Curves and Modular Forms*, GTM 97, Springer, 1984/1993, Chapter IV, §3, Proposition 13; Google Books: https://books.google.com/books?id=99v9XcOjhO4C.

**How verified.** Shimura paper record and theorem heading/snippet verified; theorem text itself was not available for full page-by-page collation here. Koblitz location verified by bibliographic/search record, not full text. The displayed conventional formula is provided with the normalization caveat; confidence: **medium** (verify character convention against an owned scan before quoting as a verbatim transcription).

## 2. Duke–Schulze-Pillot ternary representation theorem

**Exact theorem statement (the safe theorem-level formulation).** Their main result is an asymptotic formula for primitive representations of positive integers by a positive-definite ternary quadratic form, with the main term the genus (equivalently, in the theorem’s setup, spinor-genus) average and an error that is smaller as the integer grows, subject to the local divisibility restriction at anisotropic primes. In particular it implies that sufficiently large locally represented integers satisfying that restriction are represented by the form. The exceptional anisotropic-prime condition is that the valuations of `n` at those primes are bounded; the result is ineffective because the error estimate uses Siegel’s theorem.

**Source.** W. Duke and R. Schulze-Pillot, “Representation of integers by positive ternary quadratic forms and equidistribution of lattice points on ellipsoids,” *Inventiones Mathematicae* 99 (1990), 49–58 (often cited as 49–57), main theorem. EuDML record: https://eudml.org/doc/143750; publisher record: https://link.springer.com/article/10.1007/BF01234411.

**How verified.** EuDML/publisher bibliographic records read; primary full text not accessible in this verification. The description above is a paraphrase, **not** an exact quotation. Exact theorem hypotheses and its precise asymptotic error should be checked in the article before citation. Confidence: **medium-low**.

## 3. Iwaniec’s coefficient bound and Duke’s weight-3/2 extension

**Iwaniec source/result.** H. Iwaniec, “Fourier coefficients of modular forms of half-integral weight,” *Inventiones Mathematicae* 87 (1987), 385–402 (the commonly cited pagination is 385–401), https://eudml.org/doc/143426. The result generally cited from this paper is, for a fixed holomorphic cusp form of half-integral weight `k/2` with `k` odd and `k/2 ≥ 5/2`, a squarefree-index bound of the shape

> `a(n) ≪ n^{k/4−1/4−1/28+ε}`

when the weight is denoted `k/2` (equivalently, with weight `κ`, `a(n) ≪ n^{κ/2−1/4−1/28+ε}`). This notation distinction matters: the proposed exponent `k/2−1/2−1/28` is equivalent if the symbol `k` denotes the full odd numerator of the weight. The bound applies to squarefree `n`; constants depend on the form and `ε`.

**Duke extension.** W. Duke, “Hyperbolic distribution problems and half-integral weight Maass forms,” *Inventiones Mathematicae* 92 (1988), 73–90, https://www.math.ucla.edu/~wdduke/preprints/hyperbolic.pdf. Duke’s work treats the weight-`3/2` case using half-integral-weight Maass forms, extending the coefficient estimate/related distribution result to this lowest relevant weight; it is not a blanket replacement of Iwaniec’s holomorphic theorem in all weights.

**How verified.** Iwaniec bibliographic record read at EuDML; Duke PDF search record and its introduction read (it explicitly says Iwaniec gave an estimate for holomorphic cusp forms of half odd-integral weight). Exact Iwaniec theorem statement not fully checked against the paper. Confidence: **medium**; exponent above clarified by distinguishing `k` (odd numerator) from actual weight `κ=k/2`.

## 4. Waldspurger and Kohnen–Zagier central-value formula

**Exact quotation (Kohnen–Zagier, Theorem 1).** For a normalized Hecke eigenform `f∈S_{2k}` on `SL₂(Z)`, and its corresponding form `g=Σc(n)q^n∈S_{k+1/2}` on `Γ₀(4)`, for a fundamental discriminant `D` with `(-1)^kD>0`, their displayed theorem is

> `c(|D|)²/(g,g) = ((k−1)!/(π^k)) · |D|^{k−1/2} · L(f,D,k)/(f,f)`.

The paper’s formula is printed as equation (3) in Theorem 1. For arbitrary scaling of `g`, use `|c(|D|)|²`; the theorem’s normalization conventions for Petersson products are stated immediately there. This is the level-one case; Kohnen’s later work treats odd squarefree levels under the corresponding newform/plus-space hypotheses.

**Source.** W. Kohnen and D. Zagier, “Values of L-series of modular forms at the center of the critical strip,” *Inventiones Mathematicae* 64 (1981), 175–198, Theorem 1; full PDF: https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01389166/fulltext.pdf. J.-L. Waldspurger, “Sur les coefficients de Fourier des formes modulaires de poids demi-entier,” *Journal de Mathématiques Pures et Appliquées* 60 (1981), 375–484 (general representation-theoretic formula; KZ cite the 1981 result).

**How verified.** Read the full Kohnen–Zagier PDF, including Theorem 1 and equation (3). Note its exact printed coefficient is `((k−1)!/π^k)`, under its Petersson norm conventions. Confidence: **high** for level one; the wider odd-squarefree-level statement is not quoted as KZ Theorem 1.

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

## 9. Corrections after internal review (lane)
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
