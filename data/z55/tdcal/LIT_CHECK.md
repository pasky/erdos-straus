# Literature check: short divisor intervals and related questions

**Scope/status rule.** VERIFIED-PRIMARY means I inspected the cited paper/PDF itself. VERIFIED-SECONDARY means I inspected a named secondary source. UNVERIFIED means no primary statement was checked; it is not a negative result. Quotes below are verbatim or close transcription; OCR mathematical typography is normalized. This is a partial literature audit, not an exhaustive proof that no result exists. The queried bibliography/details left UNVERIFIED are intentionally not reconstructed from memory.

## Q1. Pointwise short-interval divisor asymptotic

**VERIFIED-PRIMARY — X. Li and X. Yang, “An improvement on Gauss’s Circle Problem and Dirichlet’s Divisor Problem,” arXiv:2308.14859v2 (2023), Theorem 1.2 and Definition 1.1, pp. 2–3 (PDF).** Quote: “R(X)=Oε(X^{θ*+ε}) and Δ(X)=Oε(X^{θ*+ε}) for all ε>0,” where “θ*=0.314483…”; Definition 1.1 gives θ*=0.3144831759741…. The paper says the preceding Huxley divisor exponent was 131/416. This improves the pointwise Δ bound. It does **not** state a short-difference estimate or a short-interval asymptotic.

**VERIFIED-PRIMARY — A. Ivić, “On the mean square of the divisor function in short intervals,” J. Théorie des Nombres de Bordeaux 21 (2009), 251–261, introduction equations (1.12)–(1.13), pp. 254–255; PDF: https://www.numdam.org/item/10.5802/jtnb.669.pdf.** The paper gives the short-difference omega result

> (1.12) Δ(x+h)−Δ(x)=Ω{√h log^{3/2}(√x/h)}  (x^ε≤h≤x^{1/2−ε}),

and identifies the following as **Jutila’s conjecture**, not a theorem:

> (1.13) Δ(x+h)−Δ(x) ≪ε x^ε√h  (x^ε≤h≤x^{1/2−ε}).

Thus do not cite the conjectured square-root bound as proved. Ivić (1.6) also records the elementary/Shiu bound Δ_k(x+h)−Δ_k(x) ≪ h log^{k−1}x for x^ε≤h≤x.

**Consequence (deduction from verified bounds, not a separately quoted theorem).** Since D(x,y)=y log x+(2γ−1)y+Δ(x+y)−Δ(x) under the usual summatory-error convention (some conventions absorb the −1 into the main term), a pointwise Δ bound O(x^{θ+ε}) gives a uniform error o(y) when y≥x^{θ+η}, η>0. For the requested convention y log x+2γy the constant-term convention must be checked: the standard summatory formula is Σ_{n≤t}d(n)=t log t+(2γ−1)t+Δ(t); hence an interval has main term y log x+(2γ−1)y, not y log x+2γy, up to O(y²/x) for y=o(x). The stated +2γ appears inconsistent with the standard d(n) convention. If literal +2γ is intended, the asserted asymptotic is false for y=o(x), since it differs by y.

The smallest threshold specifically via the best cited pointwise Δ bound is therefore θ*=0.314483… (arbitrarily small ε loss), with the preceding 131/416 bound superseded. Whether a **proved** pointwise short-difference result yields a smaller threshold: **UNVERIFIED**. I did not inspect Jutila 1984, Huxley’s book/papers, Kolesnik, or Heath-Brown/Tsang primary sources. The cited Ivić treatment explicitly labels the √h short-difference assertion a conjecture.

## Q2. Almost-all short intervals / mean squares

**VERIFIED-PRIMARY — Ivić, same paper, equations (1.7)–(1.14), pp. 253–255.** Ivić states that the k=2 cases of (1.3),(1.4) were treated by Coppola–Salerno and Jutila, and records their range X^ε≤h≤(1/2)√X. Define I₂(X,h) as in (1.8) of that paper. The transcribed statements are:

> (1.7) Σ₂(X,h)=8π⁻² Xh log³(√X/h)+O(Xh L^{5/2}√L),  L=log X.

> (1.8) I₂(X,h)= (1/4π²) Σ_{n≤X/(2h)} d²(n)n^{-3/2} ∫_X^{2X} x^{1/2}|exp(2πih√(n/x))−1|² dx + Oε(X^{1+ε}h^{1/2}).

OCR/extraction renders some integrand symbols imperfectly; consult the linked PDF before reusing its exact kernel. The robust checked statement is (1.9):

> I₂(X,h) ≍ Xh log³(√X/h)  (X^ε≤h≤X^{1/2−ε}).

Ivić further states (1.10), the matching mean square for E(x+h)−E(x), and (1.12), the omega result for Δ differences, given in Q1. Ivić’s own stronger mean-square formula is:

> (1.14) ∫_T^{2T}(Δ(x+U)−Δ(x))²dx = T U Σ_{j=0}^3 c_j log^j(√T/U) + Oε(T^{1/2+ε}U²)+Oε(T^{1+ε}U^{1/2}),

for 1≪U≤(1/2)√T, with c₃=8π⁻² (as reported immediately before (1.14)). Ivić says the analogous formula holds for E differences, with different coefficients, and that an analogous formula follows for Σ₂(X,h).

These are mean-square statements, **not** pointwise asymptotics for every interval. By Chebyshev they imply relative concentration for almost every x at suitable h, but I do not assert a sharp uniform exceptional-set threshold without carrying through constants/ranges. “As small as possible” thresholds such as h=X^ε, h→∞, or logarithmic h, and precise exceptional-set/higher-moment results: **UNVERIFIED** here.

**Bibliographic trail checked in Ivić’s reference list (not the primary papers): VERIFIED-PRIMARY as a transcription of Ivić’s bibliography only.** [1] G. Coppola and S. Salerno, “On the symmetry of the divisor function in almost all short intervals,” Acta Arith. 113 (2004), 189–201. [4] M. Jutila, “On the divisor problem for short intervals,” Ann. Univ. Turkuensis Ser. A I 186 (1984), 23–30. Their detailed theorem statements were not independently verified from those papers.

## Q3. Integer points near curves

**VERIFIED-PRIMARY — M. N. Huxley, “The rational points close to a curve,” Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 21 (1994), 357–375, Theorem 1, pp. 358–359; PDF: https://www.numdam.org/item/ASNSP_1994_4_21_3_357_0.pdf.** The checked theorem counts rational points (a/q,b/q), denominators Q≤q≤2Q, near a scaled curve f(x)=T F(x/M), and gives three upper bounds under the displayed curvature hypothesis. Its setup says the integer point satisfies |n−f(m)|≤δ (in the integer-point discussion) and emphasizes that for small δ one cannot expect a nonzero lower bound. **This is not the requested theorem for R(f,N,δ)=#{n∈[N,2N]:||f(n)||<δ}; it does not supply an asymptotic density.** The PDF’s OCR loses some exponents/inequalities in the theorem display, so I do not reproduce those formulae from OCR.

**UNVERIFIED.** Exact derivative-based R(f,N,δ) bounds from Huxley 1989 “The integer points close to a curve” (Mathematika 36 (1989), 198–215), Huxley–Sargos (Acta Arith. 69 (1995), 359–366; J. Théor. Nombres Bordeaux 18 (2006)), and Filaseta–Trifonov (Proc. LMS 73 (1996)): statements and theorem numbers not checked in the primary texts. In particular no verified statement here proves R=2δN+o(δN) for f(n)=x/n, N≈√x, δ≈x^{-1/4}. Treat that asymptotic as **UNVERIFIED / not established by the inspected source**, not as an asserted impossibility.

## Q4. Additive twists and σ_it

**UNVERIFIED.** No primary source was checked for pointwise power-saving estimates of Σ_{x<n≤x+y}d(n)e(nα), especially y=x^{1/4}, y≤x^{1/3}, irrational/minor-arc α. Also unverified: short sums of σ_it(n)=Σ_{d|n}d^{it}, Motohashi/Ivić results for ζ(s)ζ(s−it), and any relevant Δ(x;it) bounds. No claim of nonexistence.

## Q5. Erdős–Rosenfeld and divisors near √n

**VERIFIED-SECONDARY (bibliographic metadata only) — EuDML record for P. Erdős and M. Rosenfeld, “The factor-difference set of integers,” Acta Arith. 79 (1997), no. 4, 353–359, https://eudml.org/doc/206983.** The record verifies title/authors/journal/pages, not the paper’s theorem or the requested near-√n divisor question.

**UNVERIFIED.** Exact conjecture/question concerning the number of divisors of n in an interval of length n^{1/4} about √n; what Erdős–Rosenfeld proved; and follow-ups attributed to Ford, Tenenbaum, or Ruzsa. No theorem or quote should be attached to these at present.

## Q6. Beyond Voronoi for one point x; Bombieri–Iwaniec

**VERIFIED-PRIMARY (limited).** Li–Yang, arXiv:2308.14859v2, Theorem 1.2, explicitly establishes its Δ exponent by combining Bombieri–Iwaniec methods and decoupling (Introduction, pp. 2–3). This concerns the global pointwise Δ(X), not a short difference Δ(x+y)−Δ(x) or D(x,y) at y≤x^{1/3}.

**UNVERIFIED.** Whether spectral/Kuznetsov, a resonance-curve implementation of Huxley’s *Area, Lattice Points and Exponential Sums* (1996), or decoupling has a pointwise short-interval result of the asked form. The requested precise first-/second-spacing-problem theorem and the proposed Iwaniec–Kowalski theorem number were not independently checked; no double-sum bound is quoted.

## Q7. Thin hyperbolic strips / dyadic divisors

**UNVERIFIED.** I did not locate and inspect a primary paper giving pointwise asymptotics for weighted lattice points (k,m) with x<km≤x+y and a smooth phase, or for the dyadic divisor restriction d≈√x in a short interval. No claim of absence.

## Summary table

| Item | Verified? | One-line statement |
|---|---|---|
| Q1: global Δ exponent | VERIFIED-PRIMARY | Li–Yang Theorem 1.2: Δ(X)≪εX^{0.314483…+ε}; improves Huxley 131/416. |
| Q1: short difference | VERIFIED-PRIMARY / UNVERIFIED | Ivić (1.13) quotes Jutila’s √h estimate as a conjecture; sharper proved pointwise thresholds not checked. |
| Q1: requested main term | VERIFIED-PRIMARY deduction | Standard divisor summatory convention gives (2γ−1)y, not 2γy; literal requested constant is off by y. |
| Q2: mean square | VERIFIED-PRIMARY | Ivić (1.9),(1.14): short-difference second moments in power-sized h ranges; not an everywhere pointwise result. |
| Q2: almost-all minimum h | UNVERIFIED | No sharp exceptional-set or logarithmic-length threshold independently checked. |
| Q3: curve counting | VERIFIED-PRIMARY (limited) | Huxley 1994 Theorem 1 counts nearby rational points; not the requested R asymptotic. |
| Q3: f=x/n asymptotic | UNVERIFIED | No inspected source proves R=2δN+o(δN) in the stated scaling. |
| Q4 | UNVERIFIED | Additive-twist / σ_it short-sum claims not checked. |
| Q5 | VERIFIED-SECONDARY (metadata only) | EuDML verifies Erdős–Rosenfeld citation only; theorem/conjecture not checked. |
| Q6 | VERIFIED-PRIMARY (limited) | Li–Yang uses Bombieri–Iwaniec and decoupling for Δ globally; short differences/double-spacing claim unverified. |
| Q7 | UNVERIFIED | No primary statement checked on pointwise weighted thin hyperbolic strips. |

## Correction by the lane author (TDCAL)
The "(2γ−1)y, not 2γy" remark in Q1 above is **wrong** and is withdrawn. With D(t) = t log t + (2γ−1)t + Δ(t),
D(x+y) − D(x) = (x+y)log(x+y) − x log x + (2γ−1)y + Δ(x+y) − Δ(x), and (x+y)log(x+y) − x log x = y log x + y + O(y²/x).
So the interval main term is y log x + 2γy + O(y²/x), as in data/z54/bilinjac/LIT_CHECK.md §5(a). Nothing else in this
file depends on that remark.
