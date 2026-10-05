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

**Lemma 2.3 (forced accuracy; PROVED, elementary).** Let `q>x` with `gcd(q,Q)=1`, and
`N':=#{p≤x: p∈H, p∤q}≥N_x−ω(q)`; assume `N'≥1` and `N_x≤φ(q)/2`.
(a) If 𝒽 contains `1_{a mod q}` for every unit a, every bound 𝔈 valid for `m_x` on 𝒽 has
`𝔈≥1/2`.
(b) If 𝒽 contains all nontrivial Dirichlet characters mod q, then
`𝔈²≥N'(φ(q)−N')/(φ(q)−1)`; if it contains all `e(an/q)`, `a≢0 (q)`, then
`𝔈²≥N_x(1−N_x/φ(q))`. Both are `≥N_x/3` when `N_x≥3ω(q)`.

*Proof.* The primes counted by N' are distinct units mod q. (a) A unit class containing one of
them has `∫1_a dm_x≥1`, while `N_xE_H1_a=N_x/φ(q)≤1/2` (H is a class mod Q, coprime to q).
(b) Characters: `E_Hχ=0` for `χ≠χ_0`, and `Σ_{χ}|Σ_{p∤q}χ(p)|²=φ(q)N'`; the principal character
contributes `N'²`, so the `φ(q)−1` others have mean square `N'(φ(q)−N')/(φ(q)−1)`.
Additive: `E_He(a·/q)=c_q(a)/φ(q)` (Ramanujan sum). With `S(a):=Σ_{p≤x,p∈H}e(ap/q)` and
`Σ_a|S(a)|²=qN_x` (`p≤x<q` distinct mod q), `Σ_aS(a)\overline{c_q(a)}=qN'`,
`Σ_a|c_q(a)|²=qφ(q)`, `Σ_a|S(a)−N_xc_q(a)/φ(q)|²=q(N_x−2N_xN'/φ(q)+N_x²/φ(q))≥qN_x(1−N_x/φ(q))`; the term `a=0`
vanishes (`c_q(0)=φ(q)`), so some `a≠0` has `|S(a)−N_xc_q(a)/φ(q)|²≥N_x(1−N_x/φ(q))`. ∎

**Corollary 2.4 (oblivious linear transfers are capped at 1/4; PROVED implication).**
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
oblivious linear transfer, whatever is assumed about the primes (GRH included).**

*Proof.* Let `log x<c'𝓛^4/log𝓛` (else nothing to prove). Split `B=B_sh+B_deep` (h_i with
`≤k` resp. `≥k+1` big primes). By Lemma 1.1, `E_HB=E_νB−E_ρB_deep≤η·Σ_{deep}|c_i|`; the
certificate needs `N_xE_HB>Σ_{deep}|c_i|𝔈_i` with `𝔈_i≥1/2` (classes) or `≥√(N_x/3)`
(characters) by Lemma 2.3 (applicable: deep moduli are `>x²`, coprime to Q, and
`ω(q)≤𝓛^4`, `N_x≥3ω(q)` for the x in question). So `N_xη>1/2` resp. `√N_x η>1/√3`. If there is no
deep term, `E_HB=E_νB≤0` (O14 Thm 4.5's argument). ∎

*Reading.* GRH improves accuracy from "BV/Gallagher level x^c" to "square-root error at every
modulus"; Lemma 2.3 says square root is also the floor. Neither touches the barrier, which is a
property of F (the cost `‖B‖_×/E B≥e^{c𝓛^4/log𝓛}` of every minorant), not of the primes.
"Oblivious" = the error bound does not depend on *which* classes contain primes; a certificate
that knows which deep classes are prime-free is using the actual primes ≤ x (cf. §4).

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

Hence Thm 1.2, Thm 2.2 and Cor 2.4 hold verbatim for `P_1` (with η doubled): every minorant
`B≤F` has `E_{P_1}B≤2η‖B‖_×`. Moreover, if `B∈𝒱_{k−s}` (level `log D≤0.6𝓛(k−s)`), where s is the
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
unless `X_dη≥1/2`, i.e. `log x≥c𝓛^4/log𝓛`; and the Haar-weighted fake `X_dν^{(d)}` below
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
`E_{P_d}B=E_νB−E_ρB≤P_d(G')+(8r*)^{k+1}Σ|c_i|`.
*Size of G'.* Primes `p|d`, `p>y` contribute `≤ω_{>y}(d)/y≤(log x)/(y log y)<λ/2` (`y=𝓛^6`). The
other `p∈(y,V]` divide x independently with probability `1/p`; for `t:=y`,
`P(Σξ_p/p≥λ/2)≤e^{−tλ/2}∏_p(1+(e^{t/p}−1)/p)≤e^{−λy/2}exp(Σ_{p>y}e t/p²)≤e^{3−λy/2}`.
So `P_d(G')≤e^{−c'𝓛^6}`.
*Certificates.* `|#{n≤x: n∈H̃_d∩C}−X_dP_d(C)|≤1` for every class C (exact integer counting).
A class-ℓ¹ certificate gives `Σ F dm^{(d)}≥X_dE_{P_d}B−Σ|c_i|≤X_de^{−c'𝓛^6}+Σ|c_i|(X_dη−1)`,
which is `<1` unless `X_dη>1` (as `X_de^{−c'𝓛^6}<1/2`). ∎

*Remark 4.2 (a sanity check that this is a method barrier).* For integers the conclusion is
false: perfect squares `m²∈H̃_1` are avoiders (O13 Lemma 3.1: event classes are Jacobi
non-residues mod M), so `Σ_{n≤x}F(n)1_H(n)≥c√x/Q`. Squares are not periodic, so they are
invisible to class-ℓ¹ certificates. (In the Mordell-hard fibre, squares are also what makes the
fibre nonempty.) For primes no such non-periodic avoider family is known; the closest periodic
one, `∏_{ℓ≤T}1[(n/ℓ)=1]≤F`, has `‖·‖_×/mean=2^{π(T)}`, consistent with Thm 1.2.

**Corollary 4.3 (what Type I/II input would have to supply; Assessment built on Prop 4.1).**
A Vaughan/Heath-Brown proof of `Σ_{p≤x,p∈H}F(p)>0` at `log x≍𝓛^3` needs, as Type I input,
`Σ_{n≤x,d|n}F(n)1_H(n)=X_dE_{P_d}F·(1+o(1))` for (a weighted majority of) `d≤x^{1/3}`, and
`E_{P_d}F≈δ` is `e^{−𝓛^{3+o(1)}}`, so the relative error must be `≤x^{−1/C}` (C large).
By Prop 4.1 no oblivious class/character/additive-character method can produce even the lower
half of this at `log x<c𝓛^4/log𝓛`; the Type II sums are then moot. Under a Siegel zero the Type I
level rises to `x^{1−ε}` — a constant factor in `log D`, against a required `log D≍𝓛·log x/polylog`
(superpolynomial level `D=x^{𝓛^{1−o(1)}}`). **The bottleneck is the sieve dimension
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
