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

Strong support dependence (η grows with L; the needed support grows with
N, consistent with Lemma 2.3). Optimal R (N = 30): reflection-symmetric,
≈ 0 on W, ≈ 11.4 mass in each half of Z peaking at height ≈ 1.15 at
distance ≈ N/3 from the window, remaining ≈ 7 spread thinly up to |x| ≈ 16N.
