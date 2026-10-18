# z30_genus_split — relocate T1 into an explicit main term (O260; SINGLE_P_COUNT §2)

**Idea.** CONDITIONAL_ES Prop 3.1(3)/7.3: any bound |S₁| < S₀ (principal character vs the rest) must be square-sensitive,
which no standard conjecture is. Split the character expansion of the pair form R(p) = Σ_{(u,B)} 1[p ≡ −(u+B) (4uB)] by
character ORDER instead: order ≤ 2 (genus) vs order ≥ 3.
**Result (PROVED, Lemma 2.1 / Prop 2.2).** R* = M_gen + X; M_gen ≥ 0 depends only on the quadratic characters of n;
M_gen(m²) = X(m²) = R(m²) = 0; M_gen(n) > 0 ⟺ (★) at some n·y² with the pair in the size range of n. So T1 is carried
entirely by the order-≤2 characters, and an upper bound for |X| is no longer refuted at squares.
**Barrier screen.** T1: passes by construction. B3: M_gen is still polylog (≈ M₀·[0.67, 1.46] at 10⁶); the residual X
must still be bounded at Poisson scale — the polylog lottery is not removed, only the square obstruction is relocated.
B6: n/a (pointwise identity). B2: X is still a divisor-in-class event.
**Iteration.** v1 "genus main term explains the lower tail" — partially false: genus explains ≈ 25 % of var(R − M₀) at 10⁶,
and failures have M_gen/M₀ ∈ [0.57, 0.92], not ≈ 0. v2: add full local conditioning at small primes (z30_local_main_term).
**Cheap numerics.** `scripts/z30_rgen.c` (Y = 0 column Mg); `scripts/z30_check_forms.py` (exact rational check, squares).
**Assessment.** PROVED dictionary; a genuine reformulation of the conditional target (L)+(U), not an existence mechanism.
