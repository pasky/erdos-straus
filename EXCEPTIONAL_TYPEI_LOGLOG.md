# EXCEPTIONAL_TYPEI_LOGLOG — attacking ET's open Type I bound Σ_{p≤N} f_I(p) ≪ N log² N (task O111)

Status labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6 (`sources/elsholtz-tao-1107.1010.pdf`);
MN3 = `EXCEPTIONAL_MN3.md` (§3 there: the obstruction region R_bad / R**, Lemma 3.1, Thm 3.8);
DI = Deshouillers–Iwaniec, Invent. Math. 70 (1982) 219–288. `L = log N`.

## 0. Summary (work in progress; updated as lemmas are added)

* Literature (2026-10, search-limited, research subagent + own check): no removal of ET's `log log N` found.
  ET v6 cites Jia, Sci. China Math. 55 (2012) 465–474 ("mean values … 4/p"), yet still states the Type I
  `log log N` as open (ET p. 5); Jia's text was not accessible (abstract only).
* Lemma 2.2 (PROVED, elementary): the level-d Heegner points of MN3 Lemma 3.1 are **uniformly separated**
  in the hyperbolic plane: distinct points satisfy `cosh dist ≥ 3/2`, independently of d.
  (Numerically the minimum is ≥ 3: `scripts/ttl_separation.py`.)
* Plan (§3): per-d count = (#classes)·(mean of an automorphic Poincaré-type function) + error, with the
  error bounded by Cauchy–Schwarz in a Sobolev norm: `‖Σδ_z‖_{H^{-2}}² ≪ #classes` (by separation) times
  the variance of the counting function (by the DI large sieve). Heuristic outcome: relative error
  `(d/a)^{1/2}`, complementary to MN3's (K_a) (relative error `a/d`).

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
`α = (1−γ)/2`** — harmless by Lemma 1.1. EVIDENCE that the per-d errors are no larger than this:
`scripts/ttl_perd.py` (`.out.txt`).

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
`ψ(u) = φ(x/λ) W(y/Y)`, `φ, W ∈ C_c^∞`, `supp φ ⊂ [−2,−1]`, `supp W ⊂ [1,2]`, `0 < λ ≤ 1/4`, `Y ≤ 1`.
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
`δ_{𝔠∞}y^{1/2+it} + φ_{𝔠∞}(½+it) y^{1/2−it}` (only for χ = 1).
(4) `n = 0`: `|∫W(y/Y)y^{1/2±it}dy/y²| ≤ Y^{−1/2}|Ŵ(t)|` with `Ŵ` rapidly decreasing; the scattering
matrix is unitary on the critical line, so the n = 0 part contributes `≪ λ²/Y`.
(5) `n ≠ 0`: `|n| ≤ 𝓛/λ` up to a negligible tail (φ̂ decays rapidly), so `2π|n|y ≤ 4π𝓛Y/λ`. If
`Y/λ ≥ 𝓛^{−2}` the claim is trivial from (6) below with `N₀ ≤ 𝓛³`; otherwise expand
`K_{it}(x) = ½Σ_± Γ(±it)(x/2)^{∓it}(1 + O(x²))`. Then
`⟨P,u_j⟩ = Σ_± ½Γ(±it_j)π^{∓it_j} Y^{−1/2∓it_j} Ŵ_±(t_j) Σ_n ρ̄_j(n) λφ̂(λn)|n|^{∓it_j} + (O((𝓛Y/λ)²)-terms of the same shape)`,
with `|Γ(it)|² = π/(t sinh πt)` and `Ŵ_±` rapidly decreasing, so only `|t_j| ≤ K = 𝓛` matters.
(6) The `|n|^{∓it_j}`: split `t_j` into unit intervals `[k, k+1]`; for `t = k+τ`,
`sup_{τ∈[0,1]} |S(τ)|² ≤ |S(0)|² + ∫_0^1 (|S|² + |S'|²) dτ` with `S'` having coefficients multiplied by
`−i log|n| = O(𝓛)`; apply the large sieve to each fixed-τ coefficient vector `b_n = λφ̂(λn)|n|^{−ik−iτ}`
(`‖b‖² ≪ λ²·(𝓛/λ) = 𝓛λ`) on dyadic n-ranges `N₀ ≤ 𝓛/λ`, sum over `≪ 𝓛` intervals and `≪ 𝓛` dyadic
ranges. With `|Γ(it)|²cosh(πt) ≍ 1/(1+|t|)` this gives
`Σ_χ Σ_j |⟨P,u_j⟩|² ≪ (φ(q)/2)·𝓛^C Y^{−1}·λ·(1 + q^{1/2}M^{−1}(𝓛/λ)^{1+ε})`, and the same for the
Eisenstein part. Multiply by `2/φ(q)`. ∎
*Remark.* `(λ/Y)·q^{1/2}M^{−1}λ^{−1} = q^{1/2}/(MY) = F/(q^{1/2}√d)` (since `1/Y = qF√d`, `M = dq²`):
this is the "cusp" term `1/(Y·level)` of §3.
