# Beyond low-conductor minorants? A Wiener-norm barrier at `𝓛^4` (task O57)

Status: CHECKPOINT 1 (for parent review; self-review R57-self by a deep reviewer subagent; parent review R57 `reviews/pointwise-omega15-review.md`: no FATAL, M1–M3 and minors repaired). Labels as in DISCOVERIES.md. Notation as in
POINTWISE_OMEGA14.md (O14) and POINTWISE_OMEGA13.md (O13): `𝓛=log T`; Haar measure P on the
fibre `H={n≡r (Q)}⊂Ẑ^×`; F = indicator that no ES event `E_{M,D}={n≡−4D (M)}`, `M≤T`, holds;
*big* coordinates `X_ℓ`, ℓ prime, `ℓ>T^{0.6}`, `ℓ∤Q`; *small* coordinates = all others (x_s).

## 0. Question and answer in brief

O14 Thm 4.5: no minorant `B≤F` of level `log D≤c𝓛^4/log𝓛` has `E B>0`. Its "Not covered" list:
prime input beyond low-conductor minorants (bilinear/Type II, parity), Siegel-zero positivity,
minorants of unbounded level. The brief asks for the weakest extension not covered.

Main finding (§1): the planted law of O14 §4 is not only exact on low-level statistics, it is
**exponentially pseudorandom against every reduced product (Def 1.0) of high level**: its
deviation from Haar on any residue class, Dirichlet character or additive character, of *any*
modulus, is `≤(4r*)^{k+1}=exp(−c𝓛^4/log𝓛)`. Consequently the level hypothesis in O14 Thm 4.5 can
be replaced by a **Wiener-type norm**: every minorant `B≤F` (any level) has
`E B ≤ e^{−c𝓛^4/log𝓛}·‖B‖_×`, where `‖B‖_×` is the ℓ¹-norm of the coefficients of B in residue
classes / characters.

Scope of the consequences (§2–§3): **linear certificates (Def 2.1) with full-orbit uniform
accuracy** — one error bound for all classes (characters, additive characters) of a given
modulus, the standard sieve-remainder accounting. For such certificates the positive mean of a
minorant must live on moduli `>x` (Thm 1.2 / O14 Thm 4.5), where no orbit-uniform statement about
the primes beats the trivial bound (Lemma 2.3) — so the strength of the prime input (GRH etc.)
plays no role *within this class, by construction*; Thm 1.2 says the trivial bounds cannot pay for
the minorant. Siegel-zero main terms are handled the same way (Thm 3.1). Certificates that use the
atomicity, integrality or support of the prime measure (e.g. that classes mod `q>x` with least
representative `>x` are empty), non-periodic structure, or non-linear arguments are **not**
covered; see §6.

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
is x_s-measurable, `|h_s|≤1`): `|E_ρh|≤(4r*)^{k+1}`. ∎


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
`E_νF=0`, hence `E_νB≤0`, and `E_HB=E_νB−E_ρB≤Σ_i|c_i||E_ρh_i|≤(4r*)^{k+1}Σ|c_i|` by Lemma 1.1.
With `4r*≤8T^{−0.09}/(1−T^{−0.09})≤T^{−0.08}`: `(4r*)^{k+1}≤exp(−0.08𝓛(μ*/2−1))=exp(−c𝓛^4/log𝓛)`. ∎

*Remarks.* (i) Level-D functions (O14 Setting 2.0) with `log D≤0.6𝓛k` are combinations of
reduced products with `|I|≤k`, on which `E_ρ=0`: Thm 1.2 contains O14 Thm 4.5 (norm-free there).
(ii) `F` itself is a minorant of F, so `‖F‖_×≥δ_H/η`, `δ_H:=E_HF`: the avoider indicator's own
Wiener norm exceeds its mean by `e^{c𝓛^4/log𝓛}`.
(iii) Integrability: B is a finite combination of bounded functions, so all expectations are
finite; `ν≪P` with `dν/dP≤2` (O14 m1(b)).

## 2. Linear transfers of any accuracy: GRH, characters, additive characters

**Definition 2.1 (linear prime information).** Let 𝒽 be a family of reduced products on H
whose moduli form a finite set 𝒬, and `𝔈≥0`. Put `N_x:=#{p≤x: p∈H, p∤q ∀q∈𝒬}` and let
`m_x` below count only these primes (the finitely many `p|q` are specific numbers; inspecting
them individually is a search, not a transfer). A nonnegative measure m on H of mass `N_x` is
*𝒽-consistent at accuracy 𝔈* if `|∫h dm − N_xE_Hh|≤𝔈` for every `h∈𝒽`. A *linear certificate
at accuracy 𝔈* proves "some prime `p≤x` in H has `F(p)=1`" from the facts (i) the prime counting
measure `m_x:=Σ_{p≤x,p∈H,p∤𝒬}δ_p` is nonnegative of mass `N_x`, (ii) it is 𝒽-consistent at accuracy
𝔈. It is *valid* iff every 𝒽-consistent m has `∫F dm>0`. (Every minorant transfer is one:
from `B=Σc_ih_i≤F`, `h_i∈𝒽`, it concludes `Σ_pF(p)≥Σ_pB(p)≥N_xE_HB−𝔈Σ|c_i|>0`.)

**Theorem 2.2 (no linear certificate at accuracy `𝔈≥N_xη`; PROVED, same inputs as Thm 1.2).** In
the setting of Thm 1.2, if `𝔈≥N_x·(4r*)^{k+1}` (in particular if `𝔈≥N_xη`), then
`m_ν:=N_xν` is 𝒽-consistent at accuracy 𝔈 for *every* family 𝒽 of reduced products, and
`∫F dm_ν=0`. Hence every valid linear certificate has `𝔈<N_xη≤x·e^{−c𝓛^4/log𝓛}`; and every
minorant transfer `N_xE_HB>𝔈‖B‖_×` needs `N_x/𝔈>e^{c𝓛^4/log𝓛}` (Thm 1.2).

*Proof.* `m_ν≥0`, mass `N_x`; `|∫h dm_ν−N_xE_Hh|=N_x|E_ρh|≤N_x(4r*)^{k+1}` (Lemma 1.1);
`ν(F=1)=0` (O14 Lemma 4.1). ∎

So the only question is how small an accuracy 𝔈 can be *true* for the primes. For families
that are closed under translation, it cannot be small:

**Lemma 2.3 (forced accuracy; PROVED, elementary).** Let `q>x` with `gcd(q,Q)=1`, and
`N':=#{p counted by m_x: p∤q}` (`=N_x` if `q∈𝒬`); assume `N'≥1` and `N_x≤φ(q)/2`.
(a) If 𝒽 contains `1_{a mod q}` for every unit a, every bound 𝔈 valid for `m_x` on 𝒽 has
`𝔈≥1/2`.
(b) If 𝒽 contains all nontrivial Dirichlet characters mod q, then
`𝔈²≥N'(φ(q)−N')/(φ(q)−1)`; if it contains all `e(an/q)`, `a≢0 (q)`, then
`𝔈²≥N_x(1−N_x/φ(q))`. Both are `≥N_x/3` when `N'≥2N_x/3` (e.g. `q∈𝒬`).

*Proof.* The primes counted by N' are distinct units mod q. (a) A unit class containing one of
them has `∫1_a dm_x≥1`, while `N_xE_H1_a=N_x/φ(q)≤1/2` (H is a class mod Q, coprime to q).
(b) Characters: `E_Hχ=0` for `χ≠χ_0`, and `Σ_{χ}|Σ_{p∤q}χ(p)|²=φ(q)N'`; the principal character
contributes `N'²`, so the `φ(q)−1` others have mean square `N'(φ(q)−N')/(φ(q)−1)`.
Additive: `E_He(a·/q)=c_q(a)/φ(q)` (Ramanujan sum). With `S(a):=Σ_{p≤x,p∈H}e(ap/q)` and
`Σ_a|S(a)|²=qN_x` (`p≤x<q` distinct mod q), `Σ_aS(a)\overline{c_q(a)}=qN'`,
`Σ_a|c_q(a)|²=qφ(q)`, `Σ_a|S(a)−N_xc_q(a)/φ(q)|²=q(N_x−2N_xN'/φ(q)+N_x²/φ(q))≥qN_x(1−N_x/φ(q))`; the term `a=0`
vanishes (`c_q(0)=φ(q)`), so some `a≠0` has `|S(a)−N_xc_q(a)/φ(q)|²≥N_x(1−N_x/φ(q))`. ∎

**Corollary 2.4 (full-orbit uniform linear transfers are capped at 1/4; PROVED implication).**
Certificates through a translation-closed family 𝒽 of reduced products — residue classes
(e.g. O9/Gallagher-type and sieve transfers), Dirichlet characters (e.g. GRH:
`|ψ(x,χ)|≪x^{1/2}log²(qx)`), additive characters (e.g. Vinogradov minor-arc bounds, the
Fourier side of Maynard's restricted-digit method) — with *any* accuracy that is true for the
primes, need

```
classes:     log x ≥ c𝓛^4/log𝓛 ;       characters / additive characters: log x ≥ 2c𝓛^4/log𝓛 ,
```

provided 𝒽 contains, with each `h_i` of modulus `>x`, its translation orbit (all classes,
resp. characters, resp. additive characters of that modulus). Only `h_i` with `≥k+1` big
primes — modulus `>T^{0.6(k+1)}=e^{c'𝓛^4/log𝓛}`, so `>x` in the range of interest — carry
the positive mean (Thm 1.2). If instead every `h_i` has modulus
`≤x`, then B is a minorant of level `≤x`, and O14 Thm 4.5 gives `E B≤0` as long as
`log x≤c𝓛^4/log𝓛`. Either way: **certified `W(p)≥exp((log p)^{1/4+δ})` is impossible by any
linear transfer with full-orbit uniform accuracy, whatever true statement about the primes
is used (GRH included).** (Scope: see the Reading below and §6 (N2).)

*Proof.* Let `log x<c'𝓛^4/log𝓛` (else nothing to prove). Split `B=B_sh+B_deep` (h_i with
`≤k` resp. `≥k+1` big primes). By Lemma 1.1, `E_HB=E_νB−E_ρB_deep≤η·Σ_{deep}|c_i|`; the
certificate needs `N_xE_HB>Σ_{deep}|c_i|𝔈_i` with `𝔈_i≥1/2` (classes) or `≥√(N_x/3)`
(characters) by Lemma 2.3 (applied to the part q′ of q coprime to Q: on H a class mod q is a class mod
q′ or empty, and a character/additive character mod q restricts to one mod q′ times a constant;
deep moduli have q′ in 𝒬 up to this reduction, `>x²` and coprime to Q, so
`N'=N_x`; assume `N_x≥1`, else nothing is certified). So `N_xη>1/2` resp. `√N_x η>1/√3`. If there is no
deep term, `E_HB=E_νB≤0` (O14 Thm 4.5's argument). ∎

**Proposition 2.5 (averaged accuracy does not help; PROVED, same inputs).** Group the deep
reduced products into translation orbits O (all classes mod q, `q>x`, q∈𝒬 coprime to Q after
the reduction in Cor 2.4, `N_x≤φ(q)/2`), and suppose the
certificate bounds `|Σ_{C∈O}c_Ce_C|≤‖c_O‖_{s}‖e_O‖_{s'}` (Hölder, any `1≤s≤∞`, `1/s+1/s'=1`) with
`e_C:=∫1_Cdm_x−N_xP_H(C)` the true errors. Then it needs `N_x·η>1/2` again. Indeed:
(i) `‖ν−P‖_TV≤e^{−0.6μ*}`: conditionally on x_s the perturbation has mass
`P_0Σ_Jw_J‖σ_J‖=P_02^{k+1}`, and `P_0≤e^{−(1−p*)R}≤e^{−(1−p*)μ*}`, `k+1≤μ*/2`;
(ii) so `‖ρ_O‖_{s'}≤‖ρ_O‖_1^{1/s'}‖ρ_O‖_∞^{1/s}≤e^{−0.6μ*/s'}η^{1/s}`, with `ρ_O:=(E_ρ1_C)_{C∈O}`;
(iii) the truth has `‖e_O‖_{s'}≥(1/2)N'^{1/s'}` (N' entries `≥1/2`, Lemma 2.3(a)), `N'≥N_x/2`.
Positivity needs, for some O, `N_x‖ρ_O‖_{s'}>‖e_O‖_{s'}`, i.e.
`N_xe^{−0.6μ*/s'}η^{1/s}>(1/2)(N_x/2)^{1/s'}`; raising to the power s (`s/s'=s−1`):
`N_xη>(1/2)(e^{0.6μ*}/4)^{s−1}≥1/2` (for `s<∞`). For `s=∞` (`s'=1`) the condition reads
`N_xe^{−0.6μ*}>N_x/4`, impossible. ∎

*Reading.* GRH improves accuracy from "BV/Gallagher level x^c" to "square-root error at every
modulus"; Lemma 2.3 says square root is also the floor. Neither touches the barrier, which is a
property of F (the cost `‖B‖_×/E B≥e^{c𝓛^4/log𝓛}` of every minorant), not of the primes.
"Full-orbit uniform" = one error bound for all members of each translation orbit used. This
is a genuine restriction (self-review R57-self): for `q>x`, classes whose least positive representative
exceeds x are empty below x, which is *support* information, not knowledge of the primes, and
it permits sharper non-uniform error bounds. Certificates exploiting it are equivalent to
minorants valid only on `H∩[1,x]` (or on primes ≤ x); they are **not** covered (§5, §6 (N2)).

## 3. Siegel zeros

Two ways an exceptional zero `β_1` (real character `χ_1` mod `q_1`) can enter: (A) as a second
main term in the linear prime law, (B) through Heath-Brown's mechanism (twin primes under a
Siegel zero), which converts prime sums into divisor-weighted integer sums. (B) is treated with
Type I/II input in §4. Here (A).

Under (G) with an exceptional zero, for h of modulus in Gallagher's range,
`Σ_{p≤x,p∈H}h(p)≈N_x·E_H[(1−εχ_1)h]/(1−εE_Hχ_1)` with `ε≈x^{β_1−1}/β_1∈[0,1]` (O9 §1, O14 Lemma 4.3).
So the *Siegel-model law* is the positive measure `P_1:=(1−εχ_1)P` (density `≥0` since
`|χ_1|≤1`, `0≤ε≤1`). O14 Cor 4.6 left open whether a minorant with `E_HB≤0` can have
`E_{P_1}B>0` ("positivity from the exceptional term").

**Theorem 3.1 (the Siegel-model law has the same fake; PROVED, same inputs as Thm 1.2).** Let
`χ_1` be any real character, `ε∈[0,1]`, `ν_1:=(1−εχ_1)ν`. Then `ν_1≥0`, `F=0` ν_1-a.e., and for
every residue class, Dirichlet character or additive character h,

```
|E_{ν_1}h − E_{P_1}h| ≤ 2(4r*)^{k+1} .
```

Hence Thm 1.2, Thm 2.2 and Cor 2.4 hold for `P_1` (η doubled) **for representations by these
atoms** (classes, characters, additive characters; write `‖B‖_atom` for the corresponding
ℓ¹-infimum): every minorant `B≤F` has `E_{P_1}B≤2η‖B‖_atom`. (Arbitrary reduced products are not
closed under multiplication by χ_1: locally `h=(3χ+1)/4` is reduced, `χh=(3+χ)/4` is not — R57-self.)
Masses: `P_1(H)=1−εE_Hχ_1` and `ν_1(H)−P_1(H)=−εE_ρχ_1`, of size `≤(4r*)^{k+1}`; so the
information sets of §2 must allow the total mass to vary within the accuracy 𝔈, which they do
once `𝔈≥N_x(4r*)^{k+1}`. Moreover, if `B∈𝒱_{k−s}` (level `log D≤0.6𝓛(k−s)`), where s is the
number of big primes dividing `q_1`, then `E_{P_1}B≤0` exactly. Since Gallagher-range moduli
have `log q_1≪log x`, `s≤log x/(0.6𝓛)`, so **no minorant of level `log D≤c𝓛^4/log𝓛−log x`
gets positivity from the exceptional term**; with `log x≪𝓛^4/log𝓛` this closes the "Siegel"
item of O14 Cor 4.6's Not-claimed list (for linear transfers).

*Proof.* `ν_1≥0` and `ν_1≪ν`, so `F=0` ν_1-a.e. `E_{ν_1}h−E_{P_1}h=E_ρh−εE_ρ[χ_1h]`. Both h and
`χ_1h` are reduced products up to a unimodular constant: at a big b in the support, the
local factor of `χ_1h` is `χ_{1,b}h_b` with `|·|≤1` and mean `≤1/(b−1)` (class indicator times a
unimodular function), `0` (nontrivial character), or a normalised Gauss sum
`≤√b^{v}/φ(b^v)≤1/4` (additive times multiplicative, both nontrivial at b); a factor that
becomes trivial is constant and is dropped from I. Lemma 1.1 bounds each term by `(4r*)^{k+1}`
(its proof gives 4r*). For the exact statement: B and `χ_1B` lie in `𝒱_k` (χ_1 adds at most s
big coordinates), on which `E_ρ=0` (O14 Thm 1.3), so `E_{P_1}B=E_{ν_1}B≤E_{ν_1}F=0`. ∎

*Reading.* An exceptional zero reweights the primes by `1−εχ_1`, a bounded positive density of
small conductor. The planted fake is pseudorandom against every reduced product, so it can be
reweighted the same way. In Heath-Brown's twin-prime argument the Siegel zero is decisive
because the twin-prime problem is a *parity* problem (dimension 2, a fixed level suffices for
the integers); here the obstruction is the sieve *dimension* `κ≍𝓛³`, which already blocks the
integer problem (§4).

## 4. Type I/II, Heath-Brown/Siegel and restricted-digit primes: the integer half

Vaughan's and Heath-Brown's identities, and Heath-Brown's Siegel-zero substitution, all rewrite
`Σ_{p≤x}F(p)1_H(p)` as combinations of *integer* sums `Σ_{n≤x}w(n)F(n)1_H(n)` with
`w=α∗β` a Dirichlet convolution: Type I (`β≡1`, `α` supported on `d≤D_I`), Type II (both
supported on `[x^a,x^{1−a}]`), and, under a Siegel zero, Type I sums with `α` built from
`μ` and `1∗χ_1` up to level `x^{1−ε}`. Every such route needs at least the Type I sums, in
particular the counts `Σ_{n≤x, d|n}F(n)1_H(n)` (d=1 included), to relative precision `o(1)`
compared with their mean `≍xδ/d`. These are statements about F on the integers, with no prime in
sight. The planted fake extends to them.

**Setting 4.0.** Let `d≤x` with `gcd(d,Q)=1`, and `log x≤𝓛^4`. Let `P_d` be Haar measure on
`H̃_d:={n∈Ẑ: n≡r (Q), d|n}` (coordinates `X_p∈ℤ_p`, no unit condition; `X_p≡0 (p^{v_p(d)})` for
`p|d`). Big coordinates: `X_ℓ`, ℓ prime `>T^{0.6}`, `ℓ∤dQ`. F is defined on Ẑ (an event needs
`n≡−4D (M)`, a unit class, since `gcd(D,M)=1`).

**Proposition 4.1 (integer barrier; PROVED, same inputs as Thm 1.2).** There are absolute
`c,c'>0` such that for T large, every Q with `log Q≤T^{0.05}`, every unit r mod Q and every d as
in 4.0: every `B≤F` on `H̃_d` with a representation `B=Σc_ih_i` by reduced products (classes,
characters, additive characters; now `|E h_b|≤1/4` under Haar on `ℤ_b`) satisfies

```
E_{P_d}B ≤ e^{−c'𝓛^6} + η·Σ|c_i| .
```

Consequently the integer measure `m^{(d)}:=Σ_{n≤x, n∈H̃_d}δ_n` (mass `X_d=x/(dQ)+O(1)`,
accuracy `≤1` on every residue class) admits no class-ℓ¹ certificate of `Σ_{n}F dm^{(d)}≥1`
**that charges the uniform error 1 to every deep class** unless `X_dη≥1/2`, i.e.
`log x≥c𝓛^4/log𝓛` (forced as in Lemma 2.3(a) if the orbit is used uniformly; for integers the
support is known exactly, so support-aware accounting — empty classes cost 0 — is natural and is
**not** covered: it amounts to minorants valid only on `H̃_d∩[1,x]`, §6 (N2)); and the Haar-weighted fake `X_dν^{(d)}` below
satisfies every class/character statistic to accuracy `X_d(η+e^{−c'𝓛^6})` while giving F
mass `≤X_de^{−c'𝓛^6}<1`.

*Proof.* Rerun O14 Thm 4.5 on `H̃_d`, with one change: a small configuration x only sees the
small parts v coprime to x (events at v need x to be a unit mod v). Lemmas 4.2–4.4 of O14 are
unchanged (Lemma 4.3 does not involve x; Lemma 4.4 needs `−x/4` to be a unit mod v; `p_ℓ` gains a
factor `(ℓ−1)/ℓ`; the big ℓ dividing d are dropped, costing `≤ω(d)p*≤𝓛^4T^{−0.09}`). So
`R(x)≥0.13(L²/200)·Σ'1/v−o(1)`, Σ' over y-rough squarefree `v≤V` coprime to x.
By Mertens, `Σ_{v≤V, y-rough sqfree}1/v≤C_6log V/log y`, so
`Σ'1/v ≥ (c_3−C_6σ(x))log V/log y` with `σ(x):=Σ_{y<p≤V, p|x}1/p`. Let
`G':={σ(x)>λ}`, `λ:=c_3/(2C_6)`. Off G', `R(x)≥μ*/2`; plant (with `k+1:=⌊μ*/4⌋`) only off G' and
keep the true law on G'. Then `F=0` ν-a.s. off G', `ρ=0` on G', and Lemma 1.1 holds verbatim, so
`E_{P_d}B=E_νB−E_ρB≤P_d(G')+(4r*)^{k+1}Σ|c_i|`.
*Size of G'.* Primes `p|d`, `p>y` contribute `≤ω_{>y}(d)/y≤(log x)/(y log y)<λ/2` (`y=𝓛^6`). The
other `p∈(y,V]` divide x independently with probability `1/p`; for `t:=y`,
`P(Σξ_p/p≥λ/2)≤e^{−tλ/2}∏_p(1+(e^{t/p}−1)/p)≤e^{−λy/2}exp(Σ_{p>y}e t/p²)≤e^{3−λy/2}`.
So `P_d(G')≤e^{−c'𝓛^6}`.
*Certificates.* `|#{n≤x: n∈H̃_d∩C}−X_dP_d(C)|≤1` for every class C (exact integer counting).
A class-ℓ¹ certificate gives `Σ F dm^{(d)}≥X_dE_{P_d}B−Σ|c_i|≤X_de^{−c'𝓛^6}+Σ|c_i|(X_dη−1)`,
which is `<1` unless `X_dη>1` (as `X_de^{−c'𝓛^6}<1/2`). ∎

*Remark 4.2 (a sanity check that this is a method barrier).* For integers the conclusion is
false: perfect squares coprime to all `M≤T` are avoiders (O13 Lemma 3.1: event classes are Jacobi
non-residues mod M), so if r is a square mod Q (as for the Mordell-hard classes mod 840),
`Σ_{n≤x}F(n)1_H(n)≥#{m≤√x: m²≡r (Q), (m,P(T))=1}`, which is `≫_Q√x/𝓛` once `√x≥T²Q`. Squares are not periodic, so they are
invisible to class-ℓ¹ certificates. (In the Mordell-hard fibre, squares are also what makes the
fibre nonempty.) For primes no such non-periodic avoider family is known; the closest periodic
one, `∏_{ℓ≤T}1[(n/ℓ)=1]≤F`, has `‖·‖_×/mean=2^{π(T)}`, consistent with Thm 1.2.

**Assessment 4.3 (what Type I/II input would have to supply; heuristic, NOT a consequence of
Prop 4.1).** A Vaughan/Heath-Brown proof organised in the standard way of `Σ_{p≤x,p∈H}F(p)>0` at `log x≍𝓛^3` needs, as Type I input,
`Σ_{n≤x,d|n}F(n)1_H(n)=X_dE_{P_d}F·(1+o(1))` for (a weighted majority of) `d≤x^{1/3}`, and
`E_{P_d}F≈δ` is `e^{−𝓛^{3+o(1)}}`, so the absolute error must be `≤(x/d)·x^{−1/C}` (C large).
Prop 4.1 shows that full-orbit uniform class-ℓ¹ minorant certificates cannot produce even the
lower half of this at `log x<c𝓛^4/log𝓛`. It does not exclude signed cancellation across d,
aggregate estimates, support-aware or non-linear methods; that Type II input cannot compensate is
our assessment, not a theorem. Under a Siegel zero the Type I
level rises to `x^{1−ε}` — a constant factor in `log D`, against a required `log D≍𝓛·log x/polylog`
(superpolynomial level `D=x^{𝓛^{1−o(1)}}`). **Our reading: the bottleneck is the sieve dimension
`κ≍𝓛³/log𝓛` of the big-prime sieve, a property of the integers; prime-specific input (Type II,
parity, Siegel) addresses the other half of the problem.**

**Restricted-digit primes (Maynard, Invent. Math. 2019) — why the analogy fails.** Both sets
are sifted sets of density `x^{−1/C}` (for ES at `log x=C𝓛³`: `δ_H=e^{−𝓛^{3+o(1)}}`; for
missing digits in base b, density `X^{−(1−log(b−1)/log b)}`). Maynard's set A is periodic
modulo `X=b^k`, so `‖1_A‖_×/E1_A≤X` trivially, and its key input is that its additive-Fourier
ℓ¹-mass is `X^{c_b}` with `c_b<1/2` (product structure over digits; exact exponent from memory,
not needed): complexity *below* the square-root floor of Lemma 2.3, so additive transfers (minor
arcs) and the Type I/II analysis close. For ES, Thm 1.2 (applied to B=F) gives
`‖F‖_×/E_HF≥e^{c𝓛^4/log𝓛}=x^{c𝓛/(C log𝓛)}`: the complexity is **superpolynomial in x**, so it
exceeds every floor `x^{A}`. The digit filtration (conditions mod `b^j` refine those mod
`b^{j−1}`, period = range) has no analogue for the CRT sieve, whose period `e^{(1+o(1))T}` is
doubly exponential in `𝓛`, while x is `e^{𝓛^{3+o(1)}}`.

## 5. Minorants valid only on primes (brief item (a))

**Lemma 5.1 (Dirichlet closure; PROVED, as EXCEPTIONAL_PRIMELAW Lemma 1.2).** Let B be a finite
combination of periodic functions and L a common period of B and F (F has period
`lcm(M≤T)`). Then `B(p)≤F(p)` for all but finitely many primes `p∈H` iff `B≤F` on every unit
class mod `lcm(L,Q)` inside H, i.e. Haar-a.e. on H. *Proof.* Each such class contains infinitely
many primes (Dirichlet); B and F are constant on it. ∎

So "valid only at primes" adds nothing unless restricted to a finite range `p≤x`. Then
`U:={B>F}` is a union of unit classes mod L containing no prime `≤x`. By Linnik–Xylouris every
unit class of modulus `≤cx^{1/5}` contains a prime `≤x`, so U contains no class of modulus
`≤cx^{1/5}`: the extra knowledge is that a set of *deep* classes is prime-free up to x. In the
language of §2 this is the constraint `m(U)=0` added to the information set — support-aware,
not full-orbit uniform, hence outside Cor 2.4. It is not necessarily circular (R57-self): part of it
is pure support information (classes with no integer in `[1,x]`), which needs no knowledge of the
primes. What *is* proved: positivity cannot come from moderate single moduli (Prop 5.2).

**Proposition 5.2 (finite-range minorants of a single moderate modulus; PROVED modulo
Linnik–Xylouris).** Let B be a function of `n mod q` with `B(p)≤F(p)` for every prime `p≤x` in H.
Suppose there is a prime `ℓ_0≡3 (4)`, `ℓ_0≤T`, `ℓ_0∤qQ`, with `x≥C_L(qQℓ_0)^5` (`C_L` the
Linnik–Xylouris constant; `(qQℓ_0)^{2+ε}` under GRH). Then `B≤0` on every class of H mod q,
hence `E_HB≤0`.
*Proof.* Fix a class c of H mod `q′:=lcm(q,Q)`. The class `{n∈c, n≡−4 (ℓ_0)}` mod `q′ℓ_0` is a
unit class, so it contains a prime `p≤x`. The event `(M,D)=(ℓ_0,1)` (`M≡3 (4)`, `1|A²`) holds at
p, so `F(p)=0` and `B(c)=B(p)≤0`. ∎
So a finite-range prime-only minorant must take its positive values through moduli
`>x^{1/5}/(QT)`, or through combinations of moduli with large lcm (sieve-type sums), which
Prop 5.2 does not treat. Same situation as
EXCEPTIONAL_PRIMELAW §6 item 2 ("the gap lives at `L>N^c`").

## 6. What is and is not covered

**Covered (barrier at `log x≍𝓛^4/log𝓛`, i.e. exponent 1/4 up to `(log log)^{1/2}`).**
1. Minorants of any level, used through linear transfers whose accuracy is uniform over
   translation orbits of residue classes, Dirichlet characters or additive characters (Thm 1.2,
   Thm 2.2, Lemma 2.3, Cor 2.4), with any assumption on the primes that is *true* (GRH, or
   anything stronger: Lemma 2.3 shows the accuracies GRH provides are optimal up to logs on deep
   moduli). Hölder-averaged accounting over orbits (Prop 2.5).
2. Siegel-zero main terms (Thm 3.1): the exceptional reweighting `1−εχ_1` is transported to
   the fake. Closes O14 Cor 4.6's Siegel item for linear transfers.
3. The integer Type I sums that Vaughan / Heath-Brown identities and Heath-Brown's Siegel-zero
   method reduce to (Prop 4.1), for class-ℓ¹ certificates; Type II input is then moot (Cor 4.3,
   Assessment for the "moot" part).
4. Prime-only minorants valid at all primes (Lemma 5.1); finite-range ones of a single moderate
   modulus (Prop 5.2).

**Not covered (the precise residual).**
* (N1) *Non-periodic structure.* Certificates that exploit a non-periodic family inside the
  avoider set (the integer analogue is the squares, Remark 4.2). For primes one would need a
  "prime-rich" non-periodic family on which F is automatic; every periodic one costs
  `‖·‖_×/mean≥e^{c𝓛^4/log𝓛}` (Thm 1.2). None is known; Chebotarev-type families
  (`p` split in `ℚ(√ℓ*:ℓ≤T)`) are periodic and cost `2^{π(T)}`.
* (N2) *Support-aware / finite-range certificates*: minorants valid only on `H∩[1,x]` or on
  primes `≤x`, i.e. error accounting that is not uniform over translation orbits (e.g. using
  that classes mod `q>x` with least representative `>x` are empty). Prop 5.2 excludes single
  moduli `≤x^{1/5}/(QT)`; sieve-type combinations are open. For the integer Type I sums this is
  the natural accounting, so (N2) is the main gap in §4 (R57-self, R57).
* (N3) *Non-linear certificates*: arguments in which F (or the prime measure) enters
  non-linearly — e.g. second-moment / pair-correlation counts `Σ_{p,p'}F(p)F(p')`, entropy or
  density-increment arguments. The fake is a single measure; a joint fake for pair statistics
  is not constructed here.
* (N4) *Asymptotic evaluation of integer Type I sums by non-class-ℓ¹ means* (would be a new
  theorem about CRT sieves beyond the sieving limit, integers only; no such tool is known — the
  digit-filtration that powers restricted-digit results has no CRT analogue, §4).

**Answer to the brief.** (1a) adds nothing at all primes (Lemma 5.1); restricted to `p≤x` it
becomes support-aware accounting (N2), excluded only for single moduli `≤x^{1/5}/(QT)` (Prop 5.2). (1b) Type II cannot help on its own: the
Type I half already needs integer equidistribution of F at superpolynomial level
`x^{𝓛^{1−o(1)}}`, and every full-orbit uniform linear method is blocked there (Prop 4.1;
support-aware methods are open, (N2)); the Maynard analogue fails quantitatively (complexity `x^{O(1)}` vs `x^{𝓛/polylog}`). (1c) Siegel zeros do
not help linear transfers (Thm 3.1), and Heath-Brown's mechanism reduces to (1b). (2) No
CONDITIONAL improvement was found; the obstruction is theorem-level (Thm 1.2/2.2, Prop 2.5,
Thm 3.1, Prop 4.1) with the exact scope above. The 1/4 ceiling is a **sieve-dimension**
barrier (sieving limit `β_κ≍κ`, `κ≍𝓛³/log𝓛`, `log z≍𝓛`), not a parity barrier, and it is a
property of F, invariant under any strengthening of prime equidistribution.

## 7. Status

| item | statement | label |
|---|---|---|
| Lemma 1.1 | planted perturbation: `|E_ρh|≤(4r*)^{k+1}` for every reduced product; 0 if `|I|≤k` | PROVED (exact checks: identity 40 brute-force instances, bound 900 cases, worst ratio 2.4·10⁻⁴) |
| Thm 1.2 | every minorant `B≤F` on any fibre (`log Q≤T^{0.05}`): `E_HB≤e^{−c𝓛^4/log𝓛}‖B‖_×` | PROVED mod (G), effective Page, fundamental lemma (O14 Thm 4.5 inputs) |
| Thm 2.2 | linear certificates need accuracy `𝔈<N_xη` | PROVED (same) |
| Lemma 2.3 | forced accuracy on deep orbits: ≥1/2 (classes), `≥√(N_x/3)` (characters, additive) | PROVED (elementary) |
| Cor 2.4 | full-orbit uniform linear transfers (incl. under GRH) need `log x≥c𝓛^4/log𝓛` | PROVED implication |
| Prop 2.5 | `‖ν−P‖_TV≤e^{−0.6μ*}`; Hölder-averaged accuracy also blocked | PROVED (same) |
| Thm 3.1 | Siegel-model law `(1−εχ_1)P`: same fake (atom norm); level `≤c𝓛^4/log𝓛−log x` gives `E_{P_1}B≤0` | PROVED (same) |
| Prop 4.1 | integer (Type I) sums: class-ℓ¹ certificates blocked below `log x≍𝓛^4/log𝓛` | PROVED (same + Mertens) |
| Assessment 4.3 | Type II / Siegel (Heath-Brown) / Maynard-type routes need Type I beyond the barrier | Assessment (heuristic) |
| Prop 5.2 | finite-range prime-only minorants of one modulus `q≤x^{1/5}/(QT)`: `E_HB≤0` | PROVED mod Linnik–Xylouris |
| Lemma 5.1 | prime-only minorants = Haar minorants (Dirichlet) | PROVED |

Not claimed: anything about ES; anything about the true size of the least avoider prime;
anything in (N1)–(N4).

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; timeout 900 uv run python scripts/omega15_pseudorandom.py 1)  # Lemma 1.1 -> data/omega15/pseudorandom.txt (~1 min)
```
