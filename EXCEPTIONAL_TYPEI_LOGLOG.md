# EXCEPTIONAL_TYPEI_LOGLOG — attacking ET's open Type I bound Σ_{p≤N} f_I(p) ≪ N log² N (task O111)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`);
MN3 = `EXCEPTIONAL_MN3.md` (§3 there: the obstruction region R_bad / R**, Lemma 3.1, Thm 3.8);
DI = Deshouillers–Iwaniec, Invent. Math. 70 (1982) 219–288. `L = log N`.

## 0. Summary

* **Main result — Theorem 8.1 (CONDITIONAL on Selberg's eigenvalue conjecture (SEL) for the congruence
  groups `Γ₀(M)` with even nebentypus mod `2q`, `M | 16dq²`):** `Σ_{p≤N} f_I(p) ≪ N log² N`. This is ET's
  conjectured (OPEN-I). Proof: §§2–8. The proof is at outline level in places (Prop 5.1, Prop 7.1, the cell
  bookkeeping), and step (2a) inherits MN3's unwritten routine BT sums. A self-review (R1) found 3 FATAL
  and 5 MAJOR issues in the first draft; all were repaired in place but have not been re-reviewed.
* **Unconditionally** the same argument removes the obstruction everywhere except on a strip
  `0 < 2α − 1 + γ ≲ 0.1` next to `d = a` (`a = N^α`, `c = N^γ`), where exceptional eigenvalues
  (Kim–Sarnak 7/64) beat the saving. A strip of positive width still costs `log log N`, so ET's bound is
  **not** improved unconditionally (§9).
* New ingredients. (i) Lemma 2.2 (PROVED, elementary): the level-d Heegner points of MN3 Lemma 3.1 are
  **uniformly separated** in ℍ: distinct points have `cosh dist ≥ 3/2`, for every d (because
  `4d | disc(Q−Q')`). (ii) Prop 4.3 (PROVED): with separation, `|Σ_z P(z) − #Λ·⟨P⟩| ≪ (#Λ)^{1/2}‖(1−Δ)P₀‖₂`,
  uniformly in the group. (iii) Prop 5.1 (under SEL, via the Deshouillers–Iwaniec/Drappeau spectral large
  sieve; for `Y ≤ λ𝓛^{−3}`): the box Poincaré series has variance `≪ 𝓛^C(area + (Yλ)^{−ε}/(Y·level))`. (iv) So the per-d
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
`m_{jk} ≪ N log N` is the Type I mass of one (c-block, a-block) pair (ET (8.2) per dyadic box). So a
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
(`σ ≤ 7/64`) the loss is `Y^{−7/64} = (F√d)^{7/64}`, which beats the saving `(d/A)^{1/2}` on a strip
`α − (1−γ)/2 ≲ 0.1` of positive width, so the strip would still cost `log log N`. DI Thm 5
(`Σ_exc X^{2σ_j}|Σ a_nρ_j(n)|² ≪ (1+√(μNX))(1+√(μN^{1+ε}))‖a‖²`, checked on the scan of DI p. 232) with
`X = 1/Y` and DI Thm 6 (average over the level) give extra factors `F A^{−1/2} d^{−1/4}`, resp.
`F^{3/4}D^{1/8}/A` on average over `d ≍ D`, which still fail near `α = 1/2`. **So the plan gives (OPEN-I)
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

**Groups.** Let `d ≥ 1`, `q` squarefree, `(q, 2d) = 1`. On the `w`-side the sieve condition `q | n`
(`n = cB − A` for `Q = [A,B,C] = [f,4ad,de]`, i.e. `n = 4acd − f`) is invariant under
`Γ₀(d) ∩ Γ(q)` (if `γ ≡ ±I (q)` then `Q∘γ ≡ Q (q)`). Conjugating by `u = w/q` turns it into
`Γ_{M,q} := ±(Γ₀(M) ∩ Γ₁(q))`, `M = dq²`, whose cusp ∞ has width 1, and
`L²(Γ_{M,q}\ℍ) = ⊕_{χ mod q, χ(−1)=1} L²(Γ₀(M)\ℍ, χ)` (weight 0, nebentypus χ).
In `u`-coordinates a form `Q ∈ 𝓕_d` sits at `u_Q = (−2a + i/√d)/(fq)`.

**Hypothesis (SEL).** For all `M, q` as above and all even χ mod q, the Laplacian on
`L²(Γ₀(M)\ℍ, χ)` has no eigenvalue in `(0, 1/4)` (Selberg's eigenvalue conjecture for these congruence
groups; known unconditionally only with `λ₁ ≥ 975/4096` (Kim–Sarnak), which is **not** enough here, §3.2).

**Spectral large sieve (cited).** DI Thm 2 (trivial χ) and Drappeau, Proc. LMS 114 (2017),
arXiv:1504.05549, §4.2.2 Prop. 1 (nebentypus χ of conductor `q₀ | q`): for `K ≥ 1`, `N₀ ≥ 1/2`,
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

**Proposition 5.1 (variance; PROVED conditional on (SEL), modulo the cited large sieve).** Let
`P = P_ψ` on `Γ_{M,q}`, `P₀ = P − ⟨P⟩`, and `𝓛 = log(2 + 1/(λY) + M)`. Then
`‖(1−Δ)P₀‖₂² ≪_{φ,W,ε} 𝓛^{C} · [ (λ/Y)(1 + q^{1/2} M^{−1} (𝓛/λ)^{1+ε}) + λ²/Y ]`,
with `L²` norms on `Γ_{M,q}\ℍ`.
*Proof (outline with all steps; the analytic facts used are standard).*
(1) `(1−Δ)P_ψ = P_{ψ'}` with `ψ' = (1−Δ)ψ = φ(x/λ)W̃(y/Y) − (y/λ)² φ''(x/λ)W(y/Y)`,
`W̃ = W − v²W''`; the second piece is `O((Y/λ)²)` times a function of the same type, so it suffices to
bound `‖P₀‖₂²` for `ψ = φ(x/λ)W(y/Y)` with arbitrary fixed `φ, W`.
(2) Spectral decomposition (no residual spectrum except constants for χ = 1; no exceptional spectrum by
(SEL)): `‖P₀‖² = (2/φ(q))·Σ_χ [Σ_j |⟨P,u_j⟩|² + (4π)^{−1}Σ_𝔠 ∫|⟨P,E_𝔠(·,½+it)⟩|² dt]`, the factor
being the index normalisation between `Γ₀(M)\ℍ` and `Γ_{M,q}\ℍ`.
(3) Unfolding: `⟨P,u_j⟩ = Σ_{n≠0} ρ̄_j(n) λφ̂(λn) ∫ W(y/Y) √y K_{it_j}(2π|n|y) dy/y²`, and the same with
the Eisenstein coefficients `φ_𝔠(n,t)`, plus for `n = 0` the constant terms
`δ_{𝔠∞}y^{1/2+it} + φ_{𝔠∞}(½+it) y^{1/2−it}` (for every even χ: ∞ is singular for all of them —
R1 correction; unitarity of the scattering matrix still gives `≪ λ²/Y` after the `2/φ(q)` normalisation).
(4) `n = 0`: `|∫W(y/Y)y^{1/2±it}dy/y²| ≤ Y^{−1/2}|Ŵ(t)|` with `Ŵ` rapidly decreasing; the scattering
matrix is unitary on the critical line, so the n = 0 part contributes `≪ λ²/Y`.
(5) `n ≠ 0`: `|n| ≤ 𝓛/λ` up to a negligible tail (φ̂ decays rapidly), so `2π|n|y ≤ 4π𝓛Y/λ`. By the domain hypothesis `2π|n|y ≪ 𝓛^{−2}`; expand
`K_{it}(x) = ½Σ_± Γ(±it)(x/2)^{∓it}(1 + O(x²))`. Then
`⟨P,u_j⟩ = Σ_± ½Γ(±it_j)π^{∓it_j} Y^{−1/2∓it_j} Ŵ_±(t_j) Σ_n ρ̄_j(n) λφ̂(λn)|n|^{∓it_j} + (O((𝓛Y/λ)²)-terms of the same shape)`,
with `|Γ(it)|² = π/(t sinh πt)` and `Ŵ_±` rapidly decreasing, so only `|t_j| ≤ K = 𝓛` matters.
For `|t_j| ≤ 1` the two `±` terms must not be separated (each is `≍ 1/|t|`); there use instead the Mellin
representation `K_{it}(x) = (4πi)^{−1}∫_{(σ₀)} Γ((s+it)/2)Γ((s−it)/2)(x/2)^{−s} ds` with `σ₀ = 1/𝓛`, so
that `(nY)^{−s}` has modulus `≍ 1` and the Gamma factors have an integrable `1/|v ± t|` singularity
(cost `O(𝓛)` at `t ≈ 0`, where the two Gamma poles coalesce — R1 correction; still polylog); the large sieve is then applied for each fixed `s` on the contour.
(6) The `|n|^{∓it_j}`: split `t_j` into unit intervals `[k, k+1]`; for `t = k+τ`,
`sup_{τ∈[0,1]} |S(τ)|² ≤ |S(0)|² + ∫_0^1 (|S|² + |S'|²) dτ` with `S'` having coefficients multiplied by
`−i log|n| = O(𝓛)`; apply the large sieve to each fixed-τ coefficient vector `b_n = λφ̂(λn)|n|^{−ik−iτ}`
(`‖b‖² ≪ λ²·(𝓛/λ) = 𝓛λ`) on dyadic n-ranges `N₀ ≤ 𝓛/λ`, sum over `≪ 𝓛` intervals and `≪ 𝓛` dyadic
ranges. With `|Γ(it)|²cosh(πt) ≍ 1/(1+|t|)` this gives
`Σ_χ Σ_j |⟨P,u_j⟩|² ≪ (φ(q)/2)·𝓛^C Y^{−1}·λ·(1 + q^{1/2}M^{−1}(𝓛/λ)^{1+ε})`, and the same for the
Eisenstein part. Multiply by `2/φ(q)`. ∎
*Remark.* `(λ/Y)·q^{1/2}M^{−1}λ^{−1} = q^{1/2}/(MY) = F/(q^{1/2}√d)` (since `1/Y = qF√d`, `M = dq²`):
this is the "cusp" term `1/(Y·level)` of §3.

## 6. Per-d counts with the sieve congruence (conditional on (SEL))

**Parity.** The Type I forms are `𝓕_d^I := {[f, 4ad, de] : ef − 4a²d = 1, e,f > 0, a ∈ ℤ}`
(`B ≡ 0 (mod 4d)`), a subset of 𝓕_d that is not `Γ₀(d)`-stable (MN3 Lemma 3.1, R108). It **is** stable
under `Γ₀(2d) ∩ Γ⁰(2)` (w-side; R1: *not* `Γ₀(d)∩Γ(2)` when d is even — e.g. d = 2,
`[[1,0],[2,1]]` maps `[1,8,18]` to a form with `B = 44`): with `γ_z = [[p,t],[r,s]] ∈ Γ⁰(2d) ∩ Γ₀(2)` (z-side),
`B' = 2Apt + B(ps+tr) + 2Crs ≡ 0 (4d)` because `2d | t`, `4d | B`, `C = de`, `2 | r`. So take
`Γ' := Γ₀(2d) ∩ Γ(2q)` (w-side) and `u = w/(2q)`: `u_Q = (−2a + i/√d)/(2qf)`, cusp width 1, and
`Γ'' ⊇ Γ₁(M)` with `M | 16dq²`; (SEL) and the large sieve are applied to `Γ₀(M)` with characters mod `2q`.

**Local densities.** For a prime `ℓ ∤ 2d` put
`g_{c,d}(ℓ) := #{(A,B,C) ∈ 𝔽_ℓ³ : B² − 4AC = −4d, cB − A = 0} / #{(A,B,C) : B² − 4AC = −4d}`,
and `g_{c,d}(q) = Π_{ℓ|q} g_{c,d}(ℓ)`. Then `g = (ℓ−1)/(ℓ² + χ(ℓ)ℓ)` if `ℓ ∤ c` (χ = `(−d/ℓ)`), and
`g = (1+χ(ℓ))/(ℓ + χ(ℓ))` (R1: the quadric has `ℓ² + χℓ` points) if `ℓ | c`. For `ℓ | 2d`, no n is divisible by ℓ (n is odd; if `ℓ | d` then
`n ≡ −f` and `f | 4a²d+1 ≡ 1 (ℓ)`), so those primes are not sieved.

**Lemma 6.1 (main term factorises; PROVED).** For `q` squarefree, `(q,2d) = 1`, let
`Λ̃(q) = {u_Q : Q ∈ 𝓕_d^I, q | cB − A}`, `#Λ(q)` its orbifold count mod `Γ'_q := Γ₀(2d)∩Γ(2q)`,
`V(q) = vol(Γ'_q\ℍ)` (w-side). Then `#Λ(q)/V(q) = g_{c,d}(q) · #Λ(1)/V(1)`.
*Proof.* `[Γ'_1 : Γ'_q] = |SL₂(ℤ/q)|` (strong approximation, `(q,2d) = 1`). For one `Γ'_1`-orbit
`O = Γ'_1·Q₀`, the weighted number of `Γ'_q`-orbits in `O ∩ Λ̃(q)` is
`e_{Q₀}^{−1} · #{g ∈ SL₂(ℤ/q) : Q̄₀∘g ∈ S_q}` with `S_q = {cB − A ≡ 0}`; by orbit–stabiliser this is
`e_{Q₀}^{−1}|SL₂(ℤ/q)| · |S_q ∩ 𝒪(Q̄₀)|/|𝒪(Q̄₀)|`. For `ℓ ∤ 2d` the orbit `𝒪(Q̄₀)` mod ℓ is the whole
quadric `{B² − 4AC = −4d}` (SL₂(𝔽_ℓ) acts on binary forms through SO of the discriminant form, which is
transitive on each non-zero level set — Witt), so the ratio is `g_{c,d}(ℓ)`, independent of Q₀; CRT. ∎

**Theorem 6.2 (per-d count; PROVED conditional on (SEL) and the cited large sieve).** Let
`ψ(u) = φ(x/λ)W(y/Y)` as in §5, with `λ ≍ A/(qF)`, `Y ≍ 1/(qF√d)` (i.e. `f ≍ F`, `a ≍ A`), `F ≥ 8A`.
Then with `𝔐_d := (#Λ(1)/V(1)) ∫ψ dμ` (independent of q and of the sieve),
`|Σ_{Q∈𝓕_d^I, q | n(Q)} ψ(u_Q) − g_{c,d}(q) 𝔐_d| ≪_ε 𝓛^C q (#Λ(1))^{1/2} (A√d + F^{1+ε} d^{−1/2})^{1/2}`.
*Proof.* Cor 4.4 (separation, Lemma 2.2, holds for the subset `Λ̃(q)`), Lemma 6.1 for the main term, and
Prop 5.1 with `λ/Y ≍ A√d`, `q^{1/2}/(MY) ≍ F/(q^{1/2}√d)`, `λ²/Y ≤ λ/Y`; finally
`#Λ(q) = g(q)|SL₂(ℤ/q)| #Λ(1) ≪ q² #Λ(1)`. ∎

**Lemma 6.3 (class numbers; PROVED, standard).** `#Λ(1) ≤ 6·h(−4d)·r(d)` where `h(−4d) ≪ d^{1/2} log d`
is the number of SL₂(ℤ)-classes of forms of discriminant −4d and `r(d) ≤ 4·∏_{p^k∥d} p^{⌊k/2⌋}`.
Hence `Σ_{d≤D} #Λ_d(1) ≪ D^{3/2}(log D)^3`.
*Proof.* `#Λ(1) ≤ [Γ₀(d)∩Γ(2) : …]`-weighted count of pairs (SL₂-class `[Q₀]`, coset `γ ∈ Γ⁰(d)\SL₂(ℤ)`)
with `Q₀∘γ ∈ 𝓕_d`; the factor 6 = `[Γ₀(d) : Γ₀(d)∩Γ(2)] ≤ 6`. Cosets ↔ second columns `(t:s) ∈ ℙ¹(ℤ/d)`,
and `Q₀∘γ ∈ 𝓕_d` forces `Q₀(t,s) ≡ 0 (d)`. `𝓕_d` forms are primitive (`gcd(f, 4ad) = 1` since `ef − 4a²d = 1`; R1: `(f,e) = 1` is false in general).
For odd `p^k ∥ d` and primitive `Q₀ = [A,B,C]` with `p ∤ A` (WLOG after SL₂-change), points with
`p | s` give `Q₀ ≡ A t² ≢ 0`; points `(t:1)` need `(2At + B)² ≡ B² − 4AC ≡ 0 (p^k)`, i.e. t in one class
mod `p^{⌈k/2⌉}`: `p^{⌊k/2⌋}` points. For `p = 2` the same argument with `4A` gives `≤ 4·2^{⌊k/2⌋}`.
`Σ_{d≤D} r(d) d^{1/2} log d ≪ D^{3/2} (log D) Σ_{m} m/m^{3}·… ≪ D^{3/2}(log D)^3`. ∎

## 7. The complementary counts (PROVED, unconditional; Poisson + Weil)

Fix `c`, a squarefree `q` and smooth weights `W_i ∈ C_c^∞([1,2])`. 𝓛 = log N.

**Proposition 7.1 ((K_a): fixed a).** Let `(q, 2a) = 1`, `m = 4a²`, and
`S_a(q) := Σ_{e,f ≥ 1, ef ≡ 1 (m), q | n} W₁(e/E) W₂(d/D)`, `d := (ef−1)/m`, `n := 4acd − f`.
Assume `min(E,F) ≥ N^{c₀}` (R1: for tiny e the claimed density is false, e.g. a = c = 1, e = 3, q = 5).
Then `S_a(q) = g'_{c,a}(q) S_a(1)·(1 + O(N^{−10})) + O(𝓛^C τ(a)^C q · a)`, where
`g'_{c,a}(ℓ) = #{(e,f) ∈ 𝔽_ℓ² : f(ce − a) ≡ c}/ℓ² = (ℓ−1)/ℓ²` (ℓ ∤ c) resp. `1/ℓ` (ℓ | c), and
`S_a(1) ≍ D φ(m)/m` (main term `= (φ(m)/m²)∫∫W₁(e/E)W₂((ef−1)/(mD)) de df`).
*Proof.* For `(q,2a)=1`, `q | n ⟺ f(ce − a) ≡ c (q)` (multiply `a n = c(ef−1) − af` by `ā`). So
`(e,f)` runs over a set `𝒮 ⊂ (ℤ/mq)²` (CRT: `ef ≡ 1 (m)` times the curve `f(ce−a) ≡ c` mod q). Poisson
in `(e,f)` mod `mq`: `S = (mq)^{−2} Σ_{h,k} Ŵ(h/(mq), k/(mq)) Σ_{(e,f)∈𝒮} e((he+kf)/(mq))`,
`Ŵ(ξ,η) = ∫∫W₁(x/E)W₂((xy−1)/(mD)) e(−ξx−ηy)dxdy`. On the support `x ≍ E`, `y ≍ F := mD/E`, with
`∂_x^i∂_y^j ≪ E^{−i}F^{−j}`, so `Ŵ(h/mq, k/mq) ≪_B EF(1+|h|E/mq)^{−B}(1+|k|F/mq)^{−B}`. The complete
sum factors as `S(h',k';m)·T_q` with `|T_q| ≤ 3^{ω(q)} q`. `(h,k) = (0,0)`: the main term, which
factorises as `g'(q)×`(q = 1 term). `h = 0 ≠ k` (and symmetrically): `S(0,k';m) = c_m(k')`, and the
smooth k-sum of Ramanujan sums is `Σ_{δ|m} δμ(m/δ) Σ_{δ|k≠0} Ŵ(0,k/mq) ≪ 𝓛^C τ(m) q·E/m` (Poisson back in k;
the k = 0 term cancels against `Σ_{δ|m}μ(m/δ) = 0`); this is `≪ 𝓛^C τ(m) q D/F`. `hk ≠ 0`: Weil,
`|S(h',k';m)| ≤ τ(m)(h,k,m)^{1/2}m^{1/2}`, and there are `≪ 𝓛^2 (mq)²/(EF)` effective pairs (none if
`E` or `F > mq𝓛`), giving `≪ 𝓛^C τ(m)^2 3^{ω(q)} q m^{1/2}`. Total error `≪ 𝓛^C τ(a)^C q (a + D/F + D/E)`;
cells with `min(E,F) ≤ 𝓛^{C'}` are treated by Prop 7.2 instead. ∎
*Consequence.* Summing `|R|` over `a ≍ A` and `q ≤ Q`: `≪ 𝓛^C Q² A²` against the mass `≍ A D`: a level
`Q = (D/A)^{1/2}𝓛^{−C}` whenever `D > A`, i.e. `α < (1−γ)/2`.

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
(2b) Inside `R_bad(η₁)`, split each cell into sequences σ: fixed a if `D ≥ A` (Prop 7.1), fixed d if
`D < A` (Thm 6.2 with the cusp `f' = min(e,f)`, after splitting the x-range into `O(1)` periods when
`a/(qf') > 1/4`). This needs `f' ≥ A/8`. That fails only on the thin strip `a ≤ b < 8ca`
(`α ≤ β < α + γ + o(1)`, using `e = (a+b)/c`), whose mass per c-block `c ≍ 2^j` is `≪ N L j`; there BT
(saving `1/j`) costs `≪ Σ_{j≤ηL} N L ≪ η N L²`. With `f' = min(e,f) ≤ 2A√D`, the cusp term of Thm 6.2 is
`f'^{(1+ε)/2}/A ≪ N^{ε} D^{1/4}A^{−1/2}`, which has an **absolute** power margin near `α = (1−γ)/2`
(`≈ N^{−1/8+ε}`). Relative remainders per cell are then `≪ L^C Q²N^{−κδ}`, `δ := |2α − 1 + γ|`, with
an absolute κ > 0 (Prop 7.1: `Q²A/D`; Thm 6.2: `Q²(D/A)^{1/2}`).
(3) Sieve per sequence with `z = N^{θ}`, **`θ = κδ/8`** (R1: θ = κδ/4 made `Q²N^{−κδ}` with `Q = z²` equal
to 1), sieving only primes `ℓ > ℓ₀`, `ℓ ∤ 2cs` (`s ∈ {a,d}`): the remainder is `≪ L^C N^{−κδ/2}` times
the mass, and the main term is `≪ X_σ (2cs/φ(2cs))/(θ L)`. Here `Σ_σ X_σ s/φ(s) ≪ (count of the enlarged cell)
+ remainder`, and `s/φ(s) = Σ_{k|s}μ²(k)/φ(k)` with MN3 Prop 2.3 (`4k` resp. `4k²` in place of 4) gives
`≪ AD L` summed over the e-cells. The weight `c/φ(c)` is O(1) on average over c.
(4) Layers with `δ L ≤ C log L` are treated by BT: cost `≪ Σ_{j≤ηL} N L (log L)/j ≪ N L (log L)²`.
(5) All other cells cost `≪ (N L per (c-block j, a-layer k))·min(1/j, C/k)`, where k is the layer
distance from `α = (1−γ)/2`. Lemma 1.1 gives `≪ N L²`. ∎

*Status of the proof (honest; after the self-review R1 = `review` tool, 2026-10-09).* Every step above is either cited (ET, MN3, DI, Drappeau, Weil, Selberg's
sieve) or proved in §§2,4,6,7; §5's Prop 5.1 and §7's Prop 7.1 are written at the level of a careful
outline (the Bessel/Mellin bookkeeping and the Ramanujan-sum terms are standard but not written in full),
and the cell bookkeeping in (2)–(5) is not written with explicit constants. Step (2a) inherits MN3's unwritten "routine" BT harmonic sums.
So Thm 8.1 is a **conditional theorem with an outline-level proof**, not a finished proof. Hostile review
needed. R1 found 3 FATAL items (Prop 7.1 for tiny divisors; the spectral corner `β ≈ α`; the M2 densities)
and 5 MAJOR items (parity group for even d; density signs; the domain of Prop 5.1; the sieve level eating the
saving; the Eisenstein terms for χ ≠ 1). All are addressed above by restricting domains, re-routing cells, or
correcting formulas. They have not been re-reviewed.

## 9. What is unconditional, and where (SEL) enters

* Everything except Prop 5.1's treatment of exceptional eigenvalues is unconditional. With exceptional
  eigenvalues `λ = 1/4 − σ²` the unfolded coefficient picks up `(nY)^{−σ}`; with Kim–Sarnak `σ ≤ 7/64` the
  spectral error is multiplied by `Y^{−7/64} = (qF'√d)^{7/64}`, which kills the saving `(D/A)^{1/2}` on a strip
  `0 < 2α − 1 + γ ≲ 0.1`; DI Thm 5 (with `X = 1/Y`) and DI Thm 6 (average over the level) were checked
  (§3.2) and also fail at `α = 1/2`. Humphries' density theorem (ANT 12 (2018), Thm 1.5:
  `N(σ) ≪ vol^{1−4σ+ε}`) with the pointwise coefficient bound loses `N₀ = F'/A`, again failing near
  `α = 1/2`. **So unconditionally the method leaves a strip of positive width in `α`, which still costs a
  `log log N`.** Removing it needs either Selberg's conjecture (exactly, not a numerical approximation of it),
  or a weighted large sieve for exceptional eigenvalues at `X ≈ 1/Y` with no loss, or a beyond-Weil bound for
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
