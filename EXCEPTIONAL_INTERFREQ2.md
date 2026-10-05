# EXCEPTIONAL_INTERFREQ2 — hybrid methods: small classes exact, large classes trivial (task O25)

Status: **in progress (O25).** Labels follow `DISCOVERIES.md`. PROVED means
proved in this file, internal checks only. No θ > 3/4 is claimed. Notation
as in `EXCEPTIONAL_INTERFREQ.md` (IF below), `EXCEPTIONAL_KARY2.md` (K2).

## 1. The hybrid class, precisely

Fix N ≥ 2. For a finite representation
`ν = Σ_i a_i 1[n ≡ b_i (mod d_i)]` split the index set into
`𝒮 = {i : d_i ≤ N/2}` (small) and `𝓛 = {i : d_i > N/2}` (large), and write
`ν_𝒮, ν_𝓛` for the two partial sums. For a class `b mod d` put
`c(b,d) = #{1 ≤ n ≤ N : n ≡ b (d)}`, so `l(d) := ⌊N/d⌋ ≤ c(b,d) ≤ ⌈N/d⌉ =: u(d)`
and both values occur.

**Definition 1.1 (position-blind charge).** A function β(a,d) is a
*position-blind charge* if `β(a,d) ≥ a·c(b,d)` for every residue b. The
least one is `β*(a,d) = a·u(d)` for a > 0 and `a·l(d)` for a < 0.
For d > N this is "a class meets [1,N] at most once" (charge a⁺);
for N/2 < d ≤ N "once or twice".

**Definition 1.2 (hybrid method).** A *hybrid method* for an avoider set
𝒜 ⊂ ℤ takes a majorant ν (ν ≥ 0 on ℤ, ν ≥ 1 on 𝒜) with a representation,
evaluates the small part by *any* valid upper bound for `Σ_{n≤N}ν_𝒮(n)`
(the exact value being the least possible), and charges each large term a
position-blind charge. Its bound satisfies

    B ≥ B_hyb(ν) := Σ_{n≤N} ν_𝒮(n) + Σ_{i∈𝓛} β*(a_i, d_i) ≥ Σ_{n≤N} ν(n).   (1.1)

The usual form `N/d + O(1)` (IF Rem 2.6: charge `a_iN/d_i + |a_i|`) is a
position-blind charge, hence dominates β*. A cutoff `D_s < N/2` is also
covered: classes in `(D_s, N/2]` charged blindly cost at least their exact
count. So it suffices to bound

    H*(N; 𝒜) := inf_{ν, representation} B_hyb(ν).

## 2. LP duality for H*

**Lemma 2.1 (projection; PROVED).** Let 𝒜 be Q-periodic. Replacing ν by its
conditional average ν̄ mod Q (K2 Cor 6.1 proof: `a1[b (d)] ↦ a(d'/d)1[b (d')]`,
`d' = gcd(d,Q)`) gives a majorant of 𝒜 with `B_hyb(ν̄) ≤ B_hyb(ν)`.

*Proof.* The class `b mod d'` is the disjoint union of the `d/d'` classes
`b + kd' mod d` (k mod d/d'), so `c(b,d') = Σ_k c(b+kd',d)`. Hence
`(d'/d)c(b,d')` is the average of the lifted counts, so it lies in
`[l(d), u(d)]`. If `d' ≤ N/2` the new term is small and evaluated
exactly: `a(d'/d)c(b,d') ≤ β*(a,d)` for both signs of a. If `d' > N/2`,
`max_b c(·,d') ≤ (d/d')u(d)` and `min_b c(·,d') ≥ (d/d')l(d)`, so
`β*(a(d'/d), d') ≤ β*(a,d)`. Small terms stay small (`d' ≤ d`) and the exact
count of `(d'/d)1[b (d')]` is the average of the counts of its lifts. ∎

**Proposition 2.2 (dual of the hybrid; PROVED).** Let 𝒜 be Q-periodic and
`λ_N(n) = #{1 ≤ m ≤ N : m ≡ n (Q)}` on ℤ/Q. Then

    H*(N; 𝒜) = max { μ(𝒜) :  μ ≥ 0 on ℤ/Q;
                      μ(s) = λ_N(s)              for every class s mod d | Q, d ≤ N/2;
                      l(d) ≤ μ(s) ≤ u(d)          for every class s mod d | Q, d > N/2 }.

*Proof.* By Lemma 2.1 the infimum may be taken over representations with
all moduli dividing Q; this is a finite LP. ν ≥ 0 and ν ≥ 1 on 𝒜 is
`ν ≥ 1_𝒜` pointwise on ℤ/Q. Write large coefficients as `a⁺ − a⁻`
with cost `u a⁺ − l a⁻`. The primal is feasible (ν ≡ 1) and the dual is
feasible (μ = λ_N, since `λ_N(s) = c(b,d) ∈ [l,u]` for d | Q). The dual
variable of `ν(n) ≥ 1_𝒜(n)` is μ(n) ≥ 0; a free small coefficient gives an
equality, `a⁺` gives `μ(s) ≤ u(d)`, `a⁻` gives `μ(s) ≥ l(d)`. Finite LP
duality. ∎

So a cap for hybrid methods is the same as a measure μ ≥ 0 that agrees
with the interval on small classes, is *position-blindly* consistent with
it on large classes, and puts mass `≥ N e^{−O(S)}` on 𝒜.
