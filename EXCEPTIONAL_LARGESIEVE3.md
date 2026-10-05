# EXCEPTIONAL_LARGESIEVE3 — H_LS∞ for forced families via sparsity (task O59)

Status: **in progress** (agent O59, branch `side-agent/hls-sparse`). Labels as
in `DISCOVERIES.md`. Notation: LS = `EXCEPTIONAL_LARGESIEVE.md`, LS2 =
`EXCEPTIONAL_LARGESIEVE2.md`, K2 = `EXCEPTIONAL_KARY2.md`, K3 =
`EXCEPTIONAL_KARY3.md`, EK = `EXCEPTIONAL_KARY.md`.

Setting (LS §1). 𝔊 is a finite mixture of ℛ(M)-, (a,D)-, Case-A and selector
classes (K2 Def 2.0), `𝒜 = 𝒜(𝔊)`, `M₀` the lcm of the moduli. A large-sieve
bound is an N-large-sieve system `(Θ,w)` (LS (LS)), any rational frequencies,
any weights; it is CRT-admissible if `Z ≤ 1/L` with `L ≤ F_w(π)` for every
probability π on `𝒜 mod M'` (LS §1), `F_w(π) = Σ_θ w_θ|π̂(θ)|²`. Facts:
`w_θ ≤ 1/N` (LS Fact 1.1), `Σ_θ w_θ ≤ 1` (LS Fact 4.0). By LS Rem 3.3 we
may and do take π uniform on all CRT digits not resolved by `M₀`, so only
θ with `den θ | M₀` matter; we write `M' = M₀`.

## 0. Summary (so far)

| item | statement | label |
|---|---|---|
| Thm 1.1 | **smooth–rough splitting.** For any `z`, the z-smooth CRT coordinates cost only the *density* of a measure on the z-smooth avoider set (no Fourier or level information at all); only the z-rough part needs Fourier control, in the `ℓ^{2+2β}` sense of LS Thm 4.1 | PROVED |
| Lemma 2.1 | the z-smooth part costs `log ρ ≤ 16𝔐(z) + 2W₁ + log 2`, `𝔐(z) ≪ (log z)³(log log z)³` (sequential law with square base, conditioned on a good set) | PROVED (K2 §§2–4; Case A via ElT Prop 1.4) |
| Thm 3.1 | **rough-slice mixtures**: if every modulus of 𝔊 has at most one prime factor `> z = exp((log N)^{1/4})`, every CRT-admissible large sieve (any rational frequencies, any denominators, any weights) saves `≤ C(log N)^{3/4}(log log N)³` | PROVED (same inputs) |

## 1. The smooth–rough splitting

Fix `z ≥ W₁` (W₁ an absolute constant, chosen in Lemma 2.1). Write
`M₀ = M_s M_r` with `M_s` z-smooth and `M_r` z-rough (all prime factors
`> z`). By CRT `n ↔ (c, r)`, `c = n mod M_s`, `r = n mod M_r`, and every
θ with `den θ | M₀` is uniquely `θ = θ_s + θ_r`, `den θ_s | M_s`,
`den θ_r | M_r`, with `e(nθ) = e(cθ_s)e(rθ_r)`.

For a class `C = (b mod G)` of 𝔊 write `G = G_s G_r` likewise.
* `𝒜_s ⊂ ℤ/M_s`: the residues c avoiding every class with `G_r = 1`.
* For `c ∈ 𝒜_s`, the *fibre family* `𝔊_c = {(b_C mod G_r(C)) : C ∈ 𝔊,
  G_r(C) > 1, c ≡ b_C (mod G_s(C))}` and its avoider set `𝒜_c ⊂ ℤ/M_r`.

Then `𝒜 mod M₀ = {(c,r) : c ∈ 𝒜_s, r ∈ 𝒜_c}`.

For a probability σ on a finite cyclic group `ℤ/m` and `p' ≥ 2` put
`𝓡_{p'}(σ) = Σ_{θ ∈ m^{−1}ℤ/ℤ} |σ̂(θ)|^{p'}` (θ = 0 included, `σ̂(0) = 1`).

**Theorem 1.1 (smooth–rough splitting; PROVED).** Let `0 < β ≤ 1/2`,
`p' = 2 + 2β`. Let `π_s` be a probability on `𝒜_s` with
`π_s(c) ≤ ρ/M_s` for all c, and for each `c ∈ supp π_s` let `π_c` be a
probability on `𝒜_c` (this presupposes `𝒜_c ≠ ∅` for every
`c ∈ supp π_s`; review R59 D6(c)). Then every CRT-admissible bound B from any
N-large-sieve system satisfies

    log(N/B) ≤ β log N + log ρ + log E_{c∼π_s} 𝓡_{p'}(π_c).            (1.1)

*Proof.* Let `π = Σ_c π_s(c) δ_c ⊗ π_c`; it is supported on 𝒜, and
`π̂(θ_s + θ_r) = Σ_c π_s(c) e(cθ_s) π̂_c(θ_r)`.
*Hausdorff–Young in c* (as in LS Thm 4.1). Fix `θ_r`. Put
`f(c) = M_s π_s(c) π̂_c(θ_r)` on `ℤ/M_s` (uniform probability on the group,
counting measure on the dual), so `π̂(θ_s+θ_r) = f̂(θ_s) := E_c f(c)e(cθ_s)`.
With `p = p'/(p'−1) ∈ (1,2)`, Hausdorff–Young gives
`Σ_{θ_s}|f̂(θ_s)|^{p'} ≤ (E_c|f|^p)^{p'/p}`. Now
`E_c|f|^p = E_{c∼π_s}[(M_sπ_s(c))^{p−1}|π̂_c(θ_r)|^p] ≤ ρ^{p−1}E_{π_s}|π̂_c(θ_r)|^p`,
and `(p−1)p'/p = 1`, so by Jensen (`p'/p ≥ 1`)
`Σ_{θ_s}|π̂(θ_s+θ_r)|^{p'} ≤ ρ (E_{π_s}|π̂_c(θ_r)|^p)^{p'/p} ≤ ρ E_{π_s}|π̂_c(θ_r)|^{p'}`.
Summing over `θ_r`: `𝓡_{p'}(π) ≤ ρ E_{π_s}𝓡_{p'}(π_c)`.
*Hölder* (LS Thm 4.1, with Facts 1.1 and 4.0):
`F_w(π) ≤ (Σ_θ w_θ)^{β/(1+β)}(Σ_θ w_θ|π̂(θ)|^{p'})^{1/(1+β)} ≤ (𝓡_{p'}(π)/N)^{1/(1+β)}`.
So `B ≥ 1/F_w(π) ≥ (N/𝓡_{p'}(π))^{1/(1+β)}` and
`log(N/B) ≤ (β log N + log 𝓡_{p'}(π))/(1+β) ≤ β log N + log⁺𝓡_{p'}(π)`
(`𝓡 ≥ 1` since θ = 0 contributes 1). ∎

*Remarks.* (a) Nothing is assumed about the smooth frequencies `θ_s`: their
denominators may have any number of prime factors `≤ z`, i.e. any level.
The smooth coordinates are paid for by `log ρ` only — a pure density
statement about `𝒜_s`. What this closes (review R59 D2):
(i) for rough-slice mixtures, all frequencies (Theorem 3.1);
(ii) for an arbitrary mixture, the frequencies with **z-smooth
denominators only** (`θ_r = 0`; then `π̂(θ_s) = π̂_s(θ_s)` and HY gives
`Σ_{θ_s}|π̂_s|^{p'} ≤ ρ`), *provided* `𝒜_c ≠ ∅` for all `c ∈ supp π_s` —
not automatic when 𝔊 has classes with several primes `> z`, since rough
classes can cover a whole fibre and Lemma 2.1's `π_s` does not see them.
Mixed frequencies `θ_s + θ_r` (`θ_r ≠ 0`, even of small rough level) in a
general mixture are **not** covered: they need a fibre measure with the
rough-level comparison of Rem 1.1(c) for every `c ∈ supp π_s`, a
K2-Lemma-1.1-type statement for the fibre families `𝔊_c` uniformly in c,
which is not proved (fibre families are not of the four K2 types, and K2's
moments are only averaged over c). That part is CONJECTURE, inside
(H_rough) of §4.
(b) In the fibres only the rough frequencies enter, through the
`ℓ^{p'}` mass `𝓡_{p'}(π_c)` (LS's (H_LS) restricted to z-rough
coordinates). For product measures `π_c` this is LS Thm 4.1's computation
(§3). What remains open in general is the case where classes of 𝔊 have
**two or more** prime factors `> z` (§4).
(c) The same proof with a level split instead of Hölder gives: if
`E_{π_c}H ≤ e^{S_r}E_U H` for all `H ≥ 0` with rough frequencies of rough
level `≤ 2λ'` and `|π̂_c(θ_r)|² ≤ e^{S_r}/N` above rough level λ', then
`log(N/B) ≤ log ρ + S_r + log 2` (Cauchy–Schwarz plus LS2 Lemma 2.2 on the
low part; `Σw ≤ 1` on the high part). This is LS2 Prop 5.2 with the smooth
coordinates removed from both conditions.

## 2. The smooth part costs only a density

`Q'` is K2's sequential law (EK §4.1, K2 §§2–4): square base `R_W^□`
uniform on the W-smooth coordinate (K2 Lemma 2.3), then the plain rule in
increasing order of the primes `ℓ > W` on the coordinates `ℤ/ℓ^{E_ℓ}`,
`ν = U`, caps `δ_ℓ = ℓ^{−1/2}`; `F_ℓ` is the activated forbidden set (classes
with top prime ℓ whose cofactor requirement is met by the past),
`p_ℓ = U(F_ℓ)`. Running it up to z gives a law on `ℤ/M_s`; the classes
decided there are exactly the classes with z-smooth modulus. Inputs used:
* (Q1) `E_{Q'}Σ_{W<ℓ≤y}p_ℓ ≤ 𝔐(y) ≤ K₃(log y)³(log log y)³` (K2 §3 and
  Cor 3.7; Case A via ElT Prop 1.4);
* (Q2) `E_{Q'}p_ℓ² ≤ Cℓ^{−7/4}(log ℓ)^c` for `ℓ > W` (K2 Lemma 4.3, any
  family 𝔊 ⊆ 𝔘);
* (Q3) leak: `Σ_{ℓ>W}E[p_ℓ1{p_ℓ>ℓ^{−1/2}}] ≤ C W^{−1/4}(log W)^{3c+2}`
  (K2 Lemma 4.3);
* (Q4) chain rule: `Q'(n ≡ b (mod m)) ≤ Γ(m)/m` (K2 §2).

Fix `W = W₁` absolute and so large that the bounds in (Q2), (Q3) give
`Σ_{ℓ>W}4E p_ℓ² ≤ 1/8` and leak `≤ 1/8`.

**Lemma 2.1 (bounded-density measure on 𝒜_s; PROVED, inputs (Q1)–(Q4)).**
Let `z ≥ y₀` and let E be any event in the z-smooth coordinates with
`Q'(E) ≤ 1/8`. Let `G` be the event: `y_ℓ ∉ F_ℓ` for all `W < ℓ ≤ z`,
`p_ℓ ≤ 1/2` for all `W < ℓ ≤ z`, and `Σ_{W<ℓ≤z}p_ℓ ≤ 8𝔐(z)`. Then
`Q'(G∖E) ≥ 1/2`, `π_s := Q'(· | G∖E)` is supported on `𝒜_s`, and

    π_s(c) ≤ ρ/M_s,     log ρ ≤ 16𝔐(z) + 2W₁ + log 2.

*Proof.* `Q'(y_ℓ ∈ F_ℓ for some ℓ) ≤` leak `≤ 1/8` (on light ℓ the plain
rule never lands in `F_ℓ`, EK Lemma 2.1(1)); `Q'(∃ℓ: p_ℓ > 1/2) ≤
Σ4Ep_ℓ² ≤ 1/8`; Markov and (Q1) give `Q'(Σp_ℓ > 8𝔐(z)) ≤ 1/8`. So
`Q'(G∖E) ≥ 1/2`. On G every z-smooth class is avoided: the base avoids the
W-smooth ones (K2 Lemma 2.3(1)), and a class with top prime `ℓ ∈ (W,z]`
can only be hit by `y_ℓ ∈ F_ℓ`. *Density.* Given the past, `y_ℓ` is
uniform on `ℤ/ℓ^{E_ℓ}∖F_ℓ` (light) or on `ℤ/ℓ^{E_ℓ}` (heavy), so each
step has conditional probability `≤ ℓ^{−E_ℓ}(1−p_ℓ)^{−1}`, and on G,
`Π(1−p_ℓ)^{−1} ≤ e^{2Σp_ℓ} ≤ e^{16𝔐(z)}` (`p ≤ 1/2`). The base has
density `Q₀/|R_W^□| ≤ e^{2W₁}` (K2 Lemma 2.3(2); `Q₀` is K2's base
modulus, the lcm of `8P_W` and the W-smooth parts of the moduli).
Conditioning on an event of probability `≥ 1/2` at most doubles the
density. (Review R59 D6(a): `Q₀` need not divide `M_s` because of the
factor `8P_W`; either replace `M_s` by `lcm(M_s, Q₀)` throughout, which
changes nothing in Theorem 1.1, or take `π_s` to be the marginal on
`ℤ/M_s` — marginalisation does not increase the maximal density.) ∎

## 3. Rough-slice mixtures: every large sieve is capped

**Theorem 3.1 (PROVED; inputs as Lemma 2.1).** Let `z = exp((log N)^{1/4})`
and let 𝔊 be any mixture (any moduli, no B, no bound on their size) in which
every modulus has **at most one** prime factor `> z` (to any power). Then
every CRT-admissible N-large-sieve bound — any rational frequencies, any
denominators, any weights — saves

    log(N/B) ≤ C (log N)^{3/4} (log log N)³.

*Proof.* Every fibre family `𝔊_c` consists of classes mod `ℓ^v`, ℓ > z
prime: a slice system. For `ℓ > z` let `F_ℓ^r(c) ⊂ ℤ/ℓ^{E_ℓ}` be the union
of the classes of `𝔊_c` at ℓ and `p^r_ℓ(c)` its density. These are
exactly the activated sets of `Q'` at the primes `ℓ > z` (every class with a
prime `> z` has it as its top prime, and its cofactor is z-smooth), so
(Q2) and (Q4) apply to them. Take `κ = 3/4`, `β = (log N)^{−1/4}`,
`α = 2β(1−κ) = β/2`, and the event `E = E₁ ∪ E₂`,
* `E₁ = {∃ℓ > z : p^r_ℓ(c) > ℓ^{κ−1}}`:
  `Q'(E₁) ≤ Σ_{ℓ>z}ℓ^{2−2κ}Ep_ℓ² ≤ CΣ_{ℓ>z}ℓ^{−5/4}(log ℓ)^c ≤ 1/16` for
  N large;
* `E₂ = {Σ_{ℓ>z}p^r_ℓ(c)ℓ^{−α} > 16 J}`, `J = E_{Q'}Σ_{ℓ>z}p^r_ℓℓ^{−α}`:
  `Q'(E₂) ≤ 1/16`.

Let `π_s` be as in Lemma 2.1 and, for `c ∈ supp π_s`, `π_c = ⊗_{ℓ>z}`
uniform on `ℤ/ℓ^{E_ℓ} ∖ F^r_ℓ(c)` (other rough digits uniform). It lives on
`𝒜_c`. As in LS Thm 4.1, `π̂_c(Σ_ℓ a_ℓ/ℓ^{E_ℓ}) = Π_ℓ φ_{ℓ,c}(a_ℓ)` with
`φ(0) = 1`, `|φ(a)| ≤ g := p/(1−p)` and `Σ_{a≠0}|φ(a)|² = g` (Parseval),
so `Σ_{a≠0}|φ(a)|^{p'} ≤ g^{1+2β} ≤ 2p·(2ℓ^{κ−1})^{2β} ≤ 4p^r_ℓ(c)ℓ^{−α}`
off `E₁`, and
`log 𝓡_{p'}(π_c) ≤ Σ_ℓ log(1 + 4p^r_ℓℓ^{−α}) ≤ 64 J` off `E₂`.
*J.* By (Q4), `E p^r_ℓ ≤ Σ_{C : P(G_C) = ℓ}Γ(G_C)/G_C`, so
`J ≤ ∫_{z}^{∞} y^{−α} d𝔐(y) ≤ α∫_z^∞ 𝔐(y) y^{−1−α} dy ≤ αK₃∫_0^∞
t³(log(e+t))³e^{−αt}dt ≤ Cα^{−3}(log(e+1/α))³` (partial summation; the
boundary terms are `≤ 0` at z and vanish at ∞).
Theorem 1.1 now gives `log(N/B) ≤ β log N + 16𝔐(z) + 2W₁ + log 2 + 64J`,
and `β log N = (log N)^{3/4}`, `𝔐(z) ≤ K₃(log N)^{3/4}(log log N)³`,
`J ≤ C(log N)^{3/4}(log log N)³`. ∎

*Remarks.* (a) Compare LS Cor 4.2 (ET Cor 3.4 slice families, moduli
`q₀ℓ` with `q₀ ≤ ℓ^C`, `C < 1`). Theorem 3.1 drops the condition on `q₀`
entirely (any number of small primes, any size) and needs no `ℓ₀'`
enlargement, because the small coordinates are paid by density (Lemma 2.1)
instead of by a product structure. (b) The `(log log N)³` is K2's
Rankin loss in `𝔐` (K2 Rem 3.8); K3's local moment should remove it but
this is not checked here. (c) By Theorem 1.1 the only remaining source of
an (E1) escape over forced families is the set of classes with **two or
more prime factors above** `exp((log N)^{1/4})`, entering through
correlations of the fibre measures `π_c` between such primes (§4).

## 4. The residual problem: two or more rough primes per class

By Theorem 1.1 (Hölder form) and Remark 1.1(c) (level-split form), H_LS∞
for forced families is now equivalent to a statement about the **z-rough
fibre families** `𝔊_c` (`z = exp((log N)^{1/4})`, all primes `> z`), for
`c` in a set of `Q'`-probability `≥ 7/8`:

> **(H_rough)** there is a probability `π_c` on `𝒜_c` with
> `log 𝓡_{2+2β}(π_c) ≤ C(log N)^{3/4+o(1)}`, `β = (log N)^{−1/4}`;
> *or* (level-split form) `π_c` with cheap comparison
> `E_{π_c}H ≤ e^{S_r}E_U H` for `H ≥ 0` of rough level `≤ 2λ'` and
> `|π̂_c(θ_r)|² ≤ e^{S_r}/N` above rough level `λ' ≍ log N`,
> `S_r ≤ C(log N)^{3/4+o(1)}`.

Theorem 3.1 proves (H_rough) when every class has one rough prime (product
measures). In the fibres the family is **sparse in the strongest sense
available**: by (Q4) and K2 §3, the expected activated mass at a rough
prime ℓ (top-prime order) is at most the increment
`Σ_{C: P(G_C)=ℓ}Γ(G_C)/G_C` of 𝔐 at ℓ (and `Σ_{ℓ>z}ℓ^{−α}·`increment
`≪ α^{−3}(log 1/α)³`, as in Theorem 3.1), and the mass of classes divisible
by a rough `D` is expected to be `≤ D^{−1}(log N)^{O(1)}` ((Sp) of LS2
§8.2; Assessment, not needed below). The dense-bundle mechanism of LS2 Thm 8.5 is therefore
absent; what is missing is a **correlation-decay** statement for a measure
on `𝒜_c` at many rough primes simultaneously.

**Lemma 4.1 (two-copy form of the `ℓ^{p'}` mass; PROVED).** For a
probability σ on `ℤ/M_r` and a set S of rough primes let
`P_S(σ) = Σ_{θ: supp(den θ) = S}|σ̂(θ)|²` and `s_S(σ) = max_{supp(den θ)=S}|σ̂(θ)|`.
Then
* `P_S(σ) = E_{x,y∼σ iid} Π_{ℓ∈S} h_ℓ(x,y)`, `h_ℓ = ℓ^{E_ℓ}1[x ≡ y (ℓ^{E_ℓ})] − 1`,
  and `Σ_{S⊆T}P_S(σ) = M_T·σ⊗σ(x ≡ y (M_T))` (`M_T = Π_{ℓ∈T}ℓ^{E_ℓ}`);
* `𝓡_{2+2β}(σ) ≤ Σ_S s_S(σ)^{2β}P_S(σ)`.

*Proof.* `Σ_{a mod ℓ^E, a≢0}e(a(x−y)/ℓ^E) = h_ℓ(x,y)`; multiply over S and
average over `σ⊗σ`. The second identity is Parseval mod `M_T`. The last line
is `|σ̂|^{2+2β} ≤ s_S^{2β}|σ̂|²` on each support class. ∎

For a product measure, `P_S = Π_{ℓ∈S}g_ℓ` and `s_S = Π_{ℓ∈S}max|φ_ℓ|`, and
Lemma 4.1 reproduces Theorem 3.1. So (H_rough) follows from **product decay
of both** the two-copy correlations `P_S` and the sup `s_S`, with per-prime
factors `≍` the activated mass. The collision side (`Σ_{S⊆T}P_S`) is pure
density and is controlled by inflation (EK Lemma 2.1(2)); the difficulty is
the Möbius-inverted, signed quantity `P_S`, and `s_S`.

### 4.2 Why the symmetric (LLL / Kotecký–Preiss) route fails

For the uniform measure on `𝒜_c` the natural tool is a cluster expansion
with polymers = connected sets of classes. Its convergence (KP) needs, for
each rough prime p and **each** residue b, the *conditional* mass
`m*(p,b) = Σ_{C ∋ p, b_C ≡ b (p^{v})} p^{v}/G_r(C)` to be small. On average
over b this is the mass at p, `≪ (log N)^{O(1)}/p`. But:

**Lemma 4.2 (residue concentration; PROVED).** The class `−4 (mod M)`
belongs to ℛ(M) for every `M ≡ 3 (mod 4)` (take `D = 1 | A_M²`). Hence for
the family `{−4 mod pM' : M' ≤ X, pM' ≡ 3 (4), M' z-rough}` and the residue
`b ≡ −4 (mod p)`, `m*(p,b) = Σ_{M'}1/M' ≍ log X/log z` (Mertens over
z-rough `M'`, half of them in the right class mod 4), which is
`≍ A(log N)^{3/4}` for `X = N^{A}`.

So a fibre family can be locally **dense at one residue** although sparse
on average, and every proof must either average over residues or use the
top-prime (sequential) order, in which the class `−4 mod pM'` is charged
at its top prime with activation probability `≍ 1/(cofactor)` and the
relevant sums run over ℓ-smooth cofactors only (K2 §3). In that order the
*average* influence of a coordinate `x_p` on all later coordinates is
`≪ Σ_{C∋p} 1/G_r ≪ (log N)^{O(1)}/p` (sparsity), while its worst-case
influence is `≍ p·m(p)`, which is not small (Lemma 4.2 again).

### 4.3 Why one-step bounds lose (Assessment)

Peeling the top prime ℓ of a sequential law gives
`𝓡(π_{≤ℓ}) = 𝓡(π_{<ℓ}) + Σ_{a≢0}𝓡(π_{<ℓ}·k̂_·(a))`, where `k̂_y(a)` is the
Fourier transform of the conditional law at ℓ. In `ℓ²` (β = 0) the second
term is exactly `E_{π_{<ℓ}}[ρ_{<ℓ}g_ℓ]` (Parseval), i.e. the
density-weighted activated mass — the right size. For `β > 0` every
operator bound on multiplication by `k̂_·(a)` that we tried loses:
Young (`ℓ¹` of the Fourier transform of the activation indicator) loses a
square root of the number of classes; Riesz–Thorin between `ℓ²`
(`‖k̂‖_∞`, a **sup over activation patterns**) and `ℓ^∞` replaces the
π-average of the activated mass by a sum over all patterns — the product
sub-law cost `ℓ^{B+o(1)}` of LS2 §5. Global Hausdorff–Young loses the full
density `e^{(mass)}`. A proof has to keep the π-average inside the
`ℓ^{p'}` norm, i.e. it is a genuine multi-scale correlation-decay
statement.

## 5. Numerics (EVIDENCE / sanity checks only)

`scripts/largesieve3_checks.py`: (1) Theorem 1.1's core inequality
`𝓡_{p'}(π) ≤ ρ E_{π_s}𝓡_{p'}(π_c)` on 20 random toy rough-slice mixtures
over `ℤ/(3·5·7·11·13)` (max ratio 0.867 ≤ 1; π checked to live on 𝒜);
(2) the local bound `Σ_{a≠0}|φ|^{p'} ≤ g^{1+2β}` and Parseval `= g`;
(3) Lemma 4.1's two-copy identity and `𝓡 ≤ Σ_S s_S^{2β}P_S` for a random
non-product measure mod 105.

## Replay

    ulimit -v 8000000
    timeout 600 env PYTHONPATH=scripts uv run --with numpy python scripts/largesieve3_checks.py
