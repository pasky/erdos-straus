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
