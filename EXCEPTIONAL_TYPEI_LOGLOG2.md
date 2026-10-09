# EXCEPTIONAL_TYPEI_LOGLOG2 — closing the exceptional-eigenvalue strip of (D)32 (task O116)

Status labels as in DISCOVERIES.md. TTL = `EXCEPTIONAL_TYPEI_LOGLOG.md` (Thm 8.1, CONDITIONAL on (SEL));
DI = Deshouillers–Iwaniec, Invent. Math. 70 (1982) 219–288 (scan `sources/o111/deshouillers-iwaniec-1982.pdf`,
journal pages 219–288 = PDF pages 1–70; p. 232 = PDF p. 14). `L = log N`. Work in progress.

## 0. Summary (running)

* **Re-examination of TTL §3.2/§9.** TTL checked DI Thm 5 (one level) and DI Thm 6 (average over the level,
  general coefficients). It did **not** consider **DI Thm 7** (DI p. 233, (1.41)), the level-averaged
  exceptional large sieve for the **constant sequence** `a_n = 1`:
  `Σ_{q≤Q} Σ^{(q)}_{λ_j exc} X^{4iκ_j} |Σ_{n≤N} ρ_{j∞}(n)|² ≪_ε (QN)^ε (Q + N + X√N) N`
  (DI's "Conjecture" `Q + N + X√N` in place of Thm 6's `Q + N + NX`, proved for `a_n = 1`; equivalently, with the
  weight `Y^{2σ_j}`, `Y = X²`, the bracket is `Q + N + √(NY)` — DI (8.17), p. 276; the audit (§5) found that the
  radical in (1.41) covers only N).
  In TTL Prop 5.1 the unfolded coefficients are `b_n = λφ̂(λn)` — a smooth function of n, not a general
  sequence — so partial summation reduces them to `a_n = 1` (Lemma 1.2 below), and the levels `M = 4dq²` of
  TTL vary with `d ≍ D`, which is exactly an average over the level. §1–§2 show that at `q = 1` this
  removes the exceptional obstruction up to the `(QN)^ε` loss of DI Thm 7, provided the weight
  `(nY)^{−2σ_j}` is kept n-dependent (the crude weight `Y^{−2σ_j}` fails in TTL case (b3)).
* Remaining issues, treated below: (i) the `(QN)^ε` (Lemma 1.1 bookkeeping tolerates a loss
  `N^{O(1/log L)}`, i.e. a strip `δ ≤ C/log L` costs only `O(N L²)`; §3); (ii) the sieve moduli `q > 1`
  need the exceptional spectrum of `Γ₀(4dq²)` with **even nebentypus mod q** (TTL §5), which DI Thm 7 does not
  cover (§4).

## 1. The input from DI and the reduction to `a_n = 1`

**DI normalisation (DI (1.34), p. 230; as in TTL §5).** For `Γ₀(q)` (trivial character), `u_j` an orthonormal
basis of Maass cusp forms, `u_j(z) = √y Σ_{n≠0} ρ_{j∞}(n) K_{iκ_j}(2π|n|y) e(nx)`, `λ_j = 1/4 + κ_j²`;
exceptional means `λ_j < 1/4`, i.e. `iκ_j ∈ (0, 1/4]` real (DI Thm 4 gives `iκ_j ≤ 1/4`). Write
`σ_j := iκ_j` (= TTL's `σ_j`, `λ_j = 1/4 − σ_j²`).

**DI Theorem 7 (cited; DI p. 233, (1.41); read off the scan).** Let `Q, N, X ≥ 1`, `ε > 0`. Then
`Σ_{q≤Q} Σ_{j exc for Γ₀(q)} X^{4σ_j} |Σ_{n≤N} ρ_{j∞}(n)|² ≪_ε (QN)^ε (Q + N + X√N) N`.
(With `Y := X²`: weight `Y^{2σ_j}`, bracket `Q + N + √(NY)`, as in the proof, DI (8.17)–(8.19), §8.3, pp. 276–278.)

**Lemma 1.2 (partial summation; PROVED, elementary).** Let `c : [1,∞) → ℂ` be `C¹` with
`c(t) → 0` and `∫_1^∞ |c'(t)| dt < ∞`, and `S_j(t) := Σ_{n≤t} ρ_{j∞}(n)`. Then
`|Σ_{n≥1} c(n) ρ_{j∞}(n)|² ≤ (∫_1^∞|c'|)·∫_1^∞ |c'(t)| |S_j(t)|² dt`.
*Proof.* `Σ_{n≥1} c(n)ρ(n) = −∫_1^∞ S_j(t) c'(t) dt` (Abel summation; the boundary term vanishes as
`S_j(t) ≪_j t^{3/2}` and `c(t)`decays as in the application — Schwartz decay), then Cauchy–Schwarz with
the measure `|c'| dt`. ∎

**Drappeau's nebentypus version (cited; Drappeau, Proc. LMS 114 (2017), arXiv:1504.05549, §4.2.3, Lemma 4.10;
statement as extracted by a research subagent, `/tmp/o116_lit.md` — to be eyeballed against the PDF).** For a Dirichlet
character χ mod `q₀`, `Y ≥ 1`, `Q ≥ q₀`, and `a_n = 1_{N<n≤2N}`-type interval coefficients,
`Σ_{q≤Q, q₀|q} Σ_{f ∈ 𝓑(q,χ), t_f ∈ iℝ} Y^{2|t_f|} |Σ_{N<n≤2N} a_n n^{1/2}ρ_{f,∞}(n)|² ≪_ε (QN)^ε (Q/q₀ + N + (NY)^{1/2}) N`
(Drappeau's `n^{1/2}ρ_f(n)` is DI's `ρ_j(n)` up to an absolute constant; `Y^{2|t_f|} = Y^{2σ_j}`, the same
normalisation as DI (8.17)). For `q₀ = 1` this is DI Thm 7. Every summand is `≥ 0`, so the bound holds for any
subset of the levels `q ≤ Q, q₀ | q` — e.g. `{4dq² : d ≍ D}` when `q₀ | q`. A sharp interval `(N, N₁]`,
`N₁ ≤ 2N`, is the difference of two prefix sums, so (with `|x−y|² ≤ 2|x|²+2|y|²`) the same bound holds for
`S_j(t) := Σ_{n≤t} ρ_j(n)` with `N` replaced by `2t` (dyadic decomposition of `[1,t]` and Cauchy–Schwarz over the
`≪ log 2t` blocks: an extra factor `log² 2t`).

Notation for the rest: **(DI7_ε)** denotes the resulting bound, uniformly in `M₀, t, X ≥ 1` and in the
character modulus `q₀ | q`:
`Σ_{M ≤ M₀, q₀|M} Σ_{j exc} Y^{2σ_j} |S_j(t)|² ≤ C_ε (M₀ t)^ε (log 2t)² (M₀ + t + √(tY)) t`  for all `Y ≥ 1`.

## 2. The exceptional part of TTL Prop 5.1, averaged over d (PROVED rel. (DI7_ε))

Setting of TTL §5–§6: q squarefree, `(q,2d) = 1`, `M = 4dq²`, χ even mod q, `ψ(u) = φ(x/λ)W(y/Y)`,
`Y ≤ λ𝓛^{−3}`, `P_χ = Σ_{Γ_∞\Γ₀(M)} χ̄(γ)ψ∘γ`, `B_j(s) = Σ_{n≠0} ρ̄_j(n) b_n(s)`, `b_n(s) = λφ̂(λn)|n|^{−s}`.

**Lemma 2.1 (exceptional coefficients on a shifted line; PROVED).** Let `u_j` be an exceptional cusp form of
`(Γ₀(M), χ)`, `t_j = iσ_j`, `0 < σ_j ≤ 1/4`. With `s_v := σ_j + 1/𝓛 + iv` and
`B̃_j(s) := Σ_{n≠0} ρ̄_j(n) λφ̂(λn) (π|n|Y)^{−s}`:
`|⟨P_χ, u_j⟩|² ≪ 𝓛⁴ Y^{−1} ∫_ℝ |𝒲(s_v)| |B̃_j(s_v)|² dv`.
*Proof.* TTL Prop 5.1 Step 2 gives `⟨P_χ,u_j⟩ = Y^{−1/2}(8πi)^{−1}∫_{(σ)} G_{t_j}(s)𝒲(s) B̃_j(s) ds` on any line
`σ > σ_j` (the Mellin formula for `K_{it}` needs `Re s > |Im t|`). Take `σ = σ_j + 1/𝓛`. There
`G_{t_j}(s) = Γ((s−σ_j)/2)Γ((s+σ_j)/2)` has arguments of real part in `[1/(2𝓛), 1]`, so by TTL Step 3
`|G_{t_j}(s_v)| ≪ 𝓛² e^{−π|v|/2}`. Cauchy–Schwarz in v with the measure `|G𝒲| dv`. ∎
(No contour shift is made, so the `1/σ_j` singularities of `Γ(±σ_j)` never appear.)

**Proposition 2.2 (averaged exceptional variance; PROVED rel. (DI7_ε)).** Fix q, `λ > 0`, `D ≥ 1`, `F' ≥ 1`, and for
each `d ≍ D`, `(d, 2q) = 1`, the TTL test function `ψ_d(u) = φ(x/λ)W(y/Y_d)` with `Y_d = 1/(2qF'√d)`. Put
`M₀ := 8Dq²`, `Y₀ := 1/(2qF'√D)` (so `Y_d ∈ [Y₀/√2, Y₀]`), `λ₋ := min(λ, 1)`, and let `𝓔_d` be the exceptional part
of TTL Prop 5.1 Step 1 for `P = P_{ψ_d}` on `Γ_{M,q}`, `M = 4dq²`:
`𝓔_d := (2/φ(q)) Σ_{χ even mod q} Σ_{u_j ∈ 𝓑(M,χ), t_j ∈ iℝ} |⟨P_χ, u_j⟩|²`. Then for every `ε ∈ (0, 1/4]`
`Σ_{d≍D} 𝓔_d ≪ 𝓛^C C_ε (M₀/(λ₋Y₀))^{2ε} Y₀^{−1} [λ₋M₀ + 1 + λ₋Y₀^{−1/2}]`,
with C and the implied constant depending only on φ, W (𝓛 as in TTL Prop 5.1, `≥ log(1/Y₀)`).
*Proof.* Split `B̃_j(s) = Σ_{n≥1} ρ̄_j(n)c₊(n) + Σ_{n≥1} ρ̄_j(−n)c₋(n)`, `c_±(t) := λφ̂(±λt)(πtY_d)^{−s}`; the `n < 0`
part is the `n > 0` part of the reflected basis `u_j(−z̄)` of `(Γ₀(M), χ̄)` (TTL Step 6), again exceptional with the
same σ_j, so it suffices to treat `n > 0` and all even χ. Put `w(t) := max(1, 1/(πtY₀))` and
`Φ(t) := λ²|φ̂'(±λt)| + λ|φ̂(±λt)|/t` (max over ±). For `s = s_v`: `|(πtY_d)^{−s}| = (πtY_d)^{−σ_j−1/𝓛} ≤ e²w(t)^{σ_j}`
(if `πtY_d ≤ 1` use `Y_d ≥ Y₀/√2` and `(1/Y₀)^{1/𝓛} ≤ e`; otherwise it is ≤ 1), so `|c₊'(t)| ≤ e²(2+|v|)Φ(t)w(t)^{σ_j}`.
Abel summation as in Lemma 1.2 and Cauchy–Schwarz with the measure `Φ dt`:
`|Σ_n ρ̄_j(n)c₊(n)|² ≤ e⁴(2+|v|)²(∫_1^∞Φ)·∫_1^∞ Φ(t) w(t)^{2σ_j}|S_j(t)|² dt`.
Sum over d, χ, j and apply (DI7_ε) for each t with weight `Y = w(t) ≥ 1` and the levels `{4dq² : d ≍ D}` (`≤ M₀`,
divisible by the conductor of χ; positivity); note `√(t·w(t)) ≤ √t + (πY₀)^{−1/2}`. With Lemma 2.1 and
`Y_d^{−1} ≤ √2 Y₀^{−1}`:
`Σ_d 𝓔_d ≪ 𝓛⁴Y₀^{−1}(∫|𝒲(s_v)|(2+|v|)²dv)(∫Φ)∫_1^∞Φ(t)C_ε(M₀t)^ε log²(2t)(M₀ + 2t + Y₀^{−1/2}) t dt`
(the average `(2/φ(q))Σ_χ` of a maximum over χ is ≤ that maximum). Here `∫|𝒲(σ+iv)|(2+|v|)²dv ≪ 1` for
`0 ≤ σ ≤ 1/2` (TTL Step 2); since φ̂ is Schwartz, `∫_1^∞Φ ≪ 𝓛λ₋` and `∫_1^∞Φ(t)t^{1+a}dt ≪ λ₋^{−a}` for `0 ≤ a ≤ 2`
(for `λ ≤ 1` the integrand is `≪ λt^a` on `t ≤ 1/λ` and Schwartz-small beyond; for `λ > 1` everything is `≪ λ^{−B}`).
Bounding `(M₀t)^ε log²(2t) ≪ 𝓛²M₀^ε t^{2ε}` and using `a ∈ {2ε, 1+2ε}` gives the claim (`λ₋^{−2ε} ≤ (λ₋Y₀)^{−2ε}`). ∎
*Remarks.* (1) The weight `w(t)^{2σ_j} ≈ (tY)^{−2σ_j}` must be kept t-dependent: with the crude weight
`Y₀^{−2σ_j}` the third term would be `λ₋^{1/2}Y₀^{−1/2}·Y₀^{−1}`, larger by `λ^{−1/2}`, which fails in TTL case (b3).
(2) This is where the `a_n = 1` structure is used: the whole n-range is absorbed at once by partial summation. TTL
§3.2's DI Thm 5/6 bookkeeping could not do this (Thm 6 has `NX` instead of `X√N`).

## 3. Unconditional averaged per-d count, and the strip

**Theorem 3.1 (TTL Thm 6.2 averaged over d, unconditional; PROVED rel. (DI7_ε) and the TTL inputs).** In the
setting of TTL Thm 6.2 (`f' ≍ F'` the cusp variable, `a ≍ A`, `λ ≍ A/(qF')`, `Y_d = 1/(2qF'√d)`), with
`E_d(q) := Σ_{Q∈𝓕_d^I, q|n(Q)} ψ_d(u_Q) − g_{c,d}(q)𝔐_d`, for every `ε ∈ (0,1/4]` and `A, D, F', q ≤ N`:
`Σ_{d≍D} |E_d(q)| ≪ 𝓛^C C_ε^{1/2} N^{4ε} · AD · [q²(D/A)^{1/2}(1 + A/(qF'))^{1/2} + q^{3/2}F'^{1/2}/A + q^{5/4}F'^{1/4}D^{1/8}A^{−1/2}]`.
*Proof.* TTL Cor 4.4 and Lemma 6.1/Thm 6.2's last line give `|E_d(q)| ≪ q(#Λ_d(1))^{1/2}V_d^{1/2}`,
`V_d := ‖(1−Δ)P₀^{(d)}‖²`; TTL Step 0 writes `(1−Δ)P₀` as `P_{ψ'} − ⟨P_{ψ'}⟩` with ψ' a sum of two functions of the
same type, so it suffices to bound V_d for ψ. Parseval (TTL Step 1) splits `V_d = V_d^{gen} + 𝓔_d`; `V_d^{gen}` (cusp
forms with `t_j ∈ ℝ`, Eisenstein part, constant terms) is bounded by TTL Steps 2–7 **without (SEL)** (SEL was used
there only to assert `t_j ∈ ℝ`; the large sieve over the subset `t_j ∈ ℝ` is bounded by the full one, positivity):
`V_d^{gen} ≪ 𝓛^C[(λ/Y_d)(1+λ) + q^{1/2}M^{−1}λ^{−1−ε}/Y_d]`. Cauchy–Schwarz over d and TTL Lemma 6.3
(`Σ_{d≍D}#Λ_d(1) ≪ D^{3/2}𝓛²`): `Σ_d|E_d(q)| ≪ 𝓛^C q D^{3/4}(Σ_d V_d^{gen} + Σ_d 𝓔_d)^{1/2}`, where
`Σ_d V_d^{gen} ≪ 𝓛^C N^{ε}[D(λ/Y₀)(1+λ) + q^{−3/2}/Y₀]` and Prop 2.2 (`(M₀/(λ₋Y₀))^{2ε} ≤ N^{8ε}`, `λ₋M₀ ≤ 8q²Dλ`).
With `λ/Y₀ ≍ A√D` and `1/Y₀ = 2qF'√D` the three terms `q²Dλ(1+λ)/Y₀`, `1/Y₀`, `λY₀^{−3/2}` give the relative errors
`q²(D/A)^{1/2}(1+λ)^{1/2}`, `q^{3/2}F'^{1/2}/A`, `q A^{−1/2}Y₀^{−1/4} ≍ q^{5/4}F'^{1/4}D^{1/8}A^{−1/2}`. ∎

**Corollary 3.2 (the TTL cases (b2), (b3), (b5) unconditionally; PROVED rel. (DI7_ε)).** Let `δ = 2α−1+γ > 0`
(so `A/D ≍ N^{δ}`) and use the cusp variable chosen in TTL §8: (b2) `F' = e ≤ 4A`, used by TTL only when `k ≥ 2j`, so `δ ≥ 2γ`; (b3) `F' = min(e,f) ∈ [8A, 3A√D]`;
(b5) `F' = f ≤ A` with `A/f ≤ N^{δ/2}`. Then the relative remainder (Thm 3.1 divided by AD) is
`≪ 𝓛^C C_ε^{1/2} N^{4ε} q² (N^{−δ/4} + N^{−1/20})`.
*Proof.* First term: as in TTL (b2)/(b5), `(1+A/(qF'))^{1/2} ≤ 2N^{δ/4}` (b2: `(A/e)^{1/2} ≤ N^{γ/2} ≤ N^{δ/4}` as `δ ≥ 2γ`;
b5: by hypothesis), and `λ ≤ 1/8` in (b3); so it is `≪ q²N^{−δ/4}`. Second term: `F'^{1/2}/A ≪ D^{1/4}A^{−1/2} ≤ A^{−1/4}`.
Third term: in (b3) `F'^{1/4}D^{1/8}A^{−1/2} ≪ (A√D)^{1/4}D^{1/8}A^{−1/2} = (D/A)^{1/4} ≍ N^{−δ/4}`; in (b2), (b5)
`≪ A^{1/4}D^{1/8}A^{−1/2} ≤ A^{−1/8}`. In all three cases `D < A`, so `A ≫ N^{(1−η)/2}` and `A^{−1/8} ≪ N^{−1/20}`
for `η ≤ 1/10`. ∎

## 4. The Type I sum

**Hypothesis (EFF).** (DI7_ε) holds with `C_ε ≤ exp(exp(A₀/ε))` for an absolute `A₀` and all `ε ∈ (0,1/4]`, for DI
Thm 7 and for its nebentypus form, Drappeau Lemma 4.10, uniformly in the character modulus. (DI and Drappeau state
`≪_ε` and do not give the ε-dependence. §5 explains why their proofs give EFF; this is an Assessment.)

**Theorem 4.1.** Let `L = log N`.
(i) (PROVED relative to TTL's cited inputs, DI Thm 7 and Drappeau Lemma 4.10; **no (SEL)**.) There is an absolute C
such that for every `ε₀ ∈ (0,1)`: `Σ_{p≤N} f_I(p) ≤ C ε₀ N L² log L + O_{ε₀}(N L²)`. In particular
`Σ_{p≤N} f_I(p) = o(N log²N log log N)`.
(ii) (CONDITIONAL on (EFF).) `Σ_{p≤N} f_I(p) ≪ N log²N`.
(iii) More generally, if `C_ε ≤ G(1/ε)` with G nondecreasing, then `Σ_{p≤N} f_I(p) ≪ N L²(1 + w_N log L)`, where
`w_N := inf{w ∈ [L^{−1/2}, 1] : log G(128/w) ≤ wL/32}`.
*Proof.* Dyadic in N, as in TTL §8. TTL uses Thm 6.2, and hence (SEL), only in the cases (b2), (b3) and (b5) of (2b).
It uses them only through `Σ_{d≍D}|E_d(q)|` (TTL §6 Remark D11; Cauchy–Schwarz over d). Replace that use by Thm 3.1 and
Cor 3.2. Their bound differs from TTL's (SEL) bound only by a factor `≪ 𝓛^C C_ε^{1/2}N^{4ε}q` and by the term `N^{−1/20}`.
In TTL (3) take `κ = 1/4`, so `z = N^{δ/32}` and `Q = z² = N^{δ/16}`, and use `Σ_{q≤Q}3^{ω(q)}q² ≪ 𝓛^C Q³`. Fix a
threshold `w ∈ (0,1]` and put `ε := w/128`. For `δ ≥ w` the sieve remainder, and the `|r_σ(1)|` part of the main
term, are then `≪ 𝓛^C C_ε^{1/2}(N^{−δ/4+3δ/64+δ/32} + N^{3δ/64+δ/32−1/20}) ≤ 𝓛^C C_ε^{1/2} N^{−11δ/64}` times the mass.
This uses `δ ≤ 1/3 + 4η₁ ≤ 0.35` on R_bad, so `N^{5δ/64−1/20} ≤ N^{−11δ/64}`.
Call a layer `k = ⌊δL⌋` **good** if `δ ≥ w` and `𝓛^C C_ε^{1/2}N^{−11δ/64} ≤ 1/(δL)`. On good layers TTL's steps (3)
and (5) apply unchanged (saving `C/k`, Lemma 1.1).
On every other layer of the `D < A` side, use TTL (b4) (Brun–Titchmarsh on 4ad) for the whole layer, as in TTL (4).
It costs `≪ NL/j` for each c-block `j ≥ 1`, plus `≪ NL` for the block `c ≍ 1` (Lemma 1.1's remark in TTL). That is
`≪ NL log L` per layer. All other parts of TTL §8 ((1), (2a), bands, (b1), (b4)) are unconditional and unchanged.
(i) Take `w = ε₀`. Then `C_ε = C_{ε₀/128}` is a constant, and `N^{−11δ/64} ≤ N^{−ε₀/6}`. So for `N ≥ N₀(ε₀)` every
layer with `δ ≥ ε₀` is good. There are `≤ ε₀L + 1` bad layers, costing `≪ ε₀NL² log L + NL log L`. The rest is TTL's
`O(NL²)`. Then sum dyadically over N.
(ii) Take `w = w_N := 256A₀/log L`. Then `log C_ε ≤ exp(A₀/ε) = exp(128A₀/w) = L^{1/2}`. For `δ ≥ w` we have
`(11/64)δL ≥ 44A₀L/log L ≥ L^{1/2}/2 + (C+1)log L + log L` when `L ≥ L₀(A₀)`. So every layer with `δ ≥ w_N` is good.
The `≤ w_N L + 1` bad layers cost `≪ (w_N L + 1)NL log L ≪ A₀NL²`.
(iii) As in (ii), with `w = w_N`. For `δ ≥ w_N` we have `log C_ε ≤ log G(128/w_N) ≤ w_N L/32 ≤ δL/32`, and
`11δL/64 − δL/64 = 5δL/32 ≥ (C+2)log L` because `δ ≥ L^{−1/2}`. Bad layers number `≤ w_N L + 1`. ∎
*Remark.* Only the D < A side of the strip ever used (SEL). The (b1) side, `D ≥ A`, is unconditional by Weil (TTL
Prop 7.1). So "the strip" of TTL §9 is exactly the set of layers that are not good, and it lies inside `0 < δ < w`.
