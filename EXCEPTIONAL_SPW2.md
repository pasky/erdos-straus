# EXCEPTIONAL_SPW2 — weak SPW (task O53)

Status: **in progress (O53).** Labels as in `DISCOVERIES.md`. Notation as in
`EXCEPTIONAL_SPW.md` (SPW1) and `EXCEPTIONAL_INTERFREQ2.md` (IF2): N ≥ 2,
D = ⌊N/2⌋, W = λ_N = 1_{[1,N]}, c(b,d) = #{1 ≤ n ≤ N : n ≡ b (d)},
L₀ = lcm(1..D), S_A = C_A(log N)^{3/4}(log log N)^{3/4} (IF Thm 2.5; the
log log factor may be dropped by KARY3, DISCOVERIES (D)24).

## 1. Exactly what Theorem 5.2 needs

**Lemma 1.1 (exact quantitative requirement; PROVED implication).** Suppose
that at every large N there is R ≥ 0 on ℤ with (P1) of SPW, and with
`R(s) ≤ 1 − η_N` on classes of modulus > CN meeting [1,N], `R(s) ≤ K_N` on
classes of modulus > CN missing [1,N], and `|R(s) − c(s)| ≤ Δ′_N` on classes
of modulus in (N/2, CN] (C fixed, η_N ≤ 1/2 ≤ K_N). Put
`ℓ_N := log(K_N/η_N) + log(1 + Δ′_N/K_N)`. Then every hybrid bound B
(IF2 Def 1.2) for 𝒜(𝔊) with `T_mid ≤ c·B` satisfies, for N ≥ N₀,

    log(N/B) ≤ C′(log N)^{3/4} + ℓ_N + log(1 + c) + O(1)

as long as `η_N/K_N ≥ N^{−A₁}` (C′ depending on A, A₁, C). In particular:
* `ℓ_N ≤ C(log N)^{3/4}` ⇒ the 3/4 cap (same shape as KARY3);
* `ℓ_N ≤ (log N)^θ`, θ ∈ (3/4, 1) ⇒ a θ-cap (savings ≤ (log N)^θ(1+o(1)));
* `ℓ_N ≍ c log N` (σ_N = N^{−c}) gives only `B ≥ N^{1−c−o(1)}`, i.e. **no
  cap of the form (log N)^θ, θ < 1** — polynomially small σ does *not*
  suffice for anything ES-relevant.

*Proof.* SPW1 Lemma 1.4 turns R into SPW(C, σ, Δ₀) with σ = η/(2K),
Δ₀ = Δ′/(2K) (mix `(1 − 1/(2K))λ_N + R/(2K)`). IF2 Prop 9.1 gives Flat with
θ = σ/(2(σ + τ + 1/(2C))) ≍ σ, t = θ/2, s₀ = σ/2, Δ = 6θ + Δ₀. IF2 Thm 5.2
(its proof: s₀ enters only through `log T_{>CN} ≤ log(N/s₀) + O(1)` in the
level, so s₀ ≥ N^{−A₁} costs a constant in S′) gives
`log(N/B) ≤ S′ + log((1 + Δ(1+c))/t)`, and
`log(1/t) + log(1 + Δ(1+c)) ≤ log(K/η) + log(1 + Δ′/K) + log(1+c) + O(1)`. ∎

So the target is: **a measure with exact small-modulus window profile in
which every full large class loses a fraction η_N, with sparse large classes
allowed mass K_N, and log(K_N/η_N) = O((log N)^{3/4})** (weak SPW). SPW1
Thm 3.2 forces η_N/K_N ≲ (log N)^{−1/2}, harmless.

## 2. The relaxed problem RSPW and first numerics

**Definition 2.1.** RSPW(C, η, K) at N: R ≥ 0 on ℤ with (P1), `R(s) ≤ 1 − η`
on every class of modulus > CN meeting [1,N] ("full"), `R(s) ≤ K` on every
class of modulus > CN missing [1,N] ("sparse"). (Medium classes: measured,
not imposed; Lemma 1.1 only needs Δ′ ≤ K·e^{O((log N)^{3/4})}.)
By Lemma 1.1, RSPW with η fixed and K ≤ e^{O((log N)^{3/4})} gives the cap.

**Lemma 2.2 (the near zone is invisible; PROVED).** A class of modulus
e > CN through n₀ ∈ [1,N] contains no point of the *near zone*
`Z := [N − CN, 0] ∪ [N+1, CN+1]` (C ≥ 1). *Proof.* Its other points are
n₀ ± je, j ≥ 1, and n₀ + e ≥ CN + 2, n₀ − e ≤ N − CN − 1. ∎
So in RSPW, points of Z are constrained only by sparse classes (≤ K) and
(P1); in particular **SPW1 Lemma 9.3 (σ ≤ 2/5) disappears once K ≥ 3/2**
(its 5 lifts include 2 sparse ones). SPW1 Thm 3.2's Fejér argument still
applies: with ρ_e ≤ K off W, T(x_in) ≤ −η + (K+1)e/(2(M+1)r); and instead
of |T| ≤ 1 use |T̂(k)| ≤ Σρ_e + N = 2N, so T (degree < m₀) has
‖T‖_∞ ≤ 4m₀N/e and ‖T′‖_∞ ≤ 8πm₀²N/e², independent of K. Optimising r
gives `η ≲ m₀√(K/M)`, i.e. **K ≳ η²·log N/m₀²** is forced (PROVED, same
proof with these two changes). This is harmless for Lemma 1.1 (σ = η/(2K) ≍ 1/log N
if η fixed).

**Lemma 2.3 (near zone alone cannot work for N > 40; PROVED).** If R − λ_N
is supported in an interval of length ℓ, then either R = λ_N or
ℓ > Φ(D) := Σ_{d≤D} φ(d) (≈ 0.304 D²). *Proof.* f = R − λ_N has zero class
sums mod every d ≤ D iff F(z) = Σ f(x)z^x vanishes at every root of unity of
order ≤ D, i.e. ∏_{d≤D}Φ_d(z) | F(z) (Laurent), degree Φ(D). ∎
(Φ(D) > 3N already for D ≥ 12–13.) So far mass (at distance ≫ CN) is
unavoidable; it must be spread over the lines n₀ + eℤ.

**Numerics (EVIDENCE; `scripts/spw2_relaxed_lp.py`, HiGHS, support
[−L, N+L], C = 2, medium unconstrained).**

| N | L | K | η | max sparse class | max medium dev |
|---|---|---|---|---|---|
| 12, 16 | 8N | ∞ | 1.000 (R = 0 on W, all mass in Z) | — | — |
| 20 | 8N | ∞ | 0.955 | | |
| 30 | 16N | ∞ / 1.5 | 0.861 / 0.860 | 1.73 / 1.50 | 2.58 / 2.36 |
| 50 | 4N / 8N / 16N | ∞ | 0.482 / 0.675 / 0.755 | 1.60 (16N) | 2.32 |
| 50 | 16N | 1.5 | 0.754 | 1.50 | 2.31 |
| 80 | 4N / 8N / 16N | ∞ | 0.303 / 0.512 / 0.663 | | |
| 12–20 | 8N | 1 | 0.667 (= Lemma 9.3 with K = 1) | | |
| 30 | 64N / 128N | ∞ | 0.893 / 0.905 (R = 0 on W; far mass ≈ 5.5) | | |
| 50 | 32N / 64N | ∞ | 0.798 / 0.820 (far mass ≈ 15) | | |

(`scripts/spw2_relaxed_fast.py` = vectorised K = ∞ version, same values;
data/spw2/relaxed_Lscan.txt.) Every finite-support optimum is a genuine
measure on ℤ, so e.g. at N = 50 RSPW(2, 0.82, K ≈ 1.6) holds, hence
SPW(2, ≈ 0.25) via SPW1 Lemma 1.4 (EVIDENCE: floating-point LP, not
re-verified in exact arithmetic).

Strong support dependence (η grows with L; the needed support grows with
N, consistent with Lemma 2.3). Optimal R (N = 30): reflection-symmetric,
≈ 0 on W, ≈ 11.4 mass in each half of Z peaking at height ≈ 1.15 at
distance ≈ N/3 from the window, remaining ≈ 7 spread thinly up to |x| ≈ 16N.

## 3. RSPW also degenerates, but only like (log N)^{−1/3}

**Theorem 3.1 (K-free edge bound; PROVED).** Let C > 1, M, e, m₀ be as in
SPW1 Thm 3.2 (e the least multiple of L_M = lcm(1..M) exceeding CN,
m₀ = e/D). If R ≥ 0 has (P1) and `R(s) ≤ 1 − η` on every class of modulus
e meeting [1,N] (no condition at all on other classes), then for every
integer 1 ≤ r < min(N−1, (C−1)N−1)/2

    η ≤ eN/(4(M+1)r²) + e/((M+1)r) + 4πm₀²N(2r+1)/e².               (3.1)

With r = ⌈N·M^{−1/3}⌉ this gives **η ≤ c(C)·M^{−1/3} ≍_C (log N)^{−1/3}**,
uniformly in K (sparse classes, near zone and medium classes unrestricted).

*Proof.* As in SPW1 Thm 3.2: ρ = projection of R to ℤ/e, W = {1..N} ⊂ ℤ/e,
K = Fejér kernel of degree M on ℤ/e (K(t) ≤ e/(4(M+1)t²) for 1 ≤ |t| ≤ e/2),
φ = K∗1_W, τ := e/(2(M+1)r). T = K∗(ρ − 1_W) has Fourier support in
|k| < m₀ (frequencies m₀ ≤ |k| ≤ M are pinned by (P1)). Now ρ ≤ 1 − η only
on W, so: (a) |T̂(k)| ≤ |ρ̂(k)| + |1̂_W(k)| ≤ 2N, hence
T(x) = (1/e)Σ_{|k|<m₀}T̂(k)e(kx/e) has |T(x) − T(y)| ≤ 4πm₀²N|x − y|/e².
(b) x_in = 1 + r: every y ∉ W is at cyclic distance ≥ r + 1 from x_in
(the far side is at distance ≥ min(N − r, e − N + r) > r), so
Σ_{y∉W}K(x_in − y)ρ(y) ≤ (e/(4(M+1)r²))Σρ = eN/(4(M+1)r²) =: A, and
T(x_in) ≤ (1 − η)φ(x_in) + A − φ(x_in) ≤ −η + ητ + A ≤ −η + τ + A, using
φ(x_in) ≥ 1 − τ (SPW1 tail bound). (c) x_out = −r: T(x_out) ≥ −φ(x_out) ≥ −τ.
So η ≤ T(x_out) − T(x_in) + A + 2τ, and (a) with |x_out − x_in| = 2r + 1
gives (3.1). For r = ⌈NM^{−1/3}⌉, e ≤ (C+1)N: the three terms are
O_C(M^{−1/3}), O_C(M^{−2/3}), O(m₀²M^{−1/3}/C²). ∎

So RSPW with fixed η is false for large N even with K = ∞, but the decay is
only (log N)^{−1/3}; weak forms (η_N ≥ e^{−(log N)^{3/4}}) are untouched.

## 4. Dual picture and where a proof (or refutation) must act

**Lemma 4.1 (dual of RSPW with K = ∞; PROVED, finite LP duality on ℤ/Q′
plus SPW1 Lemma 1.1).** On the periodic model, the optimal η is

    η* = 1 − sup { −Σ_{n≤N} g(n) / Z : g ∈ V_D, z ≥ 0 on full classes of
                    modulus > CN, g + Σ z_s 1_s ≥ 0,  Z = Σ z_s }.

In particular η* = 0 iff there is ν = g + P ≥ 0 (g a small-modulus
combination, P ≠ 0 a nonnegative combination of *full* large classes)
with ν ≡ 0 on [1,N]. (IF2 Example 3.2 is such a ν, but at the medium
modulus N + 1.) Weak duality direction is elementary:
Σ_x R ν = Σ_W g + Σ z_s R(s) ≥ 0.

Consequences for certificates (PROVED, by Lemma 2.2): ν must vanish on W and
be ≥ 0 on the near zone Z, where P ≡ 0; so g ≥ 0 on Z, g = −P ≤ 0 on W.

**Assessment 4.2 (heuristic dichotomy; not proved).** Write R = R_Z + R_F
(near / far, R ≈ 0 on W as in all LP optima).
* *Near part.* R_Z − W has Fourier transform E(α), a trigonometric
  polynomial of degree ≲ 2CN. Farey points of order D are a sampling set at
  that scale except within ≍ 1/(qD) of a/q, q ≲ 8C. The η-jump of R − W at
  each edge puts ≍ η²D energy of E into the dense part, hence (large-sieve
  heuristic, ≈ 0.3D² samples per unit frequency) Σ_{F_D}|E|² ≳ cη²D³.
  So the far part must carry F_D-content of ℓ²-size ≳ ηN^{3/2}.
* *Spread far part.* A far part with density profile "smooth envelope ×
  bounded weights" carries F_D-content of ℓ²-size ≲ (its mass) ≤ N
  (random-design/min-norm computation; the same mechanism as SPW1 Prop 2.3).
  This alone would force η ≲ N^{−1/2}.
* *Structured far part.* Content can also be carried coherently (mass at x
  with x ≡ edge mod many d); but coherence mod d and d′ puts x on the full
  line through the edge point of modulus lcm(d,d′) > CN, and a
  Cauchy–Schwarz count over pairs (d,d′) again gives η ≲ √(λ/D) (λ = line
  capacity) for *exact* coherence. Partial coherence (x ≡ edge + small mod d)
  escapes this count — it is exactly what near-zone mass does, and far
  points can do it only with a bias of size ≍ η in Σ_d cos(2π(x−c)/d), whose
  positivity again costs ≍ 1/√D.

So all *natural* construction mechanisms point to a barrier at η ≍ N^{−1/2},
which would **refute** weak SPW (Lemma 1.1 needs η_N/K_N ≥ e^{−O((log N)^{3/4})}).
The LP values (η ≈ 0.9, 0.82, ≥ 0.73 at N = 30, 50, 80) are not in
conflict (the heuristic constants give ≈ 6/√D ≥ 0.9 there). Nothing here is
proved; the rigorous obstruction is only Thm 3.1 ((log N)^{−1/3}).
