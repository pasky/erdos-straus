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

**Notation (DI (8.4)).** For `Q, Y, N ≥ 1`, `t ∈ ℝ` and an interval `I = (N, N₁]`, `N₁ ≤ 2N`, put
`S(Q,Y,N,t;I) := Σ_{Q<q≤16Q} Σ_{j exc, Γ₀(q)} Y^{2σ_j} |Σ_{n∈I} n^{it} ρ_{j∞}(n)|²` (σ_j = iκ_j ∈ (0,1/4], DI's
normalisation, TTL2 §1), and `S*(Q,Y,N) := sup_I S(Q,Y,N,0;I)`. Two trivial facts:
**(M)** for `Y ≥ Y' ≥ 1`: `S(Q,Y',N,t;I) ≤ S(Q,Y,N,t;I) ≤ (Y/Y')^{1/2} S(Q,Y',N,t;I)` (as `0 < 2σ_j ≤ 1/2`, Selberg
3/16 = DI Thm 4, proved there with absolute constants).
**(PS)** `S(Q,Y,N,t;I) ≤ 2(1+t²) S*(Q,Y,N)`. *Proof.* With `A(ξ) := Σ_{N<n≤ξ}ρ(n)`, Abel summation gives
`Σ_{n∈I} n^{it}ρ(n) = N₁^{it}A(N₁) − it∫_N^{N₁}A(ξ)ξ^{it−1}dξ`; so `|·|² ≤ 2|A(N₁)|² + 2t²(log 2)∫_N^{2N}|A(ξ)|²dξ/ξ`
(Cauchy–Schwarz for `dξ/ξ` on `[N,2N]`); multiply by `Y^{2σ_j}`, sum, and use `(log 2)² ≤ 1`. ∎

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
`ch(πκ_j) = cos(πσ_j) ∈ [2^{−1/2}, 1]` and `|κ_j| ≤ 1/4`; take K = 1, `Y = 1` weights `= 1`, `‖a‖² ≤ N`, and sum over
`Q < q ≤ 16Q`: `Σ_q (1 + N^{1+δ}/q) ≤ 15Q + 1 + N^{1+δ}log 16`. So (P3) holds with `K₂ := 17K_{T2}`. ∎
