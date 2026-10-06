# EXCEPTIONAL_LARGESIEVE6 — the soft-pivotal lemma (task O71)

Status: **in progress** (agent O71, branch `side-agent/soft-pivotal`).
Labels as in `DISCOVERIES.md`. Notation: LS4 = `EXCEPTIONAL_LARGESIEVE4.md`,
LS5 = `EXCEPTIONAL_LARGESIEVE5.md` (all their notation is used: Setting 2.0
of LS5 = truncated forbidding, `Y = Σ_q w_q p̃_q`, `σ_tilt`, `Z`; LS4
Lemma 1.1, Thm 4.2, Lemma 5.1, (A\*)), LS3, K2 as there. `β = (log N)^{−1/4}`,
`z = exp((log N)^{1/4})`, `w_ℓ = (Kℓ^{−γ})^{2β}`.

## 0. Plan and summary (updated as the work proceeds)

| item | statement | label |
|---|---|---|
| Lemma 1.1 | **global prefactors in (A\*) are free**: `|σ̂| ≤ Λ·Π Kℓ^{−γ}` costs only `2β log Λ` in the Rényi bound | PROVED (trivial) |
| Cor 1.2 | hence the tilt normalisation `Z^{−1} ≤ (4/3)e^{8m_c/3}` costs `≤ 6βm_c`: LS4 Thm 4.2 holds with (A\*) for `σ_tilt` **with prefactor `Z^{−1}`**, and LS4 Lemma 5.1 / Thm 5.2 transfer to `σ_tilt` (repairing the LS5 caution R67 M3 at the level of normalisation) | PROVED (implication; inputs as LS4 Thm 4.2) |

## 1. Global prefactors are free

**Lemma 1.1 (PROVED).** Let σ be a probability on `ℤ/M_r`, `0 < β ≤ 1/2`,
`w_ℓ ∈ [0,1]`, `Λ ≥ 1`, and suppose

    |σ̂(θ)|^{2β} ≤ Λ^{2β} Π_{ℓ∈supp θ} w_ℓ      for every θ ≠ 0.

Then `𝓡_{2+2β}(σ) ≤ Λ^{2β} E_T 𝓡_2(σ_T)` (T as in LS4 Lemma 1.1).

*Proof.* With `P_S = Σ_{supp θ=S}|σ̂(θ)|² ≥ 0` (`P_∅ = 1`):
`𝓡_{2+2β} = 1 + Σ_{S≠∅}Σ_{supp θ=S}|σ̂|²|σ̂|^{2β} ≤ 1 + Λ^{2β}Σ_{S≠∅}w_SP_S
≤ Λ^{2β}Σ_S w_SP_S`, and `Σ_S w_SP_S = E_T𝓡_2(σ_T)` (LS4 Lemma 1.1). ∎

So (A\*) in LS4 Thm 4.2 may be weakened to

> **(A\*_Λ)** for c off the exceptional event and every θ ≠ 0 with z-rough
> denominator: `|σ̂_c(θ)| ≤ Λ_c · Π_{ℓ∈supp θ} K ℓ^{−γ}`,

at the additive cost `2β·log Λ_c` in `log 𝓡_{2+2β}(σ_c)`. Since
`2β = 2(log N)^{−1/4}`, a prefactor as large as `Λ_c = e^{O(m_c)}` (even
`N^{1/2}`) is harmless: it costs `O(βm_c)` (resp. `(log N)^{3/4}`).

**Corollary 1.2 (tilted law with prefactor; PROVED as an implication,
inputs as LS4 Thm 4.2 with LS5 Setting 2.0).** In LS4 Thm 4.2 take
`σ_c = σ_tilt,c` (LS5 Prop 2.1) and replace (A\*) by (A\*_Λ) with
`Λ_c = Λ'·Z_c^{−1}`, `Λ' ≥ 1` a constant. Then the conclusion of LS4
Thm 4.2 holds with `512J` replaced by `C·J` and an extra `2β log Λ'`.
Moreover LS4 Lemma 5.1 holds for `σ = Q'Φ/E_{Q'}Φ` with any `Φ ≥ 0` that
depends on the path only through the activated sets `F_q`, `F̃_q` and
membership in 𝒜 (in particular `Φ = 1_𝒜 e^{−2Y}`), in the form

    |σ̂(θ)| ≤ (‖Φ‖_∞ / E_{Q'}Φ) · Π_{ℓ∈S} 4U(R_ℓ)/(1−δ_ℓ),

so LS4 Thm 5.2 and Cor 5.3 hold verbatim for the tilted law.

*Proof.* Off the exceptional event `Q'_c(𝒜_c) ≥ 3/4`, so LS5 Prop 2.1 gives
`log E_T𝓡_2 ≤ 6m_c + 1` and `Z_c ≥ (3/4)e^{−8m_c/3}`. By Lemma 1.1,
`log 𝓡_{2+2β}(σ_c) ≤ 6m_c + 1 + 2β(log Λ' + 8m_c/3 + log(4/3)) ≤ 7m_c + 2
+ 2β log Λ'` for N large; LS3 Thm 1.1 and `m_c ≤ 32J` conclude as in LS4
Thm 4.2. For Lemma 5.1: its proof uses `1_G` only through (i) the pinned
representation `σ(x_S = v) = E_{Q'}[Φ]^{−1}E_{coins}[Φ(path(v))Π_{ℓ∈S}
k_ℓ(v_ℓ|past)]`, valid for any `Φ ≥ 0`, (ii) `0 ≤ Φ·Π|Ω_ℓ|k_ℓ ≤
‖Φ‖_∞Π(1−δ_ℓ)^{−1}`, and (iii) the fact that if `v_ℓ, v'_ℓ ∉ R_ℓ` the two
corner paths have identical activated sets, truncations, coin decisions
and avoider membership (LS4 proof, unchanged under truncated forbidding:
`F̃_ℓ` is a function of `F_ℓ`), hence identical Φ. In Thm 5.2 the factor
`Q'(G)^{−1} ≤ 2` becomes `Z_c^{−1}`, absorbed by Lemma 1.1. ∎

*Remark.* LS5 (Caution, R67 M3) noted that the pinned bound for the tilt
carries `Z^{−1}`, exponentially large in `m_c`, and that the tilt can make
an individual Fourier coefficient large. Both are true, and both are
harmless for the Hölder route: (A\*) is used only through Lemma 1.1, where a
prefactor enters raised to the power `2β`. What stays relevant is the
**product** structure `Π_{ℓ∈S}Kℓ^{−γ}`; the soft-pivotal lemma below may
therefore bound all tilt factors by 1 pointwise (no tilt-bias estimate is
needed).

## 2. The soft-pivotal bound

### 2.1 Cube calculus

S is a finite set, functions are on corners `A ⊆ S`. For `A ∩ T = ∅` put
`D_Tf(A) = Σ_{B⊆T}(−1)^{|T∖B|}f(A∪B)` (`D_∅f = f`), and
`‖D_Tf‖ = max_{A⊆S∖T}|D_Tf(A)|`. ℓ is **pivotal** for f, `ℓ ∈ Piv(f)`, if
`f(A∪ℓ) ≠ f(A)` for some `A ∌ ℓ`.

**Lemma 2.1 (Leibniz; PROVED, elementary).** (a)
`D_T(fg)(A) = Σ_{U⊆T} D_Uf(A)·D_{T∖U}g(A∪U)`.
(b) For finitely many factors `ψ_i` (i ∈ 𝓘):
`‖D_T Π_iψ_i‖ ≤ Σ_{f: T→𝓘} Π_{i∈𝓘}‖D_{f^{−1}(i)}ψ_i‖`.
(c) `D_Tψ ≡ 0` unless `T ⊆ Piv(ψ)`; `‖D_Tψ‖ ≤ 2^{|T|−1}‖ψ‖_∞` for
0/1-valued ψ and `T ≠ ∅`; and if `ψ = F∘u` with F L-Lipschitz on the range
of u, then for `T ≠ ∅`

    ‖D_Tψ‖ ≤ 2^{|T|−1} L Δ(u) · 1[T ⊆ Piv(u)],   Δ(u) := max_{A,A'}|u(A) − u(A')|.

*Proof.* (a) Induction on |T|: for `T = T'∪{ℓ}` apply `D_ℓ(FG)(A) =
D_ℓF(A)G(A∪ℓ) + F(A)D_ℓG(A)` to each term of the formula for T' (with
`F = D_Uf`, `G(·) = D_{T'∖U}g(·∪U)`); the two pieces are the terms `U∪ℓ`
and U of the formula for T. (b) iterate (a) and take absolute values.
(c) `D_T = D_{T∖ℓ}D_ℓ`; if ℓ is not pivotal, `D_ℓψ ≡ 0`; `Piv(F∘u) ⊆
Piv(u)`. A 0/1 function has `|D_ℓψ| ≤ 1`, and `|D_ℓ(F∘u)| ≤ LΔ(u)`; then
`D_{T∖ℓ}` of a function bounded by M is bounded by `2^{|T|−1}M`. ∎

The point of (c) for Lipschitz factors: **one** factor `LΔ(u)` is gained
however many coordinates are charged to the factor; no Faà di Bruno sums
(and no Bell numbers) are needed.

### 2.2 The corner paths and the factorisation

Setting: LS5 Setting 2.0 (truncated forbidding, caps `δ_q ≤ 1/2`), Q′ the
sequential law on the rough coordinates 𝒫 (finite), `Φ = 1_𝒜e^{−2Y}`,
`σ = σ_tilt = Q′Φ/Z`. Coins (LS4 §3): `c_q ~ U(Ω_q)` and a uniformly random
ordering `π_q` of `Ω_q`, all independent; given the past, `x_q = c_q` if
`c_q ∉ F̃_q`, otherwise the first element of `π_q` outside `F̃_q` (law
`U(·|Ω_q∖F̃_q)`, as LS4).

Fix θ ≠ 0, `S = supp θ`, independent uniform `v, v' ∈ Ω_S`, and coins for
`q ∉ S`. For `A ⊆ S` let `v^A` take the value `v'_ℓ` for `ℓ ∈ A` and `v_ℓ`
otherwise, and let `x^A` be the **corner path**: `x^A_ℓ = v^A_ℓ` on S, and
the coin rule (with the activated sets of `x^A`) off S. Write `F_q(A)`,
`F̃_q(A)`, `p̃_q(A)` for the sets/masses along `x^A`.

Pinned representation (as in LS4 Lemma 5.1): integrating the S-coordinates
step by step,
`σ(x_S = v) = Z^{−1}E_{coins}[Φ(x^v)Π_{ℓ∈S}k_ℓ(v_ℓ | x^v_{<ℓ})]`, so with
`Ψ(A) := Φ(x^A)Π_{ℓ∈S}|Ω_ℓ|k_ℓ(v^A_ℓ | x^A_{<ℓ})` and LS4 Lemma 3.1's
expansion (`χ_θ` is non-trivial in every ℓ ∈ S),

    |σ̂(θ)| ≤ Z^{−1} E_{coins,v,v'} |D_SΨ(∅)|.                     (2.1)

On every corner, since `x^A_q ∉ F̃_q(A)` for `q ∉ S` by construction,
`1_𝒜(x^A) = Π_{q∉S}1[x^A_q ∉ F_q(A)∖F̃_q(A)]·Π_{ℓ∈S}1[v^A_ℓ ∉ F_ℓ(A)]`
and `|Ω_ℓ|k_ℓ(a) = 1[a ∉ F̃_ℓ]/(1−p̃_ℓ)`. Hence `Ψ = Π_{i∈𝓘}ψ_i` with the
factors

| factor | definition | type | weight `κ_i` |
|---|---|---|---|
| `h_ℓ`, ℓ ∈ S | `1[v^A_ℓ ∉ F_ℓ(A)]` | 0/1 | 1 |
| `g_ℓ`, ℓ ∈ S | `(1 − p̃_ℓ(A))^{−1}` (≤ 2, Lipschitz 4) | soft | `2Δ_ℓ` |
| `λ_q`, q ∉ S | `1[x^A_q ∉ F_q(A)∖F̃_q(A)]` (leak) | 0/1 | 1 |
| `φ_q`, q ∈ 𝒫 | `e^{−2w_q p̃_q(A)}` (Lipschitz `2w_q`) | soft | `w_qΔ_q` |

where `Δ_q = max_{A,A'}|p̃_q(A) − p̃_q(A')|`. (`1[v ∉ F̃]·1[v ∉ F] = 1[v ∉ F]`
was used at ℓ ∈ S.)

**Proposition 2.2 (soft-pivotal bound; PROVED).** With
`W_B := Σ_{i∈𝓘} κ_i·1[B ⊆ Piv(ψ_i)]` (the *joint influence weight* of
`B ⊆ S`, a function of the coins and of `v, v'`),

    |σ̂_tilt(θ)| ≤ Z^{−1} · 4^{|S|} · E_{coins,v,v'} Σ_{𝔅 partition of S} Π_{B∈𝔅} W_B.

Moreover, writing `N_q` for the number of classes C with top q whose
off-top matching status along `x^A` is not the same for all corners A,
`Δ_q ≤ N_q·q^{−1}` (more precisely `≤ Σ_C q^{−v_q(G_C)}` over those C).

*Proof.* Lemma 2.1(b) for `Ψ = Πψ_i`. Factors with `f^{−1}(i) = ∅`
contribute `‖ψ_i‖_∞ ≤ 1`, except `g_ℓ ≤ (1−δ_ℓ)^{−1} ≤ 2`: together
`≤ 2^{|S|}`. A factor with `T = f^{−1}(i) ≠ ∅` contributes, by Lemma
2.1(c), at most `2^{|T|}κ_i 1[T ⊆ Piv(ψ_i)]` (0/1: `2^{|T|−1}`; `g_ℓ`:
`2^{|T|−1}·4Δ_ℓ`; `φ_q`: `2^{|T|−1}·2w_qΔ_q`). The `2^{|T|}` multiply to
`2^{|S|}`. So `|D_SΨ| ≤ 4^{|S|}Σ_fΠ_{i∈f(S)}κ_i1[f^{−1}(i) ⊆ Piv(ψ_i)]`.
Group the maps f by the partition `𝔅 = {f^{−1}(i)}` of S; f is then an
injective assignment of blocks to factors, and dropping injectivity gives
`≤ Σ_𝔅Π_{B∈𝔅}Σ_iκ_i1[B ⊆ Piv(ψ_i)]`. Insert in (2.1). For `Δ_q`: the
truncation `p̃ = min(p, ⌊δ|Ω|⌋/|Ω|)` is 1-Lipschitz in p, and
`|p_q(A) − p_q(A')| ≤ U(F_q(A) Δ F_q(A'))`, which is at most the total
mass of the classes whose activation differs. ∎

*Remarks.* (a) **Outside tops are charged by their damping.** A witness
class through ℓ ∈ S whose top q lies outside S makes ℓ pivotal only for
`φ_q` (and for `λ_q`, which is 0/1 but non-constant only on heavy steps)
— unless it also changes the path (see §3); it then costs `κ = w_qΔ_q ≤
w_qN_q/q`, not 1. This is exactly the soft-pivotal mechanism missing in
LS5 §4 (caveat R67): in the undamped event `E_S` of LS5 such a witness
counted fully, and `Σ_q 1/q = ∞` over the witnesses `(−4D, ℓq)`.
(b) Compared with LS4 Lemma 3.1 ("every ℓ ∈ S pivotal for Ψ") the Leibniz
split assigns each ℓ to **one** factor; the partition sum is the precise
form of LS4 §3.2's covering events, with the blocks of 𝔅 playing the
role of LS5 Lemma 3.1's label blocks.
(c) No tilt-bias estimate is used: all factors are bounded pointwise and
the expectation is over the **untilted** product space of coins and
`(v, v')`. The price `Z^{−1}` is free by Lemma 1.1.

## 3. Where pivotality comes from: chains of varying classes

Fix coins, v, v′ (with `v_ℓ ≠ v′_ℓ` for all ℓ ∈ S; otherwise `D_SΨ = 0`).
A class C (of the fibre family) is **matched off-top by x** if
`x_p ≡ b_C (mod p^{v_p(G_C)})` for every prime `p | G_C`, `p ≠ top(C)`; it
is **varying** if this status is not the same for all corner paths. Let
`𝒟 = {r ∉ S : x^A_r is not constant in A}` (divergent outside coordinates),
`F^∪_r = ∪_AF̃_r(A)`, `F^∩_r = ∩_AF̃_r(A)`. For `ℓ ∈ S` write
`ℓ ∈ Piv(F_q)` if `F_q(A∪ℓ) ≠ F_q(A)` for some `A ∌ ℓ`.

**Lemma 3.1 (chains; PROVED).**
(i) If `r ∈ 𝒟` then some class with top r is varying, and either
`c_r ∈ F^∪_r∖F^∩_r`, or `c_r ∈ F^∩_r` and the first element of `π_r`
outside `F^∩_r` lies in `F^∪_r∖F^∩_r`.
(ii) A varying class is matched off-top by some corner path and has an
off-top coordinate in `S ∪ 𝒟`.
(iii) If `ℓ ∈ Piv(F_q)` then there are `k ≥ 1`, coordinates
`ℓ = r_0 < r_1 < … < r_k = q` with `r_1,…,r_{k−1} ∈ 𝒟` (outside S), and
classes `C_1,…,C_k` with `top(C_j) = r_j`, `r_{j−1} | G_{C_j}`, each
matched off-top by some corner path. (A *chain from ℓ to q*.)
(iv) Pivot sets of the factors of §2.2: `Piv(φ_q), Piv(g_q) ⊆ Piv(F_q)`;
`Piv(λ_q) ⊆ Piv(F_q)`, and `Piv(λ_q) = ∅` unless `F_q(A) ≠ F̃_q(A)` for
some A (q *heavy in some corner*); for ℓ′ ∈ S,
`Piv(h_{ℓ′}) ⊆ {ℓ′} ∪ Piv(F_{ℓ′})`, where `ℓ′ ∈ Piv(h_{ℓ′})` requires
`{v_{ℓ′}, v′_{ℓ′}} ∩ ∪_AF_{ℓ′}(A) ≠ ∅`, and `ℓ ∈ Piv(h_{ℓ′})`, `ℓ ≠ ℓ′`,
requires `ℓ ∈ Piv(F_{ℓ′})` and `{v_{ℓ′}, v′_{ℓ′}} ∩ ∪_AF_{ℓ′}(A) ≠ ∅`.

*Proof.* (i) If `F̃_r(A)` is the same set for all A, the coin rule gives
the same `x_r` on every corner (same `c_r`, same `π_r`); so some
`F̃_r(A)` differ, hence some `F_r(A)` differ (`F̃` is a function of `F`),
hence some class with top r is varying. If `c_r ∉ F^∪` every corner keeps
`c_r`; if `c_r ∈ F^∩` every corner replaces, and the replacements are the
first elements of `π_r` outside the various `F̃_r(A) ⊇ F^∩`; they all equal
the first element outside `F^∩` unless that element lies in some
`F̃_r(A)∖F^∩ ⊆ F^∪∖F^∩`. (ii) Off-top matching depends only on the
off-top coordinates; if all of them are constant across corners, so is
the status. Coordinates in `S` vary (`v ≠ v′`), outside ones vary iff in
𝒟. (iii) Take `A ∌ ℓ` with `F_q(A∪ℓ) ≠ F_q(A)`; some class `C_k` with top
q is matched off-top by exactly one of `x = x^A`, `x′ = x^{A∪ℓ}`, so x, x′
differ at an off-top coordinate r of `C_k`. The corners A, A∪ℓ agree on
`S∖ℓ`, so `r = ℓ` (stop, `k = 1`… after relabelling) or `r ∉ S`; then
x, x′ differ at r, so `r ∈ 𝒟` and, by the argument of (i) applied to the
two paths x, x′, `F_r(x) ≠ F_r(x′)`; recurse with q replaced by `r < q`.
The recursion stops (at ℓ) because x and x′ agree below ℓ. Every class
found is matched off-top by x or x′. (iv) `p̃_q` and `x_q` (q ∉ S) are
functions of `F_q` (and of fixed coins); `λ_q ≡ 1` on corners where
`F_q = F̃_q`; `h_{ℓ′} = 1[v^A_{ℓ′} ∉ F_{ℓ′}(A)]` changes along an edge
only if `v^A_{ℓ′}` changes (edge in direction ℓ′) or `F_{ℓ′}` changes,
and in both cases the indicator is 0 at one end, i.e.
`v^A_{ℓ′} ∈ F_{ℓ′}(A)` there. ∎

So, for every block `B ⊆ S`,

    W_B ≤ Σ_{ℓ′∈S} 1[B ⊆ Piv(h_{ℓ′})] + Σ_{ℓ′∈S} 2Δ_{ℓ′}1[B ⊆ Piv(F_{ℓ′})]
          + Σ_{q∉S} 1[q heavy in some corner]·1[B ⊆ Piv(F_q)]
          + Σ_{q} w_qΔ_q·1[B ⊆ Piv(F_q)].                          (3.1)

Each `ℓ ∈ B` needs a chain to the charged top (Lemma 3.1(iii)) — or, for
`h_ℓ` itself, the self-coincidence `{v_ℓ, v′_ℓ} ∩ F_ℓ ≠ ∅`. Chains run
**upward** through divergent outside coordinates only; a chain may end at
an outside top q only through `φ_q` (weight `w_qΔ_q`) or a leak `λ_q`
(only on heavy steps), and otherwise must reach an S-top `ℓ′ > ℓ`, where
it meets ℓ′'s own coincidence.

## 4. Removing the partition sum: the Walsh form of the soft-pivotal bound

*Why Prop 2.2 is lossy.* Its partition sum over 𝔅 and the assignment of
blocks to individual factors `φ_q` overcount when many factors are
functions of the same event. Example: if `v_ℓ ≡ −4 (mod ℓ)` for every
`ℓ ∈ B` (probability `Π_{ℓ∈B}ℓ^{−1}`), the residue `−4 mod q` is
activated at every `q ≡ 3ℓ^{−1} (4)` iff `A ⊉ B`, so
`Π_qφ_q(A) = e^{−c}·e^{c1[A⊇B]}` with `c = Σ_q 2w_q/q·(…) = O_γ(1)`: the
true `|D_B| = e^{−c}(e^{c}−1) = O(1)`, but Prop 2.2 sums over all
partitions of B into blocks charged to distinct q's and gets
`≍ Bell(|B|)` (a per-prime loss `|B|/log|B|`, fatal for `|S| ≫ z^{1−γ}`).
The cure is to treat all soft factors as **one** exponential and expand it
in the Walsh basis of the corner cube.

**Lemma 4.1 (exponential Walsh-cover bound; PROVED).** Let U be finite,
`Y*: 2^U → [0,∞)`, `χ_R(A) = (−1)^{|A∩R|}`,
`a_R = 2^{−|U|}Σ_A Y*(A)χ_R(A)` (so `Y* = Σ_R a_Rχ_R`), and
`‖a‖′ = Σ_{R≠∅}|a_R|`. Then

    |D_U e^{−Y*}(∅)| ≤ 2^{|U|} e^{‖a‖′} Σ_{𝒯 ⊆ 2^U∖{∅}, △𝒯 = U} Π_{R∈𝒯}|a_R|
                    ≤ 2^{|U|} e^{2‖a‖′} Π_{ℓ∈U} ( Σ_{R∋ℓ} β_R ),

`β_R := max(|a_R|, |a_R|^{1/|R|})` (△ = symmetric difference). Moreover
`a_R = 0` unless `R ⊆ Piv(Y*)`, `|a_R| ≤ Δ(Y*)/2` for `R ≠ ∅`, and
`Y* ↦ a` is linear.

*Proof.* `D_Uf(∅) = (−1)^{|U|}Σ_Aχ_U(A)f(A) = (−1)^{|U|}2^{|U|}f̂(U)`.
`e^{−Y*} = e^{−a_∅}Π_{R≠∅}(cosh a_R − χ_R sinh a_R)` (as `χ_R = ±1`);
expanding, `χ_{R_1}⋯χ_{R_k} = χ_{R_1△⋯△R_k}`, so
`|f̂(U)| ≤ e^{−a_∅}Π_{R≠∅}cosh a_R·Σ_{△𝒯=U}Π_{R∈𝒯}|tanh a_R|`, and
`a_∅ = mean(Y*) ≥ 0`, `cosh x ≤ e^{|x|}`, `|tanh x| ≤ |x|`. Second
inequality: a family with `△𝒯 = U` covers U; every cover contains a
minimal subcover 𝒯₀, so the sum is `≤ Π_R(1+|a_R|)·Σ_{𝒯₀ minimal}Π_{𝒯₀}|a_R|`.
In a minimal cover every R has a private element; map each `ℓ ∈ U` to an
`R(ℓ) ∋ ℓ` in 𝒯₀, private elements to their own set. Every R then receives
`n_R ∈ [1, |R|]` elements and `|a_R| = Π_{ℓ: R(ℓ)=R}|a_R|^{1/n_R} ≤
Π β_R`; distinct minimal covers give distinct maps (the image is 𝒯₀), so
`Σ_{𝒯₀}Π|a_R| ≤ Σ_{maps}Π_ℓβ_{R(ℓ)} = Π_ℓΣ_{R∋ℓ}β_R`. Finally: if
`ℓ ∈ R∖Piv(Y*)`, Y* does not depend on `A_ℓ` and `Σ_{A_ℓ}χ_ℓ = 0`; for
`R ≠ ∅`, `a_R = 2^{−|U|}Σ_A(Y*(A) − c)χ_R(A)` for any constant c. ∎

**Proposition 4.2 (soft-pivotal bound, Walsh form; PROVED).** In the setting
of §2.2 write `Ψ = H·e^{−Y*}` with the 0/1 function
`H = Π_{ℓ∈S}h_ℓΠ_{q∉S}λ_q` and
`Y* = 2Σ_{q∈𝒫}w_qp̃_q + Σ_{ℓ∈S}L_ℓ`, `L_ℓ = −log(1−p̃_ℓ)` (all functions of
the corner A). For `T ⊆ S` and a corner `A_T ⊆ T`, let
`a^{(A_T)}_R` (`R ⊆ S∖T`) be the Walsh coefficients of `Y*` restricted to
corners `A_T ∪ A′`, `A′ ⊆ S∖T`. Then

    |σ̂_tilt(θ)| ≤ Z^{−1} 2^{|S|} E_{coins,v,v′} Σ_{T⊆S} 1[T ⊆ Piv(H)]
                   · max_{A_T} e^{‖a^{(A_T)}‖′} Σ_{△𝒯 = S∖T} Π_{R∈𝒯}|a^{(A_T)}_R|      (4.1)

                 ≤ Z^{−1} 2^{|S|} E_{coins,v,v′} Σ_{T⊆S} 1[T ⊆ Piv(H)]
                   · max_{A_T} e^{2‖a^{(A_T)}‖′} Π_{ℓ∈S∖T} Σ_{R∋ℓ, R⊆S∖T} β^{(A_T)}_R

(the XOR-cover sum is 1 when `T = S`).

The Walsh coefficients obey, for `R ≠ ∅`,

    |a_R| ≤ Σ_{q∈𝒫} w_qΔ_q·1[R ⊆ Piv(F_q)] + Σ_{ℓ′∈S} Δ_{ℓ′}·1[R ⊆ Piv(F_{ℓ′})],

(more precisely `a_R` is the sum of the R-th Walsh coefficients of the
summands), and `Piv(H)` is described by Lemma 3.1(iv).

*Proof.* Lemma 2.1(a) with two factors and `‖D_TH‖ ≤ 2^{|T|}1[T⊆Piv(H)]`
(H is 0/1): `|D_SΨ| ≤ Σ_T 2^{|T|}1[T⊆Piv(H)]·max_{A_T}|D_{S∖T}e^{−Y*}(A_T)|`,
where `D_{S∖T}e^{−Y*}(A_T)` is the top difference of the restriction of
`e^{−Y*}` to the subcube over `A_T`; apply Lemma 4.1 to that restriction
(`Y* ≥ 0`). Insert in (2.1); `2^{|T|}2^{|S∖T|} = 2^{|S|}`. For the
coefficient bound use linearity and `|f̂(R)| ≤ Δ(f)/2`, `f̂(R) = 0` unless
`R ⊆ Piv(f)`, with `Δ(2w_qp̃_q) = 2w_qΔ_q` and `Δ(L_{ℓ′}) ≤ 2Δ_{ℓ′}`
(`|L′| ≤ 2` on `[0,1/2]`); `Piv(p̃_q) ⊆ Piv(F_q)`. ∎

*What Prop 4.2 says.* Each `ℓ ∈ S` is paid either **hard** (`ℓ ∈ T`:
ℓ is pivotal for the 0/1 part H, i.e. for an avoidance/forbidding event
at an S-top, or for a leak) or **soft** (`ℓ ∉ T`: through a Walsh
coefficient `a_R ∋ ℓ` of the damped activated mass). In the soft case
an outside top q enters only with its damping `w_qΔ_q ≤ w_qN_q/q`, and
coordinates that act through one and the same event share **one**
coefficient. In the example above the soft part of Y* is
`c·1[A⊉B] = c − c·2^{−|B|}Σ_{R⊆B}(−1)^{|R|}χ_R`, so `|a_R| = c2^{−|B|}`
(R ⊆ B nonempty), `‖a‖′ ≤ c`, and the **first** (XOR-cover) form of
Lemma 4.1 gives, crudely (the XOR-cover sum is at most the sum over all
families, `Π_R(1+|a_R|) ≤ e^{c}`), `|D_B e^{−Y*}| ≤ 2^{|B|}e^{2c}` — the
harmless `2^{|B|}`, not Bell(|B|); the decay `Π_{ℓ∈B}ℓ^{−1}` comes from
the probability of the configuration. (The second, per-ℓ product form is
lossy for such *spread* spectra — there it gives `2^{O(|B|²)}` — and is
meant for sparse spectra, where each ℓ lies in few supports.) The
exponential prefactor `e^{2‖a‖′}` is a product of per-event factors
`e^{2|a_R|}` — e.g. `e^{O(Σ_ℓ y_ℓ)}` when the damped change `y_ℓ` caused by
each ℓ alone is additive.

## 5. One rough prime: uniform-in-X decay (the LS5 caveat removed)

Notation for a fixed fibre (all classes are those of the fibre family,
all primes rough): `Γ(m) = Π_{p^e∥m}(1−δ_p)^{−1}` (K2), for a class C
`ω(C)` = number of primes of `G_C`, and for primes `p ≤ r`

    μ̄(ℓ)     = Σ_{C∋ℓ, top(C)>ℓ} w_{top(C)} Γ(G_C)/G_C                (damped mass through ℓ)
    m_{>r}   = Σ_{C: top(C)>r} w_{top(C)} Γ(G_C)/G_C                   (damped mass beyond r)
    ν_{>r}(P) = Σ_{C: P⊆primes(G_C), top(C)>r} w_{top(C)} Γ(G_C) Π_{p∈P}p^{v_p(G_C)}/G_C
                                     (… through the prime set P, their factors removed; ν_{>r}(∅) = m_{>r})
    Λ_{>ℓ}   = Σ_{q>ℓ} E_{Q′^{(ℓ)}}[p_q 1{p_q > δ_q}]                   (leak beyond ℓ)

`Q′^{(ℓ)}` is Q′ with the ℓ-kernel replaced by the uniform law; its kernels
are all `≤ (1−δ)^{−1}U`, so K2's chain rule `P(x ≡ b (m)) ≤ Γ(m)/m` holds
for it, also conditionally on the past (as for Q′).

**Theorem 5.1 (single rough prime, fixed fibre; PROVED).** Let
`S = supp θ = {ℓ}` and let w be non-increasing in q. Then

    |σ̂_tilt(θ)| ≤ Z^{−1} [ 4E_{Q′}p_ℓ + 8Λ_{>ℓ} + 8μ̄(ℓ)
                  + 64 Σ_{C∋ℓ, top(C)>ℓ} (Γ(G_C)/G_C)·Σ_{P⊆primes(G_C)} ν_{>top(C)}(P) ].

*Proof.* Two corners, paths `x` (value v at ℓ) and `x′` (value v′),
equal below ℓ; each has law `Q′^{(ℓ)}`. `Ψ = H·g_ℓ·e^{−2Y}` with
`g_ℓ ≤ 2` the same on both corners, so by (2.1)
`|σ̂| ≤ Z^{−1}E|Ψ(x) − Ψ(x′)| ≤ Z^{−1}E[2·1[H(x)≠H(x′)] + 2min(1, 2|Y(x)−Y(x′)|)]`.
*Hard part.* `H(x) ≠ H(x′)` needs `v ∈ F_ℓ` or `v′ ∈ F_ℓ` (probability
`≤ 2E p_ℓ`, `F_ℓ` depends on the common past) or a leak beyond ℓ in x or
x′; given the past a leak at q has probability
`(p_q−p̃_q)/(1−p̃_q) ≤ 2p_q1{p_q>δ_q}`. So `P ≤ 2Ep_ℓ + 4Λ_{>ℓ}`.
*Soft part.* Let τ be the least element of 𝒟 (∞ if none). For tops
`q ≤ τ` the paths agree off ℓ on all coordinates `< q`, so
`|p̃_q(x) − p̃_q(x′)| ≤ Σ q^{−v_q(G_C)}` over the *direct* classes C ∋ ℓ with
top q matched off-top by x or x′; for `q > τ` use `p̃_q(x) + p̃_q(x′)`.
Hence `|Y(x) − Y(x′)| ≤ V_dir + 1[τ<∞](Y_{>τ}(x) + Y_{>τ}(x′))`, with
`V_dir = Σ_{C∋ℓ}w_{top}top^{−v}1[C matched off-top by x or x′]`, and
`E V_dir ≤ 2μ̄(ℓ)` by the chain rule (`P(C matched off-top) ≤
Γ(G_C)top^{v}/G_C`). Next, by Lemma 3.1(i),(ii) and the minimality of τ,
`τ = r` requires a direct class C ∋ ℓ with top r, matched off-top by x or
x′, and a coin event at r of conditional probability
`≤ 2U(F^∪_r∖F^∩_r) ≤ 4Σ_C r^{−v_r(G_C)}` (truncation changes `F̃` by at most
twice the change of F). Conditioning on everything up to r, the chain rule
gives `E[Y_{>r}(x) | 𝓕_{≤r}] ≤ Θ_r(x_{≤r})`,
`Θ_r(y) = Σ_{C′: top q>r} w_q q^{−v′}·1[y matches C′ at its primes < r]·
Γ(G′_{(r,q)})/G′_{(r,q)}` (`G′_{(r,q)}` = the part of `G_{C′}` at primes in
`(r, q)`; the factor at r itself is dropped). Hence
`E[1{τ=r}Θ_r(x_{≤r})] ≤ Σ_{C∋ℓ, top r}4r^{−v}Σ_{C′}a_{C′}·
P(C matched off-top by x or x′, x matches C′ below r)`, and the last
probability is `≤ 2Γ(L)/L`, `L` the lcm of the two congruence moduli (one
congruence class if compatible, else 0; when the ℓ-conditions fall on
different corner values v, v′ the probability is even smaller). Let
`P₀` be the set of primes `< r` shared by `G_C` and `G_{C′}`. Since
`lcm(a,b) ≥ a·b_{P₀^c}` (b's part at primes not dividing a),
`Γ(L)/L ≤ Γ(G_C)r^{v}G_C^{−1}·Γ(G′_{<r})Π_{p∈P₀}p^{v_p(G_{C′})}/G′_{<r}`;
multiplying by `a_{C′}` (whose r-factor was dropped) and summing over
C′ with given `P₀` and given `[r | G_{C′}]` gives at most
`ν_{>r}(P₀)` resp. `ν_{>r}(P₀∪{r})`. So
`E[1{τ=r}Θ_r(x_{≤r})] ≤ 8Σ_{C∋ℓ, top r}(Γ(G_C)/G_C)Σ_{P⊆primes(G_C)}ν_{>r}(P)`,
the same for `x′`, and
`E[1{τ=r}min(1, 2Y_{>r}(x) + 2Y_{>r}(x′))] ≤ 32·Σ_{C∋ℓ, top r}(…)`.
Collect: `2E min(1,2|ΔY|) ≤ 4EV_dir + 2Σ_r 32(…)`. ∎

*Remarks.* (a) **Uniformity in X.** Every outside top enters weighted by
`w_q`: directly in `μ̄(ℓ)`, and after a divergence through the damped
tails `m_{>r}`, `ν_{>r}(p)`, which only see tops `> r ≥ top(C)`. The undamped
witnesses `(−4D, ℓq)` of the LS5 caveat now contribute
`Σ_q w_q/(ℓq)·φ(4D)^{−1}`, a convergent sum. With the undamped weights
(`w ≡ 1`) the right side would diverge with X exactly as in LS5 §4.
(b) **No residue information is used**: the bound involves only first
moments of class masses through a prime (with the prime's own factor
removed). Labels, residue-density and the (CC) count are irrelevant for
one rough prime — they enter only through coincidences *between* S-primes
(§6).
(c) The divergence cascades of the coin coupling (which for huge X are
supercritical in *undamped* mass, `(4/r)Σ_{C∋r}rΓ/G_C` can exceed 1) are
harmless here: after the first divergence everything is bounded by the
damped tail `Y_{>τ}`, whose conditional mean is a first moment.

**What the arithmetic must supply (Assessment).** For Theorem 5.1 to give
`|σ̂_c(θ)| ≤ Z_c^{−1}·ℓ^{−1}(log N)^{O(1)}γ^{−O(1)}` uniformly in X one needs, for
the fibre at typical c (on average over c, plus a second moment over c for
the exceptional event, as in LS4 Thm 5.2's `E₁`):
* (FM1) `E p_ℓ ≤ (log ℓ)^c/ℓ` and `Λ_{>ℓ} ≤ Cℓ^{−1/4}(log ℓ)^c` — K2 (Q4),
  Lemma 4.3 (proved there, on average over c).
* (FM2) the damped mass through ℓ with polylog weights:
  `Σ_{C∋ℓ, top(C)>ℓ} w_{top}Γ(G_C)2^{ω(C)}(log top)^{A}/G_C ≤ C_A ℓ^{−1}·(γβ)^{−O(1)}`,
  and for every set P of primes `≤ r`: `ν_{>r}(P) ≤ C w_r (log r)^{A}(γβ)^{−1}`.
  Partial summation reduces (FM2) to "mass through a fixed prime p with
  top q" bounds `Σ_{C∋p, top(C)=q}Γ(G_C)p^{v}/G_C ≤ (log q)^{c}/q` **on average
  over q** — for ℛ(M) this is `Σ_q(w_q/q)·avg_m τ(A²_{pqm})` with
  `A = (pqm+1)/4`, i.e. Shiu in progressions mod `pq` for long cofactors m
  (as K2 Lemma 3.2) and a Titchmarsh-divisor upper bound over the **prime**
  q for short m (Brun–Titchmarsh plus Landreau's small-divisor domination,
  K2 Lemma 3.4). *Pointwise* divisor bounds `τ(A²) ≤ A^{o(1)}` do **not**
  suffice here: summed over all outside tops with weight `w_q/q` they
  diverge for `log log X ≫ (log N)^{1/4}/γ`. (FM2) is standard in nature
  but not written out here.
Granting (FM1)–(FM2): `|σ̂_c(θ)| ≤ Z_c^{−1}C(γ)(log N)^{C}ℓ^{−1}` for every θ
with one rough prime, and since `Z_c^{−1}` is free (Lemma 1.1), (A\*) holds
for all θ with `|supp θ_r| = 1` at any rate `γ < 1/2` (the second-moment
Markov step over c needs `Σ_ℓ ℓ^{2γ−2} < ∞`). By LS4 Thm 4.2 Remark (b),
this would give the all-level 3/4 cap for every forced mixture and every
large sieve **whose frequencies have at most one prime factor `> z` in
their denominators** (CONDITIONAL on (FM2) and its second moment over c).

## 7. Numerics (EVIDENCE / sanity checks only)

`scripts/largesieve6_softpivotal_toy.py`: random rough families (40
classes, moduli with 1–3 primes) over the pool {3, 5, 7, 11, 13},
truncated forbidding with `δ = 1/2`, random `w_q ∈ [0.2, 0.9]`, the exact
tilted law by enumeration of all 15015 points; for every S with `|S| ≤ 3`
the exact `max_{supp θ=S}|σ̂(θ)|` is compared with Monte-Carlo estimates
(3000 coin/v/v′ samples) of the right sides of (2.1), Prop 2.2 and
Prop 4.2 (first form (4.1), XOR covers enumerated exactly). Seeds 1–5:
max ratio exact/bound = 0.81 for (2.1) (the pinned representation is
nearly tight), `4.9·10⁻²` for Prop 2.2, `1.5·10⁻¹` for Prop 4.2 — all
inequalities hold, and the Walsh form is ~3× sharper than the partition
form on these toys. (Toy scale only: tiny primes, large activated masses.)

## Replay

    ulimit -v 8000000
    timeout 1800 env PYTHONPATH=scripts uv run python scripts/largesieve6_softpivotal_toy.py 1 2 3 4 5
