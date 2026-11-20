# Rigidity of polynomial ES certificates on a bounded-period Proth core

## 0. Result and scope

Result: For bounded positive integers `P,L`, only finitely many `m≥1` admit a single rational-function ES triple in `T=2^(Lj)` on the whole eventual core `s=PLj` of `n=(4^m−1)2^s+1`.  
Label: PROVED (relative to Siegel's integral-points theorem and the Mordell–Schinzel primitive-square obstruction quoted in `EXPONENT_COVERING.md`, Theorem 1.2).  
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

## 2. The moving coefficient `a_m=4^m−1`

**Theorem 2 (bounded-period core).** Fix `P,L≥1`. For only finitely many `m≥1` are there `X_i ∈ Q(T)` such that for every sufficiently large integer `j` the three `X_i(2^(Lj))` are positive integers solving ES for `N_j=1+(4^m−1)2^(PLj)`. The same holds with `P,L` chosen separately for each `m` from bounded ranges. There is no restriction on how the triple or its threshold depends on `m`.

**Proof.** Apply Proposition 1 with `b=2^L`, `a=a_m`. Separate its finitely many normalized shapes into two cases.

1. **A degree outside `P Z`.** Fix a shape with a nonzero coefficient `c` at such a degree `k` and, if it occurs at all, a realizing index `m₀`. For every `m` realizing it, both `ca_m^(k/P)` and `ca_(m₀)^(k/P)` are nonzero rationals. Thus `(a_m/a_(m₀))^(k/P)` is rational. Taking prime valuations shows `a_m/a_(m₀)` is a rational `d`-th power, `d=P/gcd(P,k)>1`. For a prime `p|d`, write `a_(m₀)=D v₀^p` with `D` positive and `p`-th-power-free. Then `a_m=D v^p` for a positive **integer** `v`: each valuation of `a_m` is nonnegative and congruent to the corresponding valuation of `D∈Z` modulo `p`.

   For fixed `D,p` there are only finitely many such `m`. For odd `p`, the integral points `(v,2^m)` lie on `Y²=D X^p+1`, a hyperelliptic curve of genus `(p−1)/2≥1` (squarefree right side). For `p=2`, split `m=2h+r`, `r=0,1`; the integral points `(2^h,Dv)` lie on `Y²=D(4^r X^4−1)`, a squarefree quartic of genus one. Siegel's integral-points theorem applies to each of these fixed curves; the indicated points distinguish the indices in each case. This proves finiteness, not a computed cutoff.

2. **Only degrees in `P Z`.** Each original `X_i` lies in `Q[T^P]=Q[N]`, where `N=1+a_m T^P`. Write it as `H_i(N)` and take an integer `M≥2` clearing all coefficient denominators of the three `H_i`. Write `M=2^e M'` with `M'` odd. For arbitrarily large `j` (multiples of the order of `2` modulo `M'` if `M'>1`), `N_j≡4^m (mod M')` and `N_j≡1 (mod 2^e)`. The single class `R (mod M)` specified by these congruences is a unit square: use the roots `2^m` and `1` on the respective factors. Integrality at **one** sampled `N_j` in `R` implies integrality of `H_i(n)` for **every** integer `n` in `R`, by reduction of `M H_i(n)` modulo `M`. Positivity for all sufficiently large `n` follows from eventual positivity along the samples; the ES identity is a polynomial identity in `n` since substitution `n=1+a_m T^P` is injective. This would solve the primitive square class `R` by polynomials. It contradicts the Mordell–Schinzel obstruction as stated in the proof of [`EXPONENT_COVERING.md`, Theorem 1.2](../../EXPONENT_COVERING.md#1-setup-and-the-compactness-criterion), specifically its assertion for **all** polynomial-solvable classes at a profinite **unit** square, not just the seven ET classes. Thus this case occurs for no `m`.

The finite union over shapes, and then over any bounded choices of `P,L`, is still finite. ∎

**Reading the quantifiers.** On a bounded-period partition of the exponents it suffices that the branch through `s=0` modulo that period uses the indicated formula on its entire eventual progression. For instance, a formula rational in `2^(s/d)` with bounded positive integral `d` on `s≡0 (mod H)` with bounded `H` restricts to the theorem with `P=d`, `L=H` by taking `s=dHj`. Rational dependence on `2^m` or on `m` in the coefficients causes no problem: fix `m` first. The other branches need not be polynomial or even specified. The theorem does **not** exclude unbounded core periods, unbounded root exponents, different choices from a menu made at individual exponents with no bounded-period zero branch, or searches for divisors at each input. It supplies neither a counterexample to ES nor an all-`s` construction.
