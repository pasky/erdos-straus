# KARY3 hostile self-review

Reviewed: all six commits in `e0d463731f21ad18d77ee39c89fe57546461695c..8a215d66a57ec4bf2c9a6d832cff7fd1efae82eb`, including the new note, script, recorded output and O28 report. No implementation/document changes made outside this review.

## Verdict

**The central lossless first-moment argument and Theorem 4.1 survive review, after a small but necessary repair to the smooth exceptional-set counting in Lemma 2.3.** I find no hidden logarithmic loss in the Shiu argument or the Case-A argument. The truncated-weight construction also works: neither a wide top block nor conditioning destroys the required locality.

**Do not accept the checkpoint unchanged.** Corollary 5.3's advertised examples and “exact scope” contain substantive scope errors, including a reversed description of the remaining window. The summary of Theorem 5.1 is false for unrestricted `d₀`, its equality endpoint is mishandled, and the numerical maximum is demonstrably wrong. These are repairable; none supplies a counterexample to the principal `Cλ^{3/4}` cap. “PROVED” should not be propagated to the affected scope claims before repair.

Severity: **medium** = an incorrect mathematical statement/application or a real, locally repairable proof gap; **low** = endpoint/presentation/evidence qualification. No fatal defect in the main theorem found.

## Concrete findings

### D1 — Medium: bounded prime order is measured above fixed W, not above the moving sieve cutoff

Location: `EXCEPTIONAL_KARY3.md:392–400`, especially the examples “twin moduli, ℛ(kℓ) atoms of the 3/4 note, η-twins”.

Corollary 5.3 counts **all primes greater than the absolute constant W**. Those examples do not, as defined in the cited files, have uniformly bounded such counts. In the 3/4 note, `k` ranges over all `k ≤ K = floor(X^κ)`, `k ≡ 1 mod 4` (`paper/es-threequarter-note.tex:105–107,172–177`). Nothing bounds `ω_{>W}(k)`. A product of arbitrarily many primes `1 mod 4` above W is an admissible cofactor once X is large enough. The bounded-B inequality `kℓ ≤ ℓ^{1+2κ}` does not bound this prime count.

Likewise TW2/TW4 twin moduli have two primes above the **moving** cutoff `w₂ = (log X)^8`, with a `w₂`-smooth cofactor. That cofactor can contain arbitrarily many primes above fixed W. An η-twin condition on the largest primes does not fix this either.

**Repair:** keep the corollary for `ω_{>W}(G) ≤ r`, but remove these examples unless their cofactors are explicitly W-smooth or have bounded `ω_{>W}`. Theorem 4.1 still covers these families; what fails is the claimed bounded-r **class-order** application. A moving-base argument would need separate accounting and is not proved here.

### D2 — Medium: the stated remaining window is the window Corollary 5.3 excludes

Location: `EXCEPTIONAL_KARY3.md:402–410`.

The displayed allegedly unexcluded interval is

    L^{4θ/3−1} ≲ k ≲ L^θ/(r log L),       L = log N.

But Corollary 5.3 itself says a saving `L^θ` requires

    kr ≳ L^θ/log L.

It therefore excludes the interior below the **upper endpoint** of the purported open window. The corollary's constant is independent of r; it is not limited to fixed r. For a concrete exponent check, take `θ = 0.9`, `r = L^{0.1}`, `k = L^{0.3}`. These lie well inside the claimed open window, whereas the proved cap is

    O(L^{0.75} + L^{0.4} log L) = o(L^{0.9}).

All relevant order restrictions in Corollary 5.2 are satisfied here.

**Repair:** distinguish a known uniform bound r from no useful bound on r. Where the TU polynomial-modulus hypothesis also holds, the two proved necessary bounds combine as

    k ≳ max(L^{4θ/3−1}, L^θ/(r log L)).

If comparing with the prime-order benchmark `L^θ/log L`, the remaining gap is *above* this maximum, not below `L^θ/(r log L)`. The existing “exact scope” paragraph is not a correct description of the results.

### D3 — Medium: polynomial prime bounds do not imply polynomial modulus/level bounds

Location: `EXCEPTIONAL_KARY3.md:402–405`; also make the inherited hypotheses of Corollary 5.3 explicit.

The section/Corollary 5.2 allows arbitrary moduli whose prime factors are `≤ N^A`. From this one cannot infer either

    ω_{>W}(G) ≤ A log N/log W

or

    level(intersection of k classes) ≤ kA log N.

A squarefree product of primes up to `N^A` has logarithm of order `N^A`, not `log N`; one can arrange `G ≡ 3 mod 4`, so the issue occurs within ℛ(G) families. This is not merely about large prime powers.

TU Corollary 3.4 does assume that the **intersected class moduli** are `≤ N^A`, which makes both estimates valid. KARY3's broader family-prime hypothesis does not.

**Repair:** explicitly restore the polynomial-modulus (or radical-level) hypothesis when invoking TU's ordinary-level estimate. State that Corollary 5.3 inherits Corollary 5.2's family-prime bound. Do not present the TU fallback as a consequence for every arbitrary-modulus family covered by Theorem 5.1.

### D4 — Medium: Lemma 2.3 drops the smoothness needed for its squarefull count

Location: `EXCEPTIONAL_KARY3.md:109–116`.

The literal estimate

    #{M ≤ 2K : S_y(M) > K^{1/2}} ≪ K^{3/4}

is false. For fixed y and large K, every prime `M ∈ (K,2K]` has `S_y(M) = M`, which is not squarefull. There are order `K/log K` such integers (also in the required `3 mod 4` progression), more than `O(K^{3/4})`.

Lemma 2.1 only makes `S_y(M)` squarefull **when M is y-smooth**. The definition of `Σ₁` must retain that condition; the moment term `Σ₂` may discard it. With

    #{M ≤ 2K : P(M) ≤ y, S_y(M) > K^{1/2}},

the asserted containment in the union of squarefull-divisibility events and the `K^{3/4}` bound are correct. This is a local repair, not a failure of the method. Explicitly retain smoothness in the analogous exceptional-pair counts in Lemma 3.1 as well.

### D5 — Medium: the short Theorem 5.1 formula is false without a restriction on d₀

Locations: `EXCEPTIONAL_KARY3.md:22`; `reviews/agent-reports/AGENT_REPORT_O28.md:30–32`.

The summary substitutes

    Cλ^{3/4} + 2d₀ log(CΛ³/d₀) + O(d₀)

for the theorem's correct expression with `K₃′Λ³ + 4d₀` inside the logarithm. The substitution requires, for example, `d₀ ≤ Λ³`. The theorem allows arbitrarily small positive L₀, hence arbitrarily large `d₀ = floor(λ/L₀)`. For fixed λ and Λ the summary's right side tends to minus infinity as `d₀ → ∞`, even for the admissible majorant `ν ≡ 1`.

**Repair:** include the restriction, or retain `log(C(Λ³+d₀)/d₀)` / `log(C(1+Λ³/d₀))`. Also retain the floor in the report's definition of d₀. The fully displayed theorem does not have this defect.

### D6 — Medium: the reported numerical bound 0.25 is false, even in the committed output

Locations: `EXCEPTIONAL_KARY3.md:26,438–440`; `reviews/agent-reports/AGENT_REPORT_O28.md:73`; `scripts/kary3_moments.py:82`.

`data/kary3/moments.txt:31` already gives `u⁴b = 0.2914` for `y = 13`. Worse, the script prints only even block exponents, so the displayed table cannot certify a maximum “throughout”. I independently evaluated **every complete dyadic block** in the stated range:

| y | maximum u⁴b | K | u |
|---|---:|---:|---:|
| 7 | 0.3848284349 | 128 | 2.4934503098 |
| 13 | 0.2932047111 | 128 | 1.8916670810 |
| 23 | 0.2513946835 | 2048 | 2.4317120240 |
| 31 | 0.2476124348 | 2048 | 2.2203399524 |

**Repair:** report the computed full-block maximum (a bound of 0.385 works for this run), and compute/assert it explicitly rather than infer it from a subsampled table. The data file itself reproduces exactly; its arithmetic is not the problem.

Also, these experiments have `u < 15`, whereas Lemma 2.3 with `k = 4` requires `u ≥ 64` and sufficiently large y. Replace “as Lemma 2.3 requires” with heuristic consistency. A <1% change between two cutoffs is evidence of stabilization, not a bound on the infinite remaining tail or a proof that the sum “has converged”.

### D7 — Low, real endpoint gap: truncation is not vacuous when L₀ = λ

Locations: `EXCEPTIONAL_KARY3.md:343,387–390`.

If `L₀ = λ`, a term supported on one prime `q > e^λ` has truncated level λ but ordinary level `log q > λ`. For example, for the selector family `{0 mod q}`, `ν = 1 − 1[n ≡ 0 mod q]` is an actual majorant with this property. Thus Theorem 4.1 does not apply directly on the claimed ground that truncation is vacuous. Corollary 5.2 uses exactly this omitted endpoint when `k = 1`; Theorem 5.1 as stated requires `L₀ < λ`.

**Repair:** change “vacuous” to `L₀ > λ`, and handle equality. In Corollary 5.2 specifically, projection and `λ=Λ` remove every prime above `e^λ`, so k = 1 follows directly from Theorem 4.1; spell this out instead of citing a theorem with a strict hypothesis. For the general equality endpoint, put **all** primes with `log ℓ > λ/2` into one linear block: their truncated weights exceed λ/2, so every admissible term uses at most one. ETw's linear-window proof works without an upper endpoint and costs at most `2 log(1+3e^{−λ/4})`. Alternatively extend Theorem 5.1 itself to equality; its existing top-block proof works there. No claimed cap needs to be weakened.

## Detailed mathematical audit

### Lemma 2.1 — sound

For a y-smooth M, every prime power included in `S_y(M)` has exponent at least two. The part outside S contributes its full logarithm to `Z_y(M) log y`; contributions from primes inside S are extra nonnegative terms. Consequently

    log M ≤ log S_y(M) + Z_y(M) log y.

The threshold `S ≤ K^{1/2}` gives `Z ≥ u/2` since `M > K`. The indicator inequality is valid for nonsmooth M as well, trivially because its left side is zero; it does **not** imply that S is squarefull for such M. This distinction causes D4.

### Lemma 2.2 — sound

The partition is by the underlying primes, not by the prime powers. For a block of size m, the exact number of exponent tuples with maximum t is `t^m − (t−1)^m ≤ mt^{m−1}`. Extending the exponent range to infinity is an upper bound, giving `O_m(1/p)`. Distinctness of block primes may be dropped because all summands are nonnegative. The prime sum is bounded by

    (log y)^{m−1} Σ_{p≤y} γ′(p) log p/p ≪_W (log y)^m.

Finite small-prime factors, including `γ′(2) = 8`, change only the constant. No additional logarithm is lost through repeated powers, repeated primes or the Bell-number sum.

### Lemma 2.3 — sound after D4

I checked Shiu's original scanned pp. 162–163, not only the local paraphrase. With `F(n)=τ(n²)`, `F(p^a)=2a+1 ≤ 3^a` and `F(n) ≪_ε n^ε`, its function-class assumptions hold. For odd q, the residue `4^{-1} mod q` is reduced. The interval parameters are `V=(2K+1)/4`, `Y=K/4`; for large K,

    q ≤ K^{1/2} < (K/4)^{3/4},       V^{1/4} < Y ≤ V.

Thus `α_s=β_s=1/4` is legal uniformly. Removing the primes dividing q produces the factor

    Π_{p|q} (1−1/p)^{-1} exp(−3/p) ≤ 1,

so replacing `1/φ(q)` by `1/q` is justified without a log-log loss. The separate q = 1 argument is correct: `τ(·²)=1*2^ω` and the resulting Euler product is `O(log² K)`.

The exponent ledger checks:

- `D ≤ y^k ≤ K^{1/16}`; for `e ≤ K^{1/4}`, `lcm(D,e) ≤ K^{5/16} < K^{1/2}`. There is substantial unused Shiu range.
- For the e-tail, multiply by `e^{1/4}/Z^{1/4}`. A prime dividing D contributes `1+h(p)p^{1/4}`; other primes contribute `1+h(p)p^{-3/4}`. The former is at most 2 for `p>W`, and at most k distinct such primes occur. The latter product converges. Small primes contribute a fixed factor depending on W. Thus the asserted `c(W)2^k Z^{-1/4}` is correct.
- At `Z=K^{1/4}` the gain is `K^{-1/16}`. Taking, for example, the pointwise exponent `ε=1/1000` gives more than the displayed `K^{1−1/20}` saving.
- The bound `T(q) ≪ K^{1+ε}/q` remains valid near `q=2K`: the possible `+1` is absorbed by `K/q ≥ 1/2`; for `q>2K` the sum is empty.
- Lemma 2.2 controls the tail tuple sum as well, since `Γ(D)≥1`. There is no dependence on a maximal modulus or on B.
- The corrected squarefull count costs `K^{3/4+ε}`, comfortably below `K^{4/5}`. Polynomial savings absorb any fixed power of u because `u ≤ log K` after increasing y₀ to at least e.

The equality with an Euler product in the short-e bullet should be understood as extending a nonnegative truncated sum to all e; writing an explicit `≤` would avoid ambiguity.

### Corollary 2.4 — sound, including constants

The body bound from EK is B-free. The blocks starting at `2^{ceil(log₂ X)}` leave no gap beyond `2X`; any overlap with the body is harmless. Each tail block contributes at most `4C₄(log y)^4/(t²(log 2)²)`. For `t₀≥1`,

    Σ_{t≥t₀} t^{-2} ≤ 2/t₀,       t₀ ≥ log X/log 2.

This gives `8C₄(log y)^4/(log 2·log X)` and, at `X=y^{64}`, the claimed `C₄/(8 log 2)` coefficient. The numerical factor is not missing a dyadic-spacing logarithm.

### Elsholtz–Tao inputs and (7.10) — sufficient and uniform; one source-proof caveat

I extracted and read pp. 25–32 of `sources/elsholtz-tao-1107.1010.pdf` (the local PDF is arXiv v6). Theorem 7.1 has exactly the nonnegative-coefficient, polynomial-size and uniform prime-power-root hypotheses used here. Corollary 7.4 has constants depending on the fixed coefficient-growth exponent, not on a or b individually.

The character-sum proof of (7.10) really does give a bound uniform in k, without `k ≪ (AB)^{O(1)}`. In the middle range `A ≤ q ≤ kA` the entire dependence is `log(1+k)`. Above kA, the reciprocal character has period `O(ka) ≤ O(kA)`, and partial summation starts at kA, cancelling this period bound. Removing powers of two from a introduces a convergent sum `Σ_j 2^{-j}(log(1+k)+j)`, not a new `log A`. The size restriction in Proposition 1.4 enters when applying Theorem 7.1 to the original polynomial.

**Caveat worth recording:** on printed p. 31 the source says the small-q character in a has mean zero for every q. This is false for square q, including q = 1. Separate square q: their contribution is at most

    A log B · Σ_{q square} 1/q = O(A log B).

For nonsquares the stated mean-zero argument is valid. This elementary repair preserves complete k-uniformity and the exact bound needed here. I do not regard it as a failure of the KARY3 application, but a hostile source check should not report the proof literally flawless.

For literal endpoint accuracy quote (7.10) with `A,B ≥ 2`, or use `log(2B)`: uniform `A log B` for all real `B>1` is false as B tends to 1. Similarly Corollary 7.4 needs `N≥2`. KARY3's actual applications are well inside these ranges.

### Lemma 3.1 — both cases work

**Case (i).** Put the local moment on smooth r, not on rh. With `r ≥ K^{1/4}`, the exceptional threshold `K^{1/8}` leaves `Z_y(r) ≥ u/8`. The squarefull-pair bound is `K^{15/16} log K` before a pointwise divisor bound; retain smoothness as in D4. With `s ≤ K^{1/16}` and `D ≤ K^{1/64}`, actually `L ≤ K^{5/64}`, so the weaker `L ≤ K^{1/8}` is safe. Then `R′=2K/(hL) ≥ K^{1/8}` and `a=4h²L ≤16K^{13/8}`. For large K, `a ≤ floor(R′)^{14}` as well: there is a spare power `K^{1/8}` to absorb constants and flooring. Corollary 7.4 is genuinely uniform here. Its harmonic h-sum supplies the second logarithm, and `Σ_t h(t)/t` converges.

For `s>K^{1/16}`, the progression is through zero in r, so its count is `floor(2K/(hL)) ≤ 2K/(hL)`, without an unpayable endpoint term. The tail gain is `K^{-1/64}`. Choosing ε smaller than `1/320` and absorbing `log K` gives the displayed `K^{1−1/80}`.

**Case (ii).** Here h is large and smooth, so `S_y(h)≤K^{1/4}` leaves `Z_y(h)≥u/4`. For `t≤K^{1/16}`, `L≤K^{1/8}` and `r<K^{1/4}` give `N=floor(2K/(rL))≥K^{1/2}` for large K (indeed there is more room). The coefficient `4rL²≤4K^{1/2}≤N²` meets Theorem 7.1 with fixed `l=2`.

The root comparison has the **correct direction**. At primes dividing `2rL`, the new polynomial has no roots; at odd primes not dividing rL, multiplication by L is invertible and preserves the root count. If a prime divides L but not 2r, the old polynomial can have roots while the new one has none—again giving `≤`, not `≥`. Hensel gives at most two roots at every relevant prime power. CRT therefore gives `ρ_P(m)≤ρ_{4r}(m)` for every m.

After this comparison L occurs only as `1/L`. Applying (7.10) with coefficient `4s`, not `4sL²`, is legitimate and is the decisive avoidance of an unwanted logarithm. On `a∈[R,2R)`, replace `1/a` by `1/R` and bound by the cumulative sum to `2R≥2`. There are `O(log K)` ranges. The remaining weight `Σ_s h(s)log(1+4s)/s` converges, since `Σ_s h(s)s^{-3/4}<∞`. The large-t tail is identical in strength to case (i). No squarefreeness of r is needed for this upper bound.

### Corollaries 3.2–3.3 and Theorem 4.1 — sound

The body in Corollary 3.2 uses the B-free, Γ-weighted hyperbolic mean already proved in K2/ET; its two convergence conditions hold for this h, including the finite factor at 2. The tail with `X=y^{256}` has the same convergent dyadic sum as Corollary 2.4. The (a,D) and selector contributions already have the required log-free orders.

I reread K2 §5 specifically for any other source of `log log`. There is none. The old factor appears in the first-moment input and consequently in the choice of `s₁`. The base, locality, sequential comparison, linear window and leak do not require it. With `s₁=λ^{1/4}`, the block ratio is `O(16^i)+4`, so `Σ_i(λ/s₁)2^{-i}(1+i)=O(λ^{3/4})`. The `O(log²λ)` bookkeeping and fixed base cost are absorbable. Increase λ₀ to ensure both `s₁>2log W` and `e^{s₁}≥y₀(W)`.

Corollary 4.2 correctly uses `S=log(1/Eν)`, not the possibly smaller achieved saving, in the coarsening/case split.

### Section 4.3 — the cited transfers work, with their original hypotheses retained

- PRIMELAW: `h*(p)≤7` at small primes and `h*(p)≤2p^{-1/2}` above W suffice for every new Euler-product and tail estimate. In particular `h*(p)p^{1/4}≤1` for `p>W≥16`. The Γ* replacement is valid; no extra first-moment loss reappears.
- LARGESIEVE Theorem 3.1 constructs a nonnegative CRT square majorant with level `λ(Q₀)+2λ_Θ`; its proof only needs the K2 cap. The improved cap transfers, retaining CRT-admissibility and the fibre/denominator restrictions.
- INTERFREQ Corollary 2.3 uses `(N−D)Eν` and level at most `log D`; substitution is direct. “Moduli ≤N/2” must mean the **expanded majorant terms**, not merely the original forced classes.
- TUPLES Corollary 3.4 directly improves under its original polynomial-modulus and CRT-main-term hypotheses. This does not license D3's broader interpretation.

### Theorem 5.1 — the substantive extension is valid

The downward induction in EK Theorem 4.1 applies (S_w) to a uniform average of the original nonnegative ν with earlier coordinates fixed. It does **not** require the cost-weighted function from the other side of the induction to belong to the function class. Uniform averaging and fixing coordinates only shrink each support T, and all truncated weights are positive. Thus the proposed function class is sufficient.

The listed blocks partition the prime coordinates in increasing order for `0<L₀<λ`. If `L₀<s₁`, the intermediate blocks are empty; if `L₀<log W`, even the singleton range is empty. There is no unprocessed gap. The top block has d₀-locality regardless of how many scales or prime powers it spans. EK Theorem 2.5 is independent of block width and pattern arity. Primes beyond `e^Λ` activate no classes and contribute zero mass; alternatively project them away first.

For precision in implementing the cost, either use the conditional choice `t(h)=d₀/(E[M|h]+4d₀)` and then Jensen, or use the fixed global choice `t=d₀/(𝔐(e^Λ)+4d₀)` and average Corollary 2.6's proof over histories. Both justify the displayed global mean cost. One must not assert that the unconditional mass bound bounds every conditional mass; fortunately that assertion is unnecessary.

The sequential output law and its coordinatewise inflation are unchanged by regrouping primes. Every class is still decided at its largest prime. K2's cofactor second-moment proof uses only that order and inflation, not the logarithmic width of a block. Hence the same absolute W gives leak at most 1/2. No new log-log factor is hidden here.

Corollary 5.2 follows for `k≥2` as written; D7 repairs k = 1. Projection preserves both the truncated-level bound and prime order. For Corollary 5.3, the elementary support-union inequality `ω_{>W}(lcm(G₁,…,G_k))≤kr` is correct. The exact Theorem 5.1 bound even handles `kr>Λ³` with an `O(kr)` top cost; the upper-order restriction in Corollary 5.2 is not a fundamental obstruction. The problems are the advertised examples and open-scope interpretation, D1–D3.

### Section 6 — Λ² majorants really are in the class

For the displayed real square, every nonempty hit-intersection indicator vanishes on the whole avoider set, so `λ_∅=1` makes ν equal to 1 there and ν is nonnegative everywhere. A product of two intersection indicators is either zero or a residue-class indicator modulo an lcm. Its prime support is the union of the two supports, so squaring at most doubles the level. More generally TW4's admissible `g∈V_{λ/2}`, `g≥1` on the avoiders, has `g²` in the level-λ CRT class by the same support-union argument; it need not have the particular hit-polynomial representation displayed here.

Thus Theorem 4.1 really supersedes TW4's **mean-saving cap** for all r, and uses a weaker level charge (only primes above fixed W) than TW4's all-prime level. No bounded-B or bounded-r hypothesis is smuggled in.

Keep the word “saving” tied to `log(1/Eν)` here. A theorem about the mean alone is not a theorem about arbitrary favorable exact interval remainders. The exceptional-set translation still needs Corollary 4.2's evaluation assumptions or an applicable LARGESIEVE/INTERFREQ result. Read in TW4's existing mean-saving convention, §6 is correct; it should not erase those exclusions.

## Reproducibility and form

- Full committed replay, under a 1 GiB virtual-memory limit, reproduces `data/kary3/moments.txt` byte for byte.
- An independent factorization test confirms that `smooth_numbers` returns exactly the y-smooth integers up to 10,000, without duplicates, for each of the four y values.
- An all-block rerun, also under 1 GiB, gives the maxima in D6. The half-open block convention causes no discrepancy: all sampled M are odd and greater than 1, so none is a power-of-two endpoint.
- Brute-force root counts confirm `ρ_{4rL²}(m)≤ρ_{4r}(m)` in 11,520 cases (`1≤r,L≤12`, `1≤m≤80`), including composite moduli and noncoprime L. This supplements, not replaces, the prime-power proof.
- `git diff --check` on the reviewed commit range passes. No build step is pertinent to these Markdown/data changes; the Python replay runs successfully.
- The numerical script's enumeration/factorization logic is sound for the documented invocation. The misleading maximum comes from prose and a failure to report/check all blocks, not from corrupted data.
- The manuscript is generally well organized and makes external inputs visible. Distinguish asymptotic theorem claims from finite numerical observations, preserve the hypotheses in summary tables, and avoid calling the remaining class-order scope “exact” until D1–D3 are repaired.
