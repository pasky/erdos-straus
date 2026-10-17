# z27_pretentious_dual — balance of q ⟺ no character of U_q is ℓ¹-pretentious to 1 on S; Frobenius sees only small orders (O256)

**Idea.** Read the relation lattice Λ_q(S) through its dual: Λ*/ℤ^S ≅ Û_q (angles θ_s(ψ) of ψ(s²)). Covering radius ≍ 1/𝔻_min,
𝔻_min := min_{ψ≠1} Σ_s ‖θ_s(ψ)‖ (BALANCED_LATTICE Lemma 1.1, Prop 1.3: within k^{3/2}). Then ask which characters Frobenius sees.
**Literature.** Banaszczyk, *Math. Ann.* 296 (1993) (transference μ·λ₁* ≤ k/2); Granville–Soundararajan pretentious distance
(here flat ℓ¹ weights on k primes); Kummer theory / Hooley's Artin argument (Moree, *Integers* 12A (2012) survey);
Lagarias–Odlyzko 1977 (GRH Chebotarev).
**Barrier screen.** B1: forcing is congruence data, balance provably is not (Prop 2.2 indistinguishability: data of q in
ℚ(ζ_m, S^{1/m}), m ≤ M, is a function of the discrete logs mod the M-smooth part of (q−1)/2; a fake with the same data has
L_min ≥ (M-rough part) − 1). B2/B3/B5/B6: see BALANCED_LATTICE §5 (cap ≥ 1 only; T1-step false at squares).
**Cheap numerics** (`scripts/z27_dual.py`, data/z27/dual_1e6.txt, dual_1e7.txt; k = 3, 4, 5; q ≤ 10⁶ and q ∈ [9·10⁶, 10⁷]).
Conditioned on generation (𝔻_min > 0): the extremal character ψ_min has order exactly N in ≈ 75 % of q, order ≥ N^{0.9} in ≈ 87 %, order ≤ N^{1/2} in ≤ 0.3 %, order
≤ N^{3/(2k+4)} (nominal small-order range) in ≤ 0.07 %; P⁺(N) | ord ψ_min in 99.4–100 %. ν = 𝔻_min N^{1/k} quantiles match the uniform-random
discrete-log model to two decimals.
**Assessment.** PROVED dictionary + PROVED (abstract-vector) indistinguishability + EVIDENCE: the balance-deciding character is (almost always)
of order ≍ N, outside every Kummer field of manageable degree. The brief's Hooley-type route ("imbalance = small-ℓ index
obstruction + large-ℓ tail") is the wrong picture for balance: index obstructions are the measure-zero corner 𝔻 = 0.
