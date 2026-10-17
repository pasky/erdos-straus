# BALANCED_LATTICE — from Hypothesis W to GRH? Balanced relation lattices of small primes mod q (task O256)

Status: O256 checkpoint 1 (unreviewed). **ES is not solved here, nor any infinite case of ES.** A bounded or slowly growing
cap is NOT ES: cap 0 is the B2 divisor event (FORCED_WINDOW Prop 2.1, Prop 4.5); everything below is about cap ≥ 1.
Labels as in DISCOVERIES.md. Builds on FORCED_WINDOW (O252: Lemma 1.1, Prop 1.2, Prop 4.1, Def 4.2, Hyp W, Thm 4.3,
Cor 4.4, Prop 5.1, Prop 5.2), CAP_INTERPOLATION Thm 4.2, BRAINSTORM/z12_grh_lattice_gap. Scripts `scripts/z27_*`, memos
`BRAINSTORM/z27_*.md`.

Notation. q prime, q ≡ 3 (mod 4), N := (q − 1)/2 (odd), U_q := (F_q^*)² cyclic of order N. S a set of k odd primes ≠ q,
g_s := s², H := ⟨g_s : s ∈ S⟩ ≤ U_q, Λ = Λ_q(S) := {x ∈ ℤ^S : ∏ g_s^{x_s} = 1} (det Λ = |H|), Λ* := {y ∈ ℝ^S : y·x ∈ ℤ ∀x ∈ Λ}.
For ψ ∈ Ĥ write ψ(g_s) = e(θ_s(ψ)), θ_s ∈ ℝ/ℤ. ‖·‖ = distance to ℤ. μ_∞(Λ) := inf{r : Λ + [−r, r]^S = ℝ^S}.
L_min(q) := least L with W_L := {∏ g_s^{j_s} : 0 ≤ j_s ≤ L} = U_q (FORCED_WINDOW Prop 4.1; ∞ if H ≠ U_q).

## 0. Iteration log

(I1) *Brief's route: certify balance by Frobenius in Kummer fields.* §1 turns balance into a statement about ALL characters of
U_q (ℓ¹-pretentious distance to 1 on S). §2: Frobenius of q in ℚ(ζ_m, S^{1/m}) sees exactly the characters of order dividing
m; under GRH (Lagarias–Odlyzko) one certifies "no ε-pretentious character of order ≤ M" for a positive proportion of q in
the class, but only up to M = x^{O(1/k)}. Barrier: the characters of order ≤ M are a fraction ≤ M²/N of all characters, and
the extremal (balance-deciding) character has order ≍ N in practice (§6). Hypothesis violated by the brief's route:
"imbalance is driven by small-order (index) obstructions".

## 1. Exact dictionary: balance ⟺ no nontrivial character is ℓ¹-pretentious to 1 on S

**Lemma 1.1 (dual lattice = character group; PROVED, standard).** The map ψ ↦ θ(ψ) := (θ_s(ψ))_{s∈S} + ℤ^S is an isomorphism
Ĥ ≅ Λ*/ℤ^S. In particular ℤ^S ⊂ Λ* with index |H|, and a vector y ∈ Λ* ∖ ℤ^S is the same thing as a nontrivial character ψ of H
together with a choice of real lifts θ_s ∈ ℝ of its angles.
*Proof.* x ↦ g^x := ∏ g_s^{x_s} induces ℤ^S/Λ ≅ H. Characters of ℤ^S are x ↦ e(y·x), y ∈ ℝ^S/ℤ^S; such a character factors
through ℤ^S/Λ iff y·x ∈ ℤ for all x ∈ Λ, i.e. y ∈ Λ*. The factored character is ψ with ψ(g_s) = e(y_s). ∎

**Definition 1.2 (ℓ¹-pretentious distance on S).** For ψ ∈ Ĥ put 𝔻_S(ψ) := Σ_{s∈S} ‖θ_s(ψ)‖ (the least ℓ¹-norm in the coset
θ(ψ) + ℤ^S), and 𝔻_min(q) := min_{ψ ≠ 1} 𝔻_S(ψ). (Compare Granville–Soundararajan's 𝔻(χ, 1; y)² = Σ_{s≤y}(1 − Re χ(s))/s:
here the weights are flat, the angle enters linearly, and only the k primes of S count.)

**Proposition 1.3 (transference; PROVED, Banaszczyk + elementary).** With λ₁^{(1)}(Λ*) = min(1, 𝔻_min(q)):
`  1/(2 min(1, 𝔻_min))  ≤  μ_∞(Λ)  ≤  k^{3/2}/(2 min(1, 𝔻_min)).`
Consequently (FORCED_WINDOW Prop 4.1): if H = U_q then L_min(q) ≤ ⌈k^{3/2}/min(1, 𝔻_min)⌉, and always L_min(q) + 1 ≥
1/min(1, 𝔻_min) (when finite).
*Proof.* Lower: let y ∈ Λ* ∖ {0} and z ∈ ℝ^S with y·z ≡ ½ (mod 1). If z = λ + b with λ ∈ Λ, b ∈ [−r, r]^S, then y·b ≡ ½
and |y·b| ≤ r|y|₁, so r ≥ 1/(2|y|₁). Nonzero vectors of Λ* are either in ℤ^S (|y|₁ ≥ 1) or lifts of ψ ≠ 1 (|y|₁ ≥ 𝔻_S(ψ)).
Upper: μ_∞ ≤ μ_2 ≤ k/(2λ₁^{(2)}(Λ*)) (Banaszczyk, *Math. Ann.* 296 (1993), Thm 2.1: μ_2(Λ)·λ₁(Λ*) ≤ k/2) and
λ₁^{(2)} ≥ λ₁^{(1)}/√k. Prop 4.1(i) of FORCED_WINDOW needs μ_{(L,…,L)} ≤ 1, i.e. μ_∞ ≤ L/2; Prop 4.1(ii) gives μ_∞ ≤ (L+1)/2
when W_L = U_q. ∎
**Corollary 1.4 (scales; PROVED).** (a) (Minkowski for the cross-polytope, vol = 2^k r^k/k!) 𝔻_min(q) ≤ (k!/|H|)^{1/k}
≤ (k/e)(e k)^{1/(2k)}|H|^{−1/k}: some nontrivial character is always ℓ¹-pretentious at scale k|H|^{−1/k}.
(b) Hence **q is balanced at the random-lattice scale (L_min ≤ k^{O(1)}N^{1/k}) ⟺ (up to k^{O(1)}) no ψ ≠ 1 of U_q has
𝔻_S(ψ) ≤ N^{−1/k}k^{−C}**, i.e. the Minkowski-extremal character is not much more pretentious than forced by pigeonhole.
(c) Exact zero: 𝔻_S(ψ) = 0 for some ψ ≠ 1 ⟺ H ≠ U_q ⟺ for some prime ℓ | N all s ∈ S are ℓ-th powers mod q (the index
obstruction of FORCED_WINDOW Prop 5.2).
*Proof.* (a) Minkowski's first theorem: a symmetric convex body of volume > 2^k·det(Λ*) = 2^k/|H| contains a nonzero point
of Λ*; the ℓ¹-ball of radius r has volume (2r)^k/k!; Stirling. (b) Prop 1.3. (c) ψ ≠ 1 trivial on all g_s ⟺ H ⊂ ker ψ ⊊ U_q;
take ψ of prime order ℓ (U_q cyclic). ∎
*Reading.* Balance is a *quantitative non-pretentiousness of all characters of U_q on the k forced primes*, at the
Diophantine scale N^{−1/k} (not at a fixed scale: FORCED_WINDOW Prop 1.3). The index obstruction is the degenerate case
𝔻 = 0 and involves only characters of prime order; balance in general is decided by the **order** of the extremal character
ψ_min, which is the parameter that governs Frobenius-visibility (§2).
