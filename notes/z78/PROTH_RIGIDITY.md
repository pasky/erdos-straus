# Rigidity of polynomial ES certificates on a bounded-period Proth core

## 0. Result and scope

Result: After normalizing the target to `1+U^P`, positive polynomial ES triples integral on a fixed geometric progression before normalization have only finitely many possible shapes.  
Label: PROVED (algebraic rigidity; arithmetic application below uses named theorems).  
Scope: Rigidity of the denominator formulas, not nonexistence of ES solutions at any integer. No bound on the degrees, heights or coefficient denominators of the input triples is assumed.  
Review: none.  
Triage: BARRIER-SCOPED.  
STATUS delta: none.

## 1. A finite set of normalized shapes

**Proposition 1.** Fix integers `P≥1`, `b≥2`. Let `a>0` be rational and let `X_i(T) ∈ Q(T)` (`1≤i≤3`) give positive integral denominators for `4/(1+aT^P)` at every `T=b^j` for sufficiently large integers `j`. The threshold and all coefficients may depend on `a`. Then the `X_i` are polynomials. Put `F_i(U)=X_i(a^(−1/P)U)`, using the positive real root. The ordered triples `(F_1,F_2,F_3)` belong to a finite set depending only on `P,b`.

**Proof.** Divide a rational function into a polynomial part and a proper fraction. At integral arguments the polynomial part has bounded denominator, and the proper fraction tends to zero as the argument tends to infinity. Integrality at infinitely many such arguments forces the proper fraction to vanish there, hence identically. The ES equation likewise holds identically, by clearing denominators at infinitely many points.

Write `N=1+aT^P`. Each `X_i` is eventually positive, and indeed positive everywhere on `[0,∞)`: if there were any nonnegative root among them, to the right of the last such root all three are positive, and at least one reciprocal diverges to `+∞` on approach to the root. Their sum `4/N` stays finite. In particular `r_i=X_i(0)>0`, with `Σ 1/r_i=4`.

Order the degrees `d_1≤d_2≤d_3`. At positive infinity the slowest-decaying positive reciprocals cannot cancel, so `d_1=P`. Now `1/X_2+1/X_3=(4X_1−N)/(NX_1)` has decay of order `T^(−d_2)` and a nonzero polynomial numerator. Thus `d_2≤2P`. Similarly `1/X_3=[4X_1X_2−N(X_1+X_2)]/(NX_1X_2)` gives `d_3≤4P`. Take `B=4P`.

For any polynomial of degree at most `B`, Lagrange interpolation at `b^J,b^(J+1),…,b^(J+B)` expresses its value at zero as a sum of the sampled values with weights

`w_h = ∏_{0≤k≤B, k≠h} (−b^k)/(b^h−b^k)`.

The common scale `b^J` cancels. Taking `C` a common denominator of these weights and `J` past the integrality threshold gives `C r_i ∈ Z_{>0}`. There are only finitely many such triples: the positive integers `e_i=C r_i` satisfy `Σ 1/e_i=4/C`; after ordering them increasingly the smallest is at most `3C/4`, the next is bounded by twice the reciprocal of the positive residual after fixing the first, and the last is determined. This is the only step that needs a whole block of successive integral samples, rather than infinitely many isolated ones.

Fix one possible ordered tuple `r_i`. In the complex coefficient space of polynomials `F_i` of degree at most `B` with `F_i(0)=r_i`, impose the coefficient equations

`4F_1F_2F_3 = (1+U^P)(F_1F_2 + F_1F_3 + F_2F_3)`.

This affine algebraic set is bounded. Otherwise choose a sequence with some coefficients unbounded, with the largest coefficient modulus tending to infinity. For nonzero coefficients `c_ik` of degree `k≥1`, take `ρ=min |c_ik|^(−1/k)` for each tuple. Then `ρ→0`; after substitution `U=ρV`, every nonconstant coefficient has modulus at most one, and at least one has modulus exactly one. Pass to a subsequence with a common such index and with all rescaled coefficients convergent. The limiting polynomials `G_i` still have `G_i(0)=r_i`; at least one is nonconstant. The target has become `1`, so `Σ 1/G_i=4` identically. At infinity the nonconstant reciprocals vanish and the remaining constants contribute a proper subsum of `Σ 1/r_i=4`, impossible by positivity of the `r_i`. No positivity of the *complex* coefficients was used.

A bounded complex affine algebraic set is finite: by the constructible image theorem each coordinate projection is constructible in the affine line, hence either finite or cofinite, and a bounded projection cannot be cofinite. Take the product of the finite projections. The normalized `F_i` satisfy the displayed equations with one of finitely many allowed constant tuples; the proposition follows. ∎
