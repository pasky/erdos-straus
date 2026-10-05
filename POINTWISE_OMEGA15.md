# Beyond low-conductor minorants? A Wiener-norm barrier at `𝓛^4` (task O57)

Status: CHECKPOINT 0 (in progress). Labels as in DISCOVERIES.md. Notation as in
POINTWISE_OMEGA14.md (O14) and POINTWISE_OMEGA13.md (O13): `𝓛=log T`; Haar measure P on the
fibre `H={n≡r (Q)}⊂Ẑ^×`; F = indicator that no ES event `E_{M,D}={n≡−4D (M)}`, `M≤T`, holds;
*big* coordinates `X_ℓ`, ℓ prime, `ℓ>T^{0.6}`, `ℓ∤Q`; *small* coordinates = all others (x_s).

## 0. Question and answer in brief

O14 Thm 4.5: no minorant `B≤F` of level `log D≤c𝓛^4/log𝓛` has `E B>0`. Its "Not covered" list:
prime input beyond low-conductor minorants (bilinear/Type II, parity), Siegel-zero positivity,
minorants of unbounded level. The brief asks for the weakest extension not covered.

Main finding (§1): the planted law of O14 §4 is not only exact on low-level statistics, it is
**exponentially pseudorandom against every bounded product function of high level**: its
deviation from Haar on any residue class, Dirichlet character or additive character, of *any*
modulus, is `≤(8r*)^{k+1}=exp(−c𝓛^4/log𝓛)`. Consequently the level hypothesis in O14 Thm 4.5 can
be replaced by a **Wiener-type norm**: every minorant `B≤F` (any level) has
`E B ≤ e^{−c𝓛^4/log𝓛}·‖B‖_×`, where `‖B‖_×` is the ℓ¹-norm of the coefficients of B in residue
classes / characters. This disposes of GRH-strength transfers, Siegel-zero main terms, and
Fourier (minor-arc) transfers of the Maynard type, as long as they act linearly on a minorant
(or on F itself). What remains outside is listed precisely in §5.

## 1. The planted perturbation is pseudorandom

Setting 1.2 of O14 (one big coordinate per event, `p_b(x_s)≤p*`, `r*=p*/(1−p*)`, odds-sum
`R(x_s)=Σ_b r_b(x_s)`). Assume the *deterministic* planting condition of O14 Lemma 4.1:

```
R(x_s) ≥ (k+1) + (2k+1) r*   for every x_s,          p* ≤ 1/8.                    (1.0)
```

Let ν be the planted law of O14 Thm 1.3 (conditionally on x_s, Lemma 1.1's law on the bits
`b_b=1[X_b∈Ω_b(x_s)]`, big coordinates then drawn from Haar conditioned on their bit), and
`ρ:=ν−P`. By O14 Lemma 4.1, `F=0` ν-a.s.

**Definition 1.0.** A *reduced product* is a function `h=h_s(x_s)·∏_{b∈I}h_b(X_b)` with I a
finite set of big coordinates, `|h_s|≤1`, `|h_b|≤1` and `|E h_b|≤1/4` for `b∈I` (E = Haar).
Examples: the indicator of a residue class `a mod q` restricted to H (for `b|q` big,
`h_b=1[X_b≡a (b^{v_b(q)})]` has mean `≤1/(b−1)`); a Dirichlet character χ (I = big primes of
its conductor; the factors have mean 0); an additive character `n↦e(an/q)` (CRT splits it into
a product of local additive characters; a nontrivial local factor at a big b has mean
`c_{b^v}(·)/φ(b^v)`, of modulus `≤1/(b−1)`).

**Lemma 1.1 (pseudorandomness of the planted perturbation; PROVED).** Under (1.0), for every
reduced product h,

```
|E_ρ h| ≤ (8 r*)^{k+1},       and  E_ρ h = 0  if |I| ≤ k.
```

*Proof.* Fix x_s; write `p_b,r_b,w_J,P_0` for the quantities of O14 Lemma 1.1 at x_s. Given
the bits, the big coordinates are independent; put `β_b:=E[h_b|X_b∈Ω_b]`,
`γ_b:=E[h_b|X_b∉Ω_b]` (for `b∉I`, `h_b≡1`, so `β_b=γ_b=1`). The conditional perturbation is
`ρ_{x_s}=P_0Σ_{|J|=k+1}w_Jσ_J`, `σ_J=Σ_{y⊆J}(−1)^{|y|+1}δ_{1_y}`, so

```
E_{σ_J}[∏_{b∈I}h_b] = Σ_{y⊆J}(−1)^{|y|+1} ∏_{b∈J}(β_b if b∈y else γ_b)·∏_{b∈I∖J}γ_b
                    = −∏_{b∈J}(γ_b−β_b)·∏_{b∈I∖J}γ_b .
```

For `b∈J∖I`, `γ_b−β_b=0`; so only `J⊆I` contribute (in particular nothing if `|I|≤k`).
Bounds: `|γ_b−β_b|≤2`; and `E h_b=(1−p_b)γ_b+p_bβ_b` gives
`|γ_b|≤(|E h_b|+p_b)/(1−p_b)≤(1/4+1/8)/(7/8)<1/2`. Next, `w_J=∏_{J}r_b/e_{k+1}(r)≤r*^{k+1}/e_{k+1}(r)`,
and `e_{k+1}(r)≥1`: the chain in O14 Lemma 1.1's proof with `s=r` gives
`n·e_n(r)≥e_{n−1}(r)(R−(n−1)r*)≥(k+1)e_{n−1}(r)` for `n≤k+1`, so `e_{k+1}(r)≥(k+1)^{k+1}/(k+1)!≥1`.
Finally, with `m:=|I|≥k+1` and `|γ_b|≤1/2`,
`Σ_{J⊆I,|J|=k+1}∏_{b∈I∖J}|γ_b| ≤ C(m,k+1)2^{−(m−k−1)} ≤ 2^m2^{−(m−k−1)} = 2^{k+1}`.
Since `P_0≤1` and `|h_s|≤1`,
`|E_{ρ_{x_s}}h| ≤ r*^{k+1}·2^{k+1}·2^{k+1}=(4r*)^{k+1}`. Average over x_s (the factor `h_s(x_s)`
is x_s-measurable, `|h_s|≤1`): `|E_ρh|≤(4r*)^{k+1}≤(8r*)^{k+1}`. ∎

(The proof gives `(4r*)^{k+1}`; we keep `8r*` as slack for the Siegel variant in §3.)

**Theorem 1.2 (Wiener-norm barrier; PROVED modulo (G), the effective Page bound and the
fundamental lemma — the inputs of O14 Thm 4.5).** There are absolute `c,T_0>0` such that for
`T≥T_0`, every Q with `log Q≤T^{0.05}` and every unit class r: for every function B on the
fibre H with `B≤F` and every finite representation `B=Σ_i c_ih_i` by reduced products,

```
E_H B ≤ η·Σ_i|c_i| ,          η := exp(−c𝓛^4/log𝓛).
```

Write `‖B‖_×:=inf Σ|c_i|` over such representations; then `E_HB≤η‖B‖_×`. Only the `h_i` whose
big part involves `≥k+1≍𝓛^3/log𝓛` big primes (so of modulus `>T^{0.6(k+1)}`) contribute.

*Proof.* O14 Thm 4.5's proof shows `R(x)≥μ*:=c_9ε³𝓛³/log𝓛` for every small configuration x
on H, with `p*≤T^{−0.09}`. Take `k+1:=⌊μ*/2⌋`; then (1.0) holds for T large. By O14 Lemma 4.1
`E_νF=0`, hence `E_νB≤0`, and `E_HB=E_νB−E_ρB≤Σ_i|c_i||E_ρh_i|≤(8r*)^{k+1}Σ|c_i|` by Lemma 1.1.
With `8r*≤16T^{−0.09}/(1−T^{−0.09})≤T^{−0.08}`: `(8r*)^{k+1}≤exp(−0.08𝓛(μ*/2−1))=exp(−c𝓛^4/log𝓛)`. ∎

*Remarks.* (i) Level-D functions (O14 Setting 2.0) with `log D≤0.6𝓛k` are combinations of
reduced products with `|I|≤k`, on which `E_ρ=0`: Thm 1.2 contains O14 Thm 4.5 (norm-free there).
(ii) `F` itself is a minorant of F, so `‖F‖_×≥δ_H/η`, `δ_H:=E_HF`: the avoider indicator's own
Wiener norm exceeds its mean by `e^{c𝓛^4/log𝓛}`.
(iii) Integrability: B is a finite combination of bounded functions, so all expectations are
finite; `ν≪P` with `dν/dP≤2` (O14 m1(b)).
