# AGENT REPORT O98 — explicit ET P-count at r = 17 (branch side-agent/r17-explicit-et)

Deliverable: POINTWISE_MORDELL17C.md; scripts m17c_tail_cum.py, m17c_qcheck.py. Checkpoint: context budget reached.
**Main goal NOT achieved: (H_P) remains CONDITIONAL, so there is no unconditional sterile point.**

What is new:
1. **Lemma 1.1 (PROVED).** By Abel summation (decreasing weights), M17B Thm 4.1 needs only the *cumulative*
   bounds `Σ_{13≤K'≤K} D_P(K') ≤ C·17^{θK}` and `Σ_{9≤k'≤k} D_Q(k') ≤ 17^{3k/5}`. The admissible C grows by 17/16:
   θ = 0.4 gives 1.497 (K ≥ 13) and 2.639 (K ≥ 15). The table is floor-rounded, and the pointwise column reproduces M17B §4
   exactly. This corrects the brief's premise that "we need pointwise in K".
2. **Lemma 2.1 (PROVED, brute-checked).** Type-I/Q identities `4abd = eF+1`, `fb = aF+c`, `f(4bcd−F) = F²+4c²d`.
   A fixed `(a,d)` carries at most 2 Q-points, because the modulus `4ad` exceeds `√(4a²d+1)`. **Cor 2.2:** the Q-points
   with `c ≥ F^{1/2}` are unconditionally bounded, costing 4.3·10⁻³ of the budget. So (H_Q) is needed only for `c < F^{1/2}`.
3. **Assessment 2.3.** A plausible full route to an unconditional (H_Q) via regimes `(a,d)`, `(a,c)`, `(c,d)`, plus
   Lenstra, an explicit exponent-1/4 (CHN) constant, and Nicolas–Robin, at cost < 1. Lenstra alone leaves the region
   `γ≈0, 1/3<α<1/2` uncovered. This is NOT carried out, and it needs the exact CHN/Lenstra statements (unchecked).
4. **§3 Assessment (P).** At the symmetric point, every two-variable regime costs `N^{1/2}`, so a τ_3 `e`-regime is
   unavoidable. The θ = 0.4 constants cannot be met by any ET-type cover at any K. θ near 1/2 needs K in the hundreds,
   plus exact data below that.

Suggested next steps: (a) carry out Assessment 2.3, which would make (H_Q) unconditional for k ≥ k₀; the remaining
range would be a finite exact computation of D_Q. (b) For P, more exact data (D_P(15)) moves the base to ρ₃.
I see no explicit-analytic route for P.
