# EXCEPTIONAL_TYPEI_LOGLOG3 — towards an unconditional (EFF) (task O121)

Status labels as in DISCOVERIES.md. TTL2 = `EXCEPTIONAL_TYPEI_LOGLOG2.md` (Thm 4.1(ii) CONDITIONAL on (EFF));
DI = Deshouillers–Iwaniec, Invent. Math. 70 (1982) 219–288 (`sources/o111/…`, journal p. k = PDF p. k−218);
Dr = Drappeau, arXiv:1504.05549 (`sources/o116/…`). Audit = `scripts/ttl2_di7_effectivity_audit.md` (Assessment).

**Work in progress.** Sections are added one lemma at a time; each carries its own label.

## 0. Target and what exactly must be proved

TTL2 Thm 4.1(iii) needs (DI7_ε) — DI Thm 7 and its nebentypus form Dr Lemma 4.10, uniformly in the character
modulus — with `C_ε ≤ G(1/ε)`, G explicit. With `G(1/ε) = exp(exp(A/ε))` it gives exactly `≪ N log²N`.

**Equivalent "loss-function" form (used throughout).** For a family of inequalities `X ≤ C_ε P^ε Y` (P a size
parameter ≥ 3) put `Λ(P) := inf_{0<ε≤1/4} C_ε P^ε`. If `C_ε ≤ exp(exp(A/ε))`, then (ε = 2A/log log P)
`Λ(P) ≤ exp((log P)^{1/2} + 2A log P/log log P)`. Conversely TTL2's proof of Thm 4.1(ii) only uses (DI7_ε)
at `ε = w_N/128 ≍ A/log L`, i.e. only needs `Λ(N^{O(1)}) ≤ exp(O(L/log L))` for the relevant inequality.
(TTL2 Thm 4.1(iii): bad layers cost `w·NL² log L`; `w ≍ 1/log L` gives `O(NL²)`.)

**Classes.** Call a constant `K(δ)` (0 < δ ≤ 1/4) *of class 𝓔(B)* if `K(δ) ≤ exp(exp(B/δ))`. Plan:
every non-inductive input of DI Thm 7 gets a constant of class 𝓔(B) with an explicit (or at least explicitly
bounded) B; the induction of DI (8.19) then gives class 𝓔(A) for Thm 7 (Lemma 1.4 below).

**Dependency chain of DI Thm 7 (from the Audit; to be re-derived here).**
Thm 7 (§8.3, pp. 276–278) ⇐ Lemma 8.1 (pp. 271–273, Kuznetsov switching q ↔ c) + Thm 14 (pp. 275–276,
Kloosterman bilinear form over SL₂(ℤ)) + Thm 2 (spectral large sieve, pp. 255–261) + Selberg `iκ_j ≤ 1/4`.
Thm 14 ⇐ Lemma 8.2 (Fourier majorants) + Thm 9 at level 1 ⇐ Thm 13/Thm 8 at level 1 + Lemma 7.1 + Thm 2.
Exact identities (Kuznetsov/Petersson trace formulae, DI Thm 1 & (8.7)–(8.8)) and Weil's bound
`|S(m,n;c)| ≤ τ(c)(m,n,c)^{1/2}c^{1/2}` are accepted as cited black boxes (absolute constants, no ε).

## 1. Effective toolkit (all PROVED, elementary)

**Lemma 1.1 (explicit divisor bounds).** Let `B ≥ 1`, `0 < δ ≤ 1`, and f multiplicative with `0 ≤ f(p^a) ≤ (a+1)^B`
for all prime powers (e.g. `f = τ^B`, or `f = τ_k` with `B = k−1`). Then for all n ≥ 1
`f(n) ≤ (2B/δ)^{B·2^{B/δ}} n^δ`, a constant of class 𝓔(B log 2 + o(1)): `log log` of it is `≤ (B log 2)/δ + log(B log(2B/δ))`.
*Proof.* `f(n)/n^δ ≤ Π_{p^a‖n} ((a+1)p^{−aδ/B})^B`. If `p^{δ/B} ≥ 2` each factor is `≤ ((a+1)2^{−a})^B ≤ 1`.
Otherwise (`p < 2^{B/δ}`, at most `2^{B/δ}` primes) use `p ≥ 2`: with `c = (δ/B)log 2 < 1`,
`max_{a≥0}(a+1)e^{−ca} ≤ max(1, e^{c−1}/c) ≤ 1/c ≤ 2B/δ`. ∎

**Lemma 1.2 (logarithm absorption).** For `x ≥ 1`, `r > 0`, `δ > 0`: `(log x)^r ≤ (r/(eδ))^r x^δ`. (Maximise
`r log u − δu`.) ∎ In particular `(log x)^r ≤ x^δ` once `x ≥ exp((2r/δ)log(2r/δ))`, and constants of this type
are `exp(O_r(δ^{−1}log(2/δ)))`, far inside 𝓔(·).

**Lemma 1.3 (an explicit Gevrey-2 cutoff).** There is `η ∈ C^∞(ℝ)`, `0 ≤ η ≤ 1`, `η = 1` on `[1,2]`,
`supp η ⊂ [3/4, 9/4] ⊂ (1/2, 3)`, with `‖η^{(p)}‖_∞ ≤ 8e^{16}·36^p (p!)²` for all `p ≥ 0`.
*Proof.* (a) `h(x) := e^{−1/x}` (x > 0), `0` (x ≤ 0) satisfies `|h^{(p)}(x)| ≤ 9^p(p!)²`: for x > 0 apply Cauchy's
formula on `|z−x| = x/2`, where `Re(1/z) = Re z/|z|² ≥ (x/2)/(3x/2)² = 2/(9x)`, so
`|h^{(p)}(x)| ≤ p!(2/x)^p e^{−2/(9x)} ≤ p! 2^p (9p/2)^p e^{−p} ≤ 9^p (p!)²` (max over `u = 1/x` of `u^pe^{−2u/9}`;
`p^pe^{−p} ≤ p!`). (b) `ρ(x) := h(1/4+x)h(1/4−x)/I`, `I := ∫ h(1/4+x)h(1/4−x)dx ≥ (1/4)e^{−16}` (on `|x| ≤ 1/8`
both factors are `≥ e^{−8}`). ρ ≥ 0, `∫ρ = 1`, `supp ρ ⊂ [−1/4,1/4]`, and by Leibniz
`|ρ^{(p)}| ≤ I^{−1}9^p Σ_k C(p,k)k!²(p−k)!² ≤ I^{−1}9^p(p+1)(p!)² ≤ 4e^{16}18^p(p!)²`.
(c) `ρ₈(x) := 2ρ(2x)` (support `[−1/8,1/8]`, `|ρ₈^{(p)}| ≤ 2^{p+1}·4e^{16}18^p(p!)²`), and
`η := 1_{[7/8,17/8]} * ρ₈`. Then `η = 1` on `[1,2]`, `supp η ⊂ [3/4,9/4]`, `0 ≤ η ≤ 1`, and for `p ≥ 1`
`η^{(p)}(x) = ρ₈^{(p−1)}(x−7/8) − ρ₈^{(p−1)}(x−17/8)`, so `‖η^{(p)}‖_∞ ≤ 2·2^p·4e^{16}18^{p−1}((p−1)!)² ≤ 8e^{16}36^p(p!)²`. ∎
*Use.* Any of DI's "fixed smooth η" can be taken to be this η (or an affine rescaling of it, which multiplies the
p-th derivative bound by `(scale)^p`). Then an integration by parts of order p costs at most `C^{p+1}(p!)²`,
and with `p ≍ 1/δ` this is `exp(O(δ^{−1}log(2/δ)))`, inside 𝓔(·).

## 2. DI Thm 7 from three effective inputs: the induction made explicit (PROVED rel. (P1)–(P3))

**Notation (DI (8.4)).** For `Q, Y, N ≥ 1`, `t ∈ ℝ` and a closed interval `I = [N, N₁]`, `N ≤ N₁ ≤ 2N` (closed, as in
DI (8.17), so that n = 1 is covered by `[1,1]`; all input proofs only use `m, n ∈ [N, 2N]`), put
`S(Q,Y,N,t;I) := Σ_{Q<q≤16Q} Σ_{j exc, Γ₀(q)} Y^{2σ_j} |Σ_{n∈I} n^{it} ρ_{j∞}(n)|²` (σ_j = iκ_j ∈ (0,1/4], DI's
normalisation, TTL2 §1), and `S*(Q,Y,N) := sup_I S(Q,Y,N,0;I)`. Two trivial facts:
**(M)** for `Y ≥ Y' ≥ 1`: `S(Q,Y',N,t;I) ≤ S(Q,Y,N,t;I) ≤ (Y/Y')^{1/2} S(Q,Y',N,t;I)` (as `0 < 2σ_j ≤ 1/2`, Selberg
3/16 = DI Thm 4, proved there with absolute constants).
**(PS)** `S(Q,Y,N,t;I) ≤ 2(1+t²) S*(Q,Y,N)`. *Proof.* With `A(ξ) := Σ_{N≤n≤ξ}ρ(n)` (sum over `[N,ξ]`, again an admissible interval), Abel summation gives
`Σ_{n∈I} n^{it}ρ(n) = N₁^{it}A(N₁) − it∫_N^{N₁}A(ξ)ξ^{it−1}dξ`; so `|·|² ≤ 2|A(N₁)|² + 2t²(log 2)∫_N^{2N}|A(ξ)|²dξ/ξ`
(Cauchy–Schwarz for `dξ/ξ` on `[N,2N]`); multiply by `Y^{2σ_j}`, sum, and use `(log 2)² ≤ 1`. ∎

S is defined by the same finite sum for every real `Q > 0` (empty if `16Q < 1`); this is needed only to make sense of
the right side of (P2) when `πNY/Q < 1` — in that range `ttl3_lemma81_effective.md` §3.5 bounds the left side of (P2) by
its error term alone, and the induction below only invokes (P2) when `πNY/Q ≥ N ≥ 1` (R-C M2).
**Inputs (to be proved effective in §§3–6), for every `δ ∈ (0, 1/10]`, all `Q, Y, N ≥ 1` and all I:**
* **(P1)** (DI p. 276–277: (8.7) + Thm 14) `S*(Q,Y,N) ≤ K₁(δ)(QNY)^δ (Q + N + Y) N`.
* **(P2)** (DI Lemma 8.1, (8.5)) `S(Q,Y,N,0;I) ≤ c(δ)∫_ℝ S(πNY/Q, Y, N, t; I) dt/(t⁴+1) + c(δ)(YN)^δ(Q + N + NY/Q)N`.
* **(P3)** (DI Thm 2, (1.29), summed over `Q < q ≤ 16Q`) `S(Q,1,N,0;I) ≤ K₂(δ)(Q + N^{1+δ})N`.
All of `K₁, c, K₂` are taken `≥ 1`.

**Proposition 2.1 (effective DI (8.19)).** Fix `δ ∈ (0,1/10]`, put
`Q₀ := max((90c)^{1/(10δ²)}, (2π)^{1/(2δ)})`, `H := max(2K₂Q₀, 10K₁, 6c)`. Then for all `Q ≥ 1`, `1 ≤ N ≤ Q`:
`S*(Q, Q^{2−2δ}/N, N) ≤ H Q^{1+4δ} N`.
*Proof.* Write `Y := Q^{2−2δ}/N` (≥ 1). Induction on k: the claim holds for `Q ≤ 2^kQ₀`.
*(A) Q ≤ Q₀.* By (M) with `Y' = 1` and (P3): `S* ≤ Y^{1/2}K₂(Q + N^{1+δ})N ≤
Q^{1−δ}N^{−1/2}·2K₂Q^{1+δ}N ≤ 2K₂Q²N ≤ 2K₂Q₀·Q^{1+4δ}N`.
*(B) Q^{1−2δ} < N ≤ Q.* By (M) with `Y₁ := Q + N ≤ 2Q` and (P1): `S* ≤ (1 + (Y/Y₁)^{1/2})K₁(QNY₁)^δ(Q+N+Y₁)N`.
Here `Y/Y₁ ≤ Q^{1−2δ}/N < 1` and `(QNY₁)^δ ≤ (2Q³)^δ`, so `S* ≤ 2·2^δ·4K₁Q^{1+3δ}N ≤ 10K₁Q^{1+4δ}N`.
(If `Y < Y₁` use the first inequality of (M) instead; same bound.)
*(C) Q > Q₀, N ≤ Q^{1−2δ}.* Then `Q^{2δ} ≥ 2π`. Put `Q₁ := πNY/Q = πQ^{1−2δ} ≤ Q/2` and `Y₁ := Q₁^{2−2δ}/N`.
Then `N ≤ Q₁`, `Y/Y₁ = (Q^{2δ}/π)^{2−2δ} ≥ 1`, and the induction hypothesis applies at `(Q₁, N)`. By (P2), (M), (PS):
`S(Q,Y,N,0;I) ≤ c∫ (Y/Y₁)^{1/2}·2(1+t²)S*(Q₁,Y₁,N) dt/(t⁴+1) + c(Q^{2−2δ})^δ(Q + N + Q^{1−2δ})N`
`≤ c·2√2π·Q^{2δ(1−δ)}·H π^{1+4δ}Q^{(1−2δ)(1+4δ)}N + 3cQ^{1+2δ}N ≤ 45cH Q^{1+4δ−10δ²}N + 3cQ^{1+2δ}N`
(`∫(1+t²)dt/(t⁴+1) = √2π`; `2√2π·π^{1.4} < 45`). Since `Q^{10δ²} ≥ 90c` and `Q^{2δ} ≥ 1`, this is
`≤ (H/2 + 3c)Q^{1+4δ}N ≤ HQ^{1+4δ}N`. Taking sup over I closes the induction. ∎

**Theorem 2.2 (effective DI Thm 7, dyadic form; PROVED rel. (P1)–(P3)).** For `δ ∈ (0,1/10]` and all `Q,Y,N ≥ 1`:
`S*(Q,Y,N) ≤ K₇(δ)(QN)^{5δ}(Q + N + √(NY))N`, `K₇ := max(H, 5K₁)`.
*Proof.* N ≤ Q: with `Y₂ := Q^{2−2δ}/N`, if `Y ≤ Y₂` use (M) and Prop 2.1; if `Y > Y₂`,
`S* ≤ (Y/Y₂)^{1/2}HQ^{1+4δ}N = HQ^{5δ}√(NY)N`. N > Q: (M) with `Y₁ := Q+N ≤ 2N` and (P1):
`S* ≤ (1 + √(Y/N))K₁(2N³)^δ·4N·N ≤ 5K₁N^{3δ}(N + √(NY))N`. ∎

**Corollary 2.3 (growth).** If `K₁, K₂, c ≤ exp(exp(B/δ))` with `B ≥ 1`, then `K₇(δ) ≤ exp(exp((B+3)/δ))` for
`δ ≤ 1/10`. *Proof.* `log Q₀ ≤ (log 90 + exp(B/δ))/(10δ²) + δ^{−1}` and `log H ≤ log 2 + exp(B/δ) + log Q₀`;
use `δ^{−2} ≤ e^{2/δ}/4` and `exp(B/δ) ≥ e^{10}` for δ ≤ 1/10. ∎

## 3. (P3) from DI Thm 2 (PROVED rel. effective Thm 2, §5)

Suppose DI Thm 2 (1.29) holds at the cusp ∞ of Γ₀(q) (`μ(∞) = 1/q`) in the form
`Σ_{|κ_j|≤K} |Σ_{N<n≤2N} a_nρ_{j∞}(n)|²/ch(πκ_j) ≤ K_{T2}(δ)(K² + q^{−1}N^{1+δ})‖a‖²`. For exceptional `κ_j = −iσ_j`,
`ch(πκ_j) = cos(πσ_j) ∈ [2^{−1/2}, 1]` and `|κ_j| ≤ 1/4`; take K = 1, `Y = 1` weights `= 1`, `‖1_I‖² ≤ N + 1 ≤ 2N` (closed
intervals; R-C M1), and sum over `Q < q ≤ 16Q`: `Σ_q (1 + N^{1+δ}/q) ≤ 15Q + 1 + (1 + log 16)N^{1+δ} ≤ 16(Q + N^{1+δ})`.
So (P3) holds with `K₂ := 32K_{T2}` (Thm 2 is proved for closed `[N,2N]`, `ttl3_thm2_effective.md` §1). ∎

## 4. (P1), (P2): effective Lemma 8.1 and the preliminary bound (`scripts/ttl3_lemma81_effective.md`)

**Proposition 4.1 (PROVED rel. effective Thm 2 (§5), effective Thm 14 (§6), the exact Kuznetsov formula DI (1.19),
Selberg's 3/16).** With `e := δ/4`, `D(e) := (2/e)^{2^{1/e}}`, `A := 2^{16384}`, (P1) and (P2) hold with
`K₁(δ) = Aδ^{−2}[1 + K_{T2}(e) + D(e)K₁₄(e)]`, `c(δ) = Aδ^{−2}[1 + K_{T2}(e)]` (P1 even with `(NY)^δ`).
Ingredients and repairs (details in the script file): (i) explicit cutoffs `Ψ(u) = η(3u−2)` (plateau `[1,4/3]`,
support `[11/12,17/12]`), `φ(x) = Ψ(Yx)`, `f(q) = η(q/Q)`: with these, the switched moduli satisfy exactly
`64C/51 ≤ c ≤ 128C/11 ⊂ (C,16C]` (DI's pictured supports `[1/2,5/2]` only give `16C/25 ≤ c ≤ 32C` — a gap in
the printed proof, repaired); (ii) the exceptional lower bound `φ̂(−iσ)/cos(πσ) ≥ Y^{2σ}/64` uniformly in
`σ ∈ (0,1/4]` for `Y ≥ 2^{32}` (DI (8.3) is not uniform near `Y = 1`; `Y < 2^{32}` is handled by (M) and Thm 2 with
`Y^{2σ} ≤ 2^{16}`); the error term of DI (8.1) is uniform down to `κ = 0` (the `1/sin πσ` cancels against the
difference of the two Bessel orders); (iii) DI (8.2) needs an extra `log Y` at `κ = 0`, kept as `L_Y = 1 + log Y`
and absorbed by `(1+1/e)Y^e`; (iv) the Mellin pair (8.9) for `f = η(·/Q)` has `|χ(it)| ≤ 2^{512}/(1+t⁴)`, uniformly
in Q, c, δ; (v) the exceptional split at `σ = e` costs `e^{−1}` (from `1/sin πσ`) and `Y^{2e}L_Y`; (vi) in (P1) the
weight `Ψ(4πY√(mn)/k)` is removed by two-variable partial summation with a k-independent majorant measure, then
`τ(k) ≤ D(e)k^e` (Lemma 1.1) and Thm 14 with `K = 32NY`; (vii) the sign of DI (1.22) vs (8.1) is opposite; both
trace-formula applications carry the same sign, which cancels. If `πNY/Q < 1` the error term alone suffices.

## 5. Effective DI Theorem 2 at the cusp ∞ (`scripts/ttl3_thm2_effective.md`)

**Proposition 5.1 (PROVED rel. the Petersson/Kuznetsov identities of DI §4, Weil's bound, Selberg's 3/16).**
For `q ≥ 1`, `K ≥ 1`, `N ≥ 1/2`, `0 < δ ≤ 1/10`, each of DI (1.28), (1.29) (exceptional spectrum included), (1.30) at
the cusp ∞ of Γ₀(q) is `≤ K_{T2}(δ)(K² + q^{−1}N^{1+δ})‖a‖²` with `K_{T2}(δ) ≤ exp(exp(100/δ))` (explicit formula in
the script). The only growing-order step is DI p. 257 (Prop 3, (1.27)): with Lemma 1.3's η and `p = ⌊32/δ⌋`
integrations by parts the non-resonant Poisson terms cost `R_p = 2^{100(p+1)}(p!)⁴`; divisor factors `τ(c)^{≤4}`
cost `(8/s)^{4·2^{4/s}}`, `s = δ/16` (this dominates). Repairs of DI's printed text: the cutoff support must be checked
for the derivative separation on p. 257; p. 259 exponent `2s` should be `3s` (harmless); the diagonal is kept as
`D_K ≤ 2K²` instead of DI's asymptotic (5.2); the Gaussian lower bound pp. 260–261 is restricted to `[|r|, |r|+1]`;
the exceptional part is handled after first establishing `σ ≤ 1/4` (Selberg) non-circularly.

## 6. Effective DI Theorem 14 (`scripts/ttl3_thm14_effective.md`)

**Proposition 6.1 (PROVED rel. effective Thm 2 at level 1, the Kuznetsov/Petersson identities for SL₂(ℤ), and
`λ₁(SL₂(ℤ)) > 1/4` (DI Thm 3)).** For `C, M, N ≥ 1`, `0 < δ ≤ 1/10`:
`Σ_{c≤C} U(c) ≤ K₁₄(δ)(CMN)^δ C(C + MN)`, `K₁₄(δ) = 2^{1200}(1 + K_{T2}(δ))(1 + 6/δ)³`, where
`U(c) := Σ*_{d mod c} |Σ_{m≤M} e(md/c)|·|Σ_{n≤N} e(nd̄/c)| ≥ |Σ_{m≤M}Σ_{n≤N} S(m,n;c)|`.
(The U-form is what DI's proof via Lemma 8.2 actually bounds: (8.14) majorises U(c) by the real, non-negative
`Σ_{m,n} f̂_M(m)f̂_N(n)S(m,n;c)`. It also dominates twisted sums `|Σ_{m,n} S_χ(m,n;c)|`, which §8 uses.)
Zero frequencies (Ramanujan sums) need only the mean divisor bound `Σ_{c≤Z}τ(c) ≤ Z(1 + log Z)`. Only fixed-order
derivatives and fixed contour shifts occur (a numerical replacement of DI Lemma 7.1 with three derivatives). Repairs:
Thm 13's Fourier separation differentiates up to six times, beyond what (7.7) controls (repaired by product
cutoffs with seven controlled derivatives); a cosh factor missing on p. 264 is restored; the `C^ε`-only form (1.52)
is not needed (the `(UV)^{δ/2}` and log factors are summed explicitly over dyadic Fourier blocks).

## 7. Assembly, trivial character

**Theorem 7.1 (effective DI Thm 7; PROVED rel. the black boxes listed in §9).** For `0 < δ ≤ 1/10` and all
`Q, Y, N ≥ 1`: `S*(Q,Y,N) ≤ K₇(δ)(QN)^{5δ}(Q + N + √(NY))N` with `K₇(δ) ≤ exp(exp(410/δ))`.
*Proof.* Thm 2.2 with (P1)–(P3) from Props 4.1, 5.1 (via §3) and 6.1. Constants: `K_{T2}(δ) ≤ exp(exp(100/δ))`,
so `K_{T2}(δ/4) ≤ exp(exp(400/δ))`; `K₁₄(δ/4) ≤ exp(exp(404/δ))`; `D(δ/4) = (8/δ)^{2^{4/δ}} ≤ exp(exp(3/δ))`;
hence `K₁, c ≤ exp(exp(405/δ))` (the factors `Aδ^{−2}` are absorbed since `exp(405/δ) − exp(404/δ) ≥ e^{4040}`),
`K₂ = 32K_{T2}(δ)`, and Cor 2.3 with `B = 405` gives `exp(exp(408/δ))`. ∎

## 8. Nebentypus (Drappeau Lemma 4.10) — the induction with repairs (PROVED rel. (P1χ)–(P3χ))

Fix r ≥ 1 and an even character χ mod r. Following Dr p. 17 the level is renamed `L = rq`
(`scripts/ttl3_nebentypus.md` §1): `Sχ(Q,Y,N,t;I) := Σ_{Q<q≤16Q} Σ_{f∈𝓑(rq,χ) exc} Y^{2σ_f}|Σ_{n∈I}n^{it}ρ_f(n)|²`,
defined for every `Q > 0` (DI normalisation of ρ_f), `Sχ* := sup_I Sχ(·,0;I)`. (M) and (PS) hold verbatim
(Selberg's 3/16 holds for Γ₁(L) ⊃ the forms of (Γ₀(L),χ); `scripts/ttl3_thm2_twisted.md`). Inputs, for
`δ ∈ (0,1/10]`, `Y, N ≥ 1` (`scripts/ttl3_lemma81_twisted.md`, `scripts/ttl3_thm2_twisted.md`):
* **(P1χ)** for all `Q > 0`: `Sχ*(Q,Y,N) ≤ K₁(δ)(NY)^δ(Q + N + Y)N`;
* **(P2χ)** for `Q ≥ 1`, with `C := πNY/(rQ)`: `Sχ(Q,Y,N,0;I) ≤ c(δ)∫Sχ(C,Y,N,t;I)dt/(1+t⁴) + c(δ)(QYN)^δ(Q + N + NY/Q)N`;
* **(P3χ)** for `Q ≥ 1`: `Sχ(Q,1,N,0;I) ≤ K₂(δ)(Q + N^{1+δ})N`;
with `K₁ = K₁χ, c = cχ, K₂ = 32K_{LSχ}` independent of r and χ. Note the switched parameter C carries the
factor `1/r` and can be `< N`, even `< 1`; there the induction hypothesis is unavailable (Dr's "r appears only with
negative powers" needs this extra branch).

**Proposition 8.1 (twisted (8.19)).** With `Q₀ := max((90c)^{1/(10δ²)}, (2π)^{1/(2δ)})` and
`H := max(2K₂Q₀, 10K₁, 200cK₁)`: for all `Q ≥ 1`, `1 ≤ N ≤ Q`, `Sχ*(Q, Q^{2−2δ}/N, N) ≤ HQ^{1+4δ}N`.
*Proof.* As Prop 2.1; cases (A), (B) verbatim (using (P3χ), (P1χ)). Case (C), `Q > Q₀`, `N ≤ Q^{1−2δ}`:
`C = πQ^{1−2δ}/r ≤ Q/2`; the error term of (P2χ) is `≤ c·Q^{3δ}·3Q·N` (`QYN = Q^{3−2δ}`).
*(C1) C ≥ N.* With `Y_C := C^{2−2δ}/N ≤ Y`, the induction hypothesis at C, (M), (PS):
the main term is `≤ c·2√2π·(Q/C)^{1−δ}HC^{1+4δ}N = 2√2π c H Q^{1−δ}C^{5δ}N ≤ 45cHQ^{1+4δ−10δ²}N ≤ (H/2)Q^{1+4δ}N`
(`C^{5δ} ≤ π^{5δ}Q^{5δ−10δ²}`, r ≥ 1).
*(C2) C < N.* No induction: (M) with `Y₁ := C + N ∈ [1, 2N]` and (P1χ) at C give
`Sχ*(C,Y,N) ≤ (1 + √(Y/N))K₁(2N²)^δ·4N·N ≤ 5K₁N^{2δ}(N + Q^{1−δ})N ≤ 10K₁Q^{1+2δ}N` (`√(YN) = Q^{1−δ}`), so the
main term is `≤ 2√2π·c·10K₁Q^{1+2δ}N ≤ 90cK₁Q^{1+2δ}N`.
In both sub-cases `Sχ ≤ (H/2 + 90cK₁ + 3c)Q^{1+4δ}N ≤ HQ^{1+4δ}N`. ∎

**Theorem 8.2 (effective Dr Lemma 4.10).** For `Q ≥ 1/16`, `Y, N ≥ 1`:
`Sχ*(Q,Y,N) ≤ K₇χ(δ)(QN+1)^{5δ}(Q + N + √(NY))N`, `K₇χ := max(H, 10K₁)`, uniformly in r, χ.
*Proof.* `Q ≥ 1`: as Thm 2.2. `Q < 1`: (M) with `Y₁ = 1 + N` and (P1χ): `≤ (1+√(Y/N))K₁(2N²)^δ·4N·N ≤ 5K₁N^{2δ}(N+√(NY))N` (`Q + N + Y₁ ≤ 4N`). ∎

## 9. Main results

**Black boxes (B1)–(B5)** (exact identities or published theorems with absolute constants; no ε):
(B1) the Petersson and Kuznetsov trace formulae for Γ₀(q) at the cusp ∞ (DI §4, (1.19)) and for (Γ₀(L), χ) at ∞
(Dr Lemma 4.5, (4.13)–(4.17), from Blomer–Harcos–Michel 2007 §2.1.4), and for SL₂(ℤ);
(B2) Weil's bound `|S(m,n;c)| ≤ τ(c)(m,n,c)^{1/2}c^{1/2}`;
(B3) a twisted Weil bound `|Sχ(m,n;c)| ≤ C_W τ(c)^{B_W}(m,n,c)^{1/2}(cr)^{1/2}` (χ mod r, r | c) with absolute
`C_W, B_W` (Dr Lemma 4.2; numerical values not certified here — any absolute values suffice);
(B4) Selberg's `λ₁ ≥ 3/16` for congruence subgroups (applied to Γ₀(q) and Γ₁(L));
(B5) `λ₁(SL₂(ℤ)) > 1/4` (DI Thm 3).

**Theorem 9.1 ((EFF) holds; PROVED rel. (B1)–(B5) and the derivations in `scripts/ttl3_*.md`).** (DI7_ε) of TTL2 §1
— DI Thm 7 and Dr Lemma 4.10 for interval/prefix coefficients, all levels `M ≤ M₀` divisible by the modulus r of an
even character χ (r = 1: trivial character), uniformly in r and χ — holds for `0 < ε ≤ 1/4` with
`C_ε ≤ 100ε^{−1}K₇χ(ε/6) ≤ exp(exp(A₀/ε))`, `A₀ := 24B_χ + 30`, `B_χ := 400 + 64b + 16 log(2 + C_W)`,
`b := max(4, ⌈B_W + 1⌉)`. (E.g. `A₀ < 2·10⁴` if `B_W ≤ 3`, `C_W ≤ 10`.)
*Proof.* Thm 8.2 (r = 1 is Thm 7.1 up to the level renaming). Constants: `K_{LSχ}(δ) ≤ exp(exp(B_χ/δ))`
(`ttl3_thm2_twisted.md`; for r = 1 one may use `K_{T2}`), hence (`ttl3_lemma81_twisted.md`, with `K₁₄(δ/4) ≤
exp(exp(404/δ))`) `K₁χ, cχ ≤ exp(exp((4B_χ+1)/δ))`, `K₂χ = 32K_{LSχ}(δ)`; as in Cor 2.3 (with the extra `200cK₁`),
`K₇χ(δ) ≤ exp(exp((4B_χ+4)/δ))`. Conversion to TTL2's form: levels `L = rq ≤ M₀` are covered by
`≤ 2 + log M₀` blocks `(Q_i, 16Q_i]`, `Q_i ≥ 1/16`; the prefix `[1,t]` by the closed intervals `[2^k, min(2^{k+1}−1, t)]`,
`k ≤ log₂ t` (Cauchy–Schwarz over `≤ 1.5 log(2t)` blocks; `Σ 2^k ≤ 2t`). With `δ = ε/6`:
`(2M₀t)^{5δ}(2 + log M₀) ≤ (12/ε)(M₀t)^ε` (Lemma 1.2), so `C_ε ≤ 2·1.5·2·(12/ε)K₇χ(ε/6) ≤ 100ε^{−1}K₇χ(ε/6)`. ∎

**Theorem 9.2 (Elsholtz–Tao Type I sum).** `Σ_{p≤N} f_I(p) ≪ N log²N`.
Status: **PROVED relative to** TTL's cited inputs (as in TTL2 Thm 4.1(i): the ET/MN3 reduction `f_I ≤ 2Σ_c w_c`,
MN3 Thm 3.8(1), DI Thm 2/Drappeau Prop 4.7 at a fixed tolerance, Brun–Titchmarsh, …), (B1)–(B5), and the
explicit-constant derivations of §§2–8 and `scripts/ttl3_*.md`. *Proof.* TTL2 Thm 4.1(ii) with Theorem 9.1:
`w_N = 256A₀/log L`. ∎ (Equivalently TTL2 Thm 4.1(iii) with `G(1/ε) = exp(exp(A₀/ε))`.)

**Honest status of the derivations.** §§1–3, 7, 8 and the reductions are written and checked here line by line. The
analytic estimates of §§4–6 (and their twisted versions) were derived by deep-mode subagents directly from the DI
scan and Drappeau's text, then checked by me structurally (statements, the ε-bookkeeping, the claimed repairs on
DI pp. 256–257, 270–278 against the scan); individual numerical majorants like `2^{1000}` were not re-derived.
They need the parent's independent hostile review before the label PROVED is final. Points most worth attacking:
(a) `ttl3_thm2_effective.md` Steps 4, 7–9 (growing-order integration by parts; Gaussian lower bound; exceptional
atoms), (b) `ttl3_thm14_effective.md` §2 (the numerical replacement of DI Lemma 7.1), (c) the uniform-in-σ
transform bounds in `ttl3_lemma81_effective.md` §2.2, (d) the twisted transfers (`ttl3_thm2_twisted.md`
resonance step; `ttl3_lemma81_twisted.md` small-C branch).
