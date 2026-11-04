# Cross-model referee report: es-count-note

Reviewed `side-agent/z56-papercount` at `bc6780d144094f41249acdefe4ce0a1c9be37908` (TeX/PDF and checks); 4 November 2026.
Recommendation: **MAJOR REVISION**, principally for a material omission in the literature/novelty discussion, not a failure of the main proofs.

## Summary

The square-sieve upper bound, windowed genus lower bound, and truncated-count variance argument withstand re-derivation, relative to the classical inputs identified below. The distinction between the actual count and its genus component is maintained. The Erdős–Straus conjecture remains open; none of these arguments supplies a solution at an arbitrary prescribed prime.
The most serious defect is that a publicly available earlier preprint claims an almost-all-prime lower bound of order `(log p)^3` for strict Type II solutions, using a related centered-variance/Bombieri–Vinogradov strategy. It is missing from the bibliography and contradicts the account of what the literature search found. This does **not** establish that this paper's specific `c=1` slice result is old, nor does this report certify that competing preprint or its claimed Lean certificate.

## Per-result audit

“CORRECT” means that the displayed argument checks relative to its stated classical inputs, not independent reconstruction of those inputs' proofs. Numbering follows the supplied PDF. Grouped rows cover each numbered result in the range.

| Result | Classification | Re-derivation / scope |
|---|---|---|
| Lemmas 2.1–2.2 | CORRECT | `n<4uBC≤2n`; prime Type II injection recovers `u=px/y`, `B=px/z`; opposite-parity coprime pair bijection requires odd primes, as now stated. |
| Lemma 2.3 | CORRECT | `(4Cu−1)(4CB−1)=4Cn+1`; reciprocity gives `(C/(4Cu−1))=1`, hence `(n/(4Cu−1))=−1`; odd squares excluded. |
| Lemma 2.4 | CORRECT | Fixing each coordinate gives a divisor count; `min(u,B,C)≤(n/2)^(1/3)`. |
| Lemmas 3.1–3.2 | CORRECT | Square detection has the required positivity/parity and multiplicity two; diagonal ≤`τ(n)`; support on positive squares suffices for both constants 4. |
| Lemma 3.4 | CORRECT | Discriminant `16(4cn+1)`; linear/repeated-root exceptions handled; nonzero-frequency sum is Kloosterman, not Salié; CRT gives `4Q^(3/2)`. |
| Theorem 3.8 / A(a) | CORRECT | Shiu applies in both small-coordinate ranges; Vaaler/third-derivative discrepancy has the displayed powers; `P=T^(1/25)`, `η=1/75` give `T^(74/75)=n^(74/225)`, with two logarithms. |
| Lemma 3.10; Proposition 3.11 | CORRECT | Poisson sign and normalization check; zero mode `V/Q+V/W`; other terms `Q n^(1/6)W^(1/2)V^(−1/6)`, `Q^(1/2)V^(1/6)W n^(−1/6)`, `Q^(3/2)`. Short intervals and dual scale below 1 are covered. |
| Theorem 3.12 / A | CORRECT | Three vertex maxima `12/37`, `104/333`, `421/1332`; minimum sieve exponent `4/333`; cube exponent `17/54`. |
| Theorem 3.14 / A(b) | CORRECT-WITH-FIX | Exponent `4/(13−4κ)` and every affine side condition check; repair the rounding explanation below. Bourgain gives `21/65` relative to his Theorem 6; conjectural endpoint `4/13`. |
| Lemma 4.2 | CORRECT | Square conditions at 8 and odd primes give the factor `1/(2φ(u))` per orientation, without requiring squarefree `w`. |
| Lemmas 4.4–4.5 | CORRECT | Möbius removal of Euler factors, both tail constants, and both hyperbola identities check; derivative-term signs are correct. |
| Proposition 4.6 | CORRECT | Primitive conductors `4^j d` and `4^(1−j)(u/d)p` multiply to `4up` and are cube-free; the second character is never principal. Window subtraction cancels every nonprincipal constant term. |
| Proposition 4.7 | CORRECT | Square terms in the truncated L-series are nonnegative; nonsquares contribute `p^(θν−κα₀+o(1))`; squarefree `u≡1 mod 4` density is `2/π²`. |
| Theorem 4.8 / B | CORRECT | `H_u/φ(u)≥(4/π²)(p/(p+1))/u`; maximizing `(3−5α₁)(15α₁−1)/64` gives `1/12`, hence `2/(3π⁴)`. Fix parameters before taking `p→∞`; effectivity survives. |
| Proposition 4.10 | CORRECT | Nonsquarefree `w` gives the different split Euler factor printed here; ramified factors and quadratic discriminants check. Principal term must retain both `L′H` and `LH′`. Uniformity is only in the stated short squarefree slices. |
| Theorem 4.12 (“D”) | CORRECT | AP hyperbola split at `4u p^(ϖ+ε)` gives a class-independent main term; large-`c` tails use C4. Errors sum to `O(p^(−δ)log p)`; optimum `α₁=19/120` yields `121/(640π⁴)`. This is density-weighted, not exact divisibility. |
| Lemmas 5.1–5.2 | CORRECT | Two orientations are disjoint for `p≥(Q+1)²/4`; mean ≥`(log Y)²/8`. |
| Lemmas 5.4–5.5 | CORRECT | All compatible CRT classes are units at level ≤`Q²`; weighted BV errors use divisor-moment budgets 5 and 170, giving stronger errors than required. |
| Lemmas 5.6–5.7 | CORRECT | Primitive-conductor decomposition is exact; conductor 1 is `M²`; deleting the principal character permits arbitrary cell centering. |
| Lemmas 5.8–5.9 | CORRECT | Progression harmonic estimates, empty cells, finite integral comparisons, and stated constants check. The formerly divergent infinite sum is already repaired. |
| Proposition 5.10 | CORRECT | Corner term ≤`4(1+log Q)²` by `Σ_{d|m}φ(d)=m`; two edges give leading constant `8ζ(2)/9`. Only an upper bound is proved. |
| Theorem C | CORRECT | `V/M²≤(2048ζ(2)/9+o(1))/log X`, with `2048ζ(2)/9=374.313885…`; Chebyshev plus discarded primes permits 1600. Threshold coefficient is `2·(1/8)·(1/4)²=1/64`. Onset is ineffective. |

## Required changes, in priority order

1. **Major: acknowledge and compare the existing competing claim.** Brian Akaka, *A cubic lower bound for strict Erdős–Straus solution counts at almost all primes*, v0.7, **14 September 2026**, [Zenodo 22754703](https://zenodo.org/records/22754703), **Theorem 1**, claims
   `#{p≤N: R_II(p)<c(log p)^3}≪N/(log N)^4`, for actual strictly ordered Type II triples.
   I visited the public record/API, read the archived PDF, and matched its MD5 to the public file (`55595fee13a5cdff54a650e86143ed66`). This is not merely an inaccessible social-media snippet: the repository already contains the PDF and discusses it in `LITERATURE_2026.md`, §2.4.
   Revise the abstract's historical positioning, §§1.4–1.6, §7(4), bibliography, and accompanying review's search claims. Explain that this paper proves a bound on the particular `c=1` line, which does not follow from a bound for the full Type II family. Compare the primitive-character variance/weighted-BV mechanisms. Clearly label Akaka's result an unrefereed claim unless independently checked; neither ignore it nor assume its certificate settles correctness. The §7 presentation of the full-Type-II cubic lower bound as an untouched future target must be qualified accordingly.
2. **Minor proof repair: Theorem 3.14, TeX 867–873.** With `1≤c₀≤Q`, use `a∈(0,1]`, not `[0,1)`. The assertion `ℓn≥4W² ⇒ Y≥ceil(W/Q)²` omits rounding. Use the already established stronger `ℓn≥4W² n^c`: for `W/Q≥1`, `Y/ceil(W/Q)²≥ℓn/(16W²)≥n^c/4`. Small `W/Q` is handled trivially. No exponent changes.
3. **Minor overclaims: §§6–7, TeX 1833–1834, 1862–1867.** Three variance samples do not establish that Proposition 5.10 “has the right order”; say they are consistent with that order. Likewise “would require control of correlations at larger level” is a limitation of enlarging the present truncation, not a proved necessity for every improvement (weight removal and other fibrations are already acknowledged).
4. **Bibliographic correction:** the title-page/HTML author order of [HLMLT] v2 is Hasanalizade, Lin, **Luna Martínez, Martin**, Treviño. The review's appeal to conflicting abstract-page metadata is not a reason to retain the wrong title-page order.

## Source audit and novelty limits

- [Elsholtz–Tao, v6](https://arxiv.org/pdf/1107.1010v6): checked **Theorem 1.1, Theorem 1.8, Propositions 1.6, 1.7, 2.6**, and equation **(1.4)**. The prime sum for `f_II` is `≍X log²X`, so division by `π(X)` gives mean `≍log³X`: the draft is **correct** on this point. The `c=1`, `(a,b,d)=(B,u,C)` correspondence matches its ordered denominators. ET's `0.549…` density-one exponent is accurately quoted, but is no longer a sufficient literature comparison by itself.
- [Elsholtz–Planitzer](https://arxiv.org/pdf/1805.02945), **Theorem 1**: `O_ε(n^ε(n³/m²)^(1/5))`, as quoted; it does not give the present subfamily bound. [Bright–Loughran](https://arxiv.org/pdf/1908.02526), **Corollary 1.4**, has the cited odd-square Type I/II obstruction.
- [Bourgain](https://arxiv.org/pdf/1408.5794), **Theorem 6**, states `(13/84+ε,55/84+ε)`; surrounding §5 specifies the exponent-pair phase class and sketches the extension. The draft's qualification is appropriate. The reciprocal phase satisfies the derivative conditions; see also Trudgian–Yang **§§1.1–1.2**, arXiv:2306.05599.
- [Iwaniec–Kowalski, author-hosted Chapter 11](https://people.math.ethz.ch/~kowalski/ik-ant-exp-sums.pdf), **Theorem 11.11 / Corollary 11.12**, gives the exact Kloosterman bound used in Cited Theorem 3.3.
- Shiu, **Theorem 1**, journal p.163, independently read from `sources/shiu-1980.pdf` ([record](https://eudml.org/doc/152201)): the stated `k<y^(1−α)`, `x^β<y≤x` range and `τ` specialization agree. For example, fixed `α=1/8`, `β=1/4` cover both applications.
- Titchmarsh, **Theorem 5.11**, [scan](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf), checked by the independent source reader: the two third-derivative terms, including `h^(1/2)`, agree.
- [Explicit Burgess paper, v2](https://arxiv.org/html/2511.17778v2), **Theorem 1.2**: verified the threshold `max(10^1143,2^(4r−2))`, cube-free restriction, and extra factors. For each fixed `r≥2` these are effectively `O_{r,ε}(f^ε)`; the paper separately handles `r=1` by Pólya–Vinogradov. These statements support the effective input independently of accessing IK **Theorem 12.6** itself.
- **Access limits:** IK **Theorem 17.1** and Graham–Kolesnik **Theorem A.6** were checked through standard restatements/cross-references, not their original book pages; an attempted full IK scan failed DNS resolution. The BV `π` formulation follows from the usual maximal `ψ` theorem by partial summation and increasing the logarithmic loss. Vaaler's Fejér majorant has the stated coefficients. Heath-Brown **Theorem 1** was not independently accessed, but Lemma 3.2 supplies a complete elementary proof of the variant actually used.
- [Salez](https://arxiv.org/pdf/1406.6307) supports the `10^17` computational statement. The historical Vaughan exceptional-set estimate, Mordell residue classes, and Yamamoto attribution were corroborated against ET's introduction, not independently checked in each original source. The Heath-Brown–Pierce [abstract](https://arxiv.org/abs/1109.1455) supports the stated power-sieve/cyclic-cover precedent.
- Targeted web/arXiv searches on the defining polynomial, square sieve, Type II upper bounds, and density-one counts found no earlier exact match for the upper-bound or genus theorems. This is a bounded search, not a priority certificate. The withdrawn Jiang arXiv:2609.09204 is another related counting lead, not established replacement literature. The concrete Akaka overlap above makes the draft's present blanket “search found nothing” account untenable.

## Computations and reproducibility

All executed check programs ran with `timeout` and `ulimit -v 6000000`; allocation and loop sizes were inspected first. Python ran through `uv`.
- `uv run --with sympy python es-count-note.checks.py`: passed; exact named vertices, `12/37`, `21/65`, `4/13`, and cube `17/54` reproduced. General-κ printed factorizations were checked analytically for signs, not treated as automated interval assertions.
- C checker compiled with `gcc -O2 -Wall -Wextra`; `zeros 10000000` reproduced exactly all fourteen listed primes and zero odd-square violations.
- `mgen` reproduced `409: 3.999068`, `577: 5.352387`, `8089: 6.790809`, `1000033: 27.736888`, `8813281: 29.083352`; values at `961`, `1225`, `9801` were zero.
- Inspected and reran `scripts/z53_pz_exactV_trial.c`, weighted mode, at `Q=100,1000,3000`: `V=2.098849,6.943898,10.887322`; final run has 5,089 pairs and streams its double sum, without a quadratic-memory array.
- The historical 65-slice L-value experiment is not implemented by the two adjacent check files and was not independently regenerated in this pass; provide its generator and exact invocation if retaining the percentage claim as a reproducible result.

## Minor presentation comments and recommendation

The paper is substantially self-contained apart from its declared analytic inputs. The corrected Type II qualification, odd-prime pair domain, slice asymptotic wording, and retained derivative terms should stay. Keep the balanced-block obstruction explicitly heuristic. Distinguish lettered introductory theorems from “Theorem D”, currently numbered 4.12 only.
**Major revision** is warranted because the claimed contribution must be repositioned against a specific prior public claim with substantial methodological overlap. The technical repairs identified here are minor; I find no reason to reject the upper-bound or genus arguments. A revised draft could be reconsidered after an explicit literature comparison and the listed corrections, without pretending that either this audit or the competing preprint proves Erdős–Straus.
