# Literature check: bilinear estimates and short intervals

Sources below were opened/fetched directly; equations are transcribed from their text/PDF extraction. `NOT VERIFIED` means the requested exact statement was not recoverable from a fetched source—not that it is false.

## 1. Heath-Brown, real character sums

**Bibliography:** D. R. Heath-Brown, “A mean value estimate for real character sums,” *Acta Arithmetica* **72** (1995), 235–275. Oxford repository copy: https://ora.ox.ac.uk/objects/uuid:b188b365-d8d1-4267-8548-49f01e6cb6a7/files/m6af40476f1b860392271a2d8ecae593b (fetched PDF).

**Theorem 1 — VERIFIED from source.** With `*` denoting restriction to positive odd square-free integers: for positive integers `M,N`, arbitrary complex `a_n`, and every `ε>0`,
\[
\sum_{m\le M}^{*}\left|\sum_{n\le N}^{*}a_n\left(\frac n m\right)\right|^2
\ll_\epsilon (MN)^\epsilon(M+N)\sum_{n\le N}^{*}|a_n|^2.
\]
The source uses `≪_ε`; the loss and both squarefree/odd restrictions are as displayed.

**Corollary 2 — VERIFIED from source.** Let `S(Q)` be the real primitive characters of conductor at most `Q`. For positive integers `N,Q`, arbitrary complex `a_n`, and every `ε>0`,
\[
\sum_{\chi\in S(Q)}\left|\sum_{n\le N}a_n\chi(n)\right|^2
\ll_\epsilon (QN)^\epsilon(Q+N)\sum_{\substack{n_1,n_2\le N\\n_1n_2=\square}}|a_{n_1}a_{n_2}|.
\]
This is the non-squarefree-variable form; the norm is a sum over ordered pairs with product a square, not an `ℓ²` norm.

**Corollary 4 — VERIFIED from source.** For positive integers `M,N`, arbitrary complex coefficients with `|a_m|,|b_n|≤1`, and every `ε>0`,
\[
\sum_{m\le M}^{\rm odd}\sum_{n\le N}^{\rm odd}a_mb_n\left(\frac n m\right)
\ll_\epsilon (MN)^\epsilon(MN^{1/2}+M^{1/2}N).
\]
The printed statement is an upper bound without absolute-value bars around the whole sum (and thus also bounds its absolute value).

## 2. Bilinear Jacobi-symbol bounds

### (a) Friedlander–Iwaniec

**Bibliography checked:** J. Friedlander and H. Iwaniec, “The polynomial `X²+Y⁴` captures its primes,” *Annals of Mathematics* (2) **148** (1998), no. 3, 945–1040. The publisher page confirms bibliographic data: https://annals.math.princeton.edu/articles/13033. Fetched arXiv author manuscript: https://arxiv.org/pdf/math/9811185.

**Requested generic bound — NOT VERIFIED (reason).** I fetched and searched the manuscript but could not locate the asserted rectangular, arbitrary-unit-coefficient estimate with the remembered `(M^{-1/6}+N^{-1/6})MN(log)^{7/6}` factor, nor identify a theorem number for it. The paper contains extensive specialized bilinear forms, but they are not grounds for attributing this exact general statement to it. I therefore do not certify the bound or its number.

### (b) Conrey–Farmer–Soundararajan

**Bibliography:** J. B. Conrey, D. W. Farmer, and K. Soundararajan, “Transition mean values of real characters,” *Journal of Number Theory* **82** (2000), 109–120. DOI: https://doi.org/10.1006/jnth.1999.2492. Fetched arXiv manuscript: https://arxiv.org/pdf/math/9903197.

**Theorem 1 — VERIFIED from source.** Define
\[
S(X,Y)=\sum_{\substack{m\le X\\m\text{ odd}}}\sum_{\substack{n\le Y\\n\text{ odd}}}\left(\frac mn\right).
\]
Uniformly for all large `X,Y`,
\[
S(X,Y)=\frac{2}{\pi^2}C(Y/X)X^{3/2}
+O\big((XY^{7/16}+YX^{7/16})\log(XY)\big).
\]
For `α≥0`, the paper defines
\[
C(α)=\frac{\sqrt α}{2π}+\frac1{2π}\sum_{k=1}^\infty\frac1{k^2}\int_0^{α}\! y\left(1-\cos\frac{2πk^2}{y}+\sin\frac{2πk^2}{y}\right)dy.
\]
(Formula transcribed from displayed definition; the other equivalent expression in the paper is omitted.) The character is the Jacobi symbol, including its usual zero values; both summation variables are odd, not necessarily squarefree.

## 3. Duke–Friedlander–Iwaniec, Kloosterman fractions

**Bibliography:** W. Duke, J. Friedlander, and H. Iwaniec, “Bilinear forms with Kloosterman fractions,” *Inventiones Mathematicae* **128** (1997), 23–43, https://doi.org/10.1007/s002220050135. Springer page fetched: https://link.springer.com/article/10.1007/s002220050135.

**Theorem 1 requested — NOT VERIFIED (reason).** The fetched journal page provided metadata/abstract-level access only, not the theorem text. I did not recover an accessible author manuscript with the exact theorem statement, so I cannot reliably quote its ranges, coprimality conditions, or norms. The familiar shape of a bound is not substituted for a source-checked theorem.

## 4. Bombieri–Iwaniec double large sieve

**Bibliography checked:** E. Bombieri and H. Iwaniec, “On the order of `ζ(1/2+it)`,” *Annali della Scuola Normale Superiore di Pisa* (4) **13** (1986), no. 3, 449–472. Numdam PDF fetched: https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf.

**Lemma 2.4 requested — NOT VERIFIED (reason).** The PDF text extraction rendered the two bilinear forms and the inequality itself as missing equations/images. The readable text confirms Lemma 2.4 begins with finite point sets `X,W⊂R^K`, arbitrary complex weights, and positive parameters `X_1,…,X_K,Y_1,…,Y_K`; it does not preserve the formula needed to state the constants and spacing sums faithfully. I do not reconstruct it from memory. A precise double-large-sieve inequality with the requested constants therefore remains unverified here.

## 5. Divisor problem in short intervals

### (a) Pointwise interval asymptotic

**Fetched source:** X. Li and X. Yang, “An improvement on Gauss’s circle problem and Dirichlet’s divisor problem,” arXiv:2308.14859v2 (14 Sep 2023), https://arxiv.org/pdf/2308.14859.

**Theorem 1.2 — VERIFIED from source.** The paper states `Δ(X)=O_ε(X^{θ*+ε})` for every `ε>0`, with `θ*=0.3144831759741…`; it defines `−θ*` as the unique root in `[-0.35,-0.3]` of its displayed equation (1.4). Here `Δ(X)=Σ_{n≤X}d(n)−X log X−(2γ−1)X`.

Consequently, for `y=o(x)` and any fixed `η>0`, the standard subtraction of the two summatory formulas gives
\[
\sum_{x<n\le x+y}d(n)=y\log x+2γy+o(y)
\]
uniformly for `y≥x^{θ*+η}`: choose the error-term epsilon smaller than `η`, and note the main-term Taylor remainder is `O(y²/x)=o(y)`. Thus the cited pointwise error exponent supports `θ=0.3144831759741…` in the usual `y=o(x)` short-interval formulation. It does **not** prove that this is an optimal/the best possible threshold. I found no verified pointwise result below `0.3` in the sources fetched for this check; absence from this search is not a nonexistence claim.

### (b) Mean square of short differences (CORRECTED after hostile review 1; re-fetched and read by the lane author)

**Source fetched:** A. Ivić, "On the mean square of the divisor function in short intervals", *J. Théor. Nombres Bordeaux*
**21** (2009), no. 2, 251–261, https://jtnb.centre-mersenne.org/item/10.5802/jtnb.669.pdf (printed pp. 252–254, text
extracted with pypdf). VERIFIED from source:
* (1.7) (Coppola–Salerno, discrete; Jutila, continuous, for k = 2): for X^ε ≤ h ≤ ½√X, L = log X,
  Σ_2(X,h) := Σ_{X≤x≤2X}(Δ(x+h) − Δ(x))² = (8/π²) X h log³(√X/h) + O(X h L^{5/2}√L).
* (1.8) is Jutila's integral representation of I_2(X,h) := ∫_X^{2X}(Δ(x+h) − Δ(x))²dx (a Voronoi-type series) + O_ε(X^{1+ε}h^{1/2});
  (1.9): I_2(X,h) ≍ X h log³(√X/h) for X^ε ≤ h ≤ X^{1/2−ε}. (1.10) concerns the zeta mean-square error E, not Δ.
* (1.12): Δ(x+h) − Δ(x) = Ω(√h log^{3/2}(√x/h)) for x^ε ≤ h ≤ x^{1/2−ε}.
* (1.13) **Jutila's conjecture**: Δ(x+h) − Δ(x) ≪_ε x^ε √h for x^ε ≤ h ≤ x^{1/2−ε} ("close to best possible, in view of (1.12)").
* (1.14) (Ivić): for 1 ≪ U ≤ ½√T, ∫_T^{2T}(Δ(x+U) − Δ(x))²dx = T U Σ_{j=0}^{3} c_j log^j(√T/U) + O_ε(T^{1/2+ε}U²) + O_ε(T^{1+ε}U^{1/2}),
  c₃ = 8π^{−2}.
The earlier transcription in this file (attributing the (1.7)-type asymptotic to the continuous I_2 via (1.8)/(1.10)) was
wrong; use (1.9), (1.14) for the continuous mean square, and (1.13) for the pointwise conjecture.

## 6. Optional: Erdős–Straus representation counts

**NOT VERIFIED (reason).** No source was fetched and checked for post-2018 improvements to the Elsholtz–Planitzer `n^{3/5+ε}` bound, so no newer exponent is reported.

## Summary

| Item | Verified? | One-line statement |
|---|---|---|
| 1 | Yes | Heath-Brown Theorem 1 and Corollaries 2/4 give squarefree mean-square and non-squarefree/bilinear forms with `(MN)^ε` losses. |
| 2(a) | No | The remembered generic Friedlander–Iwaniec Jacobi bound and theorem number were not located in the fetched manuscript. |
| 2(b) | Yes | CFS Theorem 1 gives the uniform transition asymptotic with `7/16` error powers. |
| 3 | No | DFI theorem text inaccessible from fetched journal page. |
| 4 | No | Bombieri–Iwaniec PDF extraction omitted the formula in Lemma 2.4. |
| 5(a) | Yes, as implication | Li–Yang establish `Δ(X)≪εX^{0.3144831759741…+ε}`, implying interval asymptotics above that power for `y=o(x)`. |
| 5(b) | Yes (Ivić 2009, read) | Mean square (1.9)/(1.14) ≍ Xh log³; omega (1.12); Jutila's pointwise conjecture (1.13) Δ(x+h)−Δ(x) ≪ x^ε√h. |
| 6 | No | No newer solution-count exponent verified. |
