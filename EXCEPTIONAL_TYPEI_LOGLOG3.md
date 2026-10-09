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
