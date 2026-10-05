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

## 2. Linear transfers of any accuracy: GRH, characters, additive characters

**Definition 2.1 (linear prime information).** Let 𝒽 be a family of reduced products on H
and `𝔈≥0`. Put `N_x:=#{p≤x: p∈H}`. A nonnegative measure m on H of mass `N_x` is
*𝒽-consistent at accuracy 𝔈* if `|∫h dm − N_xE_Hh|≤𝔈` for every `h∈𝒽`. A *linear certificate
at accuracy 𝔈* proves "some prime `p≤x` in H has `F(p)=1`" from the facts (i) the prime counting
measure `m_x:=Σ_{p≤x,p∈H}δ_p` is nonnegative of mass `N_x`, (ii) it is 𝒽-consistent at accuracy
𝔈. It is *valid* iff every 𝒽-consistent m has `∫F dm>0`. (Every minorant transfer is one:
from `B=Σc_ih_i≤F`, `h_i∈𝒽`, it concludes `Σ_pF(p)≥Σ_pB(p)≥N_xE_HB−𝔈Σ|c_i|>0`.)

**Theorem 2.2 (no linear certificate below `𝔈<N_xη`; PROVED, same inputs as Thm 1.2).** In
the setting of Thm 1.2, if `𝔈≥N_x·(8r*)^{k+1}` (in particular if `𝔈≥N_xη`), then
`m_ν:=N_xν` is 𝒽-consistent at accuracy 𝔈 for *every* family 𝒽 of reduced products, and
`∫F dm_ν=0`. Hence every valid linear certificate has `𝔈<N_xη≤x·e^{−c𝓛^4/log𝓛}`; and every
minorant transfer `N_xE_HB>𝔈‖B‖_×` needs `N_x/𝔈>e^{c𝓛^4/log𝓛}` (Thm 1.2).

*Proof.* `m_ν≥0`, mass `N_x`; `|∫h dm_ν−N_xE_Hh|=N_x|E_ρh|≤N_x(8r*)^{k+1}` (Lemma 1.1);
`ν(F=1)=0` (O14 Lemma 4.1). ∎

So the only question is how small an accuracy 𝔈 can be *true* for the primes. For families
that are closed under translation, it cannot be small:

**Lemma 2.3 (forced accuracy; PROVED, elementary).** Let `q>x` be a prime, `q∤Q`. 
(a) If 𝒽 contains the classes `1_{a mod q}` for all units a, then every bound 𝔈 valid for
`m_x` on 𝒽 has `𝔈≥1−N_x/(q−1)` (if `N_x≥1`).
(b) If 𝒽 contains all nontrivial Dirichlet characters mod q, or all additive characters
`e(an/q)`, `a≢0`, then `𝔈≥(N_x(q−1−N_x)/(q−2))^{1/2}` resp. `𝔈≥(N_x(q−N_x)/(q−1))^{1/2}−N_x/(q−1)`; for
`q≥x²` both are `≥(1−o(1))√N_x`.

*Proof.* The primes `p≤x` are distinct mod q and nonzero. (a) A class containing one of them
has `∫1_{a}dm_x=1` and `N_xE_H1_a=N_x/(q−1)`. (b) Characters: `Σ_{χ mod q}|Σ_{p}χ(p)|²=(q−1)N_x`
(orthogonality over the distinct units p), and the trivial character contributes `N_x²`; the
`q−2` others have mean square `N_x(q−1−N_x)/(q−2)`, and `E_Hχ=0`. Additive:
`Σ_{a mod q}|Σ_pe(ap/q)|²=qN_x`, `a=0` contributes `N_x²`, so some `a≠0` has
`|Σ_pe(ap/q)|²≥N_x(q−N_x)/(q−1)`; and `|E_He(a·/q)|=1/(q−1)` (Ramanujan sum over units mod q,
H being a union of classes mod Q coprime to q). ∎

**Corollary 2.4 (oblivious linear transfers are capped at 1/4; PROVED implication).**
Certificates through a translation-closed family 𝒽 of reduced products — residue classes
(e.g. O9/Gallagher-type and sieve transfers), Dirichlet characters (e.g. GRH:
`|ψ(x,χ)|≪x^{1/2}log²(qx)`), additive characters (e.g. Vinogradov minor-arc bounds, the
Fourier side of Maynard's restricted-digit method) — with *any* accuracy that is true for the
primes, need

```
classes:     log x ≥ c𝓛^4/log𝓛 ;       characters / additive characters: log x ≥ 2c𝓛^4/log𝓛 ,
```

as soon as 𝒽 contains one full translation orbit at some prime modulus `q>x` (in particular
whenever the minorant uses moduli `>x`, which Thm 1.2 forces: only `h_i` with `≥k+1` big primes,
modulus `>T^{0.6(k+1)}=e^{c𝓛^4/log𝓛}`, carry positive mean). If instead every `h_i` has modulus
`≤x`, then B is a minorant of level `≤x`, and O14 Thm 4.5 gives `E B≤0` as long as
`log x≤c𝓛^4/log𝓛`. Either way: **certified `W(p)≥exp((log p)^{1/4+δ})` is impossible by any
oblivious linear transfer, whatever is assumed about the primes (GRH included).**

*Proof.* Thm 2.2 + Lemma 2.3, with `N_x≤x`. The two cases cover all B (split by maximal
modulus); mixed B are in the first case. ∎

*Reading.* GRH improves accuracy from "BV/Gallagher level x^c" to "square-root error at every
modulus"; Lemma 2.3 says square root is also the floor. Neither touches the barrier, which is a
property of F (the cost `‖B‖_×/E B≥e^{c𝓛^4/log𝓛}` of every minorant), not of the primes.
"Oblivious" = the error bound does not depend on *which* classes contain primes; a certificate
that knows which deep classes are prime-free is using the actual primes ≤ x (cf. §4).
