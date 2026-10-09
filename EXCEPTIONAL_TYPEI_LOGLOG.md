# EXCEPTIONAL_TYPEI_LOGLOG — attacking ET's open Type I bound Σ_{p≤N} f_I(p) ≪ N log² N (task O111)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`);
MN3 = `EXCEPTIONAL_MN3.md` (§3 there: the obstruction region R_bad / R**, Lemma 3.1, Thm 3.8);
DI = Deshouillers–Iwaniec, Invent. Math. 70 (1982) 219–288. `L = log N`.

## 0. Summary

* **Main result — Theorem 8.1 (CONDITIONAL on Selberg's eigenvalue conjecture (SEL) for the congruence
  groups `Γ₀(M)` with even nebentypus mod `2q`, `M = 4dq²`):** `Σ_{p≤N} f_I(p) ≪ N log² N`. This is ET's
  conjectured (OPEN-I). Proof: §§2–8. After the hostile review R111 (outline; gaps D1–D3) the O112 repair
  round wrote the missing steps (§8.0 Lemmas 8.2–8.4; §8 (2b) with the strip `β > 1`; Props 5.1, 7.1 at proof
  level): the proof is now complete **relative to cited results** (list at the end of §8), CONDITIONAL on (SEL),
  and awaits a round-2 review.
* **Unconditionally** the same argument removes the obstruction everywhere except on a strip
  `0 < 2α − 1 + γ ≲ 7/32 ≈ 0.22` (`≥ 0.16` even for the smallest cusp parameters in R_bad; O112 repair, D4)
  next to `d = a` (`a = N^α`, `c = N^γ`), where exceptional eigenvalues
  (Kim–Sarnak 7/64) beat the saving. A strip of positive width still costs `log log N`, so **this argument gives no unconditional
  improvement** of ET's bound (§9); nothing is claimed about other arguments.
* New ingredients. (i) Lemma 2.2 (PROVED, elementary): the level-d Heegner points of MN3 Lemma 3.1 are
  **uniformly separated** in ℍ: distinct points have `cosh dist ≥ 3/2`, for every d (because
  `4d | disc(Q−Q')`). (ii) Prop 4.3 (PROVED): with separation, `|Σ_z P(z) − #Λ·⟨P⟩| ≪ (#Λ)^{1/2}‖(1−Δ)P₀‖₂`,
  uniformly in the group. (iii) Prop 5.1 (under SEL, via the Deshouillers–Iwaniec/Drappeau spectral large
  sieve; for `Y ≤ λ𝓛^{−3}`): the box Poincaré series has variance `≪ 𝓛^C(area·(1 + q^{1/2}M^{−1}(𝓛/λ)^{1+ε}) + λ²/Y)`, i.e. area plus a cusp term
  `≈ q^{1/2}/(MY)` (O112, D9: unified with Prop 5.1). (iv) So the per-d
  relative error is `≈ (d/a)^{1/2}`, and MN3's per-a Weil count (K_a) has relative error `≈ a/d`: the two
  are **complementary at exactly d = a**, and Lemma 1.1 shows that a saving that degenerates linearly at a
  boundary costs only `O(N log² N)`.
* MN3's (H**) is more than needed. Fine-scale equidistribution of the `≈ d^{1/2}` Heegner classes on
  `X₀(d)` (volume `≍ d`) cannot hold at scales below `d^{1/2}`. MN3's lift-counting form is not refuted by
  this (R1), but only the second moment of the lift-counting function enters here.
* Literature (2026-10, search-limited): no removal of ET's `log log N` was found. ET v6 cites Jia
  (Sci. China Math. 55 (2012) 465–474) and still calls the Type I `log log` open. No joint level–discriminant
  equidistribution with level ≍ |D| exists (Liu–Masri–Young reach `q ≤ |D|^{1/20}`). No result on
  `Σ_a S(h,k;a²)` or on divisor sums in APs to square moduli was found.
* EVIDENCE: `scripts/ttl_separation.py` (separation; min cosh ≥ 3 observed); `scripts/ttl_perd.py` (per-d
  errors are small, but R1 notes that its weight is normalised to about 20 and that its local-density main
  term is not the orbital main term of Thm 6.2: weak, sanity-level evidence only).

## 1. Set-up

For `c ≥ 1`, the Type I weight (MN3 §3.7) is
`w_c(n) = #{(a,d,f) ∈ ℕ³ : f | 4a²d+1, n = 4acd − f, n/4 < acd ≤ 3n/4}`, `f_I(p) ≤ 2Σ_c w_c(p)`.
Write `e = (4a²d+1)/f`, so `ef − 4a²d = 1`; MN3 Lemma 3.1: `M = [[e,2a],[2ad,f]] ∈ SL₂(ℤ)`.
Exponents for `n ≍ N`: `a = N^α`, `c = N^γ`, `d ≍ N^{1−α−γ}`, `e ≍ N^{β−γ}`, `f ≍ N^{1+α−β}`.
MN3 Thm 3.8 reduces (OPEN-I) to a level of distribution for `w_c`, `c ≤ N^{η₀}`; MN3 §3.4 locates the
difficulty at `α ≥ (1−γ)/2` (the (K_a) count — modular hyperbola `ef ≡ 1 (mod 4a²)` — has per-a error
`≍ a` against main term `≍ d`).

**Key accounting remark (Lemma 1.1 below).** A power saving that *degenerates linearly* at a boundary
(e.g. relative error `N^{−κ|α−1/2|}`) does **not** reintroduce `log log N`: only a positive-measure set of
cells with no power saving at all does.

**Lemma 1.1 (degenerate savings are harmless; PROVED, elementary).** Let `L ≥ 2`. For integers
`1 ≤ j, k ≤ L` let `m_{jk} ≥ 0` with `Σ_k m_{jk} ≤ M` for each j. Then
`Σ_{j,k≤L} m_{jk} min(1/j, 1/k) ≤ M·(1 + log L)` trivially, but if also `m_{jk} ≤ M/L` for all j, k, then
`Σ_{j,k} m_{jk} min(1/j,1/k) ≤ (M/L)·Σ_{j,k≤L} min(1/j,1/k) ≤ 2M`.
*Proof.* `Σ_{j,k≤L} min(1/j,1/k) = Σ_{m≤L} (2m−1)/m ≤ 2L`. ∎
*Use.* j indexes the dyadic c-block (`c ≍ 2^j`; BT gives saving `1/j`), k a dyadic distance from the bad
boundary (e.g. `a ≍ N^{1/2}2^{k}`, saving `≍ 1/k` once a level of distribution `N^{κ k/L}` is available);
`m_{jk} ≪ N log N` is the Type I mass of one (c-block, a-block) pair (ET (8.2) per dyadic box). The block
j = 0 (`c ≍ 1`, no BT saving) costs only `Σ_k NL·C/k ≪ NL log L` (O112, D12). So a
saving `min(1/j, 1/k)` costs `O(N log² N)` in total.

## 2. Separation of the level-d Heegner points

Fix `d ≥ 1`. Let `𝓕_d` be the set of integral binary forms `Q = [A, B, C] = AX² + BXY + CY²` with
`B² − 4AC = −4d`, `A > 0`, `B ≡ 0 (mod 2d)`, `C ≡ 0 (mod d)`. Each Type I quadruple gives
`Q = [f, 4ad, de] ∈ 𝓕_d` (disc `16a²d² − 4def = −4d`). Root map `z_Q = (−B + i√(4d))/(2A) ∈ ℍ`.

**Lemma 2.1 (distance formula; standard).** For positive definite forms Q, Q' of the same discriminant
`D < 0`: `cosh dist_ℍ(z_Q, z_{Q'}) = 1 + disc(Q − Q')/(2|D|)`.
*Proof.* `cosh dist(z,w) = 1 + |z−w|²/(2 Im z Im w)`. With `z = (−B+i√|D|)/2A`, `w = (−B'+i√|D|)/2A'`:
`|z−w|²·4AA' = (BA' − B'A)²/(AA') + |D|(A'−A)²/(AA')`, and `2 Im z Im w·4AA' = 2|D|`. So
`cosh − 1 = [(BA'−B'A)² + |D|(A−A')²]/(2|D|AA')`. Expanding `disc(Q−Q') = (B−B')² − 4(A−A')(C−C')`
with `4AC = B² + |D|`, `4A'C' = B'² + |D|`, `4AC' = A(B'²+|D|)/A'`, `4A'C = A'(B²+|D|)/A`, one gets
`AA'·disc(Q−Q') = (BA' − B'A)² + |D|(A − A')²`. ∎ (Checked numerically in `scripts/ttl_separation.py`.)

**Lemma 2.2 (uniform separation; PROVED).** For distinct `Q, Q' ∈ 𝓕_d`: `cosh dist(z_Q, z_{Q'}) ≥ 3/2`.
*Proof.* `B ≡ B' (mod 2d)` gives `4d² | (B−B')²`, and `C ≡ C' ≡ 0 (mod d)` gives `4d | 4(A−A')(C−C')`,
so `4d | disc(Q−Q')`. By Lemma 2.1 (|D| = 4d), `disc(Q−Q') = 8d(cosh − 1) ≥ 0`, so
`cosh − 1 ∈ ½ℤ_{≥0}`. If `cosh = 1` then `z_Q = z_{Q'}`; a positive definite form of discriminant D is
determined by its root (`Q = A(X − zY)(X − z̄Y)` and `B² − 4AC = D` fixes A), so `Q = Q'`. ∎
*Remark.* Only `B ≡ B' (2d)` and `d | C, C'` were used, so the lemma holds for any subset of 𝓕_d, e.g.
the forms with prescribed residues mod q (sieve conditions). Numerically (`ttl_separation.out.txt`)
the minimum over the enumerated pairs is `cosh ≥ 3`.

## 3. Strategy: per-d counts via Sobolev duality (outline; the rigorous lemmas follow in §§4–7)

**Coordinates.** For `Q = [f, 4ad, de] ∈ 𝓕_d` put `w_Q = z_Q/d = (−2a + i/√d)/f` (so `Im w = 1/(f√d)`,
`Re w = −2a/f`). `𝓕_d` is preserved by `Γ⁰(d)` acting by `Q ↦ Q∘γ` (check: if `d | γ₁₂` then
`C' = Q(γ₁₂, γ₂₂) ≡ 0 (d)` and `B' ≡ B (2d)`), i.e. the points `w_Q` form a `Γ₀(d)`-invariant subset
of ℍ, uniformly separated by Lemma 2.2 (distances are unchanged by `z ↦ z/d`). Write `Λ_d` for the
(finite) set of `Γ₀(d)`-classes. A smooth box `a ~ A`, `f ~ F` (weights `w₁(a/A) w₂(f/F)`) is a function
`ψ(w) = w₁(−Re w/(2A Im w √d)) w₂(1/(F√d Im w))` on `Γ_∞\ℍ`, supported in a horocyclic strip of height
`Y ≍ 1/(F√d)` and width `λ ≍ A/F` (one period if `A ≤ F/8`). It is smooth on the hyperbolic scale 1
(`y∂_x ψ ≪ Y/λ`, `y∂_y ψ ≪ 1`). Hyperbolic area `∫ψ dμ ≍ λ/Y ≍ A√d`. The count is
`N_d(ψ) = Σ_{Q ∈ 𝓕_d / Γ_∞} ψ(w_Q) = Σ_{z ∈ Λ_d} P_ψ(z)`, `P_ψ = Σ_{γ∈Γ_∞\Γ₀(d)} ψ∘γ`.

**Sobolev duality.** `N_d(ψ) = (#Λ_d / vol) ∫ψ dμ + Σ_{z∈Λ_d} P₀(z)` with `P₀ = P − ⟨P⟩`, and
`|Σ_z P₀(z)| ≤ ‖(1−Δ)P₀‖₂ · ‖Σ_z δ_z‖_{H^{−2}}`. By separation (Lemma 2.2) the second factor is
`≪ (#Λ_d)^{1/2}` uniformly in d (the kernel of `(1−Δ)^{−2}` is bounded and decays like `e^{−1.618 r}`,
while a separated set has `≪ e^R` points in a ball of radius R). The first factor is the standard
deviation of an incomplete Poincaré series. By unfolding plus the DI large sieve (DI Thm 2; `μ(∞) = 1/d`)
it is `≪ (λ/Y)(1 + N₀/d) + λ²/Y` up to polylog factors, with `N₀ = 1/λ = F/A` the number of Fourier modes,
**provided there are no exceptional eigenvalues** (otherwise there is an extra factor `≈ Y^{−2σ_j}` on the
exceptional part; DI Thm 5 controls it only partially, see §3.2).

**Heuristic outcome.** `#Λ_d ≈ d^{1/2}` (class numbers), so
`N_d = main + O((Ad + F)^{1/2})` against `main ≍ A`: a power saving iff `d < A^{1−ε}` and `F < A^{2−ε}`
(or the same with e for f, via the Fricke involution `w ↦ −1/(dw)`, which maps `w_Q` to `(2a + i/√d)/e`).
With `a = N^α`, `d ≍ N^{1−α−γ}`: this is `α > (1−γ)/2` — exactly complementary to MN3's (K_a)
(`α < (1−γ)/2`). Together with the trivial count when a divisor is below `A^{1−ε}` (a then runs over
complete residue systems), **every cell is covered, with a saving that degenerates only linearly at
`α = (1−γ)/2`** — harmless by Lemma 1.1. Weak sanity check only (see §0): `scripts/ttl_perd.py`.

### 3.2 The obstruction: exceptional eigenvalues (Assessment, to be made precise)
If `Γ₀(d)` (or the sieve group `Γ₀(d) ∩ Γ(q)`) has an exceptional eigenvalue `λ_j = 1/4 − σ_j²`, then
`⟨P_ψ, u_j⟩` picks up a factor `(nY)^{−σ_j}` from `K_{σ}(2πny) ≈ (πny)^{−σ}Γ(σ)/2`. With Kim–Sarnak
(`σ ≤ 7/64`) the loss is `Y^{−7/64} = (qF'√d)^{7/64}`, which beats the saving `(d/A)^{1/2}` on a strip
`0 < 2α − 1 + γ ≲ 7/32` of positive width (worst cells: `1/Y = qF'√d ≍ N`, loss `N^{7/64}` against the
saving `N^{−δ/2}`; `≥ 21/128 ≈ 0.16` for the smallest `F' ≥ N^{1/2−3η₁}` — O112 repair, D4), so the strip
would still cost `log log N` in this argument. DI Thm 5
(`Σ_exc X^{2σ_j}|Σ a_nρ_j(n)|² ≪ (1+√(μNX))(1+√(μN^{1+ε}))‖a‖²`, checked on the scan of DI p. 232) with
`X = 1/(N₀Y)` applied per dyadic n-block `n ≍ N₀` (the weight is `(nY)^{−2σ}`; O112 repair, D4: not `X = 1/Y`)
gives an extra variance factor `≈ 1 + (F'/(q√d))^{1/2}` (`μ = 1/M`, `M = 4dq²`), and DI Thm 6 (average over
the level) an extra factor
`F^{3/4}D^{1/8}/A` on average over `d ≍ D` (DI Thm 6 bookkeeping not re-checked by the review), which still
fail near `α = 1/2`. **So the plan gives (OPEN-I)
conditionally on Selberg's eigenvalue conjecture for congruence subgroups.** Unconditionally it would
need either a density estimate for exceptional eigenvalues with these weights, or a beyond-Weil bound for
`Σ_a S(h,k;4a²)` on the (K_a) side.

## 4. Sobolev duality with separated points (PROVED)

Notation: `Δ = y²(∂_x² + ∂_y²)` (so `−Δ ≥ 0`), `dμ = dx dy/y²`, `Γ' ⊂ SL₂(ℤ)` of finite index,
`⟨F,G⟩ = ∫_{Γ'\ℍ} F Ḡ dμ`, `V = vol(Γ'\ℍ)`. For a finite Γ'-invariant set `Λ̃ ⊂ ℍ` let
`ν_Λ = Σ_{z ∈ Γ'\Λ̃} δ_z / e_z` with `e_z = |Γ'_z/(Γ'∩{±1})|` (the orbifold weight), and
`#Λ := Σ_{z∈Γ'\Λ̃} 1/e_z`.

**Lemma 4.1 (the kernel of (1−Δ)^{−2}; standard).** There is a radial `g = g(r) ≥ 0` on ℍ,
continuous, with `g(r) ≪ (1+r) e^{−φ r}`, `φ = (1+√5)/2`, such that for every `Γ'` the operator
`(1−Δ)^{−2}` on `L²(Γ'\ℍ)` has kernel `K(z,w) = Σ_{γ∈Γ'} g(dist(z, γw))` (absolutely convergent).
*Proof.* The Selberg/Harish-Chandra transform pair: `h(t) = (5/4 + t²)^{−2}` (since `−Δ` has eigenvalue
`1/4 + t²` on `y^{1/2+it}`) is even, holomorphic in `|Im t| < √5/2`, and `∫|h(t)| t dt < ∞`, so its
point-pair invariant `k = g` is continuous and bounded, `g(0) = (4π)^{−1}∫ h(t) t tanh(πt) dt`
(Iwaniec, *Spectral methods*, §1.8, (1.62)–(1.64)). Since `h` has its first poles at
`t = ±i√5/2` (of order 2), contour shift in the inversion formula gives
`g(r) ≪ (1+r)e^{−(1/2 + √5/2) r}`. As `#{γ ∈ Γ' : dist(z,γw) ≤ R} ≪_{z,w} e^R` and `φ > 1`, the
automorphic kernel converges absolutely and is the kernel of `h(√(−Δ−1/4)) = (1−Δ)^{−2}`
(Iwaniec, Thm 1.14 / pre-trace formula). ∎

**Lemma 4.2 (H^{−2} norm of a separated set; PROVED).** If any two distinct points of `Λ̃` are at
hyperbolic distance `≥ r₀ > 0`, then `⟨ν_Λ, (1−Δ)^{−2} ν_Λ⟩ ≤ C(r₀) · #Λ`, with `C(r₀)` independent
of `Γ'` and of `Λ̃`.
*Proof.* Unfolding one variable, `⟨ν,(1−Δ)^{−2}ν⟩ = Σ_{z∈Γ'\Λ̃} e_z^{−1} Σ_{w ∈ Λ̃} g(dist(z,w))`
(each `w ∈ Λ̃` is hit by `|Γ'_w ∩ …|` group elements, which cancels the weight `e_w^{-1}`; the
`±1` ambiguity is the same on both sides). The balls `B(w, r₀/2)`, `w ∈ Λ̃`, are disjoint, and those with
`dist(z,w) ≤ R` lie in `B(z, R + r₀/2)`, so their number is `≤ area B(z,R+r₀/2)/area B(·,r₀/2)
≪_{r₀} e^{R}`. Hence `Σ_w g(dist(z,w)) ≪_{r₀} Σ_{R≥0} (1+R) e^{(1−φ)R} ≪ 1`. ∎

**Proposition 4.3 (duality; PROVED).** Let `P ∈ C^∞(Γ'\ℍ)` with `P, ΔP, Δ²P ∈ L²`, put
`⟨P⟩ = V^{−1}∫P dμ`, `P₀ = P − ⟨P⟩`. Under the hypothesis of Lemma 4.2,
`|Σ_{z∈Γ'\Λ̃} P(z)/e_z − #Λ·⟨P⟩| ≤ C(r₀)^{1/2} (#Λ)^{1/2} ‖(1−Δ)P₀‖₂`.
*Proof.* `ν(P₀) = ⟨(1−Δ)P₀, (1−Δ)^{−1}ν⟩` (self-adjointness; `(1−Δ)^{−1}ν ∈ L²` because its norm
squared is `⟨ν,(1−Δ)^{−2}ν⟩ < ∞`), then Cauchy–Schwarz and Lemma 4.2. ∎

**Corollary 4.4 (application to 𝓕_d).** Let `Γ' ⊂ Γ₀(d)` (acting on `w = z/d`) and `𝓕 ⊂ 𝓕_d`
`Γ'`-invariant, `Λ̃ = {w_Q : Q ∈ 𝓕}`. Lemma 2.2 gives `r₀ = arccosh(3/2)` (the map `z ↦ z/d` is an
isometry), so Prop 4.3 holds with an absolute constant. If `Γ'_∞ = ⟨±[[1,h],[0,1]]⟩` and
`P = P_ψ = Σ_{γ∈Γ'_∞\Γ'} ψ∘γ` with `ψ` supported in a strip of x-length `< h`, then
`Σ_{z∈Γ'\Λ̃} P_ψ(z)/e_z = Σ_{Q ∈ 𝓕/Γ'_∞} ψ(w_Q)` (unfolding; `Q ↦ w_Q` is injective because a positive
definite form of given discriminant is determined by its root), and `⟨P_ψ⟩ = V^{−1}∫_{Γ'_∞\ℍ} ψ dμ`.

## 5. Variance of the box Poincaré series (PROVED conditional on (SEL); standard spectral input)

**Groups (O112 repair, D9: one normalisation throughout, the one forced by the parity of §6).** Let `d ≥ 1`,
`q` squarefree, `(q, 2d) = 1`. On the `w`-side the Type I set with the sieve condition `q | n`
(`n = cB − A` for `Q = [A,B,C] = [f,4ad,de]`, i.e. `n = 4acd − f`) is invariant under
`Γ' := Γ₀(2d) ∩ Γ(2q)` (§6 'Parity'; if `γ ≡ ±I (q)` then `Q∘γ ≡ Q (q)`). Conjugating by `u = w/(2q)` turns it
into `Γ'' = {±[[p,t],[r,s]] ∈ Γ₀(M) : p ≡ s ≡ 1 (2q)} ⊇ Γ₁(M)`, `M = 4dq²`, whose cusp ∞ has width 1, and
`Γ₀(M)/±Γ'' ≅ (ℤ/q)^×/±1`, so `L²(Γ''\ℍ) = ⊕_{χ mod q, χ(−1)=1} L²(Γ₀(M)\ℍ, χ)` (weight 0, nebentypus χ;
characters mod 2q and mod q coincide, q odd). In `u`-coordinates `u_Q = (−2a + i/√d)/(2qf)`.

**Hypothesis (SEL).** For all `M, q` as above and all even χ mod q, the Laplacian on
`L²(Γ₀(M)\ℍ, χ)` has no eigenvalue in `(0, 1/4)` (Selberg's eigenvalue conjecture for these congruence
groups; known unconditionally only with `λ₁ ≥ 975/4096` (Kim–Sarnak), which is **not** enough here, §3.2).

**Spectral large sieve (cited).** DI Thm 2 (trivial χ) and Drappeau, Proc. LMS 114 (2017),
arXiv:1504.05549, Prop 4.7 in §4.2.2 (arXiv numbering; published numbering not checked; O112, D7)
(nebentypus χ of conductor `q₀ | q`): for `K ≥ 1`, `N₀ ≥ 1/2`,
`Σ_{|t_j|≤K} |Σ_{N₀<n≤2N₀} a_n ρ_j(n)|²/cosh(πt_j)` and the analogous Eisenstein integrals over all
singular cusps are `≪_ε (K² + q₀^{1/2} M^{−1} N₀^{1+ε}) ‖a‖²` (`μ(∞) = 1/M`; ρ_j the Fourier
coefficients at ∞ of an orthonormal basis of `L²(Γ₀(M)\ℍ, χ)`, normalised as in DI (1.34)).
(Drappeau's normalisation carries `√n ρ(n)` and a weight `(1+|t|)^{±κ}`; the difference is immaterial
for dyadic n and bounded K. Not re-derived here.)

**Test functions.** Use cells that are smooth in `(Re u, Im u)` directly:
`ψ(u) = φ(x/λ) W(y/Y)`, `φ, W ∈ C_c^∞`, `supp φ ⊂ [−2,−1]`, `supp W ⊂ [1,2]`, `0 < λ ≤ 1/4`, `Y ≤ λ 𝓛^{−3}` (R1: the proposition is false without a bound on `Y/λ`; in all
applications `Y/λ ≍ 1/(A√d)`).
(In the original variables this is `f ≍ F := 1/(qY√d)` and `a/f ≍ λq/2`: a smooth partition of unity in
`(log f, log(a/f))` is as good as one in `(log f, log a)` for the sieve.) Its hyperbolic area is
`∫ψ dμ ≍ λ/Y`.

**Proposition 5.1 (variance; PROVED conditional on (SEL) and the cited DI/Drappeau large sieve; O112: proof written in full).** Let
`P = P_ψ` on `Γ_{M,q}`, `P₀ = P − ⟨P⟩`, and `𝓛 = log(2 + 1/(λY) + M)`. Then
`‖(1−Δ)P₀‖₂² ≪_{φ,W,ε} 𝓛^{C} · [ (λ/Y)(1 + q^{1/2} M^{−1} (𝓛/λ)^{1+ε}) + λ²/Y ]`,
with `L²` norms on `Γ_{M,q}\ℍ`.
*Proof (O112 repair: written at proof level; replaces the R1 outline, and settles D8).*
**Step 0 (reductions).** `P_ψ` is smooth, bounded, and vanishes high in every cusp (in ∞ only `γ = 1` contributes
and `ψ = 0` for `y > 2Y`; at other cusps `Im γσ_𝔞z ≤ 1/(c²y) → 0`), so `P_ψ, ΔP_ψ, Δ²P_ψ ∈ L²`.
`(1−Δ)P_ψ = P_{ψ'}`, `ψ' = (1−Δ)ψ = φ(x/λ)W̃(y/Y) − (Y/λ)²φ''(x/λ)W₂(y/Y)`, `W̃ = W − v²W''`, `W₂ = v²W`,
and `∫Δψ dμ = 0`, so `(1−Δ)P₀ = P_{ψ'} − ⟨P_{ψ'}⟩`. As `Y ≤ λ`, it suffices to prove
`‖P_ψ − ⟨P_ψ⟩‖² ≪ 𝓛^C[(λ/Y)(1 + q^{1/2}M^{−1}(𝓛/λ)^{1+ε}) + λ²/Y]` for `ψ = φ(x/λ)W(y/Y)` with `φ ∈ C_c^∞([−2,−1])`,
`W ∈ C_c^∞([1,2])` arbitrary, the constant depending on finitely many derivatives of φ, W.
**Step 1 (spectral decomposition).** With `P_χ := Σ_{γ∈Γ_∞\Γ₀(M)} χ̄(γ)ψ∘γ` one has `P_ψ = (2/φ(q))Σ_χ P_χ` and
`‖P_ψ − ⟨P_ψ⟩‖²_{Γ''} = (2/φ(q))Σ_{χ even} ‖P_χ − δ_{χ=1}⟨P_1⟩‖²_{Γ₀(M),χ}` (orthogonality of the χ-isotypic parts;
`[Γ₀(M):±Γ''] = φ(q)/2`). For each χ, Parseval in `L²(Γ₀(M)\ℍ,χ)` (Iwaniec, *Spectral methods*, Thm 7.3; DI §1 for
nebentypus): `‖P_χ − δ⟨⟩‖² = Σ_j |⟨P_χ,u_j⟩|² + (4π)^{−1}Σ_𝔠 ∫_ℝ |⟨P_χ,E_𝔠(·,½+it,χ)⟩|² dt`, where `u_j` runs over an
orthonormal basis of Maass cusp forms (by (SEL) all `t_j ∈ ℝ`; the residual spectrum of a congruence group is the
constants, present only for χ = 1, and removed) and 𝔠 over the χ-singular cusps (∞ is singular for every χ).
**Step 2 (unfolding).** `u_j(z) = √y Σ_{n≠0} ρ_j(n)K_{it_j}(2π|n|y)e(nx)` (DI (1.34); cusp width 1). Since the
x-support of ψ has length `λ < 1`, `⟨P_χ,u_j⟩ = ∫_0^∞∫_0^1 ψ ū_j dx dy/y² = Σ_{n≠0} ρ̄_j(n) λφ̂(λn) I_{t_j}(n)`,
`I_t(n) := ∫_0^∞ W(y/Y) y^{1/2} K_{it}(2π|n|y) dy/y²`. Mellin: `K_{it}(x) = (4πi)^{−1}∫_{(σ)} G_t(s)(x/2)^{−s}ds`,
`G_t(s) := Γ((s+it)/2)Γ((s−it)/2)`, `σ > 0`; hence `I_t(n) = Y^{−1/2}(4πi)^{−1}∫_{(σ)} G_t(s)𝒲(s)(π|n|Y)^{−s}ds` with
`𝒲(s) := ∫_0^∞ W(v)v^{−3/2−s}dv`, entire, `|𝒲(σ+iv)| ≪_{B,σ} (1+|v|)^{−B}` uniformly for `|σ| ≤ 2`. Therefore
`⟨P_χ,u_j⟩ = Y^{−1/2}(4πi)^{−1}∫_{(σ)} G_{t_j}(s)𝒲(s)(πY)^{−s} B_j(s) ds`, `B_j(s) := Σ_{n≠0} ρ̄_j(n) b_n(s)`,
`b_n(s) := λφ̂(λn)|n|^{−s}` (absolutely convergent: `φ̂` is Schwartz, `ρ_j(n) ≪_j |n|^{1/2}`).
**Step 3 (Gamma bounds; Stirling).** For `|Re w| ≤ 1`: `|Γ(w)| ≍ |Im w|^{Re w − 1/2}e^{−π|Im w|/2}` if `|Im w| ≥ 1`, and
`|Γ(w)| ≪ 1/dist(w, −ℕ₀)` if `|Im w| ≤ 1`. Hence (a) for `|t| ≤ 1`, `s = σ₀ + iv`, `σ₀ := 1/𝓛`:
`|G_t(s)| ≪ 𝓛²e^{−π|v|/2}`; (b) for `|t| ≥ 1`, `s = −1 + iv` (distance `≥ 1/2` from all poles):
`|G_t(s)| ≪ e^{−π|t|/2}(1+|t|)^{−2}(1+|v|)^{4}` (if `|v| ≤ |t|/2` both `|v ± t| ≍ |t|`; otherwise use
`e^{−π max(|v|,|t|)/2} ≤ e^{−π|t|/2}` and `1+|t| ≤ 3(1+|v|)`).
**Step 4 (|t_j| ≤ 1).** Take `σ = σ₀`. Since `1/Y ≤ e^{𝓛}`, `|(πY)^{−s}| ≤ e`; Cauchy–Schwarz in v with the measure
`|G𝒲|dv` and (a): `|⟨P_χ,u_j⟩|² ≪ Y^{−1}𝓛⁴ ∫|𝒲(σ₀+iv)| |B_j(σ₀+iv)|² dv`.
**Step 5 (|t_j| ≥ 1).** Shift to `σ = −1`, crossing only the simple poles `s = ±it_j` (residue of `Γ((s∓it)/2)` is 2):
`⟨P_χ,u_j⟩ = Y^{−1/2}[Σ_± Γ(±it_j)𝒲(±it_j)(πY)^{∓it_j}B_j(±it_j) + (4πi)^{−1}∫_{(−1)} G_{t_j}(s)𝒲(s)B̃_j(s)ds]`, with
`B̃_j(s) := Σ ρ̄_j(n) b̃_n(s)`, `b̃_n(s) := (πY)^{−s}b_n(s)`, `|b̃_n(−1+iv)| = πY|n|·λ|φ̂(λn)|`. Using
`|Γ(it)|² = π/(t sinh πt) ≪ 1/((1+|t|) cosh πt)`, `|𝒲(±it)| ≪ (1+|t|)^{−B}` and (b) with Cauchy–Schwarz:
`|⟨P_χ,u_j⟩|² ≪ Y^{−1}cosh(πt_j)^{−1}[(1+|t_j|)^{−B}Σ_±|B_j(±it_j)|² + (1+|t_j|)^{−4}∫|𝒲(−1+iv)|(1+|v|)^4|B̃_j(−1+iv)|²dv]`.
**Step 6 (large sieve).** Let `𝒮(K; b) := Σ_{|t_j|≤K} cosh(πt_j)^{−1}|Σ_n ρ̄_j(n)b_n|²`. Split n into `±` and dyadic
blocks `N₀ < |n| ≤ 2N₀` (`N₀ = 2^i/2`, i ≥ 0; negative n via the reflection `z ↦ −z̄`, which maps an orthonormal basis of
`L²(Γ₀(M),χ)` onto one of `L²(Γ₀(M),χ̄)`, χ̄ also even). Cauchy–Schwarz over blocks with weights `w_{N₀} := 1 + |log(λN₀)|`
(`Σ_{N₀} w_{N₀}^{−2} ≪ 1`) and DI Thm 2 / Drappeau Prop 4.7 per block give
`𝒮(K; b) ≪ Σ_{N₀} w_{N₀}²(K² + q^{1/2}M^{−1}N₀^{1+ε})‖b^{(N₀)}‖²`.
For `b = b(σ₀+iv)`: `‖b^{(N₀)}‖² ≪ λ²N₀ min(1,(λN₀)^{−2B})` (and `|n|^{−σ₀} ≤ 1`), so `𝒮(K; b) ≪ 𝓛²λ(K² + q^{1/2}M^{−1}λ^{−1−ε})`.
For `b̃(−1+iv)`: `‖b̃^{(N₀)}‖² ≪ (Y/λ)²·λ²N₀ min(1,(λN₀)^{−2B})`, the same bound times `(Y/λ)² ≤ 1`.
For the `t_j`-dependent vectors `b_n(±it_j)`: on each unit interval `t_j ∈ [k, k+1]` use
`|B(t)|² ≤ 2|B(k)|² + 2∫_k^{k+1}|∂_τB(τ)|²dτ` (Gallagher); `∂_τ` multiplies `b_n` by `∓i log|n|`, i.e. by
`≪ 𝓛 + |log(λ|n|)|`, absorbed by the rapid decay of φ̂. So
`Σ_{K<|t_j|≤2K} cosh^{−1}|B_j(±it_j)|² ≪ 𝓛⁴ λ(K² + q^{1/2}M^{−1}λ^{−1−ε})`.
**Step 7 (assembly).** Steps 4–6, summing dyadically over K with the weights `(1+K)^{−B}`, `(1+K)^{−4}` against `K²`, and
integrating in v against `|𝒲|(1+|v|)^4`: `Σ_j |⟨P_χ,u_j⟩|² ≪ 𝓛^C Y^{−1}λ(1 + q^{1/2}M^{−1}λ^{−1−ε})`.
*Eisenstein part.* The n ≠ 0 terms are identical with `ρ_j(n)` replaced by `φ_𝔠(n,t)` and `Σ_j` by `Σ_𝔠(4π)^{−1}∫dt`; the
cited large sieves include this part. The constant term `δ_{𝔠∞}y^{½+it} + φ_{𝔠∞}(½+it)y^{½−it}` contributes
`λφ̂(0)Y^{−1/2}[δ_{𝔠∞}Y^{−it}𝒲(it) + φ̄_{𝔠∞}Y^{it}𝒲(−it)]`; by unitarity of the scattering matrix
(`Σ_𝔠 |φ_{𝔠∞}(½+it)|² = 1`) its total is `≪ λ²Y^{−1}∫(|𝒲(it)|² + |𝒲(−it)|²)dt ≪ λ²/Y` per χ.
Summing over the `φ(q)/2` even χ (conductor `q₀ ≤ q`) and multiplying by `2/φ(q)` gives the claim, with
`λ^{−1−ε}` written as `(𝓛/λ)^{1+ε}`. ∎
*Remark.* `(λ/Y)·q^{1/2}M^{−1}λ^{−1} = q^{1/2}/(MY) = F/(2q^{1/2}√d)` (since `1/Y = 2qF√d`, `M = 4dq²`):
this is the "cusp" term `1/(Y·level)` of §3.

## 6. Per-d counts with the sieve congruence (conditional on (SEL))

**Parity.** The Type I forms are `𝓕_d^I := {[f, 4ad, de] : ef − 4a²d = 1, e,f > 0, a ∈ ℤ}`
(`B ≡ 0 (mod 4d)`), a subset of 𝓕_d that is not `Γ₀(d)`-stable (MN3 Lemma 3.1, R108). It **is** stable
under `Γ₀(2d) ∩ Γ⁰(2)` (w-side; R1: *not* `Γ₀(d)∩Γ(2)` when d is even — e.g. d = 2,
`[[1,0],[2,1]]` maps `[1,8,18]` to a form with `B = 44`): with `γ_z = [[p,t],[r,s]] ∈ Γ⁰(2d) ∩ Γ₀(2)` (z-side),
`B' = 2Apt + B(ps+tr) + 2Crs ≡ 0 (4d)` because `2d | t`, `4d | B`, `C = de`, `2 | r`. So take
`Γ' := Γ₀(2d) ∩ Γ(2q)` (w-side) and `u = w/(2q)`: `u_Q = (−2a + i/√d)/(2qf)`, cusp width 1, and
`Γ'' ⊇ Γ₁(M)` with `M = 4dq²` (§5); (SEL) and the large sieve are applied to `Γ₀(M)` with even characters mod `q`.

**Local densities.** For a prime `ℓ ∤ 2d` put
`g_{c,d}(ℓ) := #{(A,B,C) ∈ 𝔽_ℓ³ : B² − 4AC = −4d, cB − A = 0} / #{(A,B,C) : B² − 4AC = −4d}`,
and `g_{c,d}(q) = Π_{ℓ|q} g_{c,d}(ℓ)`. Then `g = (ℓ−1)/(ℓ² + χ(ℓ)ℓ)` if `ℓ ∤ c` (χ = `(−d/ℓ)`), and
`g = (1+χ(ℓ))/(ℓ + χ(ℓ))` (R1: the quadric has `ℓ² + χℓ` points) if `ℓ | c`. For `ℓ | 2d`, no n is divisible by ℓ (n is odd; if `ℓ | d` then
`n ≡ −f` and `f | 4a²d+1 ≡ 1 (ℓ)`), so those primes are not sieved.

**Lemma 6.1 (main term factorises; PROVED).** For `q` squarefree, `(q,2d) = 1`, let
`Λ̃(q) = {u_Q : Q ∈ 𝓕_d^I, q | cB − A}`, `#Λ(q)` its orbifold count mod `Γ'_q := Γ₀(2d)∩Γ(2q)`,
`V(q) = vol(Γ'_q\ℍ)` (w-side). Then `#Λ(q)/V(q) = g_{c,d}(q) · #Λ(1)/V(1)`.
*Proof.* As matrix groups `[Γ'_1 : Γ'_q] = |SL₂(ℤ/q)|` (strong approximation, `(q,2d) = 1`); as Möbius groups it
is `|SL₂(ℤ/q)|/2` (`−I ∈ Γ(2)`, `−I ∉ Γ(2q)`), which cancels in the ratio (O112, D10). For one `Γ'_1`-orbit
`O = Γ'_1·Q₀`, the weighted number of `Γ'_q`-orbits in `O ∩ Λ̃(q)` is
`e_{Q₀}^{−1} · #{g ∈ SL₂(ℤ/q) : Q̄₀∘g ∈ S_q}` with `S_q = {cB − A ≡ 0}`; by orbit–stabiliser this is
`e_{Q₀}^{−1}|SL₂(ℤ/q)| · |S_q ∩ 𝒪(Q̄₀)|/|𝒪(Q̄₀)|`. For `ℓ ∤ 2d` the orbit `𝒪(Q̄₀)` mod ℓ is the whole
quadric `{B² − 4AC = −4d}` (O112, D10: the stabiliser of `Q̄₀` in SL₂(𝔽_ℓ) is `SO(Q̄₀)`, a torus of order `ℓ−χ(ℓ)`, so the orbit has
`ℓ(ℓ²−1)/(ℓ−χ) = ℓ² + χℓ` elements = the whole quadric), so the ratio is `g_{c,d}(ℓ)`, independent of Q₀; CRT. ∎

**Theorem 6.2 (per-d count; PROVED conditional on (SEL) and the cited large sieve).** Let
`ψ(u) = φ(x/λ)W(y/Y)` as in §5, with `λ ≍ A/(qF)`, `Y ≍ 1/(qF√d)` (i.e. `f ≍ F`, `a ≍ A`), `F ≥ 8A`.
(O112, D5: `F ≥ 8A` makes `λ ≤ 1/4`, one period; in §8 the cells with `A/8 ≤ F' < 8A` lie in bands of
bounded width and are bounded trivially, so no splitting into periods is ever needed.)
Then with `𝔐_d := (#Λ(1)/V(1)) ∫ψ dμ` (independent of q and of the sieve),
`|Σ_{Q∈𝓕_d^I, q | n(Q)} ψ(u_Q) − g_{c,d}(q) 𝔐_d| ≪_ε 𝓛^C q (#Λ(1))^{1/2} (A√d + F^{1+ε} d^{−1/2})^{1/2}`.
*Proof.* Cor 4.4 (separation, Lemma 2.2, holds for the subset `Λ̃(q)`), Lemma 6.1 for the main term, and
Prop 5.1 with `λ/Y ≍ A√d`, `q^{1/2}/(MY) ≍ F/(q^{1/2}√d)`, `λ²/Y ≤ λ/Y`; finally
`#Λ(q) = g(q)·½|SL₂(ℤ/q)|·#Λ(1) ≪ q² #Λ(1)` (D10). ∎
*Remark (O112, D11).* The per-d *relative* error is not uniform in d (by Siegel, `#Λ_d(1)` may be as small as
`d^{1/2−ε}` and the main term `𝔐_d` correspondingly small); the assembly never uses per-d relative errors, only
the absolute errors above summed over `d ≍ D` by Cauchy–Schwarz and Lemma 6.3.

**Lemma 6.3 (class numbers; PROVED, standard).** `#Λ(1) ≤ 6·h(−4d)·r(d)` where `h(−4d) ≪ d^{1/2} log d`
is the number of SL₂(ℤ)-classes of forms of discriminant −4d and `r(d) ≤ ∏_{p^k∥d} p^{⌊k/2⌋}` (O112, D13: no factor 4 at p = 2).
Hence `Σ_{d≤D} #Λ_d(1) ≪ D^{3/2}(log D)^2`.
*Proof.* `#Λ(1) ≤ [Γ₀(d)∩Γ(2) : …]`-weighted count of pairs (SL₂-class `[Q₀]`, coset `γ ∈ Γ⁰(d)\SL₂(ℤ)`)
with `Q₀∘γ ∈ 𝓕_d`; the factor 6 = `[Γ₀(d) : Γ₀(d)∩Γ(2)] ≤ 6`. Cosets ↔ second columns `(t:s) ∈ ℙ¹(ℤ/d)`,
and `Q₀∘γ ∈ 𝓕_d` forces `Q₀(t,s) ≡ 0 (d)`. `𝓕_d` forms are primitive (`gcd(f, 4ad) = 1` since `ef − 4a²d = 1`; R1: `(f,e) = 1` is false in general).
For odd `p^k ∥ d` and primitive `Q₀ = [A,B,C]` with `p ∤ A` (WLOG after SL₂-change), points with
`p | s` give `Q₀ ≡ A t² ≢ 0`; points `(t:1)` need `(2At + B)² ≡ B² − 4AC ≡ 0 (p^k)`, i.e. t in one class
mod `p^{⌈k/2⌉}`: `p^{⌊k/2⌋}` points. For `p = 2` (D13, from the review): WLOG A odd, `B = 2B'`, `A·Q₀(t,1) = (At+B')² + d`, so `2^k | Q₀(t,1)` iff
`At + B' ≡ 0 (2^{⌈k/2⌉})` — `2^{⌊k/2⌋}` points — and points `(1:s)`, `2 | s`, give `Q₀ ≡ A` odd. (Brute force over all
primitive reduced forms, d ≤ 150: `scripts/review_ttl_*.py`, max ratio 1.0.)
`Σ_{d≤D} r(d) ≤ Σ_{m} m·#{d ≤ D : m² | d} ≪ D log D`, so `Σ_{d≤D} r(d) d^{1/2} log d ≪ D^{3/2}(log D)^2`. ∎

## 7. The complementary counts (PROVED, unconditional; Poisson + Weil)

Fix `c`, a squarefree `q` and smooth weights `W_i ∈ C_c^∞([1,2])`. 𝓛 = log N.

**Proposition 7.1 ((K_a): fixed a; PROVED, unconditional — O112: written at proof level).** Let `(q, 2a) = 1`,
q squarefree, `m = 4a²`, `r = mq`, and
`S_a(q) := Σ_{e,f ≥ 1, ef ≡ 1 (m), q | n} W₁(e/E) W₂(d/D)`, `d := (ef−1)/m`, `n := 4acd − f`, `F := mD/E`.
Then `S_a(q) = g'_{c,a}(q) X_a + R_a(q)` with `X_a := (φ(m)/m²)∫∫W₁(x/E)W₂((xy−1)/(mD))dxdy ≍ Dφ(m)/m` and
`|R_a(q)| ≪ 2^{ω(q)} τ(m)² (q a + D/E + D/F)` uniformly in a, c, q, D, E (constants depending on W₁, W₂), where
`g'_{c,a}(ℓ) = (ℓ−1)/ℓ²` (ℓ ∤ c), `1/ℓ` (ℓ | c), multiplicative. In particular, if `min(E,F) ≥ N^{c₀}` the terms
`D/E + D/F` are `≤ D N^{−c₀}`, a relative error `N^{−c₀}` (R1: for tiny e the density is false, e.g. a = c = 1,
e = 3, q = 5; this is the `D/E` term).
*Proof.* (i) *Congruences.* `a n = 4a²cd − af = c(ef−1) − af = f(ce−a) − c`, so for `(a,q) = 1`, `q | n ⟺ f(ce−a) ≡ c (q)`.
Hence `(e,f) mod r` runs over `𝒮 = 𝒮_m × 𝒮_q` (CRT, `(m,q) = 1`), `𝒮_m = {ef ≡ 1 (m)}`, `𝒮_q = {f(ce−a) ≡ c (q)}`.
(ii) *Poisson.* With `W(x,y) := W₁(x/E)W₂((xy−1)/(mD))` (smooth; on its support `x ≍ E`, `y ≍ F`,
`∂_x^i∂_y^jW ≪ E^{−i}F^{−j}`), `S_a(q) = r^{−2}Σ_{h,k∈ℤ} Ŵ(h/r, k/r) 𝒦(h,k)`, `𝒦(h,k) := Σ_{(e,f)∈𝒮} e((he+kf)/r)`, and
`|Ŵ(h/r,k/r)| ≪_B EF(1+E|h|/r)^{−B}(1+F|k|/r)^{−B}`. By CRT (`1/r ≡ q̄/m + m̄/q mod 1`),
`𝒦(h,k) = S(q̄h, q̄k; m)·T_q(m̄h, m̄k)` with the Kloosterman sum `S(·,·;m)` and
`T_q(u,v) := Σ_{(e,f)∈𝒮_q} e((ue+vf)/q) = Π_{ℓ|q} T_ℓ`. For `ℓ ∤ c`, substituting `w = ce − a`:
`T_ℓ(u,v) = e(uc̄a/ℓ) S(uc̄, vc; ℓ)`; for `ℓ | c`: `f ≡ 0`, `T_ℓ = ℓ·1[u ≡ 0]`. So `|T_q| ≤ 2^{ω(q)} q` always.
(iii) *(h,k) = (0,0):* `r^{−2}Ŵ(0,0)|𝒮_m||𝒮_q| = X_a·|𝒮_q|/q²`, and `|𝒮_ℓ| = ℓ−1` (ℓ ∤ c: `f = c/(ce−a)`, `ce ≠ a`) resp. `ℓ`
(ℓ | c: `af ≡ 0`, e free), i.e. `g'(q)X_a`. `Ŵ(0,0) ≍ EF = mD` gives `X_a ≍ Dφ(m)/m`.
(iv) *h = 0 ≠ k:* `S(0,k';m) = c_m(k')`, `|c_m(k')| ≤ (k',m) = (k,m)`. For any `δ ≥ 1`,
`Σ_{k≠0, δ|k}(1+F|k|/r)^{−B} ≪ r/(δF)` (if `δF ≤ r` there are `≍ r/(δF)` terms of size O(1); otherwise the sum is
`≪ (r/(δF))^B ≤ r/(δF)`). So `Σ_{k≠0}(k,m)(1+F|k|/r)^{−B} ≤ Σ_{δ|m} δ Σ_{δ|k≠0}(…) ≪ τ(m) r/F`, and the contribution is
`≪ r^{−2}·EF·2^{ω(q)}q·τ(m)r/F = 2^{ω(q)}τ(m)E/m = 2^{ω(q)}τ(m) D/F`. *k = 0 ≠ h:* symmetrically `≪ 2^{ω(q)}τ(m) D/E`.
(v) *hk ≠ 0:* Weil and the prime-power bound (`|S(u,v;p^β)| ≤ 2p^{β/2}(u,v,p^β)^{1/2}` for odd p,
`≤ 2^{3/2}2^{β/2}(u,v,2^β)^{1/2}` for p = 2) give `|S(q̄h,q̄k;m)| ≤ 3τ(m)m^{1/2}(h,k,m)^{1/2}`. Then
`Σ_{h,k≠0}(h,k,m)^{1/2}(1+E|h|/r)^{−B}(1+F|k|/r)^{−B} ≤ Σ_{δ|m} δ^{1/2}·(r/(δE))(r/(δF)) ≪ r²/(EF)`
(`Σ_δ δ^{−3/2} < ∞`), so the contribution is `≪ r^{−2}·EF·2^{ω(q)}q·τ(m)m^{1/2}·r²/(EF) = 2^{ω(q)}τ(m) q m^{1/2} = 2^{ω(q)}τ(m)·2qa`.
In the application (fixed-a part of R_bad, §8 (b1)) `e, f ≥ N^{1/2−3η₁}` (§8 (2a)), so `min(E,F) ≥ N^{c₀}` with
`c₀ = 1/2 − 3η₁` (O112, D6: the retired Prop 7.2 is not used). ∎
*Consequence.* `Σ_{a≍A} Σ_{q≤Q} 3^{ω(q)}|R_a(q)| ≪ 𝓛^C(Q²A² + Q·AD·N^{−c₀})` (`Σ_{a≍A}τ(4a²)² ≪ A𝓛^C`), against the mass
`≍ AD`: relative `𝓛^C(Q²A/D + QN^{−c₀})`, a level `Q = (D/A)^{1/2}𝓛^{−C}` (as `Q ≤ N^{1/4} < N^{c₀/2}`) whenever `D > A`,
i.e. `α < (1−γ)/2`.

**Proposition 7.2 (M2: a small divisor) — NOT USED (R1: for fixed (d,e) the weight n is quadratic in a,
with local densities `(1 + (d(dc²e²−1)/ℓ))/ℓ`, not `≈ 1/ℓ`; small divisors are instead handled by BT
outside R_bad, §8).** Let `(q, 2d) = 1`, `e ≤ E`. For fixed `(d, e)`,
`#{a : a ≍ A, e | 4a²d+1, q | n} = W-weighted (A/(eq))·ρ_{d,e,c}(q) + O(ρ_{d}(e)·3^{ω(q)})`, where
`ρ_d(e) = #{x mod e: 4dx²+1 ≡ 0}` and `ρ_{d,e,c}(q)` counts the admissible classes mod `eq`. (Poisson in
`a` mod `eq`, trivial.) Summed over `d ≍ D`, `e ≍ E`, `q ≤ Q`: error `≪ 𝓛^C D E Q²`… against mass `AD`:
level `Q = (A/E)^{1/2}𝓛^{−C}` when `E < A`. The same with f in place of e.

## 8. Assembly: (OPEN-I) under (SEL)

### 8.0 Brun–Titchmarsh outside R_bad (O112 repair, D2; PROVED, unconditional)

Notation: `g(x) := x/φ(x)`; `L = log N`; `x ≍ X` means `X < x ≤ 2X`. A w_c-tuple (MN3 §3.7) is
`(c,a,d,f) ∈ ℕ⁴` with `f | 4a²d+1`, `n := 4acd − f`, `n/4 < acd ≤ 3n/4` (⇔ `0 < f ≤ 2n`).
Put `e := (4a²d+1)/f`, `b := ce − a`. Then (direct check) `4abd = ne + 1` and `bf = na + c`; hence
`b > 0`, `e | a+b`, and `b = (na+c)/f ≥ a/2` (as `f ≤ 2n`). Thus `4bd ≥ 2ad` and `4acd ≍ n`, so for
`c ≤ N^η` the moduli `4ad`, `4bd` are `≥ N^{1−η}/8`, and the twin moduli `4bcf' ≥ N^{1−o(1)}`,
`4cdf' ≥ N^{1−o(1)}` (MN3 Prop 3.3 exponents `1+2β+γ−α ≥ 1+β`, `2−2α+β ≥ 2−α`) — so **only `4ab`, `4acf`,
`4cdf` can be short** when `c ≤ N^η`. The four fibre parametrisations (MN3 Lemma 3.2) are:
* `acf`: fix `T = (a,c,f)`; then `(f,2a) = 1`, `d ≡ d_T := −(4a²)^{−1} (mod f)`, and `d ↦ n = 4acd − f` is
  injective with `n` in one class mod `m_T = 4acf`;
* `cdf`: fix `T = (c,d,f)`; then `a` lies in one of `ρ_d(f) := #{x mod f : 4dx² + 1 ≡ 0 (f)}` classes mod f,
  and `a ↦ n` is injective with `n` in `ρ_d(f)` classes mod `m_T = 4cdf`;
* `ab`: fix `T = (a,b,c)`; then `e = (a+b)/c ∈ ℕ`, `(e,4ab) = 1`, `d ≡ (4ab)^{−1} (mod e)` (from `4abd = ne+1`),
  `n = (4abd−1)/e`, and `d ↦ n` is injective with `n` in one class mod `m_T = 4ab`. Each `(a,b)` has
  `≤ τ(a+b)` admissible c.

**Lemma 8.2 (PROVED).** Fix `0 < η₁ < 1/2`. For `P ∈ {ab, acf, cdf}` let `𝒮_P(N)` be the set of
w_c-tuples (any c) with n prime in `(N/2, N]` and `m_P ≤ N^{1−η₁}` (`m_ab = 4ab`, `m_acf = 4acf`,
`m_cdf = 4cdf`). Then `#𝒮_P(N) ≪ η₁^{−1} N L²` for `N ≥ N₀(η₁)`.
*Proof.* Brun–Titchmarsh (Montgomery–Vaughan): for `m < y`, `π(x+y; m, r) − π(x; m, r) ≤ 2y/(φ(m) log(y/m))`.
With `x = y = N/2` and `m ≤ N^{1−η₁}`, `log(y/m) ≥ η₁L − log 2 ≥ η₁L/2` for `N ≥ N₀(η₁)`. A class with
`(r,m) > 1` contains at most one prime. So, by the injectivity above, a fibre over T contributes
`≤ ρ_T (2N/(η₁ L φ(m_T)) + 1)` (`ρ_T = 1` for ab, acf; `ρ_T = ρ_d(f)` for cdf). Since `φ(4x) ≥ 2φ(x)` and
`φ(xy) ≥ φ(x)φ(y)`:
* acf: `Σ_{acf ≤ N} 1/(φ(a)φ(c)φ(f)) ≤ (Σ_{x≤N} 1/φ(x))³ ≪ L³` (Landau: `Σ_{x≤X}1/φ(x) ≪ log 2X`);
* ab: `Σ_{ab ≤ N, a ≤ 2b} τ(a+b)/(φ(a)φ(b)) ≪ L³` by Lemma 8.3(b) summed over the `≪ L²` dyadic boxes;
* cdf: `Σ_{c ≤ N} 1/φ(c) · Σ_{df ≤ N} ρ_d(f)/(φ(d)φ(f)) ≪ L · L²` by Lemma 8.3(c) over `≪ L²` boxes.
The `+1` terms total `≤ Σ_{T: m_T ≤ N^{1−η₁}} ρ_T ≪ N^{1−η₁+ε}` (`ρ_T`, `τ(a+b) ≪ N^ε`). ∎

**Lemma 8.3 (weighted divisor sums; PROVED, elementary + Pólya–Vinogradov).** Uniformly in `A, B, D, F ≥ 1`:
(a) `Σ_{x≍X} g(x)² ≪ X`; `g(x) = Σ_{l|x} μ²(l)/φ(l)`.
(b) `Σ_{a≍A, b≍B, a ≤ 2b} τ(a+b) g(a) g(b) ≪ AB log 2B`.
(c) `Σ_{d≍D} g(d) Σ_{f≍F} ρ_d(f)/φ(f) ≪ D`.
*Proof.* (a) standard (`g² = Σ_{l|x} h(l)`, `h(p) ≤ 3/p`, `Σ h(l)/l < ∞`).
(b) Fix a. For squarefree l, `τ(n) ≤ 2#{δ | n : δ ≤ √n}` and `n = a + b ≤ 6B` give
`Σ_{b≍B, l|b} τ(a+b) ≤ 2Σ_{δ ≤ √(6B)} #{b' ≤ 2B/l : lb' ≡ −a (δ)} ≤ 2Σ_{δ≤√(6B)} (2B(l,δ)/(lδ) + 1)
≤ 4(B/l)τ(l)(1 + log 6B) + 2√(6B)` (`Σ_{δ≤Z}(l,δ)/δ ≤ τ(l)(1+log Z)`). Multiply by `μ²(l)/φ(l)` and sum over
`l ≤ 2B`: `Σ_l μ²(l)τ(l)/(lφ(l)) < ∞`, `Σ_{l≤2B} 1/φ(l) ≪ log 2B`, so `Σ_{b≍B} τ(a+b)g(b) ≪ B log 2B`. Sum over a
with (a).
(c) Let `χ_d := (−4d/·)` (Kronecker), a non-principal real character mod 4d, and `S_d(Y) := Σ_{g≤Y} χ_d(g)/g`
(`S_d(Y) := 0` for `Y < 1`). Facts: (i) `ρ_d(2^k) = 0` (k ≥ 1); for odd p, `ρ_d(p^k) = 1 + χ_d(p)` (`p ∤ d`, Hensel),
`= 0` (`p | d`); hence `ρ_d(f) ≤ (1∗χ_d)(f)` for all f (for `χ_d(p) = −1`: `0 ≤ Σ_{i≤k}(−1)^i`), and
`ρ_d(kf') ≤ ρ_d(k)ρ_d(f') ≤ 2^{ω(k)}ρ_d(f')` for squarefree k (`ρ_d(p^{1+j}) = ρ_d(p^j)` for j ≥ 1).
(ii) `R_d(Y) := Σ_{Y<f≤2Y} (1∗χ_d)(f) = Σ_{g≤2Y} χ_d(g)(Y/g + O(1)) = Y·S_d(2Y) + O(Y)` for `Y ≥ 1`.
(iii) Mean square: `Σ_{d≍D} |S_d(Y)|² ≪ D` for all `Y ≥ 1`. Indeed for `Y ≤ Y₀ := D/log²(2D)`, expand:
`Σ_{g,g'≤Y} (gg')^{−1} Σ_{d≍D} χ_d(gg')`; the terms with `χ_d(gg') ≠ 0` need gg' odd, and then
`χ_d(gg') = (−d/gg')` (Jacobi); if gg' is a square the inner sum is `≤ D` and `Σ_{gg'=□}(gg')^{−1} < ∞`; if not,
`d ↦ (d/gg')` is a non-principal character mod gg' and PV gives `≪ (gg')^{1/2} log(gg')`; total
`≪ D + Y log 2Y ≪ D`. For `Y > Y₀`, partial summation and PV in g (`|Σ_{g≤u} χ_d(g)| ≪ √d log d`) give
`S_d(Y) = S_d(Y₀) + O(√D log(2D)/Y₀) = S_d(Y₀) + O(1)` (for `D ≤ D₀` absolute, `|S_d(Y)| ≪ 1` trivially by PV).
Now `1/φ(f) = f^{−1}Σ_{k|f} μ²(k)/φ(k)`, so by (i), (ii)
`Σ_{f≍F} ρ_d(f)/φ(f) ≤ Σ_k (μ²(k)2^{ω(k)}/(kφ(k))) Σ_{f'≍F/k} ρ_d(f')/f' ≤ Σ_k (2^{ω(k)}/(kφ(k)))(|S_d(2F/k)| + C)`
(for `F/k < 1` the inner sum is `≤ 1`). Average over d with weight g(d), Cauchy–Schwarz with (a) and (iii):
`Σ_{d≍D} g(d)(|S_d(·)| + C) ≪ D`; the k-sum converges. ∎
*Remark.* (c) is the "`L(1,χ_{−4d})` is O(1) on average" input; PV suffices because only a mean square over
a full dyadic d-range is needed. (c) is also uniform per box, which §8 (D1 repair) uses.

**Lemma 8.4 (weighted Type I masses; O112 repair, D3; PROVED rel. MN3 Prop 2.3).** Let `L² ≤ A ≤ N`, `1 ≤ D ≤ N`.
(a1) If `D ≤ A`: `Σ_{a≍A, d≍D} τ(4a²d+1) g(d) ≪ AD log N`; if `D ≥ A`: the same with `g(a)` for `g(d)`.
(a2) If moreover `A, D ≥ N^{1/4}`: `Σ_{a≍A, d≍D} τ(4a²d+1) g(a) g(d) ≪ AD log N`.
(b) If `F ≤ 4A`: `Σ_{d≍D} g(d) #{(a,f) : a≍A, f≍F, f | 4a²d+1} ≪ AD` (the same with e for f: both are
divisors of `4a²d+1`).
*Proof.* (a1) `D ≤ A`: `g(d) = Σ_{l|d} μ²(l)/φ(l)`, `d = ld'`; MN3 Prop 2.3(b) with `k = 4l`, linear variable
`d' ≤ 2D/l`, quadratic `a ≤ 2A`, `l₀ = 40`: its hypotheses `8D ≤ (2A)^{40}`, `2A ≥ ω(8l)+2` hold for every l, and it
gives `≪ (AD/l) log N (1 + log(1+4l))`; `Σ_l μ²(l)(1+log(1+4l))/(lφ(l)) < ∞`. `D ≥ A`: `a = ka'`, Prop 2.3(a)
with `k = 4k²`, linear `d ≤ 2D`, quadratic `a' ≤ 2A/k`: hypotheses `16A² ≤ (2D)^{40}`, `2D ≥ ω(4k²)+2` hold for
every k; it gives `≪ (AD/k) log N`; `Σ_k 1/(kφ(k)) < ∞`.
(a2) Write `g(a)g(d) = Σ_{k|a, l|d} μ²(k)μ²(l)/(φ(k)φ(l))`, `a = ka'`, `d = ld'`; the inner sum is
`Σ_{a' ≤ 2A/k, d' ≤ 2D/l} τ(K d' a'² + 1)`, `K = 4k²l`. *Tail* `k > A^{1/2}` or `l > D^{1/2}`: `τ ≪ N^{ε}`, so it is
`≪ N^{ε} AD Σ_{k>A^{1/2}} 1/(kφ(k)) + (same in l) ≪ N^{ε}AD(A^{−1/2} + D^{−1/2}) ≪ AD` (as `A, D ≥ N^{1/4}`). *Main*
`k ≤ A^{1/2}`, `l ≤ D^{1/2}`: apply MN3 Prop 2.3 with linear variable d', quadratic variable a', and `l₀ = 40`
(fixed). If `D ≥ A`: (a) of Prop 2.3 needs `K(2A/k)² = 16lA² ≤ (2D/l)^{40}` and `2D/l ≥ ω(K)+2` — both hold since
`2D/l ≥ D^{1/2} ≥ N^{1/8}`, `16lA² ≤ 16N³`; it gives `≪ (φ(K)/K)(AD/(kl)) log N`. If `D < A`: (b) of Prop 2.3 needs
`K·2D/l = 8k²D ≤ (2A/k)^{40}` and `2A/k ≥ ω(2K)+2` — both hold (`2A/k ≥ A^{1/2} ≥ N^{1/8}`); it gives
`≪ (φ(K)/K)(AD/(kl)) log N · (1 + log(1+K))`. Summing `μ²(k)μ²(l)(1+log(1+4k²l))/(klφ(k)φ(l))` converges.
(b) For fixed `(d, f)`, `f | 4a²d+1` puts a in `ρ_d(f)` classes mod f, and `f ≤ 2F ≤ 8A`: `#{a ≍ A} ≤ ρ_d(f)(A/f + 1) ≤
9ρ_d(f)A/f`. So the sum is `≤ 9A Σ_{d≍D} g(d) Σ_{f≍F} ρ_d(f)/f ≪ AD` by Lemma 8.3(c). ∎
*Use.* (a2) bounds the Brun–Titchmarsh mass for the modulus 4ad (`Σ τ/φ(4ad) ≪ log N` per (a,d)-box: ET (8.2)
with the coprimality gain; only needed where `α ≈ 1/2`, so `A, D ≥ N^{1/4}`); (a1) bounds the sieve masses with
weight `g(s)`, `s ∈ {a,d}` the fixed variable, per (c-block, a-block) summed over all f-cells (no size condition on D); (b) is a **per-cell** bound (no log), needed in the strips `β > 1` (D1) and `β < α+γ`.

**Theorem 8.1 (CONDITIONAL on (SEL) of §5; relative to ET Prop 2.2/Lemma 2.8/(8.1)–(8.2), MN3 Prop 2.3,
Brun–Titchmarsh, Selberg's upper-bound sieve, Weil's bound, and the DI/Drappeau large sieve).**
`Σ_{p≤N} f_I(p) ≪ N log² N`.

*Proof.* Dyadic in N; `p ∈ (N/2, N]`, `L = log N`, `f_I(p) ≤ 2Σ_c w_c(p)`.
(1) `c > N^{η}` (η small fixed): MN3 Thm 3.8 part (1) (= ET (8.1)–(8.2) with BT): `≪ η^{−1}N L²`.
(2) `c ≤ N^η`, fixed c; `γ := log c/L`, `a ≍ A = N^α`, `d ≍ D`, `AD ≍ N/c`, `e ≍ N^{β−γ}`. Smooth dyadic
partition of unity in `(a, d, e)` (for spectral cells in `(f', a/f')`, `f' ∈ {e, f}`, §5), dropping ET's size
constraints (upper bound).
(2a) (O112 repair, D2.) Tuples with `min(4ab, 4acf, 4cdf) ≤ N^{1−η₁}` (`η₁ ≥ η` fixed small): Lemma 8.2,
`≪ η₁^{−1} N L²` in total (all c at once; no cells needed). The remaining tuples (c ≤ N^η, all three
moduli `> N^{1−η₁}`; `4ad, 4bd ≥ N^{1−η}/8` automatically, §8.0) have exponents in `R_bad(η₁)` up to
`O(1/L)`; the smooth cells of (2b) are taken with support in `R_bad(2η₁)` (positive weights: an upper bound).
Inside `R_bad(2η₁)` one has `e, f ≥ N^{1/2−3η₁}` (MN3 Prop 3.3: `β ≥ (1−2η₁)/2`, and
`1+α−β ≥ max(1−α−γ−2η₁, α−2η₁)`), so no tiny divisors remain (R1: this replaces the retired Prop 7.2).
(2b) (O112 repair, D1/D3/D5.) Inside `R_bad(2η₁)`. Fix the c-block `c ≍ 2^j` (`1 ≤ j ≤ ηL`); write
`δ := |2α−1+γ|`, `k := ⌊δL⌋` (a-layer index), and use smooth cells of side `O(1/L)` in `(α, β)`.
A *band* is a set of cells of bounded width (`≤ C₀/L`) in one exponent; it has `O(L)` cells per c-block.
The bands used are `|β − (α+γ)| ≤ C₀/L`, `|β−1| ≤ C₀/L`, `D ≤ 64`: in each, one of e, f is `≤ 2^{C₀+3}A`
(`e ≍ (a+b)/c`; `f ≍ N^{1+α−β}`; `f ≤ 4a²d+1`), so by Lemma 8.4(b) (constant `2^{C₀+3}` for 4) a cell has
`≪ 2^j·AD ≪ N` tuples, and **all bands together cost `≪ Σ_{j≤ηL} N L ≪ N L²` trivially**. Layers
`k ≤ C₁ log L` are treated in (4).
Away from the bands, each cell gets one of the following treatments; the *saving* is the factor by which the
cost is below the cell's weighted mass.
* (b1) `D ≥ A` (`α < (1−γ)/2`): fixed-a sequences, Prop 7.1 (applicable: `e, f ≥ N^{1/2−3η₁}`, §(2a)),
  relative remainder `≪ L^C Q² A/D = L^C Q² N^{−δ}`; saving `C/k` by (3). No condition on β.
* (b2) `D < A`, `α ≤ β < α+γ` (so `e ≍ (a+b)/c ≤ 4A`, and `f ≥ 8A` off the band `|β−1| ≤ C₀/L`, `C₀ ≥ 6`): if `k ≥ 2j`, fixed-d sequences with the
  f-cusp: Thm 6.2 (`λ = A/(qf) ≤ 1/4`), relative remainder `≪ L^C Q²(N^{−δ/2} + f^{1/2+ε}/A)`, and
  `f^{1/2}/A ≍ N^{(1−α−β)/2} ≤ N^{(γ−δ)/2} ≤ N^{−δ/4}` (as `1−2α = γ−δ`, `δ ≥ 2γ`); saving `C/k`. If
  `k < 2j`: BT on 4ad (saving `1/j ≤ 2/k`), applied to the whole layer (b4).
* (b3) `D < A`, `α+γ < β < 1` (`e, f ≥ 8A` off the bands): fixed d, cusp `f' = min(e,f) ≤ (ef)^{1/2} ≤ 3A√D`, Thm 6.2
  with `λ ≤ 1/4` (`F' ≥ 8A`); cusp term `f'^{1/2+ε}/A ≪ N^{ε}D^{1/4}A^{−1/2} = N^{(1−γ−3α)/4+ε} ≤ N^{−1/9}` (as
  `α ≥ (1−γ)/2`, `γ ≤ η`); relative remainder `≪ L^C Q² N^{−δ/2}`; saving `C/k`.
* (b4) per layer: the 4ad Brun–Titchmarsh bound. For fixed `(a,d,f)` the n's with `c ≍ 2^j` lie in an
  interval of length `≤ 4ad·2^j` in one class mod 4ad, so BT gives `≤ 8ad2^j/(φ(4ad)·j log 2)`;
  by Lemma 8.4(a2) the layer (`a ≍ A`, all f, `c ≍ 2^j`) costs `≪ N L/j` (used only for `k ≤ L/3`, where
  `δ ≤ 1/3` gives `A, D ≥ N^{1/4}`).
* (b5) **(D1)** `D < A`, `1 < β ≤ 1+2η₁` (`f < A`, possible because `R_bad` allows `β ≤ 1+η₁`; the old text
  wrongly said f' ≥ A/8 fails only for `β < α+γ`). Put `k' := ⌊(β−1)L⌋ ≥ C₀`. If `k' ≤ k/2`: fixed d with
  the **e-cusp** (forms `[e, 4ad, df] ∈ 𝓕_d^I`, linear functional `n = cB − C/d`; Lemma 6.1 and Thm 6.2 hold
  verbatim, the local density being the same `g_{c,d}` — substituting `C/d = cB` gives the same equation
  `B² − 4cdAB + 4d = 0` as `A = cB` does after `A ↔ C/d`): `λ = A/(qe) ≤ 1/4` since `e/A ≍ N^{β−γ−α} ≥ D/8`
  (cells with `D ≤ 64` form a band, so `e ≥ 8A`); cusp term `e^{1/2}/A ≍ N^{(β−γ−2α)/2} = N^{(β−1−δ)/2} ≤ N^{−δ/4}`;
  saving `C/k`. If `k' > k/2`: Brun–Titchmarsh on `4cdf ≍ N^{2−β}` (fibres `cdf` of §8.0), `log(N/m) ≥ k'·log 2/2`,
  saving `C/k'`. In both cases the saving is `≤ C/max(k, k')`, and the cell's weighted mass is `≪ N`
  **per cell**: Lemma 8.4(b) (`F ≤ A`; sieve weight `g(c)g(d)`) resp. Lemma 8.3(c) with
  `Σ_{c≍2^j} 1/φ(c) ≪ 1` (BT weight `ρ_d(f)N/φ(4cdf)`).
(3) (O112 repair, D3.) Sieve per sequence σ (fixed `s ∈ {a, d}`, all other variables smooth) with
`z = N^{θ}`, `θ = κδ/8` (κ = 1 in (b1), κ = 1/4 in (b2), (b3), (b5) after the cusp estimates), `Q = z²`,
sieving only primes `ℓ > ℓ₀`, `ℓ ∤ 2cs`, densities `g ≤ 1/ℓ` (§6, Prop 7.1): Selberg's upper bound sieve
gives `#{n ∈ σ prime} ≤ X_σ/G(z) + Σ_{q≤Q, q|P(z)} 3^{ω(q)}|r_σ(q)|` with
`G(z) ≥ c'·(φ(2cs)/(2cs)) log z`. **Main term.** `X_σ` is the model mass (`𝔐_d` resp. the (0,0) Poisson term);
by Thm 6.2 resp. Prop 7.1 at q = 1, `X_σ ≤ #σ + |r_σ(1)|`. So the main terms of a cell/layer are
`≤ (8/(c'κδL))·Σ_σ (2cs/φ(2cs))(#σ + |r_σ(1)|)`, and `2cs/φ(2cs) ≤ 2g(c)g(s) ≪ g(c)g(s)`; the `#σ` part is the
weighted mass, `≪ N` per cell (Lemma 8.4(b): cells of (b2), (b5)) resp. `≪ N L` per layer (Lemma 8.4(a1), with
`Σ_{c≍2^j} g(c) ≪ 2^j`: cells of (b1), (b3)); the `|r_σ(1)|` part is `≤ (max g)² Σ|r_σ(1)| ≪ (log L)² L^C N^{−κδ/2}`
times the mass (`g(x) ≪ log log x`). **Remainder.** `≪ L^C N^{−κδ/2}` times the mass (`Q² = N^{κδ/2}`).
Both are `≪ (C/k)` times the mass once `k ≥ C₁ log L`.
(4) Layers with `k ≤ C₁ log L`: (b4) for every cell, cost `≪ Σ_{j≤ηL} (C₁ log L)·N L/j ≪ N L (log L)²`.
(5) Summation. (b1), (b3), and (b2) with `k ≥ 2j`: per (j, k) layer cost `≪ N L·min(1/j, C/k)` (choose per
layer the better of (b4) and the spectral/Weil bound; for `k > L/3` only the latter, and
`Σ_j Σ_{L/3<k≤L} NL·C/k ≪ NL·ηL`); by Lemma 1.1, `Σ_{j,k≤L} N L min(1/j, C/k) ≪ N L²`.
(b2) with `k < 2j`: (b4) on these layers, `≪ Σ_j Σ_{k<2j} NL/j ≪ N L²`. (b5): per c-block,
`Σ_{k,k'≤L} N·C/max(k,k') = C N Σ_{m≤L}(2m−1)/m ≪ N L`, total `≪ ηN L²`. Bands: `≪ N L²` (above). With
(1) and (2a), `Σ_{p ≍ N} f_I(p) ≪ N L²`; sum over dyadic N. ∎

*Status of the proof (O112 repair round, after hostile review R111 = `reviews/exceptional-typei-loglog-review.md`).*
R111 found no FATAL defect and labelled Thm 8.1 "CONDITIONAL on (SEL), outline". O112 repaired: D1 (the strip
`1 < β ≤ 1+η₁` on the `D < A` side: e-cusp or BT on 4cdf, saving `C/max(k,k')`, per-cell masses, (b5)); D2 (BT
outside R_bad written: only `4ab, 4acf, 4cdf` are needed, Lemmas 8.2–8.3, elementary + PV); D3 (weighted masses:
Lemma 8.4 from MN3 Prop 2.3 with the large-k tail, and `X_σ ≤ #σ + |r_σ(1)|`); D4–D13 (minor). Prop 5.1 and Prop 7.1
are now written at proof level. **Label: Thm 8.1 is CONDITIONAL on (SEL), with a complete proof relative to the
cited results** — ET Prop 2.2/Lemma 2.8/(8.1)–(8.2) and MN3 Thm 3.8(1) (the reduction and the `c > N^η` part), MN3
Prop 2.3 (rel. ET Thm 7.1), the DI Thm 2 / Drappeau Prop 4.7 spectral large sieve (normalisation checked by R111,
not re-derived), the spectral theorem for `L²(Γ₀(M)\ℍ, χ)`, Brun–Titchmarsh, Selberg's sieve, Weil, Pólya–Vinogradov.
Points that are argued briefly and deserve the round-2 reviewer's attention: (i) the e-cusp variant of Lemma 6.1/
Thm 6.2 used in (b5) (same point set, linear functional `cB − C/d`; the density identity is a two-line substitution);
(ii) the smooth-cell bookkeeping (bands, layers, the choice of treatment per layer in (5)); (iii) Step 6 of Prop 5.1
(dyadic-weighted large sieve, Gallagher for the `t_j`-dependent coefficients). **Not yet re-reviewed.**

## 9. What is unconditional, and where (SEL) enters

* Everything except Prop 5.1's treatment of exceptional eigenvalues is unconditional. With exceptional
  eigenvalues `λ = 1/4 − σ²` the unfolded coefficient picks up `(nY)^{−σ}`; with Kim–Sarnak `σ ≤ 7/64` the
  spectral error is multiplied by `Y^{−7/64} = (qF'√d)^{7/64}`, which kills the saving `(D/A)^{1/2}` on a strip
  `0 < 2α − 1 + γ ≲ 7/32` (D4); DI Thm 5 (with `X = 1/(N₀Y)` per dyadic block) and DI Thm 6 (average over the level) were checked
  (§3.2) and also fail at `α = 1/2`. Humphries' density theorem (ANT 12 (2018), Thm 1.5:
  `N(σ) ≪ vol^{1−4σ+ε}`) with the pointwise coefficient bound loses `N₀ = F'/A`, again failing near
  `α = 1/2` (Humphries/DI Thm 6 numerics not re-checked by the review). **So unconditionally the method leaves a strip of positive width in `α`, which still costs a
  `log log N`; i.e. this argument gives no unconditional improvement of ET.** Removing it needs either Selberg's conjecture (exactly, not a numerical approximation of it),
  or a weighted large sieve for exceptional eigenvalues at `X ≈ 1/(N₀Y)` with no loss, or a beyond-Weil bound for
  `Σ_{a≍A} S(h,k;4a²)` (the (K_a) side; MN3 §3.4).
* The new ingredients that make the conditional result work: (i) **uniform separation** of the level-d
  Heegner points (Lemma 2.2: `4d | disc(Q − Q')`), which gives `‖Σδ_z‖_{H^{−2}}² ≪ #classes` with no loss
  in d; (ii) the observation that the per-d Sobolev bound and the per-a Weil bound are **complementary
  at exactly `d = a`**, so no third method is needed in R_bad; (iii) Lemma 1.1: a linearly degenerating
  saving costs only `O(N log² N)`.
* MN3's (H**) is stronger than what is used. The count is a lattice-point count of lifts in a horocyclic box of
  area `≍ A√d`, and only the second moment of the counting function enters, via Prop 4.3.

## Replay

```
uv run python scripts/ttl_separation.py                         # Lemma 2.1/2.2 check, ~1 min
PYTHONPATH=scripts uv run python scripts/ttl_perd.py 20000 400000 7 31 101 1009 3001 10007   # §3 evidence, ~10 min
```
Outputs: `scripts/ttl_*.out.txt`. DI 1982 scan: `sources/o111/deshouillers-iwaniec-1982.pdf` (Thm 5 on p. 232).
