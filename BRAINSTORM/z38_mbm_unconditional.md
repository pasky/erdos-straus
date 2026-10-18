# z38_mbm_unconditional — the BM-corrected singular series is ≫ (log p)² unconditionally (O268)

**Idea.** O260 spark 2 / R277 D2: (L) at full strength. Replace M_gen (all real characters; GRH gives only log log p) by the
geometric M_BM(p) = Σ_{𝒫(p)} (1 − (−uB/p))/φ(4uB) (principal + Brauer character, z38_brauer_character), in which the
arithmetic of p is a single Legendre symbol of the product uB.

**Result.** Thm 2.2 (PROVED, unconditional): M_BM(p) ≥ (1/(32π²) − o(1))(log p)² by Pólya–Vinogradov, ≥ (25/(128π²) − o(1))
(log p)² ≈ 0.0198 (log p)² by Burgess; M₀(p) ~ (3/(2π²))(log p)² ≈ 0.152 (log p)². Proof: positivity of every pair term,
restriction to u odd ≤ p^δ, B = 2B′ ≤ p/(4u), Möbius for gcd(B′, u) = 1, and |Σ_{k≤t} χ(k)/k| ≤ βlog p + o(log p) uniformly
in t (β = 1/2 PV, 1/4 + ε Burgess); optimise δ. Prop 2.3 (CONDITIONAL, GRH via Granville–Soundararajan): M_BM = M₀(1 + o(1)).
This settles the board's F4 obligation (i) (the χ_p-projector term is o(log²p) under GRH) with a derivation.

**Literature.** Pólya–Vinogradov; Burgess (Proc. LMS 1963); Granville–Soundararajan, JAMS 14 (2001) (GRH ⇒ Σ_{n≤x}χ(n) = o(x)
once log x/log log q → ∞). Analogy: Ghosh–Sarnak's local-density function δ^{(m)}(k) for Markoff surfaces (Invent. 229 (2022), §9).

**Barrier screen.** B3: the main term is now provably polylog² of the right order, but the remainder must be controlled to
o(log² p) pointwise — untouched. T1: M_BM(m²) = 0 (pair term (1 − 1)). B6: no averaging over p. Numerics: min M_BM/L² = 0.062
over primes ≤ 10⁶ (at 17), mean 0.149 at 10⁶.

**Cheap numerics.** `scripts/z38_mbm.c` (exact M_BM for all odd n; brute-force cross-check `z38_check_mbm.py`).

**Assessment.** PROVED (main term). The (L) half of the O260 split is now unconditional — for the geometric main term, not
for M_gen. What remains is purely the one-sided remainder hypothesis H⁻_BM (BM_CORRECTED_COUNT §3).
