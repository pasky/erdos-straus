# T-F: effective twisted Lemma 8.1 and the preliminary bound

**Status:** proved relative to the stipulated twisted Kuznetsov identity, the three
spectral large sieves, LOGLOG3 Proposition 6.1 in its U-form, and Selberg's
`0 < σ_f ≤ 1/4`. Uniform in every even Dirichlet character χ modulo r, including
imprimitive characters. The analytic estimates below are those proved in
`ttl3_lemma81_effective.md` §2; no twisted Weil estimate is an additional input here.

## 1. Statements and constants

Use the cusp ∞ with scaling matrix Id, level `L = rq`, and **DI coefficients**
`f(z) = √y Σ_{n≠0} ρ_f(n)K_{it_f}(2π|n|y)e(nx)`.
Thus `ρ_f(n) = 2√n ρ_f^Dr(n)` for positive n: the b in the nebentypus audit
is `ρ_f/2`, not literally `ρ_f`. This absolute normalization matters, not r.
For `I = (N,N₁]`, `N₁ ≤ 2N`, define

`Sχ(Q,Y,N,t;I) = Σ_{Q<q≤16Q} Σ_{f∈B(rq,χ), exc} Y^{2σ_f}|Σ_{n∈I} n^{it}ρ_f(n)|²`,

and `Sχ* = sup_I Sχ(Q,Y,N,0;I)`. Define this finite sum for **every Q > 0**.
Let `0 < δ ≤ 1/10`, `e = δ/4`, `D(e) = (2/e)^{2^{1/e}}`, `A = 2^{32768}`, and put

`K₁χ(δ) = Aδ⁻²[1 + K_LSχ(e) + D(e)K14(e)]`,
`cχ(δ) = Aδ⁻²[1 + K_LSχ(e)]`.

For `Q,Y,N ≥ 1` the precise inputs requested in the nebentypus audit are

**(P1χ)** `Sχ*(Q,Y,N) ≤ K₁χ(δ)(NY)^δ(Q + N + Y)N`;

**(P2χ)** with `C = πNY/(rQ)`,
`Sχ(Q,Y,N,0;I) ≤ cχ(δ)∫ℝ Sχ(C,Y,N,t;I)dt/(1+t⁴)`
`                  + cχ(δ)(QYN)^δ(Q + N/√r + NY/(√r Q))N`.

In fact our switching error is bounded by
`cχ(δ)(YN)^δ(Q + N/√r + NY/(rQ))N`, which implies the displayed weaker form.
(P1χ), with the same constant and no change to its RHS, also holds for `Q > 0`.
The sieve constant here is for DI-normalized coefficients and all three spectral
pieces in `K_LSχ(e)(T² + √r L⁻¹N^{1+e})‖a‖²`, `T ≥ 1`.
If supplied in Drappeau's `√nρ^Dr` normalization, replace `K_LSχ` by `4K_LSχ`.

## 2. Exact trace identity, transforms, and positivity

The black box used is **Drappeau Lemma 4.5, (4.13), with (4.15)–(4.17)**,
pp. 11–12, specialized to weight zero and `a = b = ∞`; its cited source for this
case is BHM07a §2.1.4. The transforms are (4.9)–(4.10), not an identity with
exceptional eigenvalues omitted. Here is the identity in explicit conventions.
For `φ ∈ C_c^∞(0,∞)`, put

`Jφ(l) = ∫₀∞ J_l(x)φ(x)dx/x`,
`Tφ(t) = πi/(2sinh(πt)) ∫₀∞ [J_{2it}(x)−J_{−2it}(x)]φ(x)dx/x`.

The value at zero is the removable limit. Put
`Sχ(m,n;k) = Σ*_{d mod k} χ̄(d)e((m d̄ + nd)/k)` for `r | k` (Dr (4.2)). Then

`Σ_{k≥1,L|k} Sχ(m,n;k)φ(4π√(mn)/k)/k = H_L + E_L + M_L`,
`M_L = Σ_{f∈B(L,χ)} Tφ(t_f) ρ̄_f(m)ρ_f(n)/cosh(πt_f)`,
`E_L = (1/(4π))Σ_{a singular}∫ℝ Tφ(t) ρ̄_a(m,t)ρ_a(n,t)dt/cosh(πt)`,
`H_L = Σ_{k≥2,k even}Σ_{f∈B_k(L,χ)} 4i^k Γ(k)Jφ(k−1) β̄_f(m)β_f(n)`.

Here `ρ_a(n,t) = 2√n ρ_a^Dr(n,t)` and `β_f(n) = √n ρ_f^Dr(n)` in the last line;
Dr's holomorphic expansion is (4.7). In particular `φ̃^Dr(t) = 4Tφ(t)`.
These are the same Bessel transforms as DI (1.19), (1.21)–(1.22), with the
**positive exceptional sign of DI §8**. The scan of DI (1.22) prints `1/(2i)`
instead of `i/2`, the opposite sign. Using Dr's exact identity above consistently
avoids a sign ambiguity; do not assert positivity for the literal printed DI sign.
There is no diagonal term in this compact-test, same-sign identity.

Take the explicit η of LOGLOG3 Lemma 1.3 and set
`Ψ(u) = η(3u−2)`, `φ(x) = Ψ(Yx)`, `g(q) = η(q/Q)`, `φ_t(x) = x^{it}φ(x)`.
Then `supp Ψ ⊂ [11/12,17/12]`, `Ψ = 1` on `[1,4/3]`, and
`supp g ⊂ [3Q/4,9Q/4]`, `g = 1` on `[Q,2Q]`.
The logarithmic derivative norms through order 12 are bounded by `H = 2^{512}`.
Write `B = 2^{2048}`, `L_Y = 1+log Y`, `Y₀ = 2^{32}`. For `Y ≥ Y₀`, §2 of
the effective untwisted note proves, with exactly these cutoffs and this T,

`|Tφ_t(v)| ≤ B(1+|t|)^4 L_Y(1+|v|)⁻⁴` for real v;
`|Jφ_t(l)| ≤ B(1+l)⁻⁴` for positive odd l;
`Tφ(−iσ)/cos(πσ) ≥ Y^{2σ}/64` for `0 < σ ≤ 1/4`;
`|Tφ_t(−iσ)| ≤ B Y^{2e}L_Y` for `0 < σ ≤ e`;
`Tφ_t(−iσ) = [π4^σ/(2sin(πσ)Γ(1−2σ))]φ*(2σ−it) + Rσ(t)` for `e < σ ≤ 1/4`,
where `φ*(s) = ∫φ(x)x^{−s}dx/x`, `|φ*(2σ−it)| ≤ 2Y^{2σ}`, `|Rσ(t)| ≤ B/e`.

These estimates involve no level or character. They follow from the J-series;
the difference of its two orders cancels the apparent pole at `σ = 0`.
The positive main kernel is
`π[(x/2)^{−2σ}/Γ(1−2σ) − (x/2)^{2σ}/Γ(1+2σ)]/(2sin(πσ))`;
its integrated remainder is at most `2^{20}L_Y Y⁻³ᐟ²`.
Thus the lower bound remains uniform as `σ → 0`; retaining `L_Y` is essential.
Dyadic spectral blocks and the stipulated sieves bound the regular part at level
`L = rv` by
`B² K_LSχ(e)(1+|t|)^4 L_Y(1 + N^{1+e}/(√r v))‖a‖²`.
Cauchy–Schwarz gives the same bound for two different unit-modulus coefficient
twists. Small exceptional parameters and the remainder use the sieve with `T = 1`.
The harmless trace-normalization factors are covered by `B²`.

## 3. Switching, step by step: (P2χ)

**First trace.** For `Y ≥ Y₀`, positivity bounds the exceptional sum over
`Q < q ≤ 2Q` by 64 times the g-weighted exceptional trace at levels rq.
Its arithmetic term is exactly
`Σ_{m,n∈I}Σ_{q,c≥1} g(q) Sχ(m,n;rqc)φ(4π√(mn)/(rqc))/(rqc)`.
The first regular error is at most
`2^{12}B² K_LSχ(e)L_Y(Q + N^{1+e}/√r)N`.
For real N use `‖1_I‖² ≤ 2N`; also `Σ g(q)/q` is bounded absolutely.

**Support and second trace.** The two cutoffs, uniformly for `m,n∈I`, imply
`64C/51 ≤ c ≤ 128C/11`, hence **`C < c < 16C`**, with `C = πNY/(rQ)`.
For fixed c, the remaining q-sum is the trace formula at level **rc**, with
`h(x) = φ(x)g(4π√(mn)/(rcx))`. The same χ modulo r is induced to rc;
there is neither a character modulo rq to transport nor a trace at level c.

**Mellin separation.** Put `G(it) = ∫g(ξ)ξ^{it}dξ/ξ`.
Then `G(it) = Q^{it}∫η(u)u^{it}du/u`,
`|G(it)| ≤ H/(1+|t|^{12})`, and `∫|G(it)|(1+|t|)^4dt ≤ 2^8H`.
Inserting inversion *before* estimating the second spectrum gives
`Th(v) = (1/(2π))∫ G(it)(rc/(4π))^{it}(mn)^{−it/2}Tφ_t(v)dt`.
In particular its inner kernel uses **dx/x**. The spectral product is
`overline{A_f(t/2)}A_f(−t/2)`, where `A_f(u) = Σ_{n∈I}n^{iu}ρ_f(n)`.
The preceding decay and spectral-error rule justify absolute convergence.

**Exceptional split.** Split at `σ = e`. All regular terms, small exceptional
parameters, and the large-σ remainders together are bounded by
`2^{24}B⁴H K_LSχ(e)e⁻¹Y^{2e}L_Y(Q + C + N^{1+e}/√r)N`.
Indeed `Σ_{C<c≤16C}1 ≤ 16C` and `Σ_{C<c≤16C}1/c < 4`, also for `C < 1`.
Since `L_Y ≤ (1+e⁻¹)Y^e`, this is at most
`2^{28}B⁴H K_LSχ(e)e⁻²(YN)^δ(Q + C + N/√r)N`.
The large-σ main term, using `sin(πσ) ≥ 2σ`, is at most
`2^{16}BH e⁻¹∫ Sχ(C,Y,N,u;I)du/(1+u⁴)`.
Here use `|A(t/2)A(−t/2)| ≤ (|A(t/2)|²+|A(−t/2)|²)/2`, then `t = ±2u`;
a product is not silently treated as a square.

**Four enlargements.** Apply this to `(Q_l,Y_l) = (2^lQ,2^lY)`, `0 ≤ l ≤ 3`.
The destination C is unchanged. Left weights dominate the desired weights;
right weights cost `Sχ(C,Y_l,…) ≤ 2^{l/2}Sχ(C,Y,…)` by Selberg.
All four enlargements cost less than `2^{12}`. Replacing C by `πNY/(rQ)`
proves even the stronger error in §1. Since `r,Q ≥ 1`, it implies (P2χ).
All displayed costs fit inside `Aδ⁻²[1+K_LSχ(e)]`.
For `1 ≤ Y < Y₀`, the direct sieve and `Y^{2σ} ≤ 2^{16}` give the error-only
bound; no alteration of C is required.

**Small cofactors.** For `C < 1/16` the destination and arithmetic sums are empty.
For `1/16 ≤ C < 1`, keep the at most fifteen positive cofactors in the defining
sum: the same counting and reciprocal-sum bounds prove the recurrence unchanged.
Do **not** import the untwisted note's error-only argument for all `C < 1`:
`Q > πNY/r` does not supply its comparison `Q > πNY`.
The (P1χ) extension below handles these finite destinations when needed in induction;
cofactor 1 itself is exactly the level sum at `Q = 1/16`.

## 4. Preliminary bound: (P1χ) and prefix rectangles

Apply the first trace directly over `Q < q ≤ 16Q`, without the g cutoff.
The regular error is at most
`2^{12}B²K_LSχ(e)L_Y(Q + N^{1+e}/√r)N`.
Put `k = rqc`. On the φ-support, `8NY < k < 32NY`, independently of r.
The number of pairs `(q,c)` is at most `τ(k/r) ≤ τ(k) ≤ D(e)k^e`.
For `w_k(m,n) = Ψ(4πY√(mn)/k)` and `u = 4πY√(mn)/k`,
`∂_m w = Ψ′(u)u/(2m)`, `∂_m∂_n w = [u²Ψ″(u)+uΨ′(u)]/(4mn)`.
Thus `|∂_m^a∂_n^b w_k| ≤ H N^{−a−b}`, `a,b∈{0,1}`.
Two-variable partial summation is dominated by a **k-independent** positive
measure (endpoint atoms and scaled Lebesgue measures), of total cost at most 16H.

Explicitly, a rectangle `(N,v] × (N,w]` is the signed sum of the four prefixes
`[1,v]×[1,w]`, `[1,N]×[1,w]`, `[1,v]×[1,N]`, `[1,N]×[1,N]`.
For each fixed prefix `(M,H′)`, both endpoints lie in `[N,2N]`, and opening Sχ gives
`|Σ_{m≤M,n≤H′}Sχ(m,n;k)| ≤ U(k;M,H′)`.
This follows by `|χ(d)| = 1` on the units; inversion of d gives precisely the
U-form stipulated in LOGLOG3 Proposition 6.1. No additive shifts are needed
because our scaling matrix is Id. Discard `r | k` only **after** this majorization.
Integrate the sum of U-bounds against the common measure, rather than claiming
a bound for a sum of k-dependent rectangle maxima.

With `K = 32NY`, the arithmetic contribution, including positivity, is at most
`2^{12}H [D(e)K^e/(8NY)] K14(e)(4KN²)^e K(K+4N²)`
`≤ 2^{24}H D(e)K14(e)(NY)^δ(N+Y)N`.
Here `N^{4e}Y^{2e} ≤ (NY)^δ`. Absorb `L_Y` in the regular error and use
`r ≥ 1`; this proves (P1χ) with the stated K₁χ. For `Y < Y₀` use the direct sieve.
The proof also works for every `Q > 0`: `Σ_{Q<q≤16Q}1 ≤ 16Q` and the reciprocal
sum is less than 4, while the multiplicity and k-support are unchanged.

## 5. Printed gaps and repairs

Dr pp. 17–18 need: `S∞∞(m,n;qc)` → `Sχ(m,n;rqc)`; `dx` → `dx/x` in the
Mellin kernel; the second coefficient's index m → n; `S(Q,N,Y,0)` → `S(Q,Y,N,0)`.
A single g only covers `(Q,2Q]`, not `(Q,16Q]`; the four simultaneous enlargements
are necessary. The pictured supports do not imply `(C,16C]`; our narrower Ψ does.
Uniform positivity near `Y = 1` and the `σ → 0` logarithm require the repairs in §2.
On p. 18, prefix differences and the positive U-bound, not merely the statement
of untwisted Thm 14, justify removing χ. The original c-support asserted there is
also unnecessary: the exact k-support above supplies the needed conductor-free bound.
