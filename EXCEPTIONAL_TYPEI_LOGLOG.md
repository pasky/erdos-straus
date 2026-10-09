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
