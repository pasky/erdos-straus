# Referee report 4: §9 of EXSET_DEPTH_BREAK.md

**Verdict: major revision. No depth-breaking result is proved. The principal algebraic, large-sieve, and cumulant inequalities survive scrutiny; several statistical and logical interpretations do not.** In particular, the independent-model tail calculation is not exact, the empirical/model tail thresholds differ, and the asserted equivalence between the proposed cumulant bounds and depth breaking is unjustified. ES remains open.

Scope: §9 only, with earlier material consulted for definitions and mass estimates. I checked the board memo, the cited theorem statements, the scripts and saved data, independently enumerated two complete numerical rows, and independently counted the actual overlap hits for all 20,000 integers in the β = 0.9 joint sample. Calculations used `ulimit -v 8000000`, timeouts, and scratch files in `/tmp/dbreak_review_0046/`. No manuscript or production script was edited.

## 1. Per-row verdicts for §9.0

The grades concern each **whole row**, including its interpretation, not just its strongest displayed inequality.

| Row | Verdict | Findings and concrete repair |
|---|---|---|
| 9a | **SOUND-WITH-MINOR** | Lemma 9.1 and the conditional reduction are correct in the intended range **1/2 < β < 1**. Supply the dyadic band-mass argument, account explicitly for the quadratic exceptional set, and center `(L_C)` or retain its linear mean term. The uncentered all-small-t formulation has an unnecessary sign obstruction, present in the data. |
| 9b | **MAJOR** | The recomputed mgf entries agree, but “no growth,” “within 0.02,” and the sampled standard errors are not correct as broadly stated. Raw A(t) grows at fixed β; at t = 0.1 one exact discrepancy is −0.02257. The SE calculation ignores fitted centering. Replace the verdict by a finite-range, centered-model comparison, with corrected SEs and no asymptotic pass/fail conclusion. |
| 9c | **MAJOR** | The advertised “exact independent law” uses a conditional Gaussian approximation. Empirical and model CDFs are evaluated at different thresholds. Correcting these issues removes the principal illustrated tail deficit. Recompute aligned tails with controlled model error; restrict “no coherent component found” to the particular 200-point diagnostics. |
| 9d | **MAJOR** | Proposition 9.2 and centered top-band `(L_C) ⇒ TB_pow` survive with minor proof repairs. The combined row nevertheless overstates its evidence: the mgf table is for X, not measured R; its SEs are wrong; “flat” is questionable; small correlation does not establish independence. The +0.50 overlap explanation **is independently substantiated**. Separate these claims and delete the converse/coincidence language. |
| 9e | **SOUND-WITH-MINOR** | Proposition 9.3(a)–(c), including the constant 8, is sound. Replace “exactly” by “up to the displayed error.” The large sieve bounds total excess from above, not the absolute covariance of just the beyond-level pairs. Repair the covariance identity and label the proposed sign mechanism as unproved. |
| 9f | **MAJOR** | Theorem 9.4 is sound, including 1.44 and 6, after replacing the numerical partition check with a proof. Lemma 9.5 needs C ≥ 1 or an O_C constant. The “needed,” “every j,” “exactly,” and “equivalent in strength” claims are not justified. State a sufficient moment route, with its logarithmic saving in required order, not a characterization of depth breaking. |

There is no fatal defect in the surviving conditional reductions or in Theorem 9.4. The claim that §9.3 computes an exact model CDF is, however, false—not merely insufficiently documented.

## 2. Lemma 9.1, quadratic rarity, and the first reduction

Write M = |I| and V = Σ_B σ_ℓ².

### Algebra and orthogonality

Every forbidden residue −4e is a nonzero quadratic nonresidue, and the w(ℓ) forbidden residues are distinct. Consequently 0 ≤ c_ℓ ≤ 1/2. Thus:

- R_ℓ is zero on zero and quadratic residues;
- on nonresidues it is F_ℓ − 2c_ℓ, hence |R_ℓ| ≤ 1;
- ΣR_ℓ = ΣR_ℓχ_ℓ = 0;
- the three probabilities and the mgf in (d) are correct.

The variance simplifies usefully to

    σ_ℓ² = ((ℓ−1)/ℓ)c_ℓ(1−2c_ℓ) ≤ 1/8.

In fact the identity

    R = X_B − μ + Q + D,       D(n) = Σ_{ℓ∈B, ℓ|n} c_ℓ,

holds for every n. Setting X_B = 0 proves (c), and splitting according to R ≤ −μ/2 proves (e), with the stated weak inequalities. Squares have R = 0 and are caught by the quadratic exceptional set; they have not been silently discarded.

### Pólya–Vinogradov and band mass

For distinct primes ℓ, ℓ′, χ_ℓχ_ℓ′ is a primitive nonprincipal quadratic character of conductor ℓℓ′. On n = 8k+1, multiplication by 8 and a translation convert it into an ordinary consecutive character sum, up to a constant of modulus one. There is no additional factor 8 in its conductor. The diagonal is bounded above by MΣc_ℓ². Therefore the recorded second-moment inequality is correct.

The ensuing estimates can be made explicit:

    Σ_B c_ℓ² ≤ y^{−1+o(1)},
    Σ_{ℓ≠ℓ′} c_ℓc_ℓ′√(ℓℓ′) log(ℓℓ′)
        ≪ z log z (Σ_B c_ℓ)² ≪ z(log z)³.

For fixed **β < 1**, the latter term is negligible compared with
N exp(−(1/2−o(1))(log N)^β). The text's unrestricted “β > 1/2” should therefore be restricted to 1/2 < β < 1 for this proof. At β = 1 this PV calculation does not give the claimed rarity bound.

One also needs μ ≍ log z, not merely a cumulative lower mass bound. It does not follow by subtracting two unspecified Θ(log x) bounds. The missing justification is standard: for a dyadic prime block (x,2x], retain divisors e ≤ x^{1/4} and apply Bombieri–Vinogradov to moduli 4e:

    Σ_{x<ℓ≤2x, ℓ≡3(4)} w(ℓ)
      ≥ Σ_{e≤x^{1/4}} [π(2x;4e,−1)−π(x;4e,−1)] ≫ x.

Here Σ_{e≤x^{1/4}}1/φ(4e) ≫ log x; the total BV error is smaller than the main term. Divisor pairing and Brun–Titchmarsh give the upper bound O(x). Every full dyadic block thus contributes mass ≍ 1. This proves both μ_(√z,z] ≍ log z and μ_top ≍ log N. The required argument is already available in `I3_DEEP_ASTRA.md:89–112,146`; cite or reproduce its restricted-modulus version.

Uniformly for n ≤ N, D(n) ≤ (log N)y^{−1+o(1)} = o(1). Eventually D ≤ μ/4, so (e) gives

    #Av(B) ≤ #{Q ≥ μ/4} + #{R ≤ −μ/2}.

Under `(L_C)`, Markov at the displayed fixed t gives the second term ≪ N exp(−cμ). Adding the quadratic exceptional set gives T1-min for any fixed 0 < δ < β−1/2, after increasing the lower cutoff on N. Constants and the sum of the two exceptional sets are absorbed by the strict exponent inequality. This conditional deduction is correct.

### The uncentered hypothesis has a real, avoidable defect

For any finite distribution,

    log E exp(−tR) = −t ER + O(t²).

Thus `(L_C)` for **every** 0 < t ≤ t₀ forces ER ≥ 0. An arbitrarily small negative rounding mean still violates it near zero, whatever finite C is chosen. This is not repaired by saying that the mean is o(1).

Independent exact rational first-moment calculations at N = 10⁷ give

    β = 0.6:  E_I R = −1408945093433394001 / 84254277802006511718750
                     = −0.00001672253480997543…;
    β = 0.75: E_I R = −0.0003047915319728762… .

These signs do not come from floating-point accumulation. Hence the literal finite-N uncentered inequality fails at these checked scales. This does **not** refute a statement asserted only for sufficiently large N, but the centered experiments are not tests of the uncentered inequality uniformly down to t = 0.

Repair: use

    log E exp(−t(R−ER)) ≤ Ct²μ,

or put −tER on the right of the original inequality. Proposition 9.3(a) makes centering harmless for the desired fixed-t tail deduction. The independent-model expansion in §9.1 is correct, uniformly on a bounded t interval after treating t = 0 by continuity.

## 3. Proposition 9.2 and the top-band implication

### Exact theorem and its application

I inspected Heath-Brown's original paper: **D. R. Heath-Brown, “A mean value estimate for real character sums,” Acta Arith. 72 (1995), 235–275, Theorem 1, p. 237**, [original PDF](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf). Its statement is

    Σ*_{m≤M} |Σ*_{r≤L} a_r (r/m)|²
       ≪_ε (ML)^ε (M+L) Σ*_{r≤L}|a_r|².

Both starred variables range over **positive odd squarefree integers**, including 1. The coefficients are arbitrary complex numbers. The character modulus in this displayed formulation is the outer variable m. This is exactly the theorem needed, not the ordinary large sieve with a squared modulus length.

For odd n = n₁n₂², n₁ is odd squarefree. Every top-band prime exceeds n₂, so (n/ℓ) = (n₁/ℓ). Reciprocity gives

    (n₁/ℓ) = (−1)^{(n₁−1)/2}(ℓ/n₁),

because every ℓ is 3 mod 4. The sign is constant across the inner prime sum and disappears on squaring. Prime support satisfies the inner squarefree condition. Taking M = ⌊N/n₂²⌋, L = N is legitimate.

Also, for arbitrarily small a > 0,

    Σ_top c_ℓ² ≪_a Σ_{m>√(2N)} m^{−2+a} ≪_a N^{−1/2+a/2}.

After assigning the small epsilon losses appropriately, each fixed n₂ contributes O_ε(N^{1/2+ε}) to the second moment. There is no missing nonsquarefree contribution in this part of the proof.

### Two small repairs to the exceptional-set proof

The printed bound N/Z + ZN^{1/2+2ε}η⁻² does not immediately give the claimed uniform η⁻² dependence when η > 1. Prove a second-moment bound instead. Since |Q_top| ≤ μ_top ≪ log N,

    Σ_{n≤N, odd} Q_top(n)²
      ≪_ε ZN^{1/2+ε} + (N/Z)(log N)².

Set Z = N^{1/4}, shrink the internal epsilons, and obtain O_ε(N^{3/4+ε}). Chebyshev now gives the stated result uniformly for all η > 0.

To assert Q_top = o(1) off O_ε(N^{3/4+ε}) integers, specify η = 1/log N and absorb its square into a smaller epsilon budget. A fixed η alone would not prove o(1).

### Centering and transfer

There is at most one top-band prime divisor of n ≤ N. Therefore the exact identity from §2 gives

    R_top = X_top − μ_top + Q_top + O_ε(N^{−1/2+ε})

for all n, not just avoiders. Further,

    |E_I R_top| ≤ 2W_top/M ≪ 1.

This follows from the first-moment rounding bound and W_top ≪ N. The assertion that the mean is a “bounded negative constant” is not proved: the cited archimedean exclusion does not determine the sign of the aggregate rounding error or establish a limit. Only O(1) is needed.

Off the quadratic exceptional set, X_top = 0 implies
R_top − E_I R_top ≤ −μ_top/2 for large N. The centered top-band `(L_C)` therefore gives

    #Av(B_top) ≪ N exp(−cμ_top) + O_ε(N^{3/4+ε}).

Since μ_top ≫ log N, this is a power saving. The transfer through Corollary 3.3 to TB_pow, U off squares, and ES₅ at primes is valid. The saving exponent must be limited by the quadratic exceptional set as well as the mgf exponent.

But **TB_pow does not imply `(L_C)`**. A bound on one zero event does not control the whole lower-side exponential moment. “Astra-5 and TB coincide” in §9.7 must be replaced by this one-way sufficient implication.

Finally, Proposition 9.2 is asymptotic and has unspecified constants. It does not certify that the omitted Q_top is negligible in the finite sampled mgfs at t = 0.25 or 1. Exponentials can amplify a rare exceptional set. The displayed numerical table measures centered **X_top**, normalized by its empirical mean, not centered R_top normalized by μ_top. Label it accordingly; directly compute Q_top or supply a quantitative transfer before presenting it as a residual-mgf measurement.

## 4. Proposition 9.3 and Theorem 9.4

### Rounding and the additive large sieve

For q odd, n = 8k+1 runs through every residue modulo q, and the count in each class differs from M/q by at most 1. Moreover,

    Σ_{a mod ℓ}|R_ℓ(a)| = 2w(ℓ)(1−2c_ℓ) ≤ 2w(ℓ).

This proves 9.3(a). A direct expansion even gives

    |E_I R² − V| ≤ 4W_B²/M,

since the L¹ norm of a distinct-prime product factors, and |R_ℓ|² ≤ |R_ℓ| on repeated primes. Subtracting the square of the mean proves the stated variance asymptotic. The looser bound printed in (b) is valid.

For (c), expand R_ℓ(8k+1) in its nonzero Fourier frequencies h/ℓ. Multiplication by 8 only permutes these frequencies and changes phases; it does not introduce denominator 8ℓ or an extra spacing loss. Fractions at distinct prime denominators are distinct and their distance modulo 1 is at least 1/(ℓℓ′) ≥ z⁻²; within a denominator the spacing is larger.

The dual additive large sieve gives constant M+δ⁻¹ (indeed M−1+δ⁻¹ is available). I checked **Kedlaya, Notes on analytic number theory, Theorem 15.5 and its proof**, [source](https://kskedlaya.org/ant/chap-largesieve.html#T-large-sieve), which explicitly supplies the weaker dual form used here and attributes the inequality to Selberg and Montgomery–Vaughan. Parseval gives coefficient energy V. Since M = ⌈N/8⌉ for integer N,

    E_I R² ≤ (1+z²/M)V ≤ (1+8z²/N)V.

The manuscript's O(N⁻¹) allowance is unnecessary. The range of k can start at zero; translation does not change the inequality.

### Theorem 9.4: all substantive steps check

**Model part.** The stronger σ_ℓ² ≤ 1/8 above verifies the stated 0.69 bound. For complex |s| ≤ 1, mean zero and |R_ℓ| ≤ 1 give

    |E exp(sR_ℓ)−1| ≤ σ_ℓ² Σ_{j≥2}1/j! = σ_ℓ²(e−2) < 1/2.

The analytic logarithm normalized to zero at s = 0 is well defined on the disk. Its absolute value is at most 2(e−2)σ_ℓ² < 1.44σ_ℓ². Cauchy's estimate gives the stated factorial bound.

**Repeated primes.** The model joint cumulant vanishes whenever at least two different primes occur, even if each occurs several times. Partition the arguments into the nonempty groups attached to different primes: those groups are independent, which is precisely the joint-cumulant vanishing criterion. For example κ(R_p,R_p,R_q,R_q) = 0 for p ≠ q. There is no flaw here.

**Block errors.** With repeated primes, the block function contains powers of R_ℓ. Since |R_ℓ| ≤ 1, their L¹ norms are no larger than that of |R_ℓ|. Thus

    δ_b ≤ M⁻¹ ∏_{distinct ℓ in b}2w(ℓ)
        ≤ M⁻¹ ∏_{i∈b}2w(ℓ_i).

The CRT modulus is the product of the distinct primes, not the product with multiplicity. The manuscript's enlargement to the latter weights is a valid upper bound.

**Product perturbation.** Expanding a product of perturbed block moments is legitimate. Each model block moment has modulus at most 1. A product of r ≥ 1 block errors carries M⁻ʳ ≤ M⁻¹; completing the selected factors to the full product only enlarges it because 2w(ℓ) ≥ 1. The factor 2^{|π|} is therefore valid, even when individual δ_b exceed 1.

**Partition bound.** Checking j ≤ 40 and quoting an asymptotic does not prove an all-j inequality. Here is a short repair, with the same constant:

    k! S(j,k) ≤ j! binom(j−1,k−1).

Represent each ordered set partition by a permutation and k−1 cuts; each has at least one representation. Therefore

    Σ_k S(j,k)(k−1)!2^k
      ≤ j! Σ_k binom(j−1,k−1)2^k/k
      = (j−1)!(3^j−1) ≤ j!3^j.

For accuracy, the actual asymptotic is (j−1)![log(3/2)]^{−j}; “j!·2.47^j” only describes exponential growth, not an asymptotic equivalent.

Summing over prime tuples proves the stronger comparison

    |κ_j(R) − κ_j(R_model)| ≤ j!(6W_B)^j/M.

The theorem and its 3j!V consequence follow. With the band mass established,

    J₀ = log(MV)/log(6C_Tz) = (1+o(1))(log N)^{1−β}.

Using a slightly smaller cutoff of the form (1−o(1))(log N)^{1−β} is safe. This is a sufficient **uniform aggregate error range**, not a proof of an optimal CRT cutoff for all uses of cumulants.

### The paragraph after Proposition 9.3 overstates what was bounded

The universally correct covariance identity is

    Var_I R − V = Σ_{ℓ≠ℓ′}Cov_I(R_ℓ,R_ℓ′) + O(W_B/M).

For E_I R², add (E_I R)², or explicitly absorb it using W_B/M = O(1) in the intended z ≤ N regime. Also, the large sieve bounds the **total excess from above**. It does not separately bound the absolute sum over ℓℓ′ > N. To isolate that sum one must handle complementary pairs, including the transition N^{1−ε} < ℓℓ′ ≤ N omitted in the discussion.

A same-shift product exclusion is a genuine negative contribution for hit indicators. It does not establish the sign of the full residual covariance, which also contains hit–character and character–character terms and different-shift interactions. The observed total variance deficit is evidence, not identification of its cause. Nor has a full Kloosterman-fraction formula for all these residual terms been displayed here.

## 5. Lemma 9.5 and the alleged “needed range”

The coefficient argument is sound after explicitly replacing cumulants by absolute-value coefficient majorants. With r² = k/(C²μ′), it gives

    E R^{2k} ≤ K√k (4C²kμ′)^k exp(√(k/μ′)/C).

The displayed 4e and 16e constants follow if **C ≥ 1**, which is harmless in this application. Without that convention an absolute implied constant cannot work uniformly in C: R ≡ 1, μ′ = 4, k = 1 satisfies all the hypotheses for arbitrarily small C, while the proposed upper bound tends to zero. Alternatively write O_C(√k).

The subsequent interpretation requires more substantial repairs:

1. Put L = log N and a = 1/2+δ < β. From (C′k/μ)^k, a saving exp(−L^a) already follows with **k = A L^a/log L**, for a sufficiently large fixed A. Orders L^a are convenient and sufficient, not literally necessary even for this estimate. The displayed formula with k = L^γ assumes γ < β; “any γ ≥ a” needs that upper restriction.
2. Bounds on absolute cumulants are sufficient for a lower-tail estimate, not necessary. A one-sided `(L_C)` does not “ask for every j” in this absolute-cumulant sense. For a concrete counterexample, let R = A(B−p), B Bernoulli(p), p = A⁻². Then

       log E exp(−tR) ≤ p(e^{−tA}−1+tA) ≤ t²/2  (t ≥ 0),

   but κ₃(R) = A³p(1−p)(1−2p) ∼ A. A uniform excellent lower-side mgf coexists with arbitrarily large absolute third cumulants.
3. Above J₀, tuples do not all have product of distinct primes > N. Repeated-prime tuples, in particular, retain small moduli. Conversely, a bound on the total cumulant can use cancellation without controlling each beyond-level joint cumulant separately.
4. No converse from T1-min to `(L_C)`, or to the proposed cumulant bounds, has been proved. Theorem 9.4 is compatible with the familiar CRT depth restriction; calling it “the cumulant form of G1” as an analogy is reasonable. Calling its missing window **exactly** G1, or `(L_C)` **equivalent in strength** to depth breaking, is not a theorem.
5. “No cumulant at all is CRT-accessible” on the top band is too strong. First moments and repeated-prime blocks remain directly evaluable. The meaningful obstruction is the uniform control of mixed distinct-prime pairs and higher aggregates; the all-tuples estimate does not give the desired O(μ) variance there.

The sound conclusion is narrower: this sufficient CRT comparison plus this moment inequality does not reach T1-min. Additional aggregate information, including information beyond the present level-controlled range, would suffice. Nothing here proves it necessary in the stated form.

## 6. Independent numerical audit

### Complete rows and model mgfs

`/tmp/dbreak_review_0046/check_numeric.py` independently constructs F_ℓ by enumerating divisors e of (ℓ+1)/4, computes Legendre symbols by Euler's criterion on every local residue, constructs R_ℓ from its definition, and accumulates in double precision over every n ≡ 1 mod 8 up to 10⁷. It does not call or copy the production hit-test shortcut. Model moments/mgfs are independently averaged over the full local residue tables.

Both rows have 1,248,419 nonsquare integers:

| β | primes | μ | V | empirical Var/V | A(0.25) | model | A(1) | model |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.6 | 21 | 1.3031757666 | 1.0434877960 | 1.0014882940 | 0.3796823886 | 0.3790844990 | 0.3251088173 | 0.3247014144 |
| 0.75 | 216 | 2.1900874391 | 2.0648437326 | 1.0201154697 | 0.4472472266 | 0.4379876559 | 0.3636603846 | 0.3569023050 |

This validates the numerical content at the table's precision, apart from harmless last-digit rounding. It does not justify the word “CERTIFIED” in a numerical-analysis sense: the production exact mode stores R in `float`, and the analysis reconstructs mgfs from logs printed to six decimals. It is a full census, not exact real arithmetic or an interval-certified calculation. At tiny quoted excesses, rounding should be bounded or more digits retained.

### The §9.3 DP is not an exact law

The recurrences for P(H=k), E[D;H=k], and E[D²;H=k] are correct. The fatal step for the **exact-law claim** is `model_cdf`: it substitutes a Gaussian for D conditional on H=k. Its first two conditional moments do not determine its tail. A small absolute variance does not ensure accurate relative probabilities, especially at 10⁻⁶-scale tails. The fixed KM = 200 also discards mass unless a truncation bound is supplied, although it is not a practical source of error at these small means. Degenerate conditional variances should be handled as atoms, not by replacing zero with 10⁻¹⁸.

There is a second, separate defect: the empirical calculation sums bins satisfying `v + 0.02 <= x`, while the model is evaluated at x itself. The empirical value is effectively at the preceding bin edge, not at the displayed threshold. The manuscript says thresholds are rounded, but the model thresholds are **not** rounded to match.

I checked β = 0.6, N = 10¹⁰ with two independent methods: two million direct draws from the local residue laws, and a controlled grid convolution. For the latter, every local variable is rounded **down** on a 10⁻⁵ grid using exact rational floors. If S is the resulting sum, then S ≤ R < S+0.0006. Thus its CDF brackets the true model CDF without a Gaussian assumption. It has 6,000,001 grid cells and total computed mass 0.9999999999999994. The bounds below control discretization; ordinary double-precision arithmetic is not formally interval-certified, but rounding is far below the displayed discrepancies.

| threshold | empirical entry in manuscript | manuscript Gaussian model at x | actual model CDF bracket at x | actual model bracket at empirical bin edge |
|---|---:|---:|---:|---:|
| −μ/2 | 0.25347173 | 0.25467982 | [0.25619058, 0.25639122] | [0.25316764, 0.25336456] at −0.84 |
| −3μ/4 | 0.15745255 | 0.16090370 | [0.16003298, 0.16015161] | [0.15730649, 0.15742664] at −1.26 |
| −μ | 0.06039874 | 0.06468597 | [0.06437778, 0.06451230] | [0.06033675, 0.06046785] at −1.68 |
| −1.25μ | 0.00702575 | 0.00673489 | [0.00712518, 0.00715696] | [0.00697673, 0.00700800] at −2.08 |

The −μ comparison is particularly revealing: the claimed 0.0604 versus 0.0647 deficit almost disappears at matching thresholds. At the first two aligned thresholds the empirical values are slightly **above**, not below, the model brackets. Hence “the negative tail follows the exact independent law, slightly below it” is not established by these calculations.

Repair all model-tail labels, compare the same thresholds, and give truncation/discretization or approximation errors. The far-tail comparison at β = 0.75 likewise needs reevaluation before drawing structural conclusions.

### Standard errors and the drop-screen

For fixed theoretical μ and a fitted empirical mean m, the influence function of
A(t) = [log average exp(−t(R−m))]/(μt²) is

    [exp(−t(R−m))/average exp(−t(R−m)) − 1 + t(R−m)]/(μt²).

`scripts/z51_dbreak_resid_analyze.py` omits the last term. Its reported SEs are consequently not the delta-method SEs of the displayed statistic. For example:

| sample | t | reported SE | corrected SE |
|---|---:|---:|---:|
| β=.75, N=10¹⁰ | .25 | .0075366 | .0021799 |
| β=.9, N=10⁹ | .25 | .0050223 | .0017026 |
| β=.9, N=10¹⁰ | .25 | .0048011 | .0017098 |

For the top-band table μ is also fitted, requiring an additional influence term −A(X−μ)/μ. The four t=.25 corrected SEs are approximately .00189, .00191, .00192, .00361, not .0055, .0052, .0049, .0086. The point estimates reproduce correctly.

This matters to “flat”: top-band A(.25) rises from .4709534 to .4853466. Under an independent-sample comparison that change is about 3.5 corrected standard errors; the last value is about 6.8 corrected SEs above the Poisson value .4608125. This is not evidence of divergence, but neither should it be called an established flat trend. The statistic can be numerically close to Poisson and statistically distinguishable from it.

Other wording defects:

- The exact β=.9, N=10⁷ row at t=.1 has excess −.02257, outside the unqualified .02 claim.
- At β=.6, raw A(.25) rises from about .3797 to .4144 as μ grows; at β=.75 it also rises. The **excess relative to the changing model** decreases, not A itself.
- The top-band excess does not exhibit that same decreasing pattern.
- μ ≤ 5 or 6.9 cannot test boundedness as μ → ∞. “No unbounded growth detected over this range” is defensible; “drop condition not met” needs an explicit, non-asymptotic definition and cannot certify the route.

## 7. Joint analysis and the overlap attribution

The parsing, n-alignment assertion, correlation, conditional probabilities, and joint/product ratio in `scripts/z51_dbreak_joint.py` are correct for these files. Integer n values are below 2⁵³, so float parsing does not lose their identity. The script's 1/√S correlation SE is a rough approximation, not a general formula.

Independent recomputation gives:

| sample | corr | P(X=0) | P(X=0 given R≤−μ/2) | joint/product |
|---|---:|---:|---:|---:|
| β=.75, N=10¹⁰, saved top | −.0220163 | .00515 | .00532559 | 1.03409 |
| β=.9, N=10⁹, saved disjoint | −.0438118 | .15810 | .14112784 | .892649 |
| β=.9, N=10⁹, overlapping top | +.4955671 | .00935 | .04133451 | 4.42080 |

The first conditional estimate contains only 22 joint zeros. The second row shows a modest but detectable lower-tail dependence; its contingency-table deviation from independence is about three standard errors. Neither small Pearson correlation nor one conditional probability establishes independence of the laws or of deeper tails.

### Directly checking the overlap, not merely subtracting saved counts

The actual z at β=.9, N=10⁹ is 4,431,556.877…. I independently sieved primes and constructed their forbidden residue sets by divisor enumeration, then counted hits with

    √(2N) < ℓ ≤ z

for **all 20,000 saved n**. This code does not use the production candidate enumerator or residual hit shortcut.

The saved “disjoint” layer omits a small additional interval above z. Its exact cutoff is not recorded in the data. The first 1,000 rows constrain it to

    4,524,959 ≤ cutoff < 4,544,279,

assuming a single threshold. In particular, the prose's “4.5·10⁶” must be read as rounded, not exact: at n=393670377 and 119903145, direct enumeration above exactly 4,500,000 gives four hits whereas the saved file records three. Record the exact cutoff and generating command; this small discrepancy does not undermine the overlap explanation.

Let O be the independently counted **true overlap**, G the extra omitted gap, and D the saved disjoint count. Then X_top = O+G+D, with G ≥ 0 on every row and 260 gap hits in total. The empirical covariance decomposition is

    Cov(R, X_top) = +2.4376759994
                 = +2.5996585789   [true overlap O]
                   −0.0010425432   [gap G]
                   −0.1609400363   [saved disjoint D].

Removing the actual overlap gives corr(R, X_top−O) = −.0439576, rather than +.4955671. Thus the positive correlation **is quantitatively accounted for by shared hits in the overlapping band** in this sample. This part of the manuscript is supported substantially more strongly than its vague independence claims.

The proposed explanation of the remaining negative correlation by same-shift archimedean exclusions is plausible but not identified by this calculation. Other cross-shift, scale, and character contributions remain. Label that sentence Assessment, not a demonstrated causal explanation.

## 8. Required revisions to §9.0 and §9.7

A defensible replacement conclusion is:

> The centered residual mgfs at the tested scales remain close to the independent-model values, although the available mass range is small. The exact algebra, quadratic exceptional-set bounds, and a uniform low-order cumulant comparison are proved. A sufficient extension of aggregate cumulant control would yield a depth-breaking tail bound, but no such extension is proved and no necessity or equivalence is established. The top-band centered exponential-moment hypothesis implies TB_pow. Tail-law and structural diagnostics are preliminary and require matched thresholds and controlled model errors.

In particular:

- Replace “no coherent residual component” by “none detected by these particular unweighted profile and small-kernel checks on the 200 most negative sampled/censused points.” A typical **unweighted** nonresidue fraction is not a statement about the weighted Q, and these diagnostics do not search all coherent mechanisms.
- Remove the assertion that all data are consistent with the literal uncentered `(L_C)`; specify the centered, fixed-positive-t hypothesis actually tested.
- Replace “needed” by “sufficient for this cumulant-moment route,” retaining the strict β > 1/2+δ condition and the logarithmic order refinement.
- Delete “equivalent in strength,” “coincide,” and the identification of every missing order with every tuple above level.
- Distinguish rigorous reductions, full floating-point censuses, controlled model approximations, and exploratory causal interpretations.

## 9. Reproducibility ledger

Scratch artifacts, all outside the repository:

- `check_numeric.py`, `check_numeric.out`: independent complete rows, direct model simulation, saved joint statistics.
- `check_tail_mean.py`, `check_tail_mean.out`: exact rational means and an independent conditional-moment recursion.
- `model_interval_dp.py`, `model_interval_dp.out`: controlled grid-law brackets, no conditional Gaussian approximation.
- `check_se.py`, `check_se.out`: corrected influence-function SEs and top-band mgf recomputation.
- `true_overlap.c`, `true_overlap.out`, `overlap_stats.py`, `overlap_stats.out`: independently enumerated actual overlap and covariance decomposition on all 20,000 rows.
- `check_overlap.c`, `infer_cutoff.c`, `check_mismatch.py` and their outputs: exact-cutoff reproducibility check; the initial 4,500,000 check deliberately exposed two mismatches rather than being suppressed.
- `sources/hb1995.pdf`, `sources/hb1995.txt`, `sources/kedlaya.txt`: inspected theorem sources. BV source: [Kedlaya, Theorem 17.1](https://kskedlaya.org/ant/chap-bombieri.html#T-bv).

Representative invocation:

    ulimit -v 8000000
    timeout 240s uv run --with numpy python /tmp/dbreak_review_0046/check_numeric.py
    timeout 180s uv run --with numpy python /tmp/dbreak_review_0046/model_interval_dp.py

The source-check and cumulant subaudits were independently reviewed against the displayed proofs and primary/secondary theorem statements before inclusion in this report.
