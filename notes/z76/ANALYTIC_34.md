# §0. Pointwise upper bound by conductor shifts

Result: For every integer n ≥ 2, R(n) ≪ε n^(8/25 + ε), sharpened to n^(7955/24966 + ε) with a modern exponent pair.  Label: PROVED (8/25 rel. Weil, Kusmin–Landau and the classical second-derivative test; 7955/24966 additionally rel. Trudgian–Yang Lemma 1.1, whose inputs include Bourgain, Huxley and Sargos).

Scope: R counts the ordered positive triples 4uBC−u−B=n, not all ES representations. No lower bound, improvement to E(N), fourth-root block saving, or result below 4/13. ES in ℕ remains open.

Review: cross-model (`data/z76/ANALYTIC_34_REVIEW.md`, Opus; fixes applied).

Triage: RECORD (campaign pointwise upper bound).

STATUS delta: Replace the §1B upper-side R estimate by “R(n) ≪ε n^(8/25+ε) for every n, PROVED rel. Weil and classical derivative tests; exponent 7955/24966 (≈0.318633) relative also to Trudgian–Yang (Bourgain/Huxley/Sargos inputs). Shift by the conductor before Cauchy in the square-sieve Poisson sum (`notes/z76/ANALYTIC_34.md`).” At export update the corresponding FRONTIER §3 and §7.1 benchmarks; retain the separate conditional 4/13 and balanced-block qualifications.

## 1. What changes

`Z53_SQSIEVE.md` already includes 21/65 relative to Bourgain's published theorem. Its Poisson formula has a periodic Kloosterman weight times a smooth reciprocal phase. Taking absolute values separately on each progression restricts the oscillatory sum to length W/Q. Instead, translate by multiples of Q, use the mean **square** of the weight once, and only then expand the square of the translates. Each resulting correlation is an **unweighted sum over all C**, of length W, not W/Q. One does not need to estimate a new trace-function correlation. At the worst block the saving from this reordering is larger than the saving from optimizing the old exponent pair. The factorisation Q=qq′ is needed for the square sieve and the complete sums, not for the shifts.

Priority scope: comparison is with `Z53_SQSIEVE.md` and `paper/es-count-note.tex` (the latter also discusses the scope of the literature search and the weaker full Type II bound of Elsholtz–Tao). Van der Corput differencing with shifts by multiples of the modulus (as in Heath-Brown’s q-analogue) is classical. The claim is an improved bound for this count, not priority for the differencing technique or an established published record.

## 2. Square-sieve and periodic inputs

Work on a dyadic block u∼U, B∼V, C∼W (x∼X means X<x≤2X), with U≤V by symmetry. Nonempty blocks have UVW ≍ n. Fixing u gives B | n+u; fixing C gives (4Cu−1)(4CB−1)=4Cn+1. Thus the block has ≪ε n^ε min(U,W) triples. There are O(log³(2n)) blocks. Ignore u=B at cost τ(n) per block. For k=uB and s=4Ck−n=u+B, the discriminant f(C,k)=s²−4k=(u−B)² is a positive square. Let Φ≥0 be smooth, compactly supported in [1/2,5], identically one on [1,4]. Weight (C,k) by 1_{C∼W} Φ(s/V); each counted pair lifts to at most two ordered triples.

Let P≥(log n)^3, and q,q′ range over distinct primes ∼P, Q=qq′. The elementary square sieve gives the block bound

    ≪ε n^ε (1+V/P) + max_Q |S_Q|,
    S_Q = Σ_{C∼W,k} Φ((4Ck−n)/V) (f(C,k)/Q).                       (1)

Indeed at a nonzero square ≤25V² only O(log n) prime symbols vanish, while there are ≫P/log P primes. Square the sum of the symbols and expand, omitting f=0 (which contributes zero anyway). The diagonal is bounded by the total mass times O(log P/P). The total mass is ≪ε V n^ε by summing over s∼V (more precisely V/2≤s≤5V), since 4Ck=n+s. Negative nonsquares do not affect positivity of the squared detector.

Write e(x)=exp(2πix) and G_c(ℓ)=Σ_{k mod Q}(f(c,k)/Q)e(ℓk/Q). The first estimate below is derived from the pointwise evaluations in `Z53_SQSIEVE.md` Lemma W, and the second is its Lemma P:

* Uniformly in ℓ (even when a prime of Q divides ℓ), Σ_{c mod Q}|G_c(ℓ)|² ≪ Q². For a prime q not dividing the local frequency, the individual bound is 2√q by Weil. For frequency 0 mod q the complete untwisted sum is 0 for q|c, q−1 if q∤c and 4cn+1≡0 mod q, and −1 otherwise. Thus the local second moment is ≤4q² in both cases. CRT multiplies the estimates, with unit rescaling of each frequency. Also Σ_{C∼W}|G_C(0)| ≪ W+Q: expand the product of 1+q·1_{4Cn+1≡0 (q)} over the two primes and count progression terms. This works when a local exceptional class is absent as well.
* Poisson summation in k gives exactly

      S_Q = Σ_{ℓ∈ℤ} Σ_{C∼W} a_ℓ(C) G_C(ℓ) e(F_ℓ(C)),
      F_ℓ(x)=−ℓ n/(4Qx),    a_ℓ(x)=V/(4Qx) Φ̂(ℓV/(4Qx)).

  This follows by splitting k mod Q and Fourier-transforming the translated bump (negative sign in the Fourier transform). The ℓ=0 term is ≪ V/Q+V/W. Put L=QW/V. The supremum plus total variation of a_ℓ on (W,2W] is ≪_A L^(−1)(1+|ℓ|/L)^(−A), by differentiating once. Abel summation therefore needs the following estimate **uniformly for subintervals** J⊂(W,2W].

## 3. Removing the periodic weight

**Shift inequality.** Let 1≤H be an integer, HQ≤W, Q≤W, g a Q-periodic sequence with Σ_{c mod Q}|g(c)|² ≪ Q². Put z(C)=1_J(C)e(F(C)). Then

    |Σ_C g(C) z(C)|² ≪ Q [W²/H + (W/H) Σ_{h=1}^{H−1} |Σ_x z(x+hQ) conj(z(x))|].    (2)

Indeed the left sum before squaring equals H^(−1) Σ_x g(x) Σ_{i=1}^H z(x+iQ) by shifting the dummy index. The x support has length ≤W+HQ+O(1), so its g mass squared (sum of |g|²) is ≪ WQ, by whole periods. Cauchy–Schwarz now discards g. The squared ℓ² norm of the inner sum is ≤H·#J_integers + 2 Σ_{1≤h<H}(H−h)|Σ_x z(x+hQ)conj(z(x))|. This proves (2). In particular there is **no** periodic factor in these last correlations.

Apply (2) with g(C)=G_C(ℓ), F=F_ℓ, ℓ≠0. The inner phase is

    D_h(x)=F_ℓ(x+hQ)−F_ℓ(x)=(ℓ h n/4) ∫₀¹ (x+t hQ)^(−2) dt.

The support J∩(J−hQ) is an interval. Set y=|ℓ|hn/2 and Y=y/W³. Up to conjugation D_h′(x)=y∫₀¹(x+t hQ)^(−3)dt. If HQ/W ≪ n^(−c) for some fixed c>0, each fixed derivative of this last function differs from the corresponding derivative of y x^(−3) by a relative O_j(HQ/W). For Y≥1 the phase therefore meets exactly the model-phase definition with σ=3 in [Trudgian–Yang §1.1, (1.1)–(1.2)](https://arxiv.org/html/2306.05599v3). For an exponent pair (κ,λ) the inner sum is ≪ Y^κ W^λ. Endpoints between integers and shortened intervals are allowed by that definition.

For 1/4≤Y<1 the second derivative has modulus ≍1/W; the classical second-derivative test gives O(√W+1). For Y<1/4 the monotone first derivative has modulus ≍Y and stays away from every integer by ≫Y, so the first-derivative test gives O(Y^(−1)). In the blocks used below W³/n ≪ W^λ, so this too is O(W^λ). Thus the bound over all nonzero frequencies is ≪ W^λ (1+|ℓ|Hn/W³)^κ. In the classical version take (1/2,1/2); for Y≥1 the same second-derivative test with |D_h″|≍Y/W gives O((WY)^(1/2)+(W/Y)^(1/2)). No modern pair is used in that version.

On inserting these estimates in (2), taking square roots, and summing the Abel bounds from §2, one obtains, for L ≳ 1,

    |S_Q| ≪ V/Q + V/W + √Q [W/√H + W^((1+λ)/2) (1+L H n/W³)^(κ/2)].               (3)

Indeed L^(−1) Σ_{ℓ≠0}(1+|ℓ|/L)^(−A)(1+|ℓ|Hn/W³)^(κ/2) ≪ (1+LHn/W³)^(κ/2) for A>2+κ. No unproved cancellation over ℓ, primes, classes, or n has been assumed. This square root in (3) is from Cauchy across all translated terms, not the hypothesis that every progression achieves square-root cancellation.

## 4. Choosing the parameters: global theorem

Use the classical pair (κ,λ)=(1/2,1/2) or the limiting pair (1418/5119,2917/5119). The latter, up to an arbitrarily small positive error in both coordinates, is the B transform (l−1/2,k+1/2) of (715/10238,7955/10238); we use this relative to the literature theorem of Trudgian–Yang (with its Bourgain, Huxley and Sargos inputs, not a re-verification of those proofs; no conjecture is invoked), *Toward optimal exponent pairs*, arXiv:2306.05599v3, Lemma 1.1, (1.6) and (1.11). The ε-perturbation costs n^O(ε) in (3) since all scales there are polynomial; re-denote ε at the end.

Write α,β,γ for block exponents to base n, with α+β+γ=1 up to O(1/log n). Let

    θ = 2(1+2κ)/(7+12κ−λ),
    ρ=β−θ,  j=2(ρ+γ−θ).

Discard min(α,γ)≤θ using the divisor bound. Otherwise β≥α≥θ, γ≥θ. Choose P=n^ρ(log n)^3, H=⌈n^j⌉. In exponent calculations below fixed log powers or constants are absorbed in n^ε, but strict polynomial margins are checked wherever required. Then Q ≍ P², V/P ≪ n^θ, √Q W/√H ≪ n^(θ+o(1)). For (3) the exponent of LHn/W³ is d=1+2ρ+j−β−2γ=1+3β−6θ. Its last term consequently has exponent

    F=ρ+[(1+λ)γ+κ d]/2

provided d≥0. The remaining necessary inequalities (ignoring harmless constant factors) are

    2ρ+γ−β≥0 (L≳1),   j+2ρ<γ (HQ/W power small),   3γ−1<λγ,
    β−2ρ≤θ,   β−γ≤θ,   d>0,   F≤θ.                                              (4)

All are affine and the domain α,γ≥θ, β≥α, α+β+γ=1 is the triangle with vertices (θ,1−2θ,θ), (θ,θ,1−2θ), ((1−θ)/2,(1−θ)/2,θ). The O(1/log n) uncertainty in the plane moves the vertices only O(1/log n); the logarithm in P preserves L≳1 at equality. Here is an exact check (a minimum or maximum below is over the three vertices):

| θ | min(γ−j−2ρ) | min d | F at vertex 1 | F at vertex 2 | F at vertex 3 |
|---|---:|---:|---:|---:|---:|
| 8/25 | 4/25 | 1/25 | θ | 7/25 | 57/200 |
| 7955/24966 | 3551/24966 | 367/8322 | θ | 37167617/127800954 | 18366361/63900477 |

The other conditions follow from 2ρ+γ−β=β+γ−2θ≥0, β−2ρ=2θ−β≤θ, β−γ≤1−3θ<θ, and 3γ−1≤2−6θ<θ/2≤λγ. Thus (1) and (3) give the claimed n^(θ+ε) on every block; logarithmically many blocks do not change the conclusion. The binding first vertex has U and W both about n^θ but V about n^(1−2θ). The shape, not the cube, determines the global exponent. The improvement over 21/65 is strict, as is the classical improvement 8/25 < 21/65.

## 5. Controls: optimal pair substitution, balanced block, and E

* **Old implementation optimized.** If one instead keeps the absolute progression sums of Z53 §4.5, a general pair gives discrepancy Q^(3/2+κ−λ) U^κ W^λ + Q^(3/2), since n/(VW)≍U. This is its displayed general-pair estimate *before* imposing λ−κ=1/2. For P as in §4 the leading term has exponent mρ+κα+λγ, m=3+2κ−2λ. The first vertex requires θ≥m/(1+3m−κ−λ). Trudgian–Yang's pair (18/199,593/796), again relative to their literature inputs including Bourgain and up to epsilons, attains θ=1346/4169 throughout the triangle: at the other two vertices that term has exponents 972773/3318524 and 987969/3318524; the residual 3ρ≤θ, Q<W and n≫W² hold throughout, so the reciprocal class phase meets the Z53 hypotheses. The ℓ=0 bound and (1) are unchanged. The old 21/65 is thus not the limit even for direct substitution.
* **Which optimization?** For the first-vertex constraint in either calculation, the displayed ratios have positive denominators on the Trudgian–Yang §1.4 convex hull. A level set of a ratio is a straight line. At the direct minimizer (vertex 2 in their indexing), the neighbors 1 and 3 have strictly larger ratios; at the shifted minimizer (vertex −4), the neighbors −3 and −5 do too. Convexity therefore proves optimality **for these first-vertex objective functions over that specific hull**, ignoring epsilons, not for arbitrary sum estimates. The other-vertex checks show these optima suffice for the stated global bounds. `scripts/z76_analytic34.py` checks all vertex arithmetic with rational numbers; output `data/z76/analytic34_vertices.txt`. Replay: `ulimit -v 6000000; timeout 30 uv run --offline --no-project python scripts/z76_analytic34.py`.
* **Balanced block and geometry (Assessment).** The first vertex above is not the fourth-root block U=V≈n^(1/4), W≈n^(1/2). (3) supplies no saving there: the √Q W/√H term alone with HQ≤W is ≥Q√W. The discriminant equation is a surface, not a plane cubic; this argument gives no new count of occupied auxiliary curves (`Z54_BILINDIV.md` §5.4), no TD or NC, and no exponent below 4/13.
* **Exceptional set (Assessment).** GRH bounds character sums over all primes, not sums weighted by exceptional membership; EH-level CRT moments still use product conductors (`paper/sieve-limits-note.tex`). No new forcing implication for actual exceptions (`EXSET_CHAR_FORCING.md` §1), or witness transport across smooth factors for I3 (`EXSET_I3.md` §4), is established.
